from moviepy.editor import *

clip=VideoFileClip("./saves/2021-07-27 18-43-59.mp4")
audioclip=AudioFileClip("5 Seconds of Summer - She Looks So Perfect (Official Video)_2.mp3")

length=clip.duration
audioclip=audioclip.subclip(0,length)
clip=clip.set_audio(audioclip)
clip.write_videofile("thiso.mp4")
