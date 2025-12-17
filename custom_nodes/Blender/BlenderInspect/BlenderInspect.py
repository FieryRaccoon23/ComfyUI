import os
import json
import subprocess
import folder_paths

from ..BlenderConfig import BLENDER_PATH

class Blender_Inspect:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("stats",)
    FUNCTION = "inspect"
    CATEGORY = "Blender"

    def inspect(self, model_path: str):
        print("[Blender_Inspect] running for:", model_path)

        blender_exe = os.path.abspath(BLENDER_PATH)

        fname = os.path.basename(model_path)

        output_root = folder_paths.get_output_directory()

        model_path = os.path.join(output_root, "3D", fname)

        #model_path = os.path.abspath(model_path)

        if not os.path.exists(model_path):
            text = f"❌ File not found:\n{model_path}"
            return {"ui": {"text": [text]}, "result": (text,)}

        # This is the Blender Python script file you just created
        script_path = os.path.join(os.path.dirname(__file__), "blender_inspect_script.py")
        script_path = os.path.abspath(script_path)

        if not os.path.exists(script_path):
            text = f"❌ Missing script:\n{script_path}"
            return {"ui": {"text": [text]}, "result": (text,)}

        cmd = [
            blender_exe,
            "-b",
            "--factory-startup",
            "--python", script_path,
            "--", model_path
        ]

        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
        except Exception as e:
            text = f"❌ Failed to run Blender:\n{e}"
            return {"ui": {"text": [text]}, "result": (text,)}

        if proc.returncode != 0:
            text = "❌ Blender returned an error.\n\nSTDERR:\n" + (proc.stderr[-4000:] if proc.stderr else "(none)")
            return {"ui": {"text": [text]}, "result": (text,)}

        lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
        if not lines:
            text = "⚠️ Blender produced no output (could not read stats)."
            return {"ui": {"text": [text]}, "result": (text,)}

        candidates = [ln for ln in lines if ln.startswith("{") and ln.endswith("}")]
        stats = None
        for ln in reversed(candidates):
            try:
                stats = json.loads(ln)
                break
            except Exception:
                pass

        if stats is None:
            text = "⚠️ Could not parse Blender output as JSON.\n\nSTDOUT (tail):\n" + "\n".join(lines[-30:])
            return {"ui": {"text": [text]}, "result": (text,)}

        pretty = (
            f"✅ Model: {model_path}\n"
            f"Mesh objects: {stats.get('mesh_objects', '?')}\n"
            f"Vertices:     {stats.get('vertices', '?')}\n"
            f"Edges:        {stats.get('edges', '?')}\n"
            f"Faces:        {stats.get('faces', '?')}\n"
            f"Triangles:    {stats.get('triangles', '?')}\n"
        )

        return {"ui": {"text": [pretty]}, "result": (pretty,)}
