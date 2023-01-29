#using this to test out the os module

import os

path = "/home/user/Downloads/CyberPunk/"
os.chdir(path)




for audioFile in os.listdir():

    if(audioFile.endswith('m4a')):
        print(audioFile[0:len(audioFile)-4], "is an m4a")

    elif(audioFile.endswith('.opus')):
        print(audioFile[0:len(audioFile)-5] , "is an opus")
    else:
        print("none")



