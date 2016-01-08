'''
pivot_and_join.py - 4th script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) pivot_and_join.py
                    Read in the medium range forecast numbers, switch to using valid_date instead of issue_date, pivot the table 
                      putting all data associated with each valid_date (and each weather station) on one line,
                      read in weather observations data, merge the 2 tables on wea_stn_cd and valid_date, write to output file
General Assembly - Data Science class project - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/5/16 - 1//16
'''
import pandas as pd

data_file_in1 = '../data/med_range_forecast.csv' # file is in 'data' directory which is sibling to directory of this script
data_file_in2 = '../data/past_observation.csv'
data_file_out = '../data/med_range_forecast_obs.csv'

print '\nRead in', data_file_in1 #medium range forecasts
print 'Rename column valid_date_calcd to valid_date so can do the join with other table'
dfmr = pd.read_csv(data_file_in1)er input data file'
dfmr.rename(columns = {'valid_date_calcd':'valid_date'}, inplace = True)
print 'Shape of table:', dfmr.shape
print 'Column datatypes:\n', dfmr.dtypes
print '\nSome data:\n', dfmr.head()

print '\nDrop column: issue_date (not needed, switching to valid_date)'
dfmr.drop('issue_date',axis=1,inplace=True)
print 'Shape of table:', dfmr.shape

print '\nPivot table on column: forecast_type_day (putting all data associated with each valid_date on one line)'
dfmr20cols = pd.pivot_table(dfmr,values='wea_num',index=['wea_stn_cd','valid_date'],columns=['forecast_type_day'])
print 'Shape of pivoted table:', dfmr20cols.shape
print 'Index:', dfmr20cols.index.names
print '\nSome data:\n', dfmr20cols.head()

print '\nRead in', data_file_in2 # actual weather observations
dfobs = pd.read_csv(data_file_in2, index_col=['wea_stn_cd','valid_date'])
print 'Shape of table:', dfobs.shape
print 'Index:', dfobs.index.names
print 'Column datatypes:\n', dfobs.dtypes
print '\nSome data:\n', dfobs.head()

print '\nMerge the medium range forecasts and weather observations tables'
dfmrobs = dfmr20cols.join(dfobs, how='inner', sort=True) #join on index ['wea_stn_cd','valid_date']
print 'Shape of table:', dfmrobs.shape
print 'Index:', dfmrobs.index.names
print '\nSome data:\n', dfmrobs.head()

print '\nSave in', data_file_out
dfmrobs.to_csv(data_file_out,float_format='%.0f') #integer values may have been converted to float when read in because of missing values,
                                                  #  but change all floats back to integer format when writing to output file.
                                                  #NOTE: Water column (observed precipitation in inches) looks like a float (and we want to write it as a float)
                                                  #  but it is a string because sometimes has 'T' value (trace), so it isn't writen in integer format


