import bpy

                # TYPE PROJECT DIR HERE! 
                # 🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻
ProjectDir_bl : r""   

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/texture/import/low/" + "low.fbx",
    collection:"low",
    use_mesh_modifiers:True
)

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/texture/import/high/" + "high.fbx",
    collection:"high",
    use_mesh_modifiers:True
)