# QGIS didn't like my selection so we use python instead.
from pathlib import Path
import geopandas as gpd
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "aoi.gpkg"
OUT.parent.mkdir(parents=True, exist_ok=True)

BOUNDS = (10.3635, 51.6196, 10.7794, 51.8868)

aoi = gpd.GeoDataFrame(
    {"name": ["harz_core"]},
    geometry=[box(*BOUNDS)],
    crs="EPSG:4326",
)
aoi.to_file(OUT, layer="aoi", driver="GPKG")
print(aoi.total_bounds)