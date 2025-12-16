import bpy, sys, os

argv = sys.argv
args = argv[argv.index("--")+1:] if "--" in argv else []

def val(flag, default=None):
    if flag in args:
        return args[args.index(flag)+1]
    return default

inp = val("--input")
outp = val("--output")
ratio = float(val("--ratio", "0.5"))

bpy.ops.wm.read_factory_settings(use_empty=True)

# import OBJ
if hasattr(bpy.ops.wm, "obj_import"):
    bpy.ops.wm.obj_import(filepath=inp)
else:
    bpy.ops.import_scene.obj(filepath=inp)

# decimate all meshes
for obj in bpy.data.objects:
    if obj.type != "MESH":
        continue
    bpy.context.view_layer.objects.active = obj
    mod = obj.modifiers.new("Decimate", "DECIMATE")
    mod.ratio = max(0.0, min(1.0, ratio))
    bpy.ops.object.modifier_apply(modifier=mod.name)

os.makedirs(os.path.dirname(outp), exist_ok=True)

# export OBJ
if hasattr(bpy.ops.wm, "obj_export"):
    bpy.ops.wm.obj_export(filepath=outp)
else:
    bpy.ops.export_scene.obj(filepath=outp)
