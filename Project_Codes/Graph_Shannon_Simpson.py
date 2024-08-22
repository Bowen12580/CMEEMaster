import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'
data_confidence = pd.read_csv(file_path_1)
data_no_confidence = pd.read_csv(file_path_2)


pre_adjustment = data_no_confidence['Shannon-Wiener'].unique()
post_adjustment = data_confidence['Shannon-Wiener'].unique()
pre_adjustment_simpson = data_no_confidence['Simpson'].unique()
post_adjustment_simpson = data_confidence['Simpson'].unique()



def annotate_and_connect(ax, pre_data, post_data, xpos_pre, xpos_post):
    """ select the appropriate positions for the annotations and connect them with a line """
    for (pre, post) in zip(pre_data, post_data):

        ax.plot([xpos_pre, xpos_post], [pre, post], color='gray', linestyle='--', linewidth=1)


    max_val_pre = pre_data.max()
    min_val_pre = pre_data.min()
    median_val_pre = pre_data.median()

    ax.text(xpos_pre - 0.02, max_val_pre, f'{max_val_pre:.2f}', ha='right', va='bottom', color='black', fontsize=10)
    ax.text(xpos_pre - 0.02, min_val_pre, f'{min_val_pre:.2f}', ha='right', va='top', color='black', fontsize=10)
    ax.text(xpos_pre - 0.02, median_val_pre, f'{median_val_pre:.2f}', ha='right', va='center', color='black', fontsize=10)


    max_val_post = post_data.max()
    min_val_post = post_data.min()
    median_val_post = post_data.median()

    ax.text(xpos_post - 0.002, max_val_post, f'{max_val_post:.2f}', ha='right', va='bottom', color='black', fontsize=10)
    ax.text(xpos_post - 0.002, min_val_post, f'{min_val_post:.2f}', ha='right', va='top', color='black', fontsize=10)
    ax.text(xpos_post - 0.002, median_val_post, f'{median_val_post:.2f}', ha='right', va='center', color='black', fontsize=10)



sns.set(style="whitegrid", palette="pastel", font_scale=1.3)


plt.figure(figsize=(10, 6))
ax = sns.boxplot(data=[pre_adjustment, post_adjustment], palette=["#8ecae6", "#ffb703"], width=0.6)
sns.stripplot(data=[pre_adjustment, post_adjustment], color=".15", size=6, jitter=False)


annotate_and_connect(ax, pd.Series(pre_adjustment), pd.Series(post_adjustment), 0, 1)

plt.xticks([0, 1], ['Pre-adjustment', 'Post-adjustment'], fontsize=12)
plt.title('Shannon Index: Pre vs Post Adjustment', fontsize=16)
plt.ylabel('Shannon Index')

plt.savefig('C:/Users/Lenovo/Desktop/shannon.png', dpi=300, bbox_inches='tight')
plt.show()


plt.figure(figsize=(10, 6))
ax = sns.boxplot(data=[pre_adjustment_simpson, post_adjustment_simpson], palette=["#8ecae6", "#ffb703"], width=0.6)
sns.stripplot(data=[pre_adjustment_simpson, post_adjustment_simpson], color=".15", size=6, jitter=False)


annotate_and_connect(ax, pd.Series(pre_adjustment_simpson), pd.Series(post_adjustment_simpson), 0, 1)

plt.xticks([0, 1], ['Pre-adjustment', 'Post-adjustment'], fontsize=12)
plt.title('Simpson Index: Pre vs Post Adjustment', fontsize=16)
plt.ylabel('Simpson Index')

plt.savefig('C:/Users/Lenovo/Desktop/simpson.png', dpi=300, bbox_inches='tight')
plt.show()
