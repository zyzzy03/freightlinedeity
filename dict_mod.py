from enum import Enum

# currently in use!
class dirs(Enum):
    dir_n = 10
    CONCEPT_ART = ["/ConceptArt", "/ConceptArt/ColourScripts", "/ConceptArt/illustration"]
    RENDER = ["/render","/render/submission", "/render/output"]
    SCENES = ["/scenes", "/scenes/blender", "/scenes/max", "/scenes/maya", "/scenes/USD"]
    TEXTURE = ["/texture", "/texture/substance", "/texture/substance/designer", "/texture/substance/painter", "/texture/export", "/texture/import", "/texture/import/low", "/texture/import/assets", "/texture/import/high"]
    ASSET = ["/asset", "/asset/models", "/asset/materials", "/asset/animations"]
    HOU = ["/hou"]
    REF = ["/ref"]
    SCRPT = ["/scripts", "/scripts/exporters"]
    UE = ["/engine/unreal", "/engine/godot", "/engine/unity"]
    X = ["/xMisc", "/xMisc/critique", "/xMisc/notes", "/xMisc/submission"]

# I'm only using an Enum because its cleaner visually, more readable, and the syntax isnt all fucky.
# unlike dictionaries....