from fastapi import APIRouter
from app.schemas.requests import TemperatureRequest
from app.gee_client import get_temperature_map

router = APIRouter()

@router.post("/temperature")
def get_temp_layer(req: TemperatureRequest):
    tile_data = get_temperature_map(req.start_date, req.end_date)
    return {
        "mapid": tile_data['mapid'],
        "token": tile_data['token'],
        "tile_url": f"https://earthengine.googleapis.com/map/{tile_data['mapid']}/{{z}}/{{x}}/{{y}}?token={tile_data['token']}"
    }
