'''
convert_gif_to_bmp.py - 2nd script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) pivot_and_join.py
                        Convert (systematically named) GIF files to BMP files (8 bit color depth with color table aka palette)
                          that are archived/historical medium range (Day 7 - Day 3) forecasts
                          from NOAA/NWS Weather Prediction Center.
                        E.G. Day 4 forecast "issued" on a Monday is "valid" on Friday.
                        Convert files for daily min/max temp prediction, probability of precipitation prediction.
                        Convert files for a specified date range.
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/4/16 - 1/21/16
'''
from PIL import Image #Pillow (PIL fork, Python Image Library)
import os #for interacting with operating system, file system
import sys #interact with the Python interpreter (~platform runtime)

local_data_dir_in = '../data/downloaded_data/'
local_data_dir_out = '../data/converted_data/'

max_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31] #non-leap year, set to 0 to skip a month
#max_day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31] #leap year - actually, did not find 2/29/12 data on website
issue_year = 2015

print
print 'For forecasts issued: year', issue_year

for issue_month in range(1,13): # 1 - 12
  for issue_day in range(1, max_day_in_month[issue_month-1]+1): # 1 - 28 or 29 or 30 or 31
    if issue_year==2013 and issue_month==3 and issue_day==3: continue #for some reason there are no 20130303 (issue date) GIF files on website
    issue_date = str(issue_year) + str('%02u' % issue_month) + str('%02u' % issue_day) #YYYYMMDD, the date that the forecasts were issued
    for forecast_day in ['3','4','5','6','7']: #forecast is valid for a date that is this many days ahead
      for forecast_type in ['MIN','MAX','POP1','POP2']: #min/max temp prediction, probability of precipitation prediction for 12Z/00Z, Z=UTC
        file_name_in = issue_date+'12_DAY'+forecast_day+'_'+forecast_type+'_filled'
        file_name_out = issue_date+'_DAY'+forecast_day+'_'+forecast_type
        print 'Convert '+local_data_dir_in+file_name_in+'.gif to '+local_data_dir_out+file_name_out+'.bmp'
        #Luckily, save method is creating BMP with 8 bit color depth with color table (aka palette), maybe because GIF is 8 bit color depth?
        Image.open(local_data_dir_in+file_name_in+'.gif').save(local_data_dir_out+file_name_out+'.bmp') #Don't even need to save the image in a variable
        sys.stdout.write('Original file size: '+str(os.stat(local_data_dir_in+file_name_in+'.gif').st_size)+' bytes; ')
        print 'converted file size:', os.stat(local_data_dir_out+file_name_out+'.bmp').st_size, 'bytes'

print 'Done!'

