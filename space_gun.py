from main import *

time = np.linspace(0, 1, sampleRate*1)
frequency1 = 100
y = np.sin(np.sin(2*np.pi*5*time)*2*np.pi*frequency1)
sd.play(y, sampleRate)
wav.write("space_gun.wav", sampleRate, y)
plt.plot(time[:1000], y[:1000])
plt.show()
