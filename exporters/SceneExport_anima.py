import bpy

                # TYPE PROJECT DIR HERE! 
                # 🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻
ProjectDir_bl : r""          

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/animations/" + "SetDressing.fbx",
    collection:"CHAR",
    use_mesh_modifiers:True
)