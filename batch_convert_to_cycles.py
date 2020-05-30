# For Blender 2.79 only - will not work in 2.80+
# Make sure you enable the add-on "Materials Utils Special" in the Preferences window

import bpy
import os
import glob

# CONFIG BEGINS HERE

# Directory of Blend files to convert. Should end in // or /. Script won't run if invalid

blend_file_directory = "C://Path//To//Your//Blend//File/Folder//"

# File extension of the converted file. .blend will *REPLACE* the original copy -
# if "Save Versions" in Blender preferences is less than 1. Otherwise, a '.blend1' of the original
# will be saved. Can also be changed to something else to ensure nothing is overwritten.

file_extension = ".blend"

# Whether or not to recurse through the folder above. If you have all your Blender
# files in seperate, individual folders, you want this to be "True". Otherwise, if you
# only want to convert Blend files in a specific folder, and ignore sub-folders, you want
# this to be "False".

recurse = True

# CONFIG ENDS HERE

blend_files = []
for file in glob.iglob(blend_file_directory + "**/*.blend", recursive=recurse):
    blend_files.append(file)

for file in blend_files:
    try:
        print("Opening: " + file)

        bpy.ops.wm.open_mainfile(filepath=file)

        converted_name = bpy.path.display_name(file) + file_extension
        converted_path = os.path.dirname(file) + "/" + converted_name

        bpy.ops.ml.refresh()

        print("Saving as: " + converted_path)

        bpy.ops.wm.save_as_mainfile(filepath=converted_path, check_existing=False)
    except:
        print("Failed to open: " + file)
        continue
