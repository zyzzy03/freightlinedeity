import time, sys, os, shutil as s, subprocess, sqlite3
import TerminalDecor_mod
import ter_mod as t
import dict_mod as dict
import sheller_mod as sheller
from rich.console import Console
from rich.table import Table

# THIRD PROTOTYPE
# ~~ Early Alpha (v03x) ~~
# TO DO:
# Buncha bug fixes and testing
# ~ Alpha (v04x onwards)~
# (v041) Cosmetic improvements (Tables, colours, Unix port, and GitHub release!)
# (v042) Substance Painter import
# (v05) Unreal Engine import (mesh and materials)
# (v06) Maya workspace.mel project creation

# ~~ Beta ~~
# TO DO:
# (v06) Qt GUI instead of terminal
# (v07) 3DS Max workspaces

# im gonna rewrite this in C++, one day, and when I mean one day
# i mean when i get the gcc compiler to fucking run


#---------------------------
# ! ricing
#---------------------------
class ricing:
    def opening():
        TerminalDecor_mod.asciiRicing.title("./icons/titlewin.txt")

    def closing():
        TerminalDecor_mod.asciiRicing.title("./icons/exit.txt")

    def quit():
        print(t.ter[0], "exiting Freightline Deity")
        print(TerminalDecor_mod.asciiRicing.title("./icons/exit.txt"))
        sys.exit()

    def wait(message):
        SourceTime = int(0)
        DepartTime = int(0)
        print("| Time to departure (Hours): ")
        SourceTime = int(input(t.ter[1]))

        if SourceTime < 0:
            return

        elif SourceTime > 0:
            DepartTime = SourceTime * 3600
            print(t.ter[0], message)
            time.sleep(DepartTime)
            print(t.ter[0], "Departed freight!")

    def clear(os_mode): # this will become the sheller module function
        if os_mode == "unix":
            subprocess.Popen("clear", shell=True)

        if os_mode == "win":
            subprocess.Popen("cls", shell=True)
            



#---------------------------
# ! SQL
#---------------------------
class database:
    def sqlSetup():
        TerminalDecor_mod.asciiSeperators.LineMid()
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        c.execute("""
        CREATE TABLE vital(
            binaryName TEXT,
            version TEXT,
            BinLocation TEXT,
            status TEXT  
        )""")

        c.execute("""
        CREATE TABLE projects(
            ProjName TEXT,
            ProjDir TEXT,
            status TEXT     
        )""")

        print(t.ter[0], "command worked without a problem! You **shouldn't** have to touch this again! :)")
        time.sleep(3)
        conn.commit()
        conn.close()


# SQL INPUTS V ========================= V
    def sqlInput_vital():
        TerminalDecor_mod.asciiSeperators.LineMid()
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        print(t.ter[0])
        name = input("> Software name: ")
        print(t.ter[0])
        version = str(input("> version: "))
        print(t.ter[0])
        bindir = input("> software root dir: ")
        
        print(t.ter[0])
        status = input("> status: ")
        print(t.ter[0])
        c.execute("INSERT INTO vital VALUES (?,?,?,?)", (name, version, bindir, status))

        conn.commit()
        conn.close()
        print(t.ter[0], name, "registered! ^_^")

    """ input a project register here """
    def sqlInput_proj():
        TerminalDecor_mod.asciiSeperators.LineMid()
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        name = input("> Project name: ")
        ProjLoc = input("> Project root: ")
        status = input("> status (e.g; PRODUCTION, legacy, LTS, experimental): ")

        c.execute("INSERT INTO projects VALUES (?,?,?);", (name, ProjLoc, status))

        conn.commit()
        conn.close()
        print(t.ter[0], name, "registered! ^^")


# SQL READ V ========================= V

    """ reading exe register """
    def sqlReadExe():
        TerminalDecor_mod.asciiSeperators.LineMid()
        os.system('mode con lines=25 cols=135')
        
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        x = c.execute("""SELECT * FROM vital;""")
        x = c.fetchall()

        print(t.ter[0] + t.ter[2] + "Apologies for the scuffed presnetation :(")

        print("|     " + "< Name >" + "     |     " + "< Version >" + "     |     " + "< Location >"  + "     |     " + "< Status >"  + "     |")
        TerminalDecor_mod.asciiSeperators.LineMid()
        for x in x:
            print(t.ter[0] + x[0] + "\t|\t" + x[1] + "\t|\t" +  x[2] + "\t|\t" +  x[3] + "\t")

        conn.commit()
        conn.close()
            

    """ reading exe register """
    def sqlReadProj():
        TerminalDecor_mod.asciiSeperators.LineMid()
        print("project mode")
            
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        c.execute("""SELECT * FROM projects;""")
        x = c.fetchall()

        print(t.ter[0] + t.ter[1] + "Apologies for the scuffed presnetation ;(")
        print(t.ter[0] + "\t" + "< Project name >" + "\t|\t" + "< Location >" + "\t|\t" + "< status >" + "\t|")
        TerminalDecor_mod.asciiSeperators.LineMid()
        for x in x:
            print(t.ter[0] + x[0] + "\t| " + x[1] + "\t| " + x[2])
        
        conn.commit()
        conn.close()
        


#---------------------------
# ! Project setup
#---------------------------
class projectSetup:
    global TargetDir

    def ProjectGen(RootDir, ArrInp):
        for i in range(len(ArrInp)):
            os.makedirs(RootDir + ArrInp[i])

    def ProjectStart():
        global TargetDir
        DirMount = input(t.ter[1] + "Input destination directroy: ")
        ProjectName = input(t.ter[1] + "Project name: ")
        ProjectStatus = input(t.ter[1] + "Project status (e.g; PRODUCTION, legacy, University, portfilio): ")
        
        TargetDir = DirMount + "/" + ProjectName
        
        # Arguments: name, ProjLoc, status
        database.sqlInput_proj(ProjectName, TargetDir, ProjectStatus)


    def ProjectSetup():
        TerminalDecor_mod.asciiSeperators.LineMid()

        print(t.ter[0], "Choose project structure type: ")
        TerminalOptions = ["Location: FLD/home/create/ProjectSetup",
                        "a    : animation",
                        "c    : character modelling", 
                        "g    : generic, catch-all project set-up",
                        "e    : environment modelling",
                        "back : return to home"]
        
        TerminalDecor_mod.asciiRicing.lister(TerminalOptions)
        i = 0
        while i < 1:
            ProjectPreset = input(t.ter[1])
            if ProjectPreset == "a": # Animation preset (7 folders)
                projectSetup.ProjectGen(TargetDir, dict.dirs.RENDER.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCENES.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.ASSET.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.REF.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.UE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.X.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCRPT.value)
                s.copy("./exporters/SceneExport_anima.py", TargetDir + "/scripts")
                print(t.ter[2], "Project created in:", TargetDir)
                i += 1

            if ProjectPreset == "c": # character modelling preset (8 folders)
                projectSetup.ProjectGen(TargetDir, dict.dirs.CONCEPT_ART.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.RENDER.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCENES.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.TEXTURE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.ASSET.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.X.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.UE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCRPT.value)
                s.copy("./exporters/SceneExport_character.py", TargetDir + "/scripts")
                print(t.ter[2], "Project created in:", TargetDir)
                i += 1

            if ProjectPreset == "G": # generic preset (9 folders)
                projectSetup.ProjectGen(TargetDir, dict.dirs.CONCEPT_ART.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.RENDER.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCENES.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.TEXTURE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.ASSET.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.REF.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCRPT.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.UE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.X.value)
                print(t.ter[2], "Project created in:", TargetDir)
                i += 1
            
            if ProjectPreset == "e": # generic preset (10 folders)
                projectSetup.ProjectGen(TargetDir, dict.dirs.CONCEPT_ART.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.RENDER.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCENES.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.TEXTURE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.ASSET.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.HOU.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.REF.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.SCRPT.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.UE.value)
                projectSetup.ProjectGen(TargetDir, dict.dirs.X.value)
                s.copy("./exporters/SceneExport_env.py", TargetDir + "/scripts")
                print(t.ter[2], "Project created in:", TargetDir)
                i += 1

            if ProjectPreset == "back":
                commands.StartingMenu()

            else:
                print(t.ter[0], "Unrecogised")


    def WorkspaceFiles():
            """ Writes scripts and Workspace files to project """
            TerminalOptions = ["Location: FLD/home/create/ProjectSetup/WorkspaceFiles",
                               "a       : animation workspace",
                               "c       : character modelling and rigging",
                               "e       : environment modelling. Contains houdini folder.",
                               "g       : generic project",
                               "maya    : include maya workspace",
                               "back    : go back"]
            
            print(t.ter[1], "choose workspace type")
            WorkspaceChoice = input(t.ter[1])


            if "a" in WorkspaceChoice:
                s.copy("./workspaces/WorkFile_animation.blend", TargetDir)
                s.copy("./exporters/SceneExport_anima.py", TargetDir + dict.dirs.SCRPT.value[1])

            if "c" in WorkspaceChoice:
                s.copy("./workspaces/WorkFile_character.blend", TargetDir)
                s.copy("./exporters/SceneExport_character.py", TargetDir + dict.dirs.SCRPT.value[1])

            if "e" in WorkspaceChoice:
                s.copy("./workspaces/WorkFile_env.blend", TargetDir)
                s.copy("./exporters/SceneExport_env.py", TargetDir + dict.dirs.SCRPT.value[1])

            if "g" in WorkspaceChoice:
                s.copy("./workspaces/WorkFile_generic.blend", TargetDir)

            if "maya" in WorkspaceChoice:
                s.copy("./workspaces/workspace.mel", TargetDir) # i wanna get to this later

            if "-r" in WorkspaceChoice:
                pass 

            if WorkspaceChoice == "back":
                commands.StartingMenu()



#---------------------------
# ! FREIGHTING
#---------------------------
class freight:
    def freighting():
        TerminalDecor_mod.asciiSeperators.LineMid()
        DepartCommands = ["Location: FLD/home/freighting",
                        "Commands",
                        "basic        : move specific folders/files. No need for registered projects/exes",
                        "intermodal   : schedule exporting from registered projects",
                        "back         : Move to previous"]
        TerminalDecor_mod.asciiRicing.lister(DepartCommands)

        DepartCommands_input = input(t.ter[1])
        if DepartCommands_input == "basic":
            print(t.ter[0], "input move directory:")
            TargetFile = input(t.ter[1])
            print(t.ter[0], "Specify final move directory:")
            FinalDir = input(t.ter[1])
                
            ricing.wait()
            s.move(TargetFile, FinalDir)


        if DepartCommands_input == "intermodal":
            conn = sqlite3.connect("register.db")
            c = conn.cursor()
            
            lmba_ExportChange = lambda name: "SceneExport_" + ExportScript_selection + ".py"
            lmba_ProjectAdder = lambda db_name, scene: db_name + scene
            lmba_ProjectAdder1= lambda db_name, BridgePath, scene: db_name + BridgePath + scene

            """ select executable """
            exe_output = c.execute("SELECT binaryName FROM vital;")
            exe_output = c.fetchall()
            
            for exe_output in exe_output:
                print(t.ter[0] + exe_output[0])

            
            BinSelect = input(t.ter[1] + "input exe name: ")
            
            exe_location = c.execute("SELECT BinLocation FROM vital WHERE binaryName = (?)", 
                                     (BinSelect,))
            exe_location = c.fetchone()

            database.sqlReadProj()
            
            print(t.ter[0])
            selection = input(t.ter[1] + "select project: ")

            """ Project directory selection """
            db_output = c.execute("SELECT ProjDir FROM projects WHERE ProjName = (?)", 
                                  (selection,))
            db_output = c.fetchone()

            conn.commit()
            conn.close()

            """ Scene file selection """
            print(t.ter[0] + "\n" + t.ter[0] + "Current directory:" + "\n" + db_output[0])
            SceneFile = input(t.ter[0] + "select scene file:" + "\n" + t.ter[1])


            """ Exporting script """
            ExporterList = ["Select export settings",
                            "anima      : animation export",
                            "b2sub      : blender to substance painter",
                            "character  : character exporter",
                            "env        : environment exporter"]
            TerminalDecor_mod.asciiRicing.lister(ExporterList)
            ExportScript_selection = input(t.ter[1])
            
            """ shell exporter """
            ExportScript = lmba_ExportChange(ExportScript_selection)
            MetaSceneRoot = lmba_ProjectAdder(db_output[0], SceneFile)
            ExportScript_final = lmba_ProjectAdder1(db_output[0], "/scripts/exporters/", ExportScript)

            print(t.ter[2] + db_output[0])
            print(t.ter[2] + SceneFile)
            print(t.ter[2] + BinSelect)
            print(t.ter[2] + ExportScript_final)
            
            ricing.wait("Departing freight...")
            sheller.portSystem.ShellPorter("WIN", 
                                           exe_location[0], 
                                           BinSelect, 
                                           MetaSceneRoot, 
                                           ExportScript_final)
            commands.StartingMenu() # returns user to start menu

        if DepartCommands_input == "back":
            commands.StartingMenu()
        
        commands.StartingMenu() #returns user to start commands instead of quitting



#---------------------------
# ! Commands
#---------------------------
class commands:
    def StartingMenu():
        TerminalDecor_mod.asciiSeperators.LineOpen()
        TerminalOptions = ["Location: FLD/home",
                           "Commands:", 
                           "create      : (Create project structure)",  
                           "freight     : (Schedule file transfer)", 
                           "settings    : (set-up defaults)",
                           "quit;       : (Terminates FLD)"]
        
        TerminalDecor_mod.asciiRicing.lister(TerminalOptions)
        LoopBreaker = 0
        while LoopBreaker < 1:
            CommandInput = input(t.ter[1])
            if CommandInput == "create":
                LoopBreaker += 1
                projectSetup.ProjectStart()
                projectSetup.ProjectSetup()
                projectSetup.WorkspaceFiles()

            if CommandInput == "freight":
                LoopBreaker += 1
                freight.freighting()

            if CommandInput == "settings":
                LoopBreaker += 1
                commands.settings()

            if CommandInput == "quit;":
                LoopBreaker += 1
                ricing.quit()
            
            elif CommandInput == "quit":
                print(t.ter[0], "ERROR: its 'quit;', not 'quit'. Remember the semicolon at the end! :)")  
            else:
                print(t.ter[0])



    def settings():
            TerminalDecor_mod.asciiSeperators.LineMid()
            TerminalOptions = ["Location: FLD/home/settings",
                                "Syntax <command> <suffix command>",
                                "Avialable suffix commands -show | -reg | -rm",
                                "setup  : (create project register: RUN FIRST)", 
                                "exe    : register software binaries/.exe to database",
                                "proj   : (Register projects)",
                                "back   : go back (duh)"]

            TerminalDecor_mod.asciiRicing.lister(TerminalOptions)

            print(t.ter[0])
            CommandInput = input(t.ter[1])
            if CommandInput == "setup": # 
                database.sqlSetup()
                commands.StartingMenu()
            

            """ register to database """
            if CommandInput == "exe -reg": 
                database.sqlInput_vital()

            if CommandInput == "proj -reg": 
                database.sqlInput_proj()
                commands.StartingMenu()
            
            """ show registered items """
            if CommandInput == "exe -show":
                database.sqlReadExe()
                commands.StartingMenu()

            if CommandInput == "proj -show":
                database.sqlReadProj()
                commands.StartingMenu()

            if CommandInput == "back": # 
                commands.StartingMenu()

# run shit here
ricing.opening()
commands.StartingMenu()