import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'
data_confidence = pd.read_csv(file_path_1)
data_no_confidence = pd.read_csv(file_path_2)


alpha_pre_shannon = np.mean(data_no_confidence['Hill Number_1'].unique())
alpha_post_shannon = np.mean(data_confidence['Hill Number_1'].unique())
alpha_pre_simpson = np.mean(data_no_confidence['Hill Number_2'].unique())
alpha_post_simpson = np.mean(data_confidence['Hill Number_2'].unique())


gamma_file_path_1 = 'C:/Users/Lenovo/Desktop/gamma_no_confidence.csv'
gamma_file_path_2 = 'C:/Users/Lenovo/Desktop/gamma_confidence.csv'
gamma_no_confidence = pd.read_csv(gamma_file_path_1)
gamma_confidence = pd.read_csv(gamma_file_path_2)


gamma_pre_shannon = gamma_no_confidence['Hill Number_1'].unique()[0]
gamma_post_shannon = gamma_confidence['Hill Number_1'].unique()[0]
gamma_pre_simpson = gamma_no_confidence['Hill Number_2'].unique()[0]
gamma_post_simpson = gamma_confidence['Hill Number_2'].unique()[0]


beta_pre_shannon = gamma_pre_shannon / alpha_pre_shannon
beta_post_shannon = gamma_post_shannon / alpha_post_shannon
beta_pre_simpson = gamma_pre_simpson / alpha_pre_simpson
beta_post_simpson = gamma_post_simpson / alpha_post_simpson


bar_width = 0.35
index = np.arange(2)


beta_values_pre = [beta_pre_shannon, beta_pre_simpson]
beta_values_post = [beta_post_shannon, beta_post_simpson]


plt.figure(figsize=(10, 6))

plt.bar(index, beta_values_pre, bar_width, label='Pre-adjustment', color='#8ecae6')
plt.bar(index + bar_width, beta_values_post, bar_width, label='Post-adjustment', color='#ffb703')

plt.xlabel('Diversity Indices')
plt.ylabel('β Diversity')
plt.title('Comparison of β Diversity: Shannon-Wiener and Simpson Indices')
plt.xticks(index + bar_width / 2, ['Shannon-Wiener', 'Simpson'])
plt.legend(loc='lower left', fontsize=8)


for i in range(len(beta_values_pre)):
    plt.text(index[i], beta_values_pre[i] + 0.01, f'{beta_values_pre[i]:.2f}', ha='center', va='bottom', color='black', fontsize=10)
    plt.text(index[i] + bar_width, beta_values_post[i] + 0.01, f'{beta_values_post[i]:.2f}', ha='center', va='bottom', color='black', fontsize=10)

plt.tight_layout()
plt.savefig('C:/Users/Lenovo/Desktop/beta_diversity.png', dpi=300)
plt.show()
