import pandas as pd

excel_file = r"/home/trish/Desktop/Coding/Gymkhana-WebTeam/APJ.ods"
# sheet_name = 'HJB'

column_to_check = 'Email'

df = pd.read_excel(excel_file)

df = df.dropna(subset=[column_to_check])

output_file = r"/home/trish/Desktop/Coding/Gymkhana-WebTeam/APJ_details.xlsx"

df.to_excel(output_file, index=False)

print("New file saved successfully.")