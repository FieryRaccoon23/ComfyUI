# blender_inspect_script.py
import bpy
import sys
import os
import json

def import_any(path: str):
    ext = os.path.splitext(path)[1].lower()

    # Start from a clean scene
    bpy.ops.wm.read_factory_settings(use_empty=True)

    if ext == ".obj":
        bpy.ops.wm.obj_import(filepath=path)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=path)
    elif ext in (".glb", ".gltf"):
        bpy.ops.import_scene.gltf(filepath=path)
    elif ext == ".ply":
        bpy.ops.wm.ply_import(filepath=path)
    elif ext == ".stl":
        bpy.ops.wm.stl_import(filepath=path)
    else:
        raise RuntimeError(f"Unsupported extension: {ext}")

def mesh_stats():
    verts = faces = edges = tris = 0
    mesh_objects = [o for o in bpy.context.scene.objects if o.type == "MESH"]

    for obj in mesh_objects:
        me = obj.data
        verts += len(me.vertices)
        edges += len(me.edges)
        faces += len(me.polygons)
        for p in me.polygons:
            tris += max(0, len(p.vertices) - 2)

    return {
        "mesh_objects": len(mesh_objects),
        "vertices": verts,
        "edges": edges,
        "faces": faces,
        "triangles": tris,
    }

def main():
    argv = sys.argv
    if "--" not in argv:
        raise RuntimeError("Expected args after --")
    path = argv[argv.index("--") + 1]

    import_any(path)
    stats = mesh_stats()

    # Print JSON as a single line (your ComfyUI node will parse the last line)
    print(json.dumps(stats))

if __name__ == "__main__":
    main()
