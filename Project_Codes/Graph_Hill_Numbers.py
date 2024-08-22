import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'
data_confidence = pd.read_csv(file_path_1)
data_no_confidence = pd.read_csv(file_path_2)


mean_confidence = data_confidence.groupby('Year_Month').agg({
    'Hill Number_0': 'mean',
    'Hill Number_1': 'mean',
    'Hill Number_2': 'mean'
}).reset_index()

mean_no_confidence = data_no_confidence.groupby('Year_Month').agg({
    'Hill Number_0': 'mean',
    'Hill Number_1': 'mean',
    'Hill Number_2': 'mean'
}).reset_index()


months = mean_confidence['Year_Month']
hill_0_pre = mean_no_confidence['Hill Number_0']
hill_0_post = mean_confidence['Hill Number_0']

hill_1_pre = mean_no_confidence['Hill Number_1']
hill_1_post = mean_confidence['Hill Number_1']

hill_2_pre = mean_no_confidence['Hill Number_2']
hill_2_post = mean_confidence['Hill Number_2']


bar_width = 0.35
index = np.arange(len(months))


fig, axs = plt.subplots(1, 3, figsize=(18, 6))


bars_pre = axs[0].bar(index, hill_0_pre, bar_width, label='Pre-adjustment', color='#8ecae6')
bars_post = axs[0].bar(index + bar_width, hill_0_post, bar_width, label='Post-adjustment', color='#ffb703')
axs[0].set_title('Hill Number 0')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Hill Number')
axs[0].set_xticks(index + bar_width / 2)
axs[0].set_xticklabels(months, rotation=45, ha='right')


for bar in bars_pre:
    yval = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2, yval + 1, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)
for bar in bars_post:
    yval = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2, yval + 1, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)


bars_pre = axs[1].bar(index, hill_1_pre, bar_width, label='Pre-adjustment', color='#8ecae6')
bars_post = axs[1].bar(index + bar_width, hill_1_post, bar_width, label='Post-adjustment', color='#ffb703')
axs[1].set_title('Hill Number 1')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Hill Number')
axs[1].set_xticks(index + bar_width / 2)
axs[1].set_xticklabels(months, rotation=45, ha='right')


for bar in bars_pre:
    yval = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)
for bar in bars_post:
    yval = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)


bars_pre = axs[2].bar(index, hill_2_pre, bar_width, label='Pre-adjustment', color='#8ecae6')
bars_post = axs[2].bar(index + bar_width, hill_2_post, bar_width, label='Post-adjustment', color='#ffb703')
axs[2].set_title('Hill Number 2')
axs[2].set_xlabel('Month')
axs[2].set_ylabel('Hill Number')
axs[2].set_xticks(index + bar_width / 2)
axs[2].set_xticklabels(months, rotation=45, ha='right')


for bar in bars_pre:
    yval = bar.get_height()
    axs[2].text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)
for bar in bars_post:
    yval = bar.get_height()
    axs[2].text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2), ha='center', va='bottom', color='black', fontsize=10)


handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2)


plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('C:/Users/Lenovo/Desktop/Hill_Number.png', dpi=300)
plt.show()
