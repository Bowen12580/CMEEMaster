import pandas as pd

# load cleaned data from CSV file
cleaned_file_path = 'C:/Users/Lenovo/Desktop/cleaned_data.csv'
cleaned_data = pd.read_csv(cleaned_file_path)

# timestamp to datetime format
cleaned_data['detected_time'] = pd.to_datetime(cleaned_data['detected_time'], utc=True)

# sort data by timestamp
sorted_data = cleaned_data.sort_values(by='detected_time')

# export sorted data to CSV file
output_time_data_path = 'C:/Users/Lenovo/Desktop/time_data_subset.csv'
sorted_data.to_csv(output_time_data_path, index=False)

print(f"Sorted data has been saved to {output_time_data_path}")
