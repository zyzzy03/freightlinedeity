import subprocess, os
from pathlib import Path

#  //////////////////////////////////////////////////////////
# // "os_specified" should be changed to what OS you want. //
# // "UNIX" For Unix, or unix-like (Linux, macOS, or BSD)  //
# // "WIN" for (you guessed it), Windows!                  //
# // This should, in theory, make porting to either easier.//
# /////////////////////////////////////////////////////////

class portSystem:                                                                       
    def ShellPorter(os_specified, arg1, arg2, arg3, arg4):                              
        if os_specified == "UNIX":                                                     
            commandShellsBlender.ShellBlenderUnix(arg1, arg2, arg3, arg4)               
                                                                                        
                                                                                        
        if os_specified == "WIN":
            commandShellsBlender.ShellBlenderWindows(arg1, arg2, arg3, arg4)


class commandShellsBlender:
    """ BASH export script for UNIX (and UNIX-like) systems """
    # def ShellBlenderUnix(BinExec, WorkingFile, PyFileDir):
    #     BinExec = os.path.join("C:/Program Files/Blender Foundation/Blender 4.4/blender ")
    #     WorkingFile = os.path.join("'C:\Temp\x.blend'")
    #     Arguments = " --background --python "
    #     PyFileDir = os.path.join("foobar")

    #     # command = BinRoot + WorkingFile + Arguments + PyFireDir
    #     print("/ ", BinExec + WorkingFile + Arguments + PyFileDir)

    #     print(BinExec + WorkingFile + Arguments + PyFileDir)
        # subprocess.Popen(BinExec + WorkingFile + Arguments + PyFileDir, shell=True)
    
    """ Shell (cmd.exe) for Windows"""
    def ShellBlenderWindows(ExeCarry, exe, FileLoc, script):
        ExeLocation = os.path.join('cd ' + ExeCarry + ' ')
        Startname = f" {exe} "
        TargetFile = os.path.join(f'"{FileLoc}"')
        ScriptLoc = os.path.join(f'"{script}"')

        ShellCommand = f'cd "{ExeCarry}" && blender {FileLoc} --background --python {ScriptLoc}'

        print("~ (command output) " + ExeLocation + "&&" + Startname + TargetFile + ' --background --python ' + ScriptLoc)
        subprocess.Popen(ShellCommand, shell=True)


class commandShellSubPaint:
    def ShellSubPaint():
        exe = '"' + exe + '"'
        mesh_import = ""

        subprocess.Popen(exe + " --mesh " + mesh_import + " --split-by-udim", shell=True)

class commandsShellMaya:
    def ShellMayaUnix():
        pass

    def ShellMayaWindows():
        pass



# found syntax (UNIX BASH)
# </dir/to/blender/bin/>blender '</path/to/BlendFile>.blend' --background --python </path/to/Python/File>
# UNIX EXAMPLE
# /home/jayjay/sw/Blender/blender "/home/jayjay/3D/projects/personal/wallpaper/scenes/blender/tux.blend" --background --python "/home/jayjay/3D/projects/personal/wallpaper/scenes/blender/tux.blend""/scripts/SceneExport_PROJ.py"

# found syntax (WINDOWS CMD)
# cd <Drive:/directory/to/exe/file> && blender "<Drive:\blend\file\directory\example>.blend" --background --python "Drive:/path/to/python/file>.py"  
# WINDOWS EXAMPLE
# cd c:/Program Files/Blender Foundation/Blender 4.4 && blender "C:\Users\Jayjay\Documents\readme.blend"  --background --python "C:\OneDrive\OneDrive - University of Gloucestershire\python\FLD_win\exporters\SceneExport_env.py"
# cd C:\Program Files\Adobe\Adobe Substance 3D Painter && "Adobe Substance 3D Painter.exe" --mesh --split-by-udim C:\OneDrive\OneDrive - University of Gloucestershire\LinuxTransfer\projects\3D\projects\personal\CivilEng\texture\import\low.fbx