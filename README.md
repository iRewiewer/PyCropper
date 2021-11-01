# PyCropper
Small cropping utility using the PIL module. It crops all files in the current directory using the same measurements.

# How to use
Either run the `cropper.exe` or `python cropper.py` depending on what you've downloaded.

You'll be asked if you want to delete the cropped files in case of bad coords or whatnot.  
Answering `y` will delete all files containing the keyword `cropped` and end the program.

The program will then ask you for the measurements of the crop.  
The defaults are for shared screens on zoom fullscreen.  
  
Finally, if everything went right, all the cropped files will be placed in a newly created `cropped` directory.  
The program will also ask if you want to delete the original files.  
