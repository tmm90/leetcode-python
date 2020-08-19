import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(1, 100.0, 1)
s1 = t
s2 = [x**2 for x in np.log2(t)]

fig, ax = plt.subplots()

ax.plot(t, s1, "--", label=r"$N$")
ax.plot(t, s2, label=r"$(log_{2}(N))^{2}$")

ax.set(xlabel='N',
       title='Complexity comparison between $N$ and $(log_{2}(N))^{2}$')
ax.grid()
ax.legend()

fig.savefig("0222_comparison_of_complexity.svg")
