from main import *

time = np.linspace(0, 1, sampleRate)
frequency1 = 512
frequency2 = 460
y = (np.sin(2*np.pi*frequency1*time)+np.sin(2*np.pi*frequency2*time))/2
sd.play(y, sampleRate)
wav.write("dialing_tone.wav", sampleRate, y)
plt.plot(time[:1000], y[:1000])
plt.show()
