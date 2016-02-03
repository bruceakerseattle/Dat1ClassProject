'''
pivot_and_join.py - 5th script in sequence 1.) download_images.py, 2.) convert_gif_to_bmp.py, 3.) extract_numbers.py, 4.) get_past_observations_cdo.py, 5.) pivot_and_join.py
                    Read in the medium range forecast numbers, switch to using valid_date instead of issue_date, pivot the table 
                      putting all data associated with each valid_date (and each weather station) on one line,
                      read in weather observations data, merge the 2 tables on wea_stn_cd and valid_date, write to output file
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/5/16 - 1/21/16
'''
import pandas as pd

pd.set_option('display.width',pd.util.terminal.get_terminal_size()[0]) #default: 80 characters
pd.set_option('display.max_columns',30) #default: 20
maxrows = pd.util.terminal.get_terminal_size()[1]-14 #leave room for some other stuff
pd.set_option('display.max_rows',maxrows) #default: 60

data_file_in1 = '../data/med_range_forecast.csv' # file is in 'data' directory which is sibling to directory of this script
data_file_in2 = '../data/past_observation.csv'
data_file_out = '../data/forecast_and_obs.csv'

print '\nRead in', data_file_in1 #medium range forecasts
print 'Rename column valid_date_calcd to valid_date so can do the join with other table'
dfmr = pd.read_csv(data_file_in1)
dfmr.rename(columns = {'valid_date_calcd':'valid_date'}, inplace = True)
#print 'Shape of table:', dfmr.shape
print 'Column datatypes:\n', dfmr.dtypes
print '\nSome data:\n', dfmr

print '\nDrop column: issue_date (not needed, switching to valid_date)'
dfmr.drop('issue_date',axis=1,inplace=True)
print 'Shape of table:', dfmr.shape

print '\nPivot table on column: forecast_type_day (putting all data associated with each valid_date on one line)'
dfmr20cols = pd.pivot_table(dfmr,values='wea_num',index=['wea_stn_cd','valid_date'],columns=['forecast_type_day'])
#print 'Shape of pivoted table:', dfmr20cols.shape
print 'Index:', dfmr20cols.index.names
print '\nSome data:\n', dfmr20cols

print '\nRead in', data_file_in2 # actual weather observations
dfobs = pd.read_csv(data_file_in2)
#print 'Shape of table:', dfobs.shape
print 'Column datatypes:\n', dfobs.dtypes
print '\nSome data:\n', dfobs

print '\nPivot table on column: wea_num_type (putting all data associated with each valid_date on one line)'
dfobs4cols = pd.pivot_table(dfobs,values='wea_num',index=['wea_stn_cd','valid_date'],columns=['wea_num_type'])
#print 'Shape of pivoted table:', dfobs4cols.shape
print 'Index:', dfobs4cols.index.names
print '\nSome data:\n', dfobs4cols

how_merge='outer'
print '\nMerge ('+how_merge+') the medium range forecasts and weather observations tables'
dfmrobs = dfmr20cols.join(dfobs4cols, how=how_merge, sort=True) #join on index ['wea_stn_cd','valid_date']
#print 'Shape of table:', dfmrobs.shape
print 'Index:', dfmrobs.index.names
print '\nSome data:\n', dfmrobs

print '\nSave in', data_file_out
dfmrobs.to_csv(data_file_out) 


                                                  
