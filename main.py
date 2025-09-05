import time, sys, os, shutil as s, subprocess, sqlite3
import TerminalDecor_mod
import ter_mod as t
import dict_mod as dict
import sheller_mod as sheller
import tree_mod as tree

from rich.console import Console
from rich.table import Table
from rich.progress import track

# THIRD PROTOTYPE
# ~ Alpha (v04x onwards)~
# (v041) Cosmetic improvements (Tables, colours, Unix port, and GitHub release!)
# (v042) Substance Painter import
# (v05) Unreal Engine import (mesh and materials)
# (v06) Maya workspace.mel project creation

# ~~ Beta ~~ (Binary release)
# (v07) Compiled binary release
# (v08) Qt GUI instead of terminal
# (v09) 3DS Max workspaces

# im gonna rewrite this in C++, one day, and when I mean one day
# i mean when i get the gcc compiler to fucking run

class initalising:
    pass


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
            
            for i in track(range(DepartTime), description=f"{t.ter[0]} progress: "):
                time.sleep(1)
            print(t.ter[0], "Departed! <(^_^)>")
            

    def exiting():
        print(t.ter[0], "type and enter anything to exit:")
        exit_letter = input(t.ter[1])

    def ShowScenes():
        pass


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
    def sqlInput_proj(name, ProjLoc, status):
        TerminalDecor_mod.asciiSeperators.LineMid()
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        # name = input("> Project name: ")
        # ProjLoc = input("> Project root: ")
        # status = input("> status (e.g; PRODUCTION, legacy, LTS, experimental): ")

        c.execute("INSERT INTO projects VALUES (?,?,?);", (name, ProjLoc, status))

        conn.commit()
        conn.close()
        print(t.ter[0], name, "registered! ^^")

    def sqlInput_proj_temp():
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

# SQL DELETE V ========================= V

    def sqlDelete_vital(delete_target):
        conn = sqlite3.connect("register.db")
        db_cursor = conn.cursor()
        
        db_cursor.execute("DELETE FROM vital WHERE binaryName = (?);", (delete_target,))

        conn.commit()
        conn.close()

    def sqlDelete_proj(delete_target):
        conn = sqlite3.connect("register.db")
        db_cursor = conn.cursor()
        
        db_cursor.execute("DELETE FROM projects WHERE binaryName = (?);", (delete_target,))

        conn.commit()
        conn.close()



# SQL READ V ========================= V
# FIX: MERGE BOTH OF THESE FUNCTIONS

    """ reading exe register """
    def sqlReadExe():
        TerminalDecor_mod.asciiSeperators.LineMid()
        
        conn = sqlite3.connect("register.db")
        c = conn.cursor()
        table = Table(title="< Registered software >")
        db_output = c.execute("""SELECT * FROM 'vital';""")
        db_output = c.fetchall()

        table.add_column("name", justify="left")
        table.add_column("version", justify="left")
        table.add_column("location", justify="left")
        table.add_column("status", justify="left")

        for db_output in db_output:
            table.add_row(db_output[0], db_output[1], db_output[2], db_output[3])

        console = Console()
        console.print(table)
        conn.commit()
        conn.close()



    """ reading exe register """
    def sqlReadProj():
        TerminalDecor_mod.asciiSeperators.LineMid()
        
        conn = sqlite3.connect("register.db")
        c = conn.cursor()

        table = Table(title="< Registered software >")
        db_output = c.execute("""SELECT * FROM 'projects';""")
        db_output = c.fetchall()

        table.add_column("Project name", justify="left")
        table.add_column("Location", justify="left")
        table.add_column("status", justify="left")

        for db_output in db_output:
            table.add_row(db_output[0], db_output[1], db_output[2])


        console = Console()
        console.print(table)
        conn.commit()
        conn.close()
        


#---------------------------
# ! Project setup
#---------------------------
class projectSetup:
    

    def ProjectGen(RootDir, ArrInp):
        for i in range(len(ArrInp)):
            os.makedirs(RootDir + ArrInp[i])

    def ProjectStart():
        global TargetDir
        global DirMount
        DirMount = input(t.ter[1] + "Input destination directroy: ")
        ProjectName = input(t.ter[1] + "Project name: ")
        ProjectStatus = input(t.ter[1] + "Project status (e.g; PRODUCTION, legacy, University, portfilio): ")
        
        TargetDir = str(DirMount + "/" + ProjectName)
        
        # Arguments: name, ProjLoc, status
        database.sqlInput_proj(ProjectName, TargetDir, ProjectStatus)


    def ProjectSetup():
        TerminalDecor_mod.asciiSeperators.LineMid()

        print(t.ter[0], "Choose project structure type: ")
        TerminalOptions = ["FLD/home/create/ProjectSetup",
                        "a    : animation",
                        "c    : character modelling", 
                        "g    : generic, catch-all project set-up",
                        "e    : environment modelling contains houdini",
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

            if ProjectPreset == "g": # generic preset (9 folders)
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
            TerminalOptions = ["FLD/home/create/ProjectSetup/WorkspaceFiles",
                            #    "a       : animation workspace",
                            #    "c       : character modelling and rigging",
                            #    "e       : environment modelling",
                               "g       : generic project",
                               "maya    : include maya workspace",
                               "-r      : Load pre-made resources into project",
                               "return    : go back"]
            
            TerminalDecor_mod.asciiRicing.lister(TerminalOptions)
            print(t.ter[1], "choose workspace type")
            WorkspaceChoice = input(t.ter[1])

            def CopyTo(loc, path): s.copy(loc, path)

            # if "a" in WorkspaceChoice:
            #     CopyTo("./workspaces/WorkFile_animation.blend", TargetDir)
            #     CopyTo("./exporters/SceneExport_anima.py", TargetDir + dict.dirs.SCRPT.value[1])

            # if "c" in WorkspaceChoice:
            #     CopyTo("./workspaces/WorkFile_character.blend", TargetDir)
            #     CopyTo("./exporters/SceneExport_character.py", TargetDir + dict.dirs.SCRPT.value[1])

            # if "e" in WorkspaceChoice:
            #     CopyTo("./workspaces/WorkFile_env.blend", TargetDir)
            #     CopyTo("./exporters/SceneExport_env.py", TargetDir + dict.dirs.SCRPT.value[1])

            if "g" in WorkspaceChoice:
                CopyTo(r"workspaces\WorkFile_generic.blend", TargetDir)
                CopyTo(r"exporters\SceneExport_b2sub.py", TargetDir + dict.dirs.SCRPT.value[1])

            if "maya" in WorkspaceChoice:
                CopyTo(r"workspaces/workspace.mel", TargetDir) # i wanna get to this later

            if "-r" in WorkspaceChoice:
                CopyTo("./resources", TargetDir + dict.dirs.X.value[0])

            if WorkspaceChoice == "return":
                commands.StartingMenu()

#---------------------------
# ! FREIGHTING
#---------------------------
class freight:
    def freighting():
        TerminalDecor_mod.asciiSeperators.LineMid()
        DepartCommands = ["FLD/home/freighting",
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
            # TO DO: Make this to comply with PEP8
            
            # # NOTE: this has the amount of elegance as an ozzy osbourne
            # interview in 1983
            
            conn = sqlite3.connect("register.db")
            c = conn.cursor()
            # FIX: After learning f-strings, I need to remove the lambdas
            # lmba_Script = lambda user_selection : "SceneExport_" + user_selection + ".py"
            lmba_ProjectAdder = lambda db_name, scene: db_name + scene
            lmba_ProjectAdder1= lambda db_name, BridgePath, scene: db_name + BridgePath + scene

            """ select executable """
            exe_output = c.execute("SELECT binaryName, version, status FROM vital;")
            exe_output = c.fetchall()
            
            for exe_output in exe_output:
                print(t.ter[0], "< Exe >" , "\t|\t", "< version >", "\t|\t", "< status >", "\t|")
                print(t.ter[0] + exe_output[0], "\t|\t", exe_output[1], "\t|\t", exe_output[2], "\t|")

            BinSelect = input(t.ter[1] + "input exe name: ")
            exe_location = c.execute("SELECT BinLocation FROM vital WHERE binaryName = (?)", 
                                                                               (BinSelect,))
            exe_location = c.fetchone()


            """ Project directory selection """
            database.sqlReadProj()            
            print(t.ter[0])
            selection = input(t.ter[1] + "select project: ")

            db_output = c.execute("SELECT ProjDir FROM projects WHERE ProjName = (?)", 
                                  (selection,))
            db_output = c.fetchone()

            conn.commit()
            conn.close()


            """ Scene file selection """
            def SceneSelection():
                global command_input # this could potentually cause varible leaks
                print(t.ter[0] + f"\n{t.ter[0]} Current scene directory: \n{t.ter[0]} {db_output[0]}/scene")
                tree.LookInside(db_output[0], f"/{BinSelect}")
                command_input = input(f"{BinSelect}/>")

            def CheckMereExistance(x):
                path_existance = os.path.exists(x)
                print(f"{t.ter[2]}{x}")
                print(f"{t.ter[2]} {path_existance}")

                if path_existance == False:
                    print(f"{t.ter[0]} ERROR! Path {x} not found!")
                    SceneSelection()
                if path_existance == True:
                    return

            SceneSelection()
            killswitch = 0
            while killswitch < 1:
                if "look inside" in command_input:
                    CheckMereExistance(f"{db_output[0]}/scenes/{BinSelect}/{command_input[12:len(command_input)]}")
                    
                    print(t.ter[0] + f"found inside: {selection}/scenes/{BinSelect}/{command_input[12:len(command_input)]}")
                    tree.LookInside(db_output[0], f"{BinSelect}/{command_input[12:len(command_input)]}")
                    SceneSelection()
                    
                if "select" in command_input:
                    CheckMereExistance(f"{db_output[0]}/scenes/{BinSelect}/{command_input[7:len(command_input)]}")
                    selected_scene_location = f"{db_output[0]}/scenes/{BinSelect}/{command_input[7:len(command_input)]}"
                    killswitch += 1

                else:
                    print(f"{t.ter[0]} ERROR! Unrecognised command! :(")
                    SceneSelection()
            



            """ Script selection """
            TerminalOptions = ["Exporter preset:",
                               "generic     : generic expoter, works for all scenes",
                               "b2sub       : [WIP] Exports high and low poly models to substance painter"]
            TerminalDecor_mod.asciiRicing.lister(TerminalOptions)
            script_selection = input(f"{t.ter[0]} Select exporter: \n {t.ter[1]}")

            # continuation of the scripts
            """ shell exporter """
            ExportScript = f"SceneExport_{script_selection}.py"

            MetaSceneRoot = f"{db_output[0]}{command_input[7:len(command_input)]}"
            ExportScript_final = f"{db_output[0]}/scripts/exporters/{ExportScript}"

            print(t.ter[2] + f"Project dir: {db_output[0]}")
            print(t.ter[2] + f"Scene dir: {selected_scene_location}")
            print(t.ter[2] + f"selected bin/exe: {BinSelect}")
            print(t.ter[2] + f"selected exporter: {ExportScript_final}")
            
            ricing.wait("Departing freight...")
            sheller.portSystem.ShellPorter("WIN",
                                           exe_location[0],
                                           BinSelect,
                                           selected_scene_location,
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
        TerminalOptions = ["FLD/home",
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
                commands.StartingMenu()

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
            TerminalOptions = ["FLD/home/settings",
                                "Syntax: <command> [space] <prompt>",
                                " -- Commands: --",
                                "show",
                                "add",
                                "delete",
                                "-- Prompts: --",
                                "setup      : (create project register: RUN FIRST)", 
                                "exe        : register software binaries/.exe to database",
                                "proj       : (Register projects)",
                                "back       : go back (duh)"]

            TerminalDecor_mod.asciiRicing.lister(TerminalOptions)

            print(t.ter[0])

            i = 0
            while i < 1:
                CommandInput = input(t.ter[1])
                if CommandInput == "setup":
                    database.sqlSetup()
                    commands.StartingMenu()
                    i += 1

                """ adds binaries/exes and projects """
                if CommandInput == "add exe":
                    database.sqlInput_vital()
                    commands.StartingMenu()
                    i += 1

                if CommandInput == "add proj":
                    database.sqlInput_proj_temp()
                    commands.StartingMenu()
                    i += 1

                """ Delete DB data """
                if CommandInput == "delete exe":
                    database.sqlReadExe()
                    deletion_target = input(f"{t.ter[0]} Exe to delete: \n {t.ter[1]}")
                    database.sqlDelete_vital(deletion_target)
                    commands.StartingMenu()
                    i += 1

                if CommandInput == "delete proj":
                    database.sqlReadProj()
                    deletion_target = input(f"{t.ter[0]} Project name to delete: \n {t.ter[1]}")
                    database.sqlDelete_proj("projects")
                    commands.StartingMenu()
                    i += 1

                """ shows registered projects and executables """
                if CommandInput == "show exe":
                    database.sqlReadExe()
                    ricing.exiting()
                    commands.StartingMenu()
                    i += 1

                if CommandInput == "show proj":
                    database.sqlReadProj()
                    ricing.exiting()
                    commands.StartingMenu()
                    i += 1

                if CommandInput == "back":
                    commands.StartingMenu()
                    i += 1
                
                else:
                    print(t.ter[0])
                    i = 0


def RunHere():
    ricing.opening()
    commands.StartingMenu()


# run shit here
RunHere()