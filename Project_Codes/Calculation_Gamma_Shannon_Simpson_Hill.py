import pandas as pd
import numpy as np


data = pd.read_csv('C:/Users/Lenovo/Desktop/time_data_subset.csv')


data['detected_time'] = pd.to_datetime(data['detected_time'], format='mixed', utc=True)

# select data from 2021.12 to 2024.4
data = data[(data['detected_time'].dt.year >= 2021) &
            (data['detected_time'].dt.year <= 2024) &
            (data['detected_time'].dt.month.isin(range(1, 13)))]


monthly_diversity = {}


final_table_confidence = pd.DataFrame()  # confidence
final_table_100 = pd.DataFrame()  # no confidence
final_table_gamma = pd.DataFrame()  # gamma


for year in range(2021, 2025):
    for month in range(1, 13):
        if year == 2021 and month < 12:
            continue
        if year == 2024 and month > 4:
            break


        monthly_data = data[(data['detected_time'].dt.year == year) &
                            (data['detected_time'].dt.month == month)]

        if monthly_data.empty:
            continue


        species_weighted_counts = monthly_data.groupby('tags')['confidence'].sum()


        total_weighted_count = species_weighted_counts.sum()


        species_relative_abundance_confidence = species_weighted_counts / total_weighted_count


        species_mean_confidence = monthly_data.groupby('tags')['confidence'].mean()


        shannon_index_confidence = -np.sum(
            species_relative_abundance_confidence * np.log(
                species_relative_abundance_confidence) * species_mean_confidence)


        simpson_index_confidence = 1 - np.sum((species_relative_abundance_confidence ** 2) * species_mean_confidence)


        Hill_number_0_confidence = np.sum(species_mean_confidence)
        Hill_number_1_confidence = np.exp(shannon_index_confidence)
        Hill_number_2_confidence = 1 / (np.sum((species_relative_abundance_confidence ** 2) * species_mean_confidence))


        temp_df_confidence = pd.DataFrame({
            'Month': f'{year}-{month:02}',
            'Species': species_relative_abundance_confidence.index,
            'Relative Abundance': species_relative_abundance_confidence.values,
            'Mean Confidence': species_mean_confidence.values,
            'Shannon-Wiener': shannon_index_confidence,
            'Simpson': simpson_index_confidence,
            'Hill Number_0': Hill_number_0_confidence,
            'Hill Number_1': Hill_number_1_confidence,
            'Hill Number_2': Hill_number_2_confidence
        })


        final_table_confidence = pd.concat([final_table_confidence, temp_df_confidence], ignore_index=True)

        # ----------------------------
        # calculate without confidence
        # ----------------------------


        species_counts = monthly_data['tags'].value_counts()


        total_count = species_counts.sum()


        species_relative_abundance_100 = species_counts / total_count


        shannon_index_100 = -np.sum(species_relative_abundance_100 * np.log(species_relative_abundance_100))


        simpson_index_100 = 1 - np.sum(species_relative_abundance_100 ** 2)


        Hill_number_0 = len(monthly_data['tags'].unique())
        Hill_number_1 = np.exp(shannon_index_100)
        Hill_number_2 = 1 / (np.sum((species_relative_abundance_100 ** 2)))


        temp_df_100 = pd.DataFrame({
            'Month': f'{year}-{month:02}',
            'Species': species_relative_abundance_100.index,
            'Relative Abundance': species_relative_abundance_100.values,
            'Shannon-Wiener': shannon_index_100,
            'Simpson': simpson_index_100,
            'Hill Number_0': Hill_number_0,
            'Hill Number_1': Hill_number_1,
            'Hill Number_2': Hill_number_2
        })


        final_table_100 = pd.concat([final_table_100, temp_df_100], ignore_index=True)

# merge data from 2021.12 to 2024.4
merged_data = data[(data['detected_time'].dt.year >= 2021) &
                   (data['detected_time'].dt.year <= 2024) &
                   (data['detected_time'].dt.month.isin(range(1, 13)))]

# ----------------------------
# gamma -considering confidence
# ----------------------------


gamma_species_weighted_counts = merged_data.groupby('tags')['confidence'].sum()


gamma_total_weighted_count = gamma_species_weighted_counts.sum()


gamma_species_relative_abundance_confidence = gamma_species_weighted_counts / gamma_total_weighted_count


gamma_species_mean_confidence = merged_data.groupby('tags')['confidence'].mean()


gamma_shannon_index_confidence = -np.sum(
    gamma_species_relative_abundance_confidence * np.log(
        gamma_species_relative_abundance_confidence) * gamma_species_mean_confidence)


gamma_simpson_index_confidence = 1 - np.sum(
    (gamma_species_relative_abundance_confidence ** 2) * gamma_species_mean_confidence)


gamma_Hill_number_0_confidence = np.sum(gamma_species_mean_confidence)
gamma_Hill_number_1_confidence = np.exp(gamma_shannon_index_confidence)
gamma_Hill_number_2_confidence = 1 / (
    np.sum((gamma_species_relative_abundance_confidence ** 2) * gamma_species_mean_confidence))

# ----------------------------
# gamma-no confidence
# ----------------------------


gamma_species_counts = merged_data['tags'].value_counts()


gamma_total_count = gamma_species_counts.sum()


gamma_species_relative_abundance_100 = gamma_species_counts / gamma_total_count


gamma_shannon_index_100 = -np.sum(gamma_species_relative_abundance_100 * np.log(gamma_species_relative_abundance_100))


gamma_simpson_index_100 = 1 - np.sum(gamma_species_relative_abundance_100 ** 2)


gamma_Hill_number_0 = len(merged_data['tags'].unique())
gamma_Hill_number_1 = np.exp(gamma_shannon_index_100)
gamma_Hill_number_2 = 1 / np.sum(gamma_species_relative_abundance_100 ** 2)


temp_df_gamma = pd.DataFrame({
    'Species': gamma_species_relative_abundance_confidence.index,
    'Relative Abundance': gamma_species_relative_abundance_confidence.values,
    'Mean Confidence': gamma_species_mean_confidence.values,
    'Shannon-Wiener': gamma_shannon_index_confidence,
    'Simpson': gamma_simpson_index_confidence,
    'Hill Number_0': gamma_Hill_number_0_confidence,
    'Hill Number_1': gamma_Hill_number_1_confidence,
    'Hill Number_2': gamma_Hill_number_2_confidence
})


temp_df_gamma_no_confidence = pd.DataFrame({
    'Species': gamma_species_relative_abundance_100.index,
    'Relative Abundance': gamma_species_relative_abundance_100.values,
    'Shannon-Wiener': gamma_shannon_index_100,
    'Simpson': gamma_simpson_index_100,
    'Hill Number_0': gamma_Hill_number_0,
    'Hill Number_1': gamma_Hill_number_1,
    'Hill Number_2': gamma_Hill_number_2
})


gamma_file_path_confidence = 'C:/Users/Lenovo/Desktop/gamma_confidence.csv'
gamma_file_path_no_confidence = 'C:/Users/Lenovo/Desktop/gamma_no_confidence.csv'

temp_df_gamma.to_csv(gamma_file_path_confidence, index=False)
temp_df_gamma_no_confidence.to_csv(gamma_file_path_no_confidence, index=False)


print("Considering Confidence:\n", final_table_confidence)


print("Not Considering Confidence:\n", final_table_100)

file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'


final_table_confidence.to_csv(file_path_1, index=False)
final_table_100.to_csv(file_path_2, index=False)

