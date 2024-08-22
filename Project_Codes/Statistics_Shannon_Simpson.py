import numpy as np
from scipy.stats import ttest_rel,spearmanr,kendalltau
import pandas as pd
file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'
data_confidence = pd.read_csv(file_path_1)
data_no_confidence = pd.read_csv(file_path_2)


pre_adjustment = data_no_confidence['Shannon-Wiener'].unique()
post_adjustment = data_confidence['Shannon-Wiener'].unique()
pre_adjustment_simpson = data_no_confidence['Simpson'].unique()
post_adjustment_simpson = data_confidence['Simpson'].unique()


t_stat, p_value = ttest_rel(pre_adjustment, post_adjustment)

t_stat_simpson, p_value_simpson = ttest_rel(pre_adjustment_simpson, post_adjustment_simpson)
print(f"T-statistic for shannon is: {t_stat}, P-value for shannon is: {p_value}")

print(f"T-statistic for simpson is: {t_stat_simpson}, P-value for simpson is: {p_value_simpson}")



def cohen_d(pre, post):

    mean_pre = np.mean(pre)
    mean_post = np.mean(post)


    std_pre = np.std(pre, ddof=1)
    std_post = np.std(post, ddof=1)


    pooled_std = np.sqrt(((len(pre) - 1) * std_pre ** 2 + (len(post) - 1) * std_post ** 2) / (len(pre) + len(post) - 2))


    d = (mean_post - mean_pre) / pooled_std
    return d


cohen_d_value = cohen_d(pre_adjustment_simpson, post_adjustment_simpson)
cohen_d_value_shannon = cohen_d(pre_adjustment, post_adjustment)
print(f"Cohen's d for Simpson Index: {cohen_d_value}")
print(f"Cohen's d for Shannon Index: {cohen_d_value_shannon}")


# Spearman's ρ
spearman_corr_shannon, spearman_p_value_shannon = spearmanr(pre_adjustment, post_adjustment)
spearman_corr_simpson, spearman_p_value_simpson = spearmanr(pre_adjustment_simpson, post_adjustment_simpson)
print(f"Spearman's ρ for Shannon Index: {spearman_corr_shannon}, P-value: {spearman_p_value_shannon}")
print(f"Spearman's ρ for Simpson Index: {spearman_corr_simpson}, P-value: {spearman_p_value_simpson}")

# Kendall's τ
kendall_corr_shannon, kendall_p_value_shannon = kendalltau(pre_adjustment, post_adjustment)
kendall_corr_simpson, kendall_p_value_simpson = kendalltau(pre_adjustment_simpson, post_adjustment_simpson)
print(f"Kendall's τ for Shannon Index: {kendall_corr_shannon}, P-value: {kendall_p_value_shannon}")
print(f"Kendall's τ for Simpson Index: {kendall_corr_simpson}, P-value: {kendall_p_value_simpson}")
