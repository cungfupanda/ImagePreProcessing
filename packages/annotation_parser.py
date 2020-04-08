import os
import cv2
import json
import numpy as np


class Annotation_Parser(object):
    def __init__(self):
        pass

    def Parse_File(self, filePath, top_left):

         with open(filePath, "r") as f:
            data = json.load(f)
            for item in data["classes"]:
                for i in range(len(data["classes"][item])):
                        #print("Original Values: ", data["classes"][item][i]["2d-bounding-rectangle"])
                        data["classes"][item][i]["2d-bounding-rectangle"]["y"] = data["classes"][item][i]["2d-bounding-rectangle"]["y"]  - top_left[0]
                        data["classes"][item][i]["2d-bounding-rectangle"]["x"] = data["classes"][item][i]["2d-bounding-rectangle"]["x"]  - top_left[1]
                        
                        for polygons in range(len(data["classes"][item][i]["polygons"])):
                                for points in range(len(data["classes"][item][polygons]["polygons"][0]["polygon"])):
                                    print("{} {} {} ".format(item, polygons, points))
                                    #print((data["classes"][item][polygons]["polygons"][0]["polygon"][points]["x"]))
                                    #print("Top Left: {}".format(top_left))
                                    data["classes"][item][polygons]["polygons"][0]["polygon"][points]["y"] = data["classes"][item][polygons]["polygons"][0]["polygon"][points]["y"]- top_left[0]
                                    data["classes"][item][polygons]["polygons"][0]["polygon"][points]["x"] = data["classes"][item][polygons]["polygons"][0]["polygon"][points]["x"]- top_left[1]
                                    #print((data["classes"][item][polygons]["polygons"][0]["polygon"][points]["y"]))
                        
                        #if item == "Bicycle":
                            #print("Found Bicycle")
                            

                                    #print(len(data["classes"][item][polygons]["polygons"][0]["polygon"]))
                            #print(len(data["classes"][item][i]["polygons"]))
                        #print("New Values: ", data["classes"][item][i]["2d-bounding-rectangle"])

            #with open(filePath, "w", encoding='utf-8') as f:
                #json.dump(data, f, ensure_ascii=False, indent="\t")

            with open(filePath, "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)


            

            
                            
                    
                
        

if __name__ == "__main__":
    print("Test script for annotation parser module")


    top_left = [157,0]

    path_to_file = r'/media/enda/750GB/3.ImageData/test-valeo-v5_cropped/valeo2-streets-high-sun/node-176156457592450-sample-0/batch-0/FV/annotations/annotations.0.json'

    AP = Annotation_Parser()
    AP.Parse_File(path_to_file, top_left)

    

   

