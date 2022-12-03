import json
import requests
import pandas as pd
from arcgis.gis import GIS
tokens = pd.read_csv(r"C:\Users\M3ECHJJJ\Documents\Tokens.csv", index_col='Site')
gis = GIS(tokens.at['uCOP','URL'])

layer_item = gis.content.get('97fe13634c964fa38f9f6608c7dc9963')
layers = layer_item.layers
flayer = layers[0]
fset = flayer.query()
features = fset.features


# %% codecell


measures = ['dtg', 'low', 'high', 'wind', 'wind_gust', 'wind_dir', 'rain', 'cloud', 'main', 'wdesc', 'pressure', 'location']
newmeasures = []
for n in range(8):
    measuresx = [x+str(n) for x in measures]
    newmeasures = newmeasures + measuresx
df = pd.DataFrame(columns=newmeasures)


# %% codecell


def geticon(desc):
    if '01' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Weather_icon_-_sunny.svg/512px-Weather_icon_-_sunny.svg.png'
    if '02' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Weather_icon_-_sunny_to_cloudy.svg/1024px-Weather_icon_-_sunny_to_cloudy.svg.png'
    if '03' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Weather_icon_-_cloudy.svg/1024px-Weather_icon_-_cloudy.svg.png'
    if '04' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Weather_icon_-_overcast.svg/120px-Weather_icon_-_overcast.svg.png'
    if '09' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Weather_icon_-_showers.svg/120px-Weather_icon_-_showers.svg.png'
    if '10' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Weather_icon_-_showers.svg/120px-Weather_icon_-_showers.svg.png'
    if '11' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Weather_icon_-_heavy_rain.svg/120px-Weather_icon_-_heavy_rain.svg.png'
    if '13' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Weather_icon_-_snowy.svg/120px-Weather_icon_-_snowy.svg.png'
    if '50' in desc:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Weather_icon_-_fog.svg/120px-Weather_icon_-_fog.svg.png'


# %% codecell

auth = tokens.at['Open Weather','API Key']
for f in features:

    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={auth}'.format(f.attributes['point_y'], f.attributes['point_x'],auth)
    response = requests.request("GET", url)
    fc = json.loads(response.text)
    push = []
    n = 0
    for d in fc['daily']:
        globals()['dtg'+str(n)] = d['dt']*1000
        globals()['low'+str(n)] = int((d['temp']['min']-273.15) * 9/5 + 32)
        globals()['high'+str(n)] = int((d['temp']['max']-273.15) * 9/5 + 32)
        globals()['wind'+str(n)] = int(d['wind_speed'])
        globals()['wind_gust'+str(n)] = int(d['wind_gust'])
        globals()['wind_dir'+str(n)] = int(d['wind_deg'])
        try:
            globals()['rain'+str(n)] = round(d['rain']*0.0393701, 2)
        except:
            globals()['rain'+str(n)] = 0
        globals()['cloud'+str(n)] = d['clouds']
        globals()['main'+str(n)] = geticon(d['weather'][0]['icon'])
        globals()['wdesc'+str(n)] = d['weather'][0]['description'].capitalize()
        globals()['pressure'+str(n)] = d['pressure']
        globals()['location'+str(n)] = f.attributes['location']
        dlist = [globals()['dtg'+str(n)], globals()['low'+str(n)],
                        globals()['high'+str(n)], globals()['wind'+str(n)], globals()['wind_gust'+str(n)],
                        globals()['wind_dir'+str(n)], globals()['rain'+str(n)], globals()['cloud'+str(n)],
                        globals()['main'+str(n)], globals()['wdesc'+str(n)], globals()['pressure'+str(n)],globals()['location'+str(n)]]
        push = push + dlist
        n = n+1
    df.loc[len(df.index)] = push


# %% codecell


for index, row in df.iterrows():
    t_feature = [f for f in features if f.attributes['location'] == row['location7']][0]
    attributes_dict = {'OBJECTID': t_feature.attributes['OBJECTID']}
    for col in df.columns:
        try:
            attributes_dict[col] = row[col]
        except:
            pass
    updates_to_push = {"attributes": attributes_dict}
    flayer.edit_features(updates=[updates_to_push])
