#Adding the project directory to the path
import sys
import os
import cv2
import shutil
import PySimpleGUI as sg

sys.path.append(os.getcwd())
from packages.file_processing import File_Processing
from packages.image_edit import Image_Edit


def Process_Images(folder_path, resolution):
    source_directory = folder_path
    dest_directory = source_directory + '_cropped'

    FP = File_Processing(source_directory, dest_directory)
    FP.Copy_Directory()


    ##Iterate the new directory looking for '.png' files
    for root, dirs, files in os.walk(dest_directory):
        for file in files:
            if file.endswith(".png"):
                png_file = os.path.join(root, file)
                img = cv2.imread(png_file)

                IE = Image_Edit(png_file)
                cropped_image = IE.Crop_Image(resolution)  
                if os.path.isfile(png_file):
                    os.remove(png_file)
                IE.Save_Image(png_file, cropped_image)
                cv2.imshow("Image", cropped_image)
                cv2.waitKey(5)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Running main module")
    
    sg.theme('DarkAmber')   # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Select the base directory path, and the required resolution')],
                [sg.In(key='-FOLDER_PATH-') ,sg.FolderBrowse()],
                [sg.InputText(key='-WIDTH-'), sg.Text('Image Width'),],
                [sg.InputText(key='-HEIGHT-'), sg.Text('Image Height')],
                [sg.Button("Process"), sg.Cancel(), ]]
    location = (100, 100)
    # Create the Window
    window = sg.Window('Image Pre-Processing', layout, location = location)
    # Event Loop to process "events"
    while True:           
        event, values = window.read()
        width = int(values['-WIDTH-'])
        height = int(values['-HEIGHT-'])
        folder_path = values['-FOLDER_PATH-']

        if event in (None, 'Cancel'):
            break

        if event == 'Process':
            resolution = [height, width]
            print(resolution)
            Process_Images(folder_path, resolution)

    window.close()
    print("Finished executing main module")







    