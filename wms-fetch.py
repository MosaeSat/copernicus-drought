import requests

# Define the base URL for the WMS GetMap request
wms_base_url = "https://drought.emergency.copernicus.eu/api/wms?"

# Parameters for the request (example for RDrI-Agri or CDI)
params = {
    'SERVICE': 'WMS',
    'VERSION': '1.1.1',
    'REQUEST': 'GetMap',
    'LAYERS': 'rdria',  # Change this to 'cdinx' for the Combined Drought Indicator
    'SRS': 'EPSG:4326',  # Coordinate reference system
    'BBOX': '-10,-35,90,65',  # Bounding box coordinates (minLon, minLat, maxLon, maxLat)
    'WIDTH': '1024',
    'HEIGHT': '1024',
    'FORMAT': 'image/png',
    'TIME': '2022-01-01'  # You can change this to the date you want or omit it for the latest data
}

# Send the request to the WMS service
response = requests.get(wms_base_url, params=params)

# Save the image if the request is successful
if response.status_code == 200:
with open('./images/drought_map.png', 'wb') as f:
    f.write(response.content)
    print("Map image saved successfully!")
else:
    print(f"Error: {response.status_code}")
