import os
import shutil


class File_Processing(object):
    def __init__(self, src, dst):
        self.source_directory = src
        self.dest_directory = dst

    def Copy_Directory(self):
        if os.path.isdir(self.dest_directory):
            print("This is already a directory, overwriting ... ")
            shutil.rmtree(self.dest_directory)

        print("Duplicating source directory, please wait")
        shutil.copytree(self.source_directory, self.dest_directory)

        print("Finished duplicating source directory")

    



if __name__ == "__main__":
    print("Main Function Executing")

    source_directory = r'/media/enda/750GB/1.Coding/1.Python-Dev/ImagePreProcessing/data/test-valeo-v5'
    dest_directory = source_directory + '_cropped'

    FP = File_Processing(source_directory, dest_directory)
    FP.Copy_Directory()

    