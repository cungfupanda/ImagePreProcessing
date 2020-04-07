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

    top_left = [157,0]

    path_to_file = r'ImagePreProcessing/packages/annotations.0.json'

    AP = Annotation_Parser(path_to_file)
    AP.Parse_File(top_left)
    

   

