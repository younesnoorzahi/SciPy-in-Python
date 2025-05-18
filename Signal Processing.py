from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, endpoint=False)
sig = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*20*t)

# Design a Butterworth filter
b, a = signal.butter(5, 15, 'low', fs=1000)
filtered = signal.filtfilt(b, a, sig)

plt.plot(t, sig, 'b-', label='Original')
plt.plot(t, filtered, 'r-', linewidth=2, label='Filtered')
plt.legend()
plt.show()