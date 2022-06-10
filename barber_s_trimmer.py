from main import *

# Barber's_Trimmer
time = np.linspace(0, 1, sampleRate)
frequency = 100
y = scipy.signal.sawtooth(2*np.pi*frequency*time)
sd.play(y, sampleRate)
wav.write("barber_s_trimmer.wav", sampleRate, y)
plt.plot(time[:2000], y[:2000])
plt.show()
