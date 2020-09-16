import folium
from geopy.geocoders import Nominatim
location=Nominatim()

city=input("enter city name: ")
loc=location.geocode(city)
map=folium.Map(location=[20.5937,78.9629],zoom_start=6)
map.add_child(folium.Marker(location=[loc.latitude,loc.longitude],popup=city,icon=folium.Icon(color='green')))
map.save("City.html")
