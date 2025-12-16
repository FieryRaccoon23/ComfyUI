import os
import tempfile
import uuid
import subprocess
import folder_paths

from ..BlenderConfig import BLENDER_PATH


class Blender_Decimate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mesh_path": ("STRING", {"default": ""}),  # input .obj path
                "ratio": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.000001, "round": False,"display": "number"}),
                "output_name": ("STRING", {"default": "decimated.obj"}),  # used only if save_file=True
                "save_file": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "output_dir": ("STRING", {"default": ""}),  # optional, used only if save_file=True
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mesh_out_path",)
    FUNCTION = "run"
    CATEGORY = "3D/Blender"

    def run(self, mesh_path, ratio, output_name, save_file, output_dir=""):
        fname = os.path.basename(mesh_path)

        output_root = folder_paths.get_output_directory()

        mesh_path = os.path.join(output_root, "3D", fname)

        if not os.path.isfile(mesh_path):
            raise FileNotFoundError(f"Input mesh not found: {mesh_path}")

        blender_exe = os.path.abspath(BLENDER_PATH)
        if not os.path.isfile(blender_exe):
            raise FileNotFoundError(f"Blender not found: {blender_exe}")

        if save_file:
            base_dir = folder_paths.get_output_directory()   # e.g. D:\ComfyUI\ComfyUI\output
            out_dir = os.path.join(base_dir, "3D")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, output_name)
        else:
            base_dir = folder_paths.get_temp_directory()     # ComfyUI temp (same drive)
            out_dir = os.path.join(base_dir, "3D")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"dec_{uuid.uuid4().hex}.obj")

        script_path = os.path.join(os.path.dirname(__file__), "blender_decimate_script.py")

        cmd = [
            blender_exe,
            "-b", "-noaudio", "--factory-startup",
            "--python", script_path,
            "--",
            "--input", mesh_path,
            "--output", out_path,
            "--ratio", str(float(ratio)),
        ]

        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"Blender failed:\n{r.stderr}\n{r.stdout}")

        if not os.path.isfile(out_path):
            raise RuntimeError(f"Output missing: {out_path}")

        return (out_path,)
