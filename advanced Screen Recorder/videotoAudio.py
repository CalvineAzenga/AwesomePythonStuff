import moviepy.editor


video=moviepy.editor.VideoFileClip('5 Seconds of Summer - She Looks So Perfect (Official Video)_2.mp4')

audio=video.audio

audio.write_audiofile('5 Seconds of Summer - She Looks So Perfect (Official Video)_2.mp3')


