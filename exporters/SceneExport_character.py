import bpy

                # TYPE PROJECT DIR HERE! 
                # 🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻🡻
ProjectDir_bl : r""          

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/models/" + "body_character.fbx",
    collection:"BODY",
    use_mesh_modifiers:True
)

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/models/" + "attire_character.fbx",
    collection:"ATTIRE",
    use_mesh_modifiers:True
)

bpy.ops.export_scene.fbx(
    filepath: ProjectDir_bl + "/asset/models/" + "props_character.fbx",
    collection:"PROPS",
    use_mesh_modifiers:True
)