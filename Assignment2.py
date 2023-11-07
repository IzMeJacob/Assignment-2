import pandas as pd

# Rename Attributes

# Load the Excel file
file_path = 'Petrol/04B-2019 Car and Petrol Survey v23042019 (N=1009).xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Display the current column names
print("Current column names:")
print(df.columns)

# Rename the attributes
# new_column_names = {'old_name_1': 'new_name_1', 'old_name_2': 'new_name_2'}  # Replace with your actual column name changes

# Rename the columns
# df = df.rename(columns=new_column_names)

# Display the updated column names
# print("\nUpdated column names:")
# print(df.columns)

# Save the updated data to a new Excel file
# new_file_path = 'path_to_save_updated_excel_file.xlsx'  # Replace with the path where you want to save the updated Excel file
# df.to_excel(new_file_path, index=False)
