import pandas as pd

# load data from CSV file
file_path = 'C:/Users/Lenovo/Desktop/data.csv'
data = pd.read_csv(file_path)

# filter out rows with missing values in 'tags' column
data_cleaned = data.dropna(subset=['tags'])

# filter out rows with confidence score outside the range of 0.6 to 1
data_cleaned = data_cleaned[(data_cleaned['confidence'] >= 0.6) & (data_cleaned['confidence'] <= 1)]

# export cleaned data to CSV file
output_cleaned_path = 'C:/Users/Lenovo/Desktop/cleaned_data.csv'
data_cleaned.to_csv(output_cleaned_path, index=False)

print(f"Cleaned data has been saved to {output_cleaned_path}")
