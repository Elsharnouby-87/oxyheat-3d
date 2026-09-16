# AQP WHR Configuration 3 web-export staging script.
import bpy
import json
import math
import os
import sys
from mathutils import Vector


def arg_after_double_dash(default_dir="/tmp/aqp-export"):
    if "--" in sys.argv:
        args = sys.argv[sys.argv.index("--") + 1:]
        if args:
            return args[0]
    return default_dir


out_dir = os.path.abspath(arg_after_double_dash())
os.makedirs(out_dir, exist_ok=True)
glb_path = os.path.join(out_dir, "AQP_WHR_Config3_Web.glb")
meta_path = os.path.join(out_dir, "scene_meta.json")

scene = bpy.context.scene
view_layer = bpy.context.view_layer

object_counts = {}
for obj in scene.objects:
    object_counts[obj.type] = object_counts.get(obj.type, 0) + 1

converted = []
failed_conversions = []
for obj in list(scene.objects):
    if obj.type not in {"CURVE", "FONT", "SURFACE", "META"}:
        continue
    try:
        if obj.name not in view_layer.objects:
            continue
        if not obj.visible_get(view_layer=view_layer):
            continue
        bpy.ops.object.select_all(action="DESELECT")
        obj.hide_set(False)
        obj.hide_viewport = False
        obj.select_set(True)
        view_layer.objects.active = obj
        original_type = obj.type
        bpy.ops.object.convert(target="MESH")
        converted.append({"name": obj.name, "from": original_type, "to": "MESH"})
    except Exception as exc:
        failed_conversions.append({"name": obj.name, "type": obj.type, "error": repr(exc)})

mins = Vector((math.inf, math.inf, math.inf))
maxs = Vector((-math.inf, -math.inf, -math.inf))
visible_meshes = 0
for obj in scene.objects:
    if obj.type != "MESH":
        continue
    try:
        if not obj.visible_get(view_layer=view_layer):
            continue
    except Exception:
        pass
    visible_meshes += 1
    for corner in obj.bound_box:
        world_corner = obj.matrix_world @ Vector(corner)
        mins.x = min(mins.x, world_corner.x)
        mins.y = min(mins.y, world_corner.y)
        mins.z = min(mins.z, world_corner.z)
        maxs.x = max(maxs.x, world_corner.x)
        maxs.y = max(maxs.y, world_corner.y)
        maxs.z = max(maxs.z, world_corner.z)

bounds = None
if visible_meshes and all(math.isfinite(v) for v in (*mins, *maxs)):
    center = (mins + maxs) * 0.5
    size = maxs - mins
    bounds = {
        "min": list(mins),
        "max": list(maxs),
        "center": list(center),
        "size": list(size),
        "radius": float(size.length * 0.5),
    }

viewport = None
try:
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type != "VIEW_3D":
                continue
            space = area.spaces.active
            r3d = space.region_3d
            viewport = {
                "screen": screen.name,
                "view_distance": float(r3d.view_distance),
                "view_location": list(r3d.view_location),
                "view_rotation_xyzw": [r3d.view_rotation.x, r3d.view_rotation.y, r3d.view_rotation.z, r3d.view_rotation.w],
                "view_perspective": r3d.view_perspective,
                "lens": float(space.lens),
                "clip_start": float(space.clip_start),
                "clip_end": float(space.clip_end),
            }
            raise StopIteration
except StopIteration:
    pass
except Exception:
    viewport = None

world_color = None
try:
    world_color = list(scene.world.color) if scene.world else None
except Exception:
    pass

metadata = {
    "source_file": bpy.data.filepath,
    "blender_version": bpy.app.version_string,
    "scene": scene.name,
    "object_counts_before_conversion": object_counts,
    "converted_to_mesh": converted,
    "failed_conversions": failed_conversions,
    "visible_mesh_count_after_conversion": visible_meshes,
    "bounds": bounds,
    "saved_viewport": viewport,
    "world_color": world_color,
}
with open(meta_path, "w", encoding="utf-8") as fh:
    json.dump(metadata, fh, ensure_ascii=False, indent=2)

print("AQP_EXPORT_META", json.dumps(metadata, ensure_ascii=False))

result = bpy.ops.export_scene.gltf(
    filepath=glb_path,
    check_existing=False,
    export_format="GLB",
    export_image_format="AUTO",
    export_texcoords=True,
    export_normals=True,
    export_tangents=False,
    export_materials="EXPORT",
    export_all_vertex_colors=True,
    export_cameras=True,
    export_lights=True,
    use_visible=True,
    export_extras=True,
    export_yup=True,
    export_apply=True,
    export_gn_mesh=True,
    export_animations=True,
    export_frame_range=False,
    export_skins=True,
    export_morph=True,
    export_gpu_instances=False,
)
print("AQP_EXPORT_RESULT", result)
print("AQP_EXPORT_GLB", glb_path, os.path.getsize(glb_path) if os.path.exists(glb_path) else -1)
