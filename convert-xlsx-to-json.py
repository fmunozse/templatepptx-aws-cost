import os
import json
import argparse
from pprint import pprint
import openpyxl

""" Example of exit format 
{
  "Hoja1": {
    "A1": "columna A1",
    "I3": "columna I3"
  },
  "aaa": {
    "A2": "columna A2",
    "J3": "columna J3"
  }
}
"""

def main(input_excel:str, output_json:str):
        
    wb = openpyxl.load_workbook(input_excel)

    json_data = {}
    #Iterate over sheets
    for sheet in wb.sheetnames:
        json_data_sheet = {}

        #Iterate over rows
        for row in wb[sheet].rows:

            #Iterate over cells 
            for cell in row:
                if cell.value is not None:
                    json_data_sheet[cell.coordinate] = str(cell.value) #Force to be string
                    #print ("coordinate: " + str(cell.coordinate) + ", value: " + str(cell.value))

        json_data[sheet] = json_data_sheet

    print(json.dumps(json_data, indent=2) )

    #generate json file 
    with open(output_json, 'w', encoding='utf-8') as outfile:
        json.dump(json_data, outfile, ensure_ascii=False, indent=2)
        print(f"File {output_json} generated")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert a excel to json')
    parser.add_argument('input_excel', type=str, help='input excel file to convert')
    parser.add_argument('output_json', type=str, help='output json generated')

    args = parser.parse_args()
    pprint(vars(args))

    if not os.path.exists(args.input_excel):
        raise Exception(f"File {args.input_excel} does not exist")

    main(args.input_excel, args.output_json)

