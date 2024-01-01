import pandas as pd

excel_file = r"C:\Users\ishaa\Downloads\apj-5.xlsx"
# sheet_name = 'HJB'

column_to_check = 'Email'

df = pd.read_excel(excel_file)

df = df.dropna(subset=[column_to_check])

output_file = r'C:\Users\ishaa\Downloads\hjb.xlsx'

df.to_excel(output_file, index=False)

print("New file saved successfully.")