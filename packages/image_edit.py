import cv2

class Image_Edit(object):
    def __init__(self, image):
        self.image = cv2.imread(image)

    def Crop_Image(self, desired_res):
        cropped_image = self.image

        #Calculate the extremeties required image
        top_row = int((self.image.shape[0] - desired_res[0])/2)
        bottom_row = int(top_row + desired_res[0])
        left_col = int((self.image.shape[1] - desired_res[1])/2)
        right_col = int(left_col + desired_res[1])
        #print("{} : {} : {} : {}".format(top_row, bottom_row, left_col, right_col))

        #Perform the crop
        cropped_image = self.image[top_row:bottom_row, left_col:right_col]
        return cropped_image

    def Save_Image(self, path, image):
        cv2.imwrite(path, image)



if __name__ == "__main__":
    print("Processing Images")

    image = r"/media/enda/750GB/1.Coding/1.Python-Dev/ImagePreProcessing/data/test-valeo-v5/valeo2-streets-high-sun/node-176156457592450-sample-0/batch-0/FV/color-images/color.0.png"

    IE = Image_Edit(image)
    cropped_image = IE.Crop_Image([1280,966])   

    cv2.imshow("cropped_image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    print("Application Complete")