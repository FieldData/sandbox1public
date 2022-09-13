#
# - Use PANDAS and associated methods
# - Use JSON package to manipulate JSON objects
#
import pandas as pd
import json

# Set filename parameters
excel_inputfile = 'dummy_data_labels.xlsx'
json_outputfile = 'json_converted.json'

# Read the excel file into a Dataframe
print(f'Reading {excel_inputfile}')
df = pd.read_excel(excel_inputfile)
print (df)
#
# Write JSON string to a file
json_split = df.to_json(orient='split')
#print(f'JSON split: {json_split}\n')
jsonObject = json.loads(json_split)
json_formatted = json.dumps(jsonObject,indent=4)

jsonOut = open(json_outputfile,'w')
jsonObject = json.loads(json_formatted)

# Format the string
json_formatted = json.dumps(jsonObject['data'],indent=4)
jsonOut.write(json_formatted)
jsonOut.close()

# Print JSON object (dictionary)
for jobj in jsonObject:
    print(f'{jobj}')

jfields = jsonObject.keys()
print (f'jfields: {jfields}')
columnList = jsonObject['columns']
print(f'ColumnList: {columnList}')

for items in jsonObject['data']:
    print(f'Items = {items}')
    for (anitem,acolumn) in zip(items,columnList):
        print(f'anitem:{anitem}, acolumn:{acolumn}')
        

        
    
    

