import os
import uuid
import subprocess
import folder_paths

from ..BlenderConfig import BLENDER_PATH


class Blender_Smooth:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mesh_path": ("STRING", {"default": ""}),  # input .obj path (ComfyUI will resolve to output/3D/<basename>)
                "iterations": ("INT", {"default": 10, "min": 0, "max": 200, "step": 1}),
                "factor": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.000001, "round": False, "display": "number"}),
                "shade_smooth": ("BOOLEAN", {"default": True}),  # normals smoothing
                "output_name": ("STRING", {"default": "smoothed.obj"}),  # used only if save_file=True
                "save_file": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "output_dir": ("STRING", {"default": ""}),  # optional override when save_file=True
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mesh_out_path",)
    FUNCTION = "run"
    CATEGORY = "3D/Blender"

    def run(self, mesh_path, iterations, factor, shade_smooth, output_name, save_file, output_dir=""):
        fname = os.path.basename(mesh_path)

        output_root = folder_paths.get_output_directory()
        mesh_path = os.path.join(output_root, "3D", fname)

        if not os.path.isfile(mesh_path):
            raise FileNotFoundError(f"Input mesh not found: {mesh_path}")

        blender_exe = os.path.abspath(BLENDER_PATH)
        if not os.path.isfile(blender_exe):
            raise FileNotFoundError(f"Blender not found: {blender_exe}")

        if save_file:
            base_dir = output_dir.strip() if output_dir.strip() else folder_paths.get_output_directory()
            out_dir = os.path.join(base_dir, "3D")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, output_name)
        else:
            base_dir = folder_paths.get_temp_directory()
            out_dir = os.path.join(base_dir, "3D")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"smooth_{uuid.uuid4().hex}.obj")

        script_path = os.path.join(os.path.dirname(__file__), "blender_smooth_script.py")

        cmd = [
            blender_exe,
            "-b", "-noaudio", "--factory-startup",
            "--python", script_path,
            "--",
            "--input", mesh_path,
            "--output", out_path,
            "--iterations", str(int(iterations)),
            "--factor", str(float(factor)),
            "--shade_smooth", "1" if bool(shade_smooth) else "0",
        ]

        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"Blender failed:\n{r.stderr}\n{r.stdout}")

        if not os.path.isfile(out_path):
            raise RuntimeError(f"Output missing: {out_path}")

        return (out_path,)
