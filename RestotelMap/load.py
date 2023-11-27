import geopandas as gpd
from .models import *
from django.contrib.gis.geos import MultiPoint, Point

def charge_donnee(shp):
    gdf = gpd.read_file(shp)
    for index,row in gdf.iterrows():
        catego_instance = Catego.objects.get(id = row['catego_id'])
        local_instance = Local.objects.get(id = row['local_id'])
        point = Point(row['longitude'], row['latitude'])
        etab = Etabl(
            nom = row['nom'],
            catego = catego_instance,
            telephone = row['telephone'],
            local = local_instance,
            latitude = row['latitude'],
            longitude = row['longitude'],
            geom = MultiPoint(point)
        )
        etab.save()
        
    