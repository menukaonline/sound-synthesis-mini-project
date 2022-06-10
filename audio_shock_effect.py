from main import *

time = np.linspace(0, 1, sampleRate*1)
frequency1 = 100
y = np.sin(np.sin(2*np.pi*frequency1*time)*2*np.pi*frequency1)
sd.play(y, sampleRate)
wav.write("audio_shock_effect.wav", sampleRate, y)
plt.plot(time[:100], y[:100])
plt.show()
