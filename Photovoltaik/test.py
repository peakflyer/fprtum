import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd

volt_si_dark_a, response_si_dark_a = np.loadtxt("data/UI_a-Si_dark.txt", unpack=True, skiprows=4)
volt_si_light_a, response_si_light_a = np.loadtxt("data/UI_a-Si_light.txt", unpack=True, skiprows=4)
volt_si_dark_c, response_si_dark_c = np.loadtxt("data/UI_c-Si_dark.txt", unpack=True, skiprows=4)
volt_si_light_c, response_si_light_c = np.loadtxt("data/UI_c-Si_light.txt", unpack=True, skiprows=4)

plt.plot(response_si_light_a, np.gradient(volt_si_light_a, response_si_light_a))
print(np.gradient(volt_si_light_a, response_si_light_a)[51])
plt.yscale("log")
plt.show()

plt.plot(response_si_light_c[:107], np.gradient(volt_si_light_c[:107], response_si_light_c[:107]))
print(np.gradient(volt_si_light_c[:107], response_si_light_c[:107])[51])
plt.yscale("log")
plt.show()
