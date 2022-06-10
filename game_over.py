from main import *

time = np.linspace(0, 1, sampleRate)
frequency1 = 440
frequency2 = 220
y = scipy.signal.square(2*np.pi*(frequency1+(frequency2-frequency1)*time)*time)
sd.play(y, sampleRate)
wav.write("game_over.wav", sampleRate, y)
plt.plot(time, y)
plt.show()
