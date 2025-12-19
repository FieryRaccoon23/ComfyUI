import bpy, sys, os

argv = sys.argv
args = argv[argv.index("--") + 1:] if "--" in argv else []

def val(flag, default=None):
    if flag in args:
        return args[args.index(flag) + 1]
    return default

inp = val("--input")
outp = val("--output")

iterations = int(val("--iterations", "10"))
factor = float(val("--factor", "0.5"))

shade_smooth_raw = str(val("--shade_smooth", "1")).lower()
shade_smooth = shade_smooth_raw in ("1", "true", "yes", "y", "on")

bpy.ops.wm.read_factory_settings(use_empty=True)

# import OBJ (newer vs older Blender operator name)
if hasattr(bpy.ops.wm, "obj_import"):
    bpy.ops.wm.obj_import(filepath=inp)
else:
    bpy.ops.import_scene.obj(filepath=inp)

# Smooth all meshes
for obj in bpy.data.objects:
    if obj.type != "MESH":
        continue

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Option A: "Shade Smooth" (normals/shading only)
    if shade_smooth and obj.data is not None:
        for poly in obj.data.polygons:
            poly.use_smooth = True

    # Option B: Smooth modifier (actually changes geometry)
    mod = obj.modifiers.new("Smooth", "SMOOTH")
    mod.factor = max(0.0, min(1.0, factor))
    mod.iterations = max(0, iterations)

    bpy.ops.object.modifier_apply(modifier=mod.name)

os.makedirs(os.path.dirname(outp), exist_ok=True)

# export OBJ (newer vs older Blender operator name)
if hasattr(bpy.ops.wm, "obj_export"):
    bpy.ops.wm.obj_export(filepath=outp)
else:
    bpy.ops.export_scene.obj(filepath=outp)
