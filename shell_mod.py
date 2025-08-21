import subprocess
import os

# found syntax (UNIX BASH)
# </dir/to/blender/bin/>blender '</path/to/BlendFile>.blend' --background --python </path/to/Python/File>
# UNIX EXAMPLE
# /home/jayjay/sw/Blender/blender "/home/jayjay/3D/projects/personal/wallpaper/scenes/blender/tux.blend" --background --python "/home/jayjay/3D/projects/personal/wallpaper/scenes/blender/tux.blend""/scripts/SceneExport_PROJ.py"

# found syntax (WINDOWS CMD)
# cd <Drive:/directory/to/exe/file> && blender "<Drive:\blend\file\directory\example>.blend" --background --python "Drive:/path/to/python/file>.py"  
# WINDOWS EXAMPLE
# cd c:/Program Files/Blender Foundation/Blender 4.4 && blender "C:\Users\Jayjay\Documents\readme.blend"  --background --python "C:\OneDrive\OneDrive - University of Gloucestershire\python\FLD_win\exporters\SceneExport_env.py"

class commandRunnersBlender:
    def shell_unix(BinExec, WorkingFile, PyFileDir):
        BinExec = "C:/Program Files/Blender Foundation/Blender 4.4/blender "
        WorkingFile = "'C:\Temp\x.blend'" 
        Arguments = " --background --python "
        PyFileDir = "foobar"

        # command = BinRoot + WorkingFile + Arguments + PyFireDir
        print("/ ", BinExec + WorkingFile + Arguments + PyFileDir)

        subprocess.Popen(BinExec + WorkingFile + Arguments + PyFileDir, shell=True)

    def shell_windows(ExeCarry, exe, FileLoc, script):
        ExeLocation = 'cd ' + ExeCarry + ' '    
        Startname = ' ' + exe + ' '
        TargetFile = '"' + FileLoc + '"'
        Arguments = '  --background --python '
        ScriptLoc = '"' + script + '"'
        
        # print("~ " + ExeLocation + "&&" + Startname + FileLoc + Arguments + ScriptLoc)
        subprocess.Popen(ExeLocation + "&&" + Startname + FileLoc + Arguments + ScriptLoc, shell=True)



# the shell from hell
commandRunnersBlender.shell_windows(r"C:\Program Files\Blender Foundation\Blender 4.4", 
                                    r"blender",
                                    '"' + r"C:\OneDrive\OneDrive - University of Gloucestershire\python\FLD_win\xyz\scenes\blender\EnvTest.blend" + '"',
                                    r"C:\OneDrive\OneDrive - University of Gloucestershire\python\FLD_win\xyz\scripts\SceneExport_env.py")