'''
convert_gif_to_bmp.py - 2nd script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) pivot_and_join.py
                        Convert (systematically named) GIF files to BMP files (8 bit color depth with color table aka palette)
                          that are archived/historical medium range (Day 7 - Day 3) forecasts
                          from NOAA/NWS Weather Prediction Center.
                        E.G. Day 4 forecast "issued" on a Monday is "valid" on Friday.
                        Convert files for daily min/max temp prediction, probability of precipitation prediction.
                        Convert files for a specified date range.
General Assembly - Data Science class project - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/4/16 - 1//16
'''
from PIL import Image #Pillow (PIL fork, Python Image Library)
import os #for interacting with operating system, file system
import sys #interact with the Python interpreter (~platform runtime)

max_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31] #non-leap year
issue_year = 2015
issue_month = 10 # 1 - 12

print
print 'For forecasts issued: year %s, month %s' % (issue_year,issue_month)

for issue_day in range(1, max_day_in_month[issue_month-1]+1):
  issue_date = str(issue_year) + str('%02u' % issue_month) + str('%02u' % issue_day) #YYYYMMDD, the date that the forecasts were issued
  for forecast_day in ['3','4','5','6','7']: #forecast is valid for a date that is this many days ahead
    for forecast_type in ['MIN','MAX','POP1','POP2']: #min/max temp prediction, probability of precipitation prediction for 12Z/00Z, Z=UTC
      file_name = issue_date+'12_DAY'+forecast_day+'_'+forecast_type+'_filled'
      print 'Convert ../data/downloaded_data/'+file_name+'.gif to ../data/converted_data/'+file_name+'.bmp'
      #Luckily, save method is creating BMP with 8 bit color depth with color table (aka palette), maybe because GIF is 8 bit color depth?
      Image.open('../data/downloaded_data/'+file_name+'.gif').save('../data/converted_data/'+file_name+'.bmp') #Don't even need to save the image in a variable
      sys.stdout.write('Original file size: '+str(os.stat('../data/downloaded_data/'+file_name+'.gif').st_size)+' bytes; ')
      print 'converted file size:', os.stat('../data/converted_data/'+file_name+'.bmp').st_size, 'bytes'

print 'Done!'

