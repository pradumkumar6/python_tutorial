import seaborn as sns
from matplotlib import pyplot as plt
fmri = sns.load_dataset("fmri")
# fmri.head()
# fmri.shape()

sns.lineplot(x="timepoint",y="signal",data=fmri)
plt.show()