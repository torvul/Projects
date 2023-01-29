# Using this to test out the pydub audiosegment


from pydub import AudioSegment
sound = AudioSegment.from_file("testopus.opus")


# 34000 = 34 seconds from the end
cutPoint = len(sound) - 34000
cut = sound[:cutPoint]

# create a new file "first_half.mp3":
cut.export("first_half.mp3", format="mp3")
