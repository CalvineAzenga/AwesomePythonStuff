# import pyaudio
# import soundfile
# import wave

# chunk=1024
# sample_format=pyaudio.paInt16
# channels=2

# smpl_rt=44400
# filename="pathtofile.wav"
# pa=pyaudio.PyAudio()

# stream=pa.open(format=sample_format,channels=channels,rate=smpl_rt,input=True,frames_per_buffer=chunk)
# print("Recording...")

# frames=[]
# a=0
# while a<100:
#     data=stream.read(chunk)
#     frames.append(data)
#     a+=1
#     print(a)    

# stream.stop_stream()
# stream.close()
# pa.terminate()

# print("Done !!!")
# import numpy as np
# rec=soundfile.write(filename, np.random.randn(10010000, 2), 44100, 'PCM_24')
# sf=wave.open(filename,'wb')
# sf.setnchannels(channels)
# sf.setsampwidth(pa.get_sample_size(sample_format))
# sf.setframerate(smpl_rt)
# sf.writeframes(b''.join(frames))
# sf.close()

import mss
from PIL import Image
asd=mss.mss()
print(asd.monitors)
img=asd.grab(asd.monitors[1])
dssd=Image.frombytes("RGB",img.size,img.bgra,"raw","BGR")
dssd.save('cally.png')



