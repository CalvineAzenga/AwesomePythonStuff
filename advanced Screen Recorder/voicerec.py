# import pyaudio
# import wave

# chunk=1024
# sample_format=pyaudio.paInt16
# channels=2

# sml_rt=44400
# seconds=40
# filename="pathtofile.wav"
# pa=pyaudio.PyAudio()

# stream=pa.open(format=sample_format,channels=channels,rate=sml_rt,input=True,frames_per_buffer=chunk)
# print("Recording...")

# frames=[]

# for i in range(0,int(sml_rt/chunk*seconds)):
#     data=stream.read(chunk)
#     frames.append(data)

# stream.stop_stream()
# stream.close()
# pa.terminate()

# print("Done !!!")

# sf=wave.open(filename,'wb')
# sf.setnchannels(channels)
# sf.setsampwidth(pa.get_sample_size(sample_format))
# sf.setframerate(sml_rt)
# sf.writeframes(b''.join(frames))
# sf.close()
