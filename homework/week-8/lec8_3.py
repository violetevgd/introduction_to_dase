import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

fmri = sns.load_dataset("fmri")
ax = sns.lineplot(x="timepoint", y="signal", hue="event", style="event",
markers=True, dashes=False, data=fmri)
plt.show()

ax = sns.barplot(x="day", y="total_bill", hue='sex', data=tips,
estimator=np.median, capsize=0.2, errcolor='c')
plt.show()