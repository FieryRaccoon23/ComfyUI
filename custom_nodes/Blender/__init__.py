
from .BlenderDecimate.BlenderDecimate import Blender_Decimate
from .BlenderInspect.BlenderInspect import Blender_Inspect

NODE_CLASS_MAPPINGS = {
    "Blender_Decimate": Blender_Decimate,
    "Blender_Inspect": Blender_Inspect
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Blender_Decimate": "Blender Decimate",
    "Blender_Inspect": "Blender Inspect Model (verts/faces/edges/tris)"
}