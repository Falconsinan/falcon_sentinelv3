import folium
import requests

def create_map(ip_list):

    m = folium.Map(location=[20,0], zoom_start=2)

    for ip in ip_list:

        try:

            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()

            lat = data["lat"]
            lon = data["lon"]

            folium.Marker(
                [lat, lon],
                popup=ip,
                icon=folium.Icon(color="red")
            ).add_to(m)

        except:
            pass

    m.save("attack_map.html")