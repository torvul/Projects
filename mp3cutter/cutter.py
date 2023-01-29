# IT WORKS: EMAIL ME Torvul16@Gmail.com if you have questions about it

from pydub import AudioSegment
import os

path = "/home/user/Downloads/CyberPunk"
os.chdir(path)




for audioFile in os.listdir():
    sound = AudioSegment.from_file(audioFile)

    # 34000 = 34 seconds from the end
    cutPoint = len(sound) - 34000
    cut = sound[:cutPoint]

    # cut.export("first_half.mp3", format="mp3")
    if(audioFile.endswith('m4a')):
        cut.export("/home/user/Desktop/CyberPunk/"+audioFile[0:len(audioFile)-4]+".mp3" , format="mp3")
        print("FINISHED: " , audioFile)
    elif(audioFile.endswith('.opus')):
        cut.export("/home/user/Desktop/CyberPunk/"+audioFile[0:len(audioFile)-5]+".mp3" , format="mp3")
        print("FINISHED: " , audioFile)
    else:
        print("Did nothing")


