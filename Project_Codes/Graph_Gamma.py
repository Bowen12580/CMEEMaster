import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


file_path_1 = 'C:/Users/Lenovo/Desktop/gamma_no_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/gamma_confidence.csv'
data_confidence = pd.read_csv(file_path_2)
data_no_confidence = pd.read_csv(file_path_1)


indices = ['Shannon-Wiener', 'Simpson', 'Richness']
pre_adjustment = [
    data_no_confidence['Hill Number_1'].unique()[0],
    data_no_confidence['Hill Number_2'].unique()[0],
    data_no_confidence['Hill Number_0'].unique()[0]
]
post_adjustment = [
    data_confidence['Hill Number_1'].unique()[0],
    data_confidence['Hill Number_2'].unique()[0],
    data_confidence['Hill Number_0'].unique()[0]
]

bar_width = 0.3
index = np.arange(len(indices))


fig, ax1 = plt.subplots(figsize=(12, 8))


bars_pre = ax1.bar(index[:2], pre_adjustment[:2], bar_width, label='Pre-adjustment', color='#8ecae6')
bars_post = ax1.bar(index[:2] + bar_width, post_adjustment[:2], bar_width, label='Post-adjustment', color='#ffb703')

ax1.set_xlabel('Diversity Indices and Hill Number 0', fontsize=14)
ax1.set_ylabel('Index Value (γ Diversity)', fontsize=14, color='#000000')
ax1.set_title('Comparison of γ Diversity: Hill Numbers 0, Shannon-Wiener, and Simpson Indices', fontsize=16)
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(indices, fontsize=12)
ax1.tick_params(axis='y', labelcolor='#000000')


for i in range(2):
    ax1.text(index[i] + bar_width / 3, pre_adjustment[i] + 0.01, f'{pre_adjustment[i]:.2f}', ha='center', va='bottom', color='#000000', fontsize=12)
    ax1.text(index[i] + 3 * bar_width / 3, post_adjustment[i] + 0.01, f'{post_adjustment[i]:.2f}', ha='center', va='bottom', color='#000000', fontsize=12)


ax2 = ax1.twinx()
bars_pre_richness = ax2.bar(index[2:], pre_adjustment[2:], bar_width, label='Pre-adjustment', color='#8ecae6')
bars_post_richness = ax2.bar(index[2:] + bar_width, post_adjustment[2:], bar_width, label='Post-adjustment', color='#ffb703')

ax2.set_ylabel('Hill Number 0 (Species Richness)', fontsize=14, color='#000000')
ax2.tick_params(axis='y', labelcolor='#000000')


for i in range(2, len(indices)):
    ax2.text(index[i], pre_adjustment[i] + 0.001, f'{pre_adjustment[i]:.2f}', ha='center', va='bottom', color='#000000', fontsize=12)
    ax2.text(index[i]+ bar_width, post_adjustment[i] + 0.001, f'{post_adjustment[i]:.2f}', ha='center', va='bottom', color='#000000', fontsize=12)


handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.9), ncol=2, fontsize=12)


plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('C:/Users/Lenovo/Desktop/gamma.png', dpi=300)
plt.show()
