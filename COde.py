def color_production(elevation):
    if elevation <=1000:
        return 'green'
    elif elevation >1000 and elevation<2000:
        return 'red'
    else:
        return 'black'


import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")

lat=data["LAT"]
lon=data["LON"]
elev=data["ELEV"]
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,ev in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(ev)+"m ",icon=folium.Icon(color=color_production(ev))))
fgw=folium.FeatureGroup(name="World")

fgw.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
              
map=map.add_child(fgv)
map=map.add_child(fgw)
map.add_child(folium.LayerControl())
map.save("map1.html")
