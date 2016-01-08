'''
analyze_errors.py - 
                    
General Assembly - Data Science class project - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/7/16 - 1//16
'''
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width',pd.util.terminal.get_terminal_size()[0])
pd.set_option('display.max_columns',30)

print '\nRead data file into pandas dataframe'
dfmrobs=pd.read_csv('../data/med_range_forecast_obs.csv')
print dfmrobs

print '\nCreate new columns that are the forecast errors'
dfmrobs['max_7_err'] = dfmrobs.max_7 - dfmrobs.max_temp
dfmrobs['max_6_err'] = dfmrobs.max_6 - dfmrobs.max_temp
dfmrobs['max_5_err'] = dfmrobs.max_5 - dfmrobs.max_temp
dfmrobs['max_4_err'] = dfmrobs.max_4 - dfmrobs.max_temp
dfmrobs['max_3_err'] = dfmrobs.max_3 - dfmrobs.max_temp

print 'For example, for Seattle, for each day\'s high temperature...'
print dfmrobs[(dfmrobs.wea_stn_cd=='KSEA')][['valid_date','max_temp','max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']]
print 'Positive number means forecast was too high'

print '\nCalculate mean (signed) error...'
print dfmrobs[(dfmrobs.wea_stn_cd=='KSEA')][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()

print '\nCalculate mean (signed) error for Portland...'
print dfmrobs[(dfmrobs.wea_stn_cd=='KPDX')][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()

print '\nCalculate mean (signed) error for Los Angeles...'
print dfmrobs[(dfmrobs.wea_stn_cd=='KLAX')][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()

print '\nPlot the errors for each day and save .png file (after creating new column valid_day)'
dfmrobs['valid_day'] = dfmrobs.valid_date - 20151000
dfmrobs[(dfmrobs.wea_stn_cd=='KSEA')].plot(kind='bar', x='valid_day', y=['max_7_err','max_5_err','max_3_err'], title='Error in High Temperature Forecast, Oct. 2015, Seattle')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../data/sea_max_err_by_day_bar.png')

plt.clf()
dfmrobs[(dfmrobs.wea_stn_cd=='KPDX')].plot(kind='bar', x='valid_day', y=['max_7_err','max_5_err','max_3_err'], title='Error in High Temperature Forecast, Oct. 2015, Portland')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../data/pdx_max_err_by_day_bar.png')

plt.clf()
dfmrobs[(dfmrobs.wea_stn_cd=='KLAX')].plot(kind='bar', x='valid_day', y=['max_7_err','max_5_err','max_3_err'], title='Error in High Temperature Forecast, Oct. 2015, Los Angeles')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../data/lax_max_err_by_day_bar.png')




