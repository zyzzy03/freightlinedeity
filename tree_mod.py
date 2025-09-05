from rich.tree import Tree
from rich import print
import os

# TO DO: Make this a dictionary


def ShowProjectTree(ProjectDirectory, name, software_type):
    main_path = f"{ProjectDirectory}/scenes"
    path_blender = f"{ProjectDirectory}/scenes/blender"
    path_max = f"{ProjectDirectory}/scenes/max"
    path_maya = f"{ProjectDirectory}/scenes/maya"
    path_USD = f"{ProjectDirectory}/scenes/USD"


    # Tree root
    tree_root = Tree(f"[projectroot]/scenes \n|")
    print(tree_root)
    
    if software_type == "blender":
        """ blender scenes """
        tree_blender = Tree("/blender \n|")
        listdir_blender = os.listdir(path_blender)

        for i in range(len(listdir_blender)):
            tree_blender.add(listdir_blender[i])
        print(tree_blender)


    if software_type == "maya":
        """ maya scenes """
        tree_maya = Tree("/maya \n|")
        listdir_maya = os.listdir(path_maya)

        for i in range(len(listdir_maya)):
            tree_maya.add(listdir_maya[i])
        print(tree_maya)

    if software_type == "3ds max":
        """ 3DS Max scenes """
        tree_max = Tree("/max \n|")
        listdir_max = os.listdir(path_max)

        for i in range(len(listdir_max)):
            tree_max.add(listdir_max[i])
        print(tree_max)


    """ USD scenes """
    tree_USD = Tree("/USD \n|")
    listdir_USD = os.listdir(path_USD)

    for i in range(len(listdir_USD)):
        tree_USD.add(listdir_USD[i])
    print(tree_USD)



def LookInside(db_path, selected_dir):
    search_path = f"{db_path}/scenes/{selected_dir}"

    listdir_paths = os.listdir(search_path)

    print(f"╚ {selected_dir}")
    for index_a in range(len(listdir_paths)):
        print(f"  └ /{listdir_paths[index_a]}")

    """
    Output:
    ╚ /<scene>
        └ <scenefile>
    """