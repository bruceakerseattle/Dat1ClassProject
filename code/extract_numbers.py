'''
extract_numbers.py - 3rd script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) pivot_and_join.py
                     Extract numbers embedded in weather forecast image file.
                     Specifically, extract daily min/max temperature prediction (Fahrenheit),
                       and probability of precipitation prediction (POP, out of 100%) from archived/historical image files
                       of NOAA/NWS Weather Prediction Center medium range forecasts (Day 7 - Day 3)
                       by identifying bit pattern of characters 0 - 9 and minus sign.
                     Dates associated with the numbers is the date in which the forecast was issued.
                     Also create one new column (valid_date_calcd) using a simple calculation.
                     FYI- Day 4 forecast "issued" on a Monday is "valid" on Friday.
                     Numbers in image are at most 3 characters (between -99 and 999), always black color,
                       always same 9 x 13 font (columns x rows), no anti-aliasing.
                     Numbers extracted from Windows BMP files (assume 8 bit color depth, with a color table)
                       which were produced previously by conversion from the downloaded GIF files.
                     Extract numbers for a specified issue date range.
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   12/5/15 - 1/21/16
'''
import struct #for reading intergers, bytes in a byte-string (from a binary file)
import os #for interacting with operating system, file system
import sys #interact with the Python interpreter (~platform runtime)
import datetime

'''
    ***** READ IN SOME DATA ***** 
'''
# Read in pixel arrays of characters for recognizing postive and negative integers (e.g. 32, 101, 7, 0, -5, -11) in the images
# Recognize 11 characters: 0,1,2,...,9,-
with open('pixel_array_of_chars.py', mode='rU') as f:
  char_patterns = eval(f.read()) # tuple of tuples of tuples: [character][row][column], value is 1 if pixel in character
                                 # image: row=y=vertical=lower-upper, column=x=horizontal=left-right, origin: lower-left (0,0) 

#Location of each of the following numbers in the image corresponds to a city (or weather station) in the continental U.S.
#Location of (lower-left pixel of) first character of number in image (weather number, e.g. max temperature)
#0-based row=y, column=x (origin=lower-left); character is 13 rows x 9 columns pixel array
with open('weather_stn_data.py', mode='rU') as f:
  chars_origins = eval(f.read()) # list of dictionaries with elements: 'icao_code','row','col',...

#column (aka x) of number in image varies slightly depending upon number of characters and positive or negative (row aka y doesn't change)
#Do negative numbers first so as to not mistake a negative number for a positive number (remember char width is 9)
x_offset_for_num_chars = [{'num_chars':3,'sign':-1,'x_offset':-9},{'num_chars':2,'sign':-1,'x_offset':-3},
                          {'num_chars':2,'sign': 1,'x_offset': 0},{'num_chars':1,'sign': 1,'x_offset': 6},
                          {'num_chars':3,'sign': 1,'x_offset':-6},{'num_chars':1,'sign': 1,'x_offset': 5}, #For some strange reason, a few locations display
                                                                                                           #  single character numbers one pixel to the left
                                                                                                           #  in the POP images, so add this element/dict.
                          {'num_chars':3,'sign':-1,'x_offset':-8}, #For some strange reason, a few locations display
                                                                   #  3 char negative numbers (e.g. -23) one pixel to the right
                                                                   #  possibly only in the MIN (temp) images, so add this element/dict.
                          {'num_chars':3,'sign': 1,'x_offset':-5}] #For some strange reason, a few locations display
                                                                   #  3 char positive numbers (e.g. 123) one pixel to the right
                                                                   #  possibly only in the MAX (temp) images, so add this element/dict.

'''
    ***** FUNCTIONS ***** 
'''
def found_num(found_chr, num_chrs, sign):
  '''
  Given the number of characters looking for,
  check that found exactly one character at first position and one or zero at 2nd position, 3rd position,...
  E.G. if looking for 2 char's, ensure found exactly 1 char in positions 1 and 2, and 0 char's in 3rd position,...
  Also, check for minus sign character depending on looking for a negative or positive number
  '''
  max_num_chrs = len(found_chr)
  retval = found_chr[0][10] == (sign < 0) #True if [found|didn't find] minus sign in first position and searching for a [negative|positive] number
  for i_chr_pos in range(max_num_chrs): #cycle thru char positions
    retval = retval and sum(found_chr[i_chr_pos]) == (1 if i_chr_pos < num_chrs else 0)
  return retval

def calc_wea_num(found_chr, num_chrs, sign):
  '''
  Calculate the weather number, e.g. min/max temperature, probability of precipitation from the char's found
  Assume the 3 character positions contain a valid integer between -99 and 999
  '''
  wea_num = 0
  nums_col = 1 #e.g. initialy looking at the one's place (which could be in the 3rd, 2nd, or 1st char position)
  for i_chr_pos in range(num_chrs-1, 0 if sign < 0 else -1, -1): #examine 1s place first, then 10s place (if exists), then 100s place (if exists)
    for i_chr in range(10): #cycle thru characters 0,1,2,3,4,5,6,7,8,9
      if found_chr[i_chr_pos][i_chr]:
        wea_num += i_chr * nums_col
        break
    nums_col = nums_col * 10 #e.g. initially 1s place, then 10s place, 100s place
  return -wea_num if sign < 0 else wea_num

def my_err_exit(msg):
  print 'Error:',msg
  sys.exit()

'''
    ***** START OF MAIN PROGRAM ***** 
'''
data_dir_from = '../data/converted_data/' #BMP image files
data_file_to = '../data/med_range_forecast.csv' #store data in this text file
file_hdr_size = 14 #bytes, always for a BMP file
invalid_wea_num = -9999 # weather number, e.g. min/max temperature prediction, probability of precipitation
valid_image_width = 896 # currently, code only works for one particulare image size

max_day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31] #non-leap year, set to 0 to skip a month
#max_day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31] #leap year - actually, did not find 2/29/12 data on website
issue_year = 2015

print
print 'Store data in', data_file_to

#if doesn't exist, create data output text file (.csv) with header (column titles)
if not os.path.exists(data_file_to):
  with open(data_file_to,mode='w') as f:
    f.write('wea_stn_cd,issue_date,forecast_type_day,wea_num,valid_date_calcd\n')

total_num_wea_stn_not_found = 0
wea_stns_not_found_msg = ''

f_to = open(data_file_to,mode='a') #open output CSV data/text file for writing to (append) 

for issue_month in range(1,13): # 1 - 12
  for issue_day in range(1, max_day_in_month[issue_month-1]+1): # 1 - 28 or 29 or 30 or 31
    if issue_year==2013 and issue_month==3 and issue_day==3: continue #for some reason there are no 20130303 (issue date) GIF files on website
    issue_date = str(issue_year) + str('%02u' % issue_month) + str('%02u' % issue_day) #YYYYMMDD, the date that the forecasts were issued
    for forecast_day in ['3','4','5','6','7']: #forecast is valid for a date that is this many days ahead
      valid_date_calcd = datetime.date(issue_year,issue_month,issue_day) + datetime.timedelta(days=int(forecast_day)) # result is an instance of class date
      for forecast_type in ['MIN','MAX','POP1','POP2']: #min/max temp prediction, probability of precipitation prediction for 12Z/00Z, Z=UTC
        file_name = issue_date + '_DAY' + forecast_day + '_' + forecast_type + '.bmp'
        black_idx = -1 #initially invalid value
        num_wea_stn_found=0
        num_wea_stn_not_found=0

        sys.stdout.write('For file spec ' + data_dir_from + file_name + ', ')

        #Read in the bytes of the image file
        with open(data_dir_from+file_name, mode='rb') as f:
          image_file_bytes = f.read()

        idx_bytes = 0 #index into bytes of the image
        if image_file_bytes[idx_bytes:idx_bytes+2] != 'BM': #verify file signature for BMP file
          my_err_exit('file signature incorrect')

        idx_bytes = 0x0A
        pixel_array_offset = struct.unpack('I', image_file_bytes[idx_bytes:idx_bytes+4])[0]
        if pixel_array_offset == 0: #verify pixel array offset
          my_err_exit('bad pixel array offset')

        idx_bytes = 0x0E
        dib_hdr_size = struct.unpack('I', image_file_bytes[idx_bytes:idx_bytes+4])[0]
        if dib_hdr_size == 0: # verify (device independent) bitmap header size
          my_err_exit('bad bitmap header size')

        idx_bytes = 0x12
        image_width = struct.unpack('I', image_file_bytes[idx_bytes:idx_bytes+4])[0]
        if image_width == 0: # verify image width
          my_err_exit('bad image width')
        elif image_width!=valid_image_width: # check for the one image width that the code currently works with
          wea_stn_not_found='incompatible image width'
          if wea_stns_not_found_msg:
            wea_stns_not_found_msg+='\n'
          wea_stns_not_found_msg+='  in '+file_name+', '+wea_stn_not_found
          num_wea_stn_not_found+=len(chars_origins)
          sys.stdout.write(wea_stn_not_found+', ')
        else:
          if image_width % 4 != 0: # verify pixel array padding is not needed (currently, code doesn't support it)
            my_err_exit('cannot handle non-zero pixel array padding')

          idx_bytes = 0x1C
          if struct.unpack('H', image_file_bytes[idx_bytes:idx_bytes+2])[0] != 8: # verify 8 bit color depth
            my_err_exit('image is not 8 bit color depth')

          idx_bytes = file_hdr_size + dib_hdr_size # file header size + DIB header size = color table offset

          #Look in color table for the color index (0,1,2,...) of (first) black color (RedGreenBlue = 0 0 0)
          for idx_color in range(256): # 4 bytes used to store each 24bit color value
            color_value = struct.unpack('BBB',image_file_bytes[idx_bytes:idx_bytes+3]) #returns tuple of 3 bytes
            if color_value == (0,0,0):
              black_idx = idx_color
              break
            idx_bytes += 4

          if black_idx < 0: # verify found black in color table
            my_err_exit('Cannot find black in color table')

          for wea_stn in chars_origins:
            # char's location in image corresponds to a weather station location
            weather_number = invalid_wea_num #will eventually hold, hopefully, the number we are trying to extract

            #Look for a "weather number" (e.g. max temperature prediction) at this location in U.S. 
            for i_x_offset in range(len(x_offset_for_num_chars)): #Cycle thru number of char's (and +/-) which affects the x-offset,
                                                                  # e.g. look for number like -23, then like -2, then like 12, then like 1, then like 123
              #Assume we are searching for at most 3 characters, i.e. integers between -99 and 999
              #During search these will be set to False except for one of them, hopefully, at each character position
              found_char = [[True,True,True,True,True,True,True,True,True,True,True], #each element (a list) corresponds to list of characters: 0,1,2,3,4,5,6,7,8,9,-
                            [True,True,True,True,True,True,True,True,True,True,True], #2nd element is 2nd character position, if exists
                            [True,True,True,True,True,True,True,True,True,True,True]] #3rd character position, if exists
              for i_row in range(13): #cycle thru pixel rows (of all 3 character positions) within the characters in image
                idx_bytes = pixel_array_offset + (wea_stn['row'] + i_row) * image_width + wea_stn['col'] + x_offset_for_num_chars[i_x_offset]['x_offset']
                bytes1_row = struct.unpack('9B',image_file_bytes[idx_bytes:idx_bytes+9]) #returns tuple of 9 bytes (color index of each of the 9 pixels)
                char1_pixel_row = [int(byt==black_idx) for byt in bytes1_row] #store a 1 if color index is index of black, else store a 0
                bytes2_row = struct.unpack('9B',image_file_bytes[idx_bytes+9:idx_bytes+18]) #not needed if looking for one character
                char2_pixel_row = [int(byt==black_idx) for byt in bytes2_row]
                bytes3_row = struct.unpack('9B',image_file_bytes[idx_bytes+18:idx_bytes+27]) #not needed if looking for one or two characters
                char3_pixel_row = [int(byt==black_idx) for byt in bytes3_row]
                for i_char in range(11): #cycle thru the 11 characters (0,1,2,...,9,-) looking for mismatches
                  if found_char[0][i_char] and char1_pixel_row != list(char_patterns[i_char][i_row]): #if not False already then compare a row w/in 1st char from image with
                    found_char[0][i_char] = False                                                     #  a row w/in char from stored char patterns, and set to False if mismatch
                  if found_char[1][i_char] and char2_pixel_row != list(char_patterns[i_char][i_row]): #not needed if looking for one character
                    found_char[1][i_char] = False
                  if found_char[2][i_char] and char3_pixel_row != list(char_patterns[i_char][i_row]): #not needed if looking for one or two characters
                    found_char[2][i_char] = False
              #For a given number of char's (and +/-) if found a valid number...
              if found_num(found_char, x_offset_for_num_chars[i_x_offset]['num_chars'],x_offset_for_num_chars[i_x_offset]['sign']):
                weather_number = calc_wea_num(found_char, x_offset_for_num_chars[i_x_offset]['num_chars'], x_offset_for_num_chars[i_x_offset]['sign'])
                #print 'For weather station code', wea_stn['icao_code'],'found weather number', weather_number
                num_wea_stn_found+=1
                break

            if weather_number == invalid_wea_num:
              wea_stn_not_found='for weather station code '+wea_stn['icao_code']+' did not find a weather number'
              sys.stdout.write(wea_stn_not_found+', ')
              num_wea_stn_not_found+=1
              if wea_stns_not_found_msg:
                wea_stns_not_found_msg+='\n'
              wea_stns_not_found_msg+='  in '+file_name+', '+wea_stn_not_found

            f_to.write('%s,%s,%s,' % (wea_stn['icao_code'],issue_date,forecast_type.lower() + '_' + forecast_day.lower()))
            if weather_number != invalid_wea_num:
              f_to.write('%i,%u%02u%02u\n' % (weather_number,valid_date_calcd.year,valid_date_calcd.month,valid_date_calcd.day))
            else:
              f_to.write(',%u%02u%02u\n' % (valid_date_calcd.year,valid_date_calcd.month,valid_date_calcd.day))
        print 'found %u out of %u weather numbers' % (num_wea_stn_found,num_wea_stn_found+num_wea_stn_not_found)
        total_num_wea_stn_not_found += num_wea_stn_not_found
f_to.close()
print 'Done! ', total_num_wea_stn_not_found, 'weather number(s) not found'
if wea_stns_not_found_msg:
  print wea_stns_not_found_msg





