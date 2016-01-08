'''
download_images.py - First script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) pivot_and_join.py
                     Download (systematically named) image files (.GIF)
                       of archived/historical medium range (Day 7 - Day 3) forecasts
                       from NOAA/NWS Weather Prediction Center.
                     E.G. Day 4 forecast "issued" on a Monday is "valid" on Friday.
                     Download files for daily min/max temp prediction, probability of precipitation prediction.
                     Download files for a specified date range.
General Assembly - Data Science class project - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/3/16 - 1//16
'''
import requests #for downloading a file at a URL
import os #for interacting with operating system, file system
from time import sleep #for pausing between URL requests

url_start = 'http://www.wpc.ncep.noaa.gov/archives/medr/'
local_data_dir = '../data/downloaded_data/'
file_name_web = ''

max_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31] #non-leap year
issue_year = 2015
issue_month = 10 # 1 - 12

print
print 'For forecasts issued: year %s, month %s' % (issue_year,issue_month)

for issue_day in range(1, max_day_in_month[issue_month-1]+1):
  issue_date = str(issue_year) + str('%02u' % issue_month) + str('%02u' % issue_day) #YYYYMMDD, the date that the forecasts were issued
  for forecast_day in ['3','4','5','6','7']: #forecast is valid for a date that is this many days ahead
    for forecast_type in ['MIN','MAX','POP1','POP2']: #min/max temp prediction, probability of precipitation prediction for 12Z/00Z, Z=UTC
      if len(file_name_web)>0:
        print 'Pause...'
        sleep(1) #pause thread for 1 second
        
      file_name_web = 'DAY'+forecast_day+'_'+forecast_type+'_'+issue_date+'12_filled.gif'
      file_name_local = issue_date+'12_DAY'+forecast_day+'_'+forecast_type+'_filled.gif' #change name slightly
      print 'Request URL:', url_start+issue_date+'/'+file_name_web
      r=requests.get(url_start+issue_date+'/'+file_name_web)
      print 'Save to:', local_data_dir+file_name_local
      with open(local_data_dir+file_name_local,mode='wb') as f:
        f.write(r.content)
        
      print 'Downloaded:', len(r.content), 'bytes;', 'saved file size:', os.stat(local_data_dir+file_name_local).st_size, 'bytes'

print 'Done!'
  
