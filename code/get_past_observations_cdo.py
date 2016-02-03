'''
get_past_observations_cdo.py - 4th script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) get_past_observations_cdo.py, 5.) pivot_and_join.py
                               Get past observations (min/max temperature, precipitation, snowfall) from Climate Data Online.
                               Get observables for a list of weather stations (mainly airports).
                               Converts from degress C and mm to degrees F and inches
                               See DataDictionary.txt for abbreviations, explanation of data elements.
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/5/16 - 1/21/16
'''
import requests, json
from time import sleep #for pausing between URL requests
import os #for interacting with operating system, file system
import sys #interact with the Python interpreter (~platform runtime)

# NOAA > NCEI (formerly NCDC) > CDO > Web Services v2 - All responses are JSON and will be a single item or a collection of items with metadata
#              www.ncdc.noaa.gov/cdo-web                Limited to 5 requests per second and 1000 requests per day
#                                                       JSON response row limit (in 'results' list) defaults to 25, max is 1000 (set 'limit' query string)
base_url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data'

my_token = '<your_token>' # www.ncdc.noaa.gov/cdo-web/token

# set query strings for the URL
data_set='datasetid=GHCND' #Daily Summary (Global Historical Climatology Network)

#start_date='startdate=2015-01-01'
#end_date='enddate=2015-06-30'
#start_date='startdate=2015-07-01'
#end_date='enddate=2015-12-31'
start_date='startdate=2016-01-01'
end_date='enddate=2016-01-07'

#TMAX, TMIN (max/min daily temperature, 1/10 C), PRCP (rain, 1/10 mm, does not include snow), SNOW (snowfall, mm)
data_types='datatypeid=TMAX&datatypeid=TMIN&datatypeid=PRCP&datatypeid=SNOW'

data_file_out = '../data/past_observation.csv' #store data in this text file
num_wea_stns = 0
num_wea_stns_with_data = 0

#if doesn't exist, create data output text file (.csv) with header (column titles)
if not os.path.exists(data_file_out):
  with open(data_file_out,mode='w') as f: 
    f.write('wea_stn_cd,valid_date,wea_num_type,wea_num\n')

# Get my list of weather stations
with open('weather_stn_data.py', mode='rU') as f: 
  list_wea_stn = eval(f.read()) # list of dictionaries with elements: 'icao_code','stn_id_cdo','weather_station',...

print

f = open(data_file_out, mode='a') #open output CSV data/text file for writing to (append) 

for wea_stn in list_wea_stn:
  num_wea_stns += 1
  wea_stn_icao = wea_stn['icao_code'] #e.g. KSEA (Seattle Tacoma airport) 
  wea_stn_id = wea_stn['stn_id_cdo'] #e.g. GHCND:USW00024233
  sys.stdout.write('For station %s %s '%(wea_stn_icao, wea_stn_id))
  #keep URL < 2000 characters
  r = requests.get(base_url+'?'+data_set+'&stationid='+wea_stn_id+'&'+data_types+'&'+start_date+'&'+end_date+'&sortfield=date&limit=1000',headers={'token':my_token})
  json_dict = r.json()
  if json_dict:
    if 'metadata' in json_dict:
      num_wea_stns_with_data += 1
      sys.stdout.write('count %u (max %u) ' % (json_dict['metadata']['resultset']['count'],json_dict['metadata']['resultset']['limit']))
      print json_dict['results'][0]['date'][:10],'thru',json_dict['results'][-1]['date'][:10]
      for row in json_dict['results']:
        if row['datatype'] in ['TMAX','TMIN']:
          strval = '%.1f'%(row['value']*9.0/50.0+32.0) #convert to Fahrenheit, resolution ~0.2F
        elif row['datatype']=='PRCP':
          strval = '%.3f'%(row['value']/254.0) #convert to inches, resolution ~0.004 inches
        elif row['datatype']=='SNOW':
          strval = '%.2f'%(row['value']/25.4) #convert to inches, resolution ~0.04 inches
        else:
          strval = ''
        f.write(wea_stn_icao+','+row['date'][0:4]+row['date'][5:7]+row['date'][8:10]+','+row['datatype'].lower()+','+strval+'\n')
    elif 'message' in json_dict:
      print 'ERROR:',json_dict['message']
    else:
      print 'ERROR:','Unknown JSON response returned'
  else:
    print 'ERROR: NO DATA'
  sleep(0.3) #pause thread (seconds)
  
f.close() #close output data/text file
print 'Done! ', '%u out of %u weather stations had data'%(num_wea_stns_with_data,num_wea_stns)



