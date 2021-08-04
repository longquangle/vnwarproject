import json 
with open('vn_province.txt') as json_file:     # name of the text file
    data = json.load(json_file)

# Convert JSON to GeoJson 
from geojson import dump
with open('vietnam_province.geojson', 'w') as f:   # name of the output geojson file
   dump(data, f)