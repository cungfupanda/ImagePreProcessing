import os
import cv2
import json
import numpy as np
import sys

sys.path.append(os.getcwd())
from packages.file_processing import File_Processing
from image_edit import Image_Edit


class Annotation_Parser(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def Parse_File(self, crop_value, cropped_image):
         box_points = [0, 0, 0, 0]
         with open(self.filePath, "r") as f:
            data = json.load(f)
            
            bounds = []
            boundpts = np.array([])
                
            for json_object, object_data in data.items():
                if json_object == "classes":
                    for class_name, details in object_data.items():
                        if class_name == "House":
                            
                            for elements in details[0]:    
                                print(details[0])    
                                print(elements)  

                                

                                x = details[1]['2d-bounding-rectangle']['x']
                                y = details[1]['2d-bounding-rectangle']['y']
                                w = details[1]['2d-bounding-rectangle']['width']
                                h = details[1]['2d-bounding-rectangle']['height']

                                #probably easiest to edit inline

                                box_points = [x, y, w, h]

                                top_line = int((crop_value[1] - crop_value[0])/2)

                                cropped_image = cv2.rectangle(cropped_image,(box_points[0], box_points[1]-top_line),(box_points[0] + box_points[2],(box_points[1]-top_line) + box_points[3]),(0,255,0),2)
                                
                                cv2.imshow("Cropped Image", cropped_image)
                                cv2.waitKey(0)


            return box_points

            
                            
                    
                
        

if __name__ == "__main__":
    print("Test script for annotation parser module")

    crop_value = [966,1280]

    top_line = int((crop_value[1] - crop_value[0])/2)

    img = cv2.imread("packages/color.0.png")
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)

    IE = Image_Edit("packages/color.0.png")
    cropped_image = IE.Crop_Image([966,1280])
    

    path_to_file = r'packages/annotations.0.json'

    AP = Annotation_Parser(path_to_file)
    box_points = AP.Parse_File(crop_value, cropped_image)
    print(box_points)

    #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    img = cv2.rectangle(img,(box_points[0], box_points[1]),(box_points[0] + box_points[2],box_points[1] + box_points[3]),(0,255,0),2)
    cropped_image = cv2.rectangle(cropped_image,(box_points[0], box_points[1]-top_line),(box_points[0] + box_points[2],(box_points[1]-top_line) + box_points[3]),(0,255,0),2)
    
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

   

