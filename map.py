import folium
import pandas

volcano_data = pandas.read_csv("Volcano_Data_world.csv")
lat = list(volcano_data["Latitude"])
lon = list(volcano_data["Longitude"])
elev = list(volcano_data["Elev"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True, color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map.html")
