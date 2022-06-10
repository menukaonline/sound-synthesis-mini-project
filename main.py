try:
    import numpy as np
    import scipy.io.wavfile as wav
    import scipy.signal
    import matplotlib.pyplot as plt
    import sounddevice as sd
except ImportError:
    import pip
    pip.main(['install', '--user', 'numpy', 'scipy', 'matplotlib', 'sounddevice'])
    import numpy as np
    import scipy.io.wavfile as wav
    import scipy.signal
    import matplotlib.pyplot as plt
    import sounddevice as sd

sampleRate = 44100

