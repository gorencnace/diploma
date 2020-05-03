import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:\\Users\\ng0632\\Documents\\DIPLOMA\\lepi urejeni rezultati\\"

df = pd.read_csv(path + "NormalDistribution_examples_100_matU_2" + ".csv")
df.apply(pd.to_numeric)

print(df.head(10))

# circle_success = ((np.asarray(df['SO'])).reshape(41, 41))
# print(circle_success)

result = df.pivot(index='A2', columns='A1', values='KU')
print(result)

fig, ax = plt.subplots(figsize=(8, 8))
title = "N(0, 1), 100 primerov, uspešnost krožnic"
plt.title(title, fontsize=16)
ttl = ax.title
ttl.set_position([0.5, 1.05])

# https://matplotlib.org/tutorials/colors/colormaps.html
# cmap options: terrain, gnuplot(2), rainbow, jet, nipy_spectral, gist_ncar, qualitive looks nice
sns.heatmap(result, vmin=0, vmax=1, fmt="", cmap='YlOrRd', ax=ax, linewidths=1)

ax.invert_yaxis()
plt.xlabel('Atom (X, X) pri prvem odštevanju')
plt.ylabel('Atom (Y, Y) pri drugem odštevanju')
plt.show()