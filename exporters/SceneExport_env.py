import bpy

                # TYPE PROJECT DIR HERE! 
                # 🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻
ProjectDir_bl : r""          

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/models/" + "mes_ENV.fbx",
    collection:"MES",
    use_mesh_modifiers:True
)

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/models/" + "SetDressing_ENV.fbx",
    collection:"SetDressing",
    use_mesh_modifiers:True
)