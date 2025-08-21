import subprocess, os
from pathlib import Path

class portSystem:
    def ShellPorter(os_specified, arg1, arg2, arg3, arg4):                              # "os_specified" should be changed to what OS you want.
        if os_specified == "UNIX":                                                      # "UNIX" For Unix, or unix-like (Linux, macOS, or BSD)
            commandShellsBlender.ShellBlenderUnix(arg1, arg2, arg3, arg4)               # "WIN" for (you guessed it), Winodws!
                                                                                        # This should, in theory, make porting to either easier.
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
        Startname = ' ' + exe + ' '
        TargetFile = os.path.join('"' + FileLoc + '"')
        ScriptLoc = os.path.join('"' + script + '"')

        print("~ (command output) " + ExeLocation + "&&" + Startname + TargetFile + ' --background --python ' + ScriptLoc)
        subprocess.Popen(ExeLocation + "&&" + Startname + TargetFile + ' --background --python ' + ScriptLoc, shell=True)


class commandShellSubPaint:
    pass

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
