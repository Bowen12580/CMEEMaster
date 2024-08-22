import numpy as np
from scipy.stats import ttest_rel, spearmanr, kendalltau
import pandas as pd


file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'
data_confidence = pd.read_csv(file_path_1)
data_no_confidence = pd.read_csv(file_path_2)


hill_0_pre = data_no_confidence.groupby('Month')['Hill Number_0'].mean()
hill_0_post = data_confidence.groupby('Month')['Hill Number_0'].mean()

hill_1_pre = data_no_confidence['Hill Number_1'].unique()
hill_1_post = data_confidence['Hill Number_1'].unique()

hill_2_pre = data_no_confidence['Hill Number_2'].unique()
hill_2_post = data_confidence['Hill Number_2'].unique()


t_stat_hill_0, p_value_hill_0 = ttest_rel(hill_0_pre, hill_0_post)
t_stat_hill_1, p_value_hill_1 = ttest_rel(hill_1_pre, hill_1_post)
t_stat_hill_2, p_value_hill_2 = ttest_rel(hill_2_pre, hill_2_post)

print(f"T-statistic for Hill Number 0: {t_stat_hill_0}, P-value for Hill Number 0: {p_value_hill_0}")
print(f"T-statistic for Hill Number 1: {t_stat_hill_1}, P-value for Hill Number 1: {p_value_hill_1}")
print(f"T-statistic for Hill Number 2: {t_stat_hill_2}, P-value for Hill Number 2: {p_value_hill_2}")


def cohen_d(pre, post):
    mean_pre = np.mean(pre)
    mean_post = np.mean(post)
    std_pre = np.std(pre, ddof=1)
    std_post = np.std(post, ddof=1)
    pooled_std = np.sqrt(((len(pre) - 1) * std_pre ** 2 + (len(post) - 1) * std_post ** 2) / (len(pre) + len(post) - 2))
    d = (mean_post - mean_pre) / pooled_std
    return d

cohen_d_value_hill_0 = cohen_d(hill_0_pre, hill_0_post)
cohen_d_value_hill_1 = cohen_d(hill_1_pre, hill_1_post)
cohen_d_value_hill_2 = cohen_d(hill_2_pre, hill_2_post)

print(f"Cohen's d for Hill Number 0: {cohen_d_value_hill_0}")
print(f"Cohen's d for Hill Number 1: {cohen_d_value_hill_1}")
print(f"Cohen's d for Hill Number 2: {cohen_d_value_hill_2}")


spearman_corr_hill_0, spearman_p_value_hill_0 = spearmanr(hill_0_pre, hill_0_post)
spearman_corr_hill_1, spearman_p_value_hill_1 = spearmanr(hill_1_pre, hill_1_post)
spearman_corr_hill_2, spearman_p_value_hill_2 = spearmanr(hill_2_pre, hill_2_post)

kendall_corr_hill_0, kendall_p_value_hill_0 = kendalltau(hill_0_pre, hill_0_post)
kendall_corr_hill_1, kendall_p_value_hill_1 = kendalltau(hill_1_pre, hill_1_post)
kendall_corr_hill_2, kendall_p_value_hill_2 = kendalltau(hill_2_pre, hill_2_post)

print(f"Spearman's ρ for Hill Number 0: {spearman_corr_hill_0}, P-value: {spearman_p_value_hill_0}")
print(f"Spearman's ρ for Hill Number 1: {spearman_corr_hill_1}, P-value: {spearman_p_value_hill_1}")
print(f"Spearman's ρ for Hill Number 2: {spearman_corr_hill_2}, P-value: {spearman_p_value_hill_2}")

print(f"Kendall's τ for Hill Number 0: {kendall_corr_hill_0}, P-value: {kendall_p_value_hill_0}")
print(f"Kendall's τ for Hill Number 1: {kendall_corr_hill_1}, P-value: {kendall_p_value_hill_1}")
print(f"Kendall's τ for Hill Number 2: {kendall_corr_hill_2}, P-value: {kendall_p_value_hill_2}")
