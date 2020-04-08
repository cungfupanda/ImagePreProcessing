import os
import json
import numpy as np


class Annotation_Parser(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def Parse_File(self, top_left):

         with open(self.filePath, "r") as f:
            data = json.load(f)
            #print(data["classes"])
            print(len(data["classes"]))
            for item in data["classes"]:
                for i in range(len(data["classes"][item])):
                        #print("Original Values: ", data["classes"][item][i]["2d-bounding-rectangle"])
                        data["classes"][item][i]["2d-bounding-rectangle"]["y"] = data["classes"][item][i]["2d-bounding-rectangle"]["y"]  - top_left[0]
                        data["classes"][item][i]["2d-bounding-rectangle"]["x"] = data["classes"][item][i]["2d-bounding-rectangle"]["x"]  - top_left[1]
                        #print("New Values: ", data["classes"][item][i]["2d-bounding-rectangle"])

            with open(self.filePath, "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent="\t")
                  
   

if __name__ == "__main__":
    print("Test script for annotation parser module")

    dest_directory = '/media/enda/750GB/3.ImageData/test-valeo-v5'

    for root, dirs, files in os.walk(dest_directory):
        for file in files:
            if file.endswith(".png"):
                print("Found an image")

    








'''
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

'''
    

   

