import ee
import os
from dotenv import load_dotenv

load_dotenv()

def init_gee():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    ee.Initialize(ee.ServiceAccountCredentials('', cred_path))

def get_temperature_map(start_date, end_date):
    image = ee.ImageCollection('MODIS/006/MOD11A2') \
        .select('LST_Day_1km') \
        .filterDate(start_date, end_date) \
        .mean() \
        .multiply(0.02) \
        .subtract(273.15)

    vis_params = {
        'min': -20,
        'max': 50,
        'palette': ['blue', 'limegreen', 'yellow', 'red']
    }

    map_id_dict = ee.Image(image).getMapId(vis_params)
    return map_id_dict
