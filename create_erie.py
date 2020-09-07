import requests
import pandas as pd

#import dail
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'http://erieny.maps.arcgis.com',
    'Connection': 'keep-alive',
    'Referer': 'http://erieny.maps.arcgis.com/apps/opsdashboard/index.html',
    'TE': 'Trailers',
}

params = (
    ('f', 'json'),
    ('where', '1=1'),
    ('returnGeometry', 'false'),
    ('spatialRel', 'esriSpatialRelIntersects'),
    ('outFields', '*'),
    ('orderByFields', 'ZIP_CODE asc'),
    ('resultOffset', '0'),
    ('resultRecordCount', '80'),
    ('resultType', 'standard'),
    ('cacheHint', 'true'),
)

response = requests.get('https://services1.arcgis.com/CgOSc11uky3egK6O/arcgis/rest/services/erie_zip_codes_confirmed_counts/FeatureServer/0/query', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://services1.arcgis.com/CgOSc11uky3egK6O/arcgis/rest/services/erie_zip_codes_confirmed_counts/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=ZIP_CODE%20asc&resultOffset=0&resultRecordCount=80&resultType=standard&cacheHint=true', headers=headers)



data = response.json()['features']

data
lists = []
for a in data:
    zipcode = a['attributes']['ZIP_CODE']
    confirmed =a['attributes']['CONFIRMED']
    pop =a['attributes']['POPULATION']
    name = a['attributes']['PO_NAME']
    sqmi = a['attributes']['SQMI']
    
    lists.append((name,pop,sqmi,zipcode,confirmed))
    
df = pd.DataFrame(lists,columns=['Name','Population','Sq Mi','Zip Code','Confirmed Cases'])

#Get Date
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'http://erieny.maps.arcgis.com',
    'Connection': 'keep-alive',
    'Referer': 'http://erieny.maps.arcgis.com/apps/opsdashboard/index.html',
    'TE': 'Trailers',
}

params1 = (
    ('f', 'json'),
)

response = requests.get('https://erieny.maps.arcgis.com/sharing/rest/content/items/dd7f1c0c352e4192ab162a1dfadc58e1/data', headers=headers1, params=params1)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://erieny.maps.arcgis.com/sharing/rest/content/items/dd7f1c0c352e4192ab162a1dfadc58e1/data?f=json', headers=headers)

timestamp = response.json()['headerPanel']['subtitle']

date = timestamp[9:18]
time = timestamp[20:]

df_tot = df.rename(columns={'Confirmed Cases':date})

df_tot.to_csv("/Users/ericoliverio/Desktop/erie_total_raw.csv",index=False)
print('File Created')
