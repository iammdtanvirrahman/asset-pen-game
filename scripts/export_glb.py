import bpy, os

out = os.path.abspath("models/gallinera_table_4k.glb")
os.makedirs(os.path.dirname(out), exist_ok=True)

# Load the scene and export all scene objects as a self-contained GLB.
bpy.ops.object.select_all(action="SELECT")
bpy.context.view_layer.objects.active = next((o for o in bpy.context.scene.objects if o.type == "MESH"), None)

bpy.ops.export_scene.gltf(
    filepath=out,
    export_format="GLB",
    use_selection=False,
    export_apply=True,
    export_texcoords=True,
    export_normals=True,
    export_materials="EXPORT",
    export_image_format="AUTO",
)
print("Exported GLB:", out, "bytes:", os.path.getsize(out))
