from PIL import Image
from os import listdir, remove, mkdir, path
from time import sleep

def clearCropped():
    for i in listdir():
        if "cropped" in i and path.isfile(i):
            remove(i)
            print("Removed " + str(i))
    sleep(3)

try:
    if(not path.exists("./cropped")):
        mkdir(path.join("./" + "cropped"))
except:
    raise("[Error] Couldn't create cropped directory. Perhaps a permission problem? Create it manually if you can: a directory called \"cropped\"")

print("Delete cropped files? [y/n]")
if "y" in str(input()):
    try:
        clearCropped()
    except:
        raise("[Error] Deleting cropped files failed. Perhaps there aren't any?")
else:
    print("Input crop coords (leave blank for defaults aka zoom):")
            
    print("(237 default) left = ", end = "")
    if len(input()) == 0: left = 237
    else: left = int(input())

    print("(96 default) top = ", end = "")
    if len(input()) == 0: top = 95
    else: top = int(input())

    print("(1460 default) right = ", end = "")
    if len(input()) == 0: right = 1460
    else: right = int(input())

    print("(1013 default) bottom = ", end = "")
    if len(input()) == 0: bottom = 1013
    else: bottom = int(input())

    print("\n\nStarting crop process..\n")

    original_listdir = listdir()

    for i in listdir():
        if i[-4:] == ".jpg" or i[-4:] == ".png":
            try:
                img = Image.open(i)
                croppedImg = img.crop((left, top, right, bottom))
                
                if i[-4:] == ".jpg": croppedImg.save("./cropped/" + i[:-4] + "_cropped.jpg")
                elif i[-4:] == ".png": croppedImg.save("./cropped/" + i[:-4] + "_cropped.png")
                else: pass

                print("[Success] Image " + str(i) + " has been cropped and saved succesfully.")
            except SystemError as e:
                print("[Error] Image " + str(i) + " has encountered error \"" + str(e) + "\"")
    
    print("\nWould you like to delete the originals? [y/n]")
    if "y" in str(input()):
        for i in original_listdir and path.isfile(i) and i[-4:] == ".jpg":
            remove(i)
