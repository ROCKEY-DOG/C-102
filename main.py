import os
import shutil

# .exe, .msi, .gif, .png, .jpg, .jpeg, .cvs, .pdf, .xls, .xlsx, .pptx

from_dir = "C:/Users/amari/OneDrive/Desktop/whjr/C-102/C102_assets-main"
to_dir = "C:/Users/amari/OneDrive/Desktop/whjr/C-102/C102_assets-main/images"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

# Move All Images files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jfif']:
        path1 = from_dir + '/' + file_name                      #Example path1 : Downloads/ImageNmae1.jpg
        path2 = to_dir + '/' + "Images_Files"                   #Example path2 : D:/My Files/Image_Files
        path3 = to_dir + '/' + "Images_Files" + '/' + file_name #Example path3 :D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 ", path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exits Before Moving
        #Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
            print("Moving " + file_name + ".........")

            # Move form path1 ---. path3
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".........")
            shutil.move(path1, path3)