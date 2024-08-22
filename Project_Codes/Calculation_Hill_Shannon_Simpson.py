import pandas as pd
import numpy as np

# Read the dataset
data = pd.read_csv('C:/Users/Lenovo/Desktop/time_data_subset.csv')


data['detected_time'] = pd.to_datetime(data['detected_time'], format='mixed', utc=True)


data['Year_Month'] = data['detected_time'].dt.strftime('%Y.%m')


final_table_confidence = pd.DataFrame()
final_table_100 = pd.DataFrame()

# Group by "Year_Month" and iterate over each group
for year_month, monthly_data in data.groupby('Year_Month'):

    species_weighted_counts = monthly_data.groupby('tags')['confidence'].sum()


    total_weighted_count = species_weighted_counts.sum()


    species_relative_abundance_confidence = species_weighted_counts / total_weighted_count


    species_mean_confidence = monthly_data.groupby('tags')['confidence'].mean()


    shannon_index_confidence = -np.sum(
        species_relative_abundance_confidence * np.log(species_relative_abundance_confidence) * species_mean_confidence)


    simpson_index_confidence = 1 - np.sum((species_relative_abundance_confidence ** 2) * species_mean_confidence)


    Hill_number_0_confidence = np.sum(species_mean_confidence)
    Hill_number_1_confidence = np.exp(shannon_index_confidence)
    Hill_number_2_confidence = 1 / (np.sum((species_relative_abundance_confidence ** 2) * species_mean_confidence))


    temp_df_confidence = pd.DataFrame({
        'Year_Month': year_month,
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
    # Calculate diversity indices not considering confidence
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
        'Year_Month': year_month,
        'Species': species_relative_abundance_100.index,
        'Relative Abundance': species_relative_abundance_100.values,
        'Shannon-Wiener': shannon_index_100,
        'Simpson': simpson_index_100,
        'Hill Number_0': Hill_number_0,
        'Hill Number_1': Hill_number_1,
        'Hill Number_2': Hill_number_2
    })


    final_table_100 = pd.concat([final_table_100, temp_df_100], ignore_index=True)


print("Considering Confidence:\n", final_table_confidence)


print("Not Considering Confidence:\n", final_table_100)

file_path_1 = 'C:/Users/Lenovo/Desktop/test1_confidence.csv'
file_path_2 = 'C:/Users/Lenovo/Desktop/test2_no_confidence.csv'


final_table_confidence.to_csv(file_path_1, index=False)
final_table_100.to_csv(file_path_2, index=False)
