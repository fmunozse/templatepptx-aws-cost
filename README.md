
## Setup :
```shell 
    python -m venv .env
```

## Quick run :
```shell 
 python convert-xlsx-to-json.py  .\examples\test.xlsx  .\examples\test-excel-to-json.json
 python templatepptx-aws-cost.py -input-aws-json .\examples\aws-estimation-export-from-awscalculator.json  -output-pptx .\examples\out.pptx
```


# Conversor EXCEL to JSON
## Description
A simple tools to convert a xlsx file to json format (see example). Only save the cells that have value and always is transform to "str"

```json
{
  "Hoja1": {
    "A1": "columna A1",
    "I3": "columna I3"
  },
  "nameSheet2": {
    "A2": "columna A2",
    "J3": "columna J3",
    "B6": "1.1122",
    "B7": "1.22"
  }
}
```

## Setup and run:
* Run 
```shell 
    python convert-xlsx-to-json.py  <input-path-to-xlsx> <output-path-output json>

```