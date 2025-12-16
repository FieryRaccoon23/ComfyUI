
from .BlenderDecimate.BlenderDecimate import Blender_Decimate

NODE_CLASS_MAPPINGS = {
    "Blender_Decimate": Blender_Decimate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Blender_Decimate": "Blender Decimate will reduce the polygon or face counts of a mesh",
}