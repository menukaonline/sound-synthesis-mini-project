from main import *

time = np.linspace(0, 5, sampleRate*3)
low_pass = scipy.signal.butter(6, 1000, fs=sampleRate, output="sos")
y = np.random.random(time.size)
y = scipy.signal.sosfilt(low_pass, y)
sd.play(y, sampleRate)
wav.write("wind.wav", sampleRate, y)
plt.plot(time, y)
plt.show()
