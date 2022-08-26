from main import *

time = np.linspace(0, 1, sampleRate*1)
frequency1 = 440
frequency2 = 880
y = np.sin(2*np.pi*(frequency1+(frequency2-frequency1)*time)*time)
sd.play(y, sampleRate)
wav.write("unknown_flute_object.wav", sampleRate, y)
plt.plot(time[:10000], y[:10000])
plt.show()

