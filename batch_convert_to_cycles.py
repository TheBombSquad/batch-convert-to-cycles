# For Blender 2.79 only - will not work in 2.80+
# Make sure you enable the add-on "Materials Utils Special" in the Preferences window

import bpy
import glob

# CONFIG BEGINS HERE

# Directory of Blend files to convert. Should not end in / or \. Script won't run if invalid
blend_file_directory = "C://Path//To//Your//Blend//File/Folder"

# File extension of the converted file. .blend will *REPLACE* the original copy -
# if "Save Versions" in Blender preferences is less than 1. Otherwise, a '.blend1' of the original
# will be saved. Can also be changed to something else to ensure nothing is overwritten.
file_extension = ".blend"

# CONFIG ENDS HERE

blend_files = glob.glob(blend_file_directory + "/*.blend")
for file in blend_files:
    try:
        print("Opening: " + file)

        bpy.ops.wm.open_mainfile(filepath=file)

        converted_name = bpy.path.display_name(bpy.data.filepath) + file_extension
        converted_path = blend_file_directory + "/" + converted_name

        bpy.ops.ml.refresh()

        bpy.ops.wm.save_as_mainfile(filepath=converted_path, check_existing=False)
    except:
        print("Failed to open: " + file)
        continue
