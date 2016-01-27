'''
analyze_errors.py - Calculate the mean (signed) errors between forecast and observed numbers (i.e. systematic errors) for a few weather stations
                    Calculate mean absolute errors
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/7/16 - 1/21/16
'''
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width',pd.util.terminal.get_terminal_size()[0])
pd.set_option('display.max_columns',30)
pd.set_option('display.max_rows',30)

print '\nRead data file into pandas dataframe'
dfmrobs=pd.read_csv('../data/forecast_and_obs.csv')
print dfmrobs

print '\nCreate new column numbering each of the five 365 day periods (1-5)' # from 20110108 - 20160107 (YYYYMMDD)
dfmrobs['year_num'] = (dfmrobs.valid_date-108)//10000 - 2010

print '\nCreate new columns that are the max temp forecast errors'
dfmrobs['max_7_err'] = dfmrobs.max_7 - dfmrobs.tmax
dfmrobs['max_6_err'] = dfmrobs.max_6 - dfmrobs.tmax
dfmrobs['max_5_err'] = dfmrobs.max_5 - dfmrobs.tmax
dfmrobs['max_4_err'] = dfmrobs.max_4 - dfmrobs.tmax
dfmrobs['max_3_err'] = dfmrobs.max_3 - dfmrobs.tmax

dfmrobs['max_7_abs_err'] = dfmrobs['max_7_err'].abs()
dfmrobs['max_6_abs_err'] = dfmrobs['max_6_err'].abs()
dfmrobs['max_5_abs_err'] = dfmrobs['max_5_err'].abs()
dfmrobs['max_4_abs_err'] = dfmrobs['max_4_err'].abs()
dfmrobs['max_3_abs_err'] = dfmrobs['max_3_err'].abs()

print '\nCreate new columns for accuracy of precipitation forecast'
dfmrobs['prcp_7_accr'] = (((dfmrobs.pop1_7+dfmrobs.pop2_7)/2.0<=5.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_7+dfmrobs.pop2_7)/2.0>5.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_6_accr'] = (((dfmrobs.pop1_6+dfmrobs.pop2_6)/2.0<=5.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_6+dfmrobs.pop2_6)/2.0>5.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_5_accr'] = (((dfmrobs.pop1_5+dfmrobs.pop2_5)/2.0<=5.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_5+dfmrobs.pop2_5)/2.0>5.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_4_accr'] = (((dfmrobs.pop1_4+dfmrobs.pop2_4)/2.0<=5.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_4+dfmrobs.pop2_4)/2.0>5.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_3_accr'] = (((dfmrobs.pop1_3+dfmrobs.pop2_3)/2.0<=5.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_3+dfmrobs.pop2_3)/2.0>5.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))

print '\nFor example, for Seattle, for each day\'s high temperature, a random sample...'
col_list=['valid_date','year_num','tmax',
          'max_7_err','max_6_err','max_5_err','max_4_err','max_3_err',
          'pop1_7','pop2_7','prcp','snow',
          'prcp_7_accr','prcp_6_accr','prcp_5_accr','prcp_4_accr','prcp_3_accr']
print dfmrobs[(dfmrobs.wea_stn_cd=='KSEA')&(dfmrobs.pop1_7.notnull())][col_list].sample(30)
print 'Positive number means forecast was too high'
'''
print '\nCalculate mean abs error, mean (signed) error and standard deviation for Seattle...'
print dfmrobs[dfmrobs.wea_stn_cd=='KSEA'][['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KSEA'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KSEA'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].std()

print '\nCalculate mean abs error, mean (signed) error and standard deviation for Portland...'
print dfmrobs[dfmrobs.wea_stn_cd=='KPDX'][['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KPDX'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KPDX'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].std()

print '\nCalculate mean abs error, mean (signed) error and standard deviation for Los Angeles...'
print dfmrobs[dfmrobs.wea_stn_cd=='KLAX'][['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KLAX'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()
print dfmrobs[dfmrobs.wea_stn_cd=='KLAX'][['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].std()
'''
print'Group by year_num, mean abs error of max temp'
dfmrobsmeanabserr=dfmrobs.groupby('year_num')[['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']].mean()
print dfmrobsmeanabserr

print'Group by year_num, mean (signed) error of max temp'
dfmrobsmeanerr=dfmrobs.groupby('year_num')[['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()
print dfmrobsmeanerr

print'Group by year_num, std dev of max temp error'
dfmrobsstddeverr=dfmrobs.groupby('year_num')[['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].std()
print dfmrobsstddeverr

print'Group by year_num, mean prcp accuracy'
dfmrobsmeanprcpaccr=dfmrobs[dfmrobs.year_num>2].groupby('year_num')[['prcp_7_accr','prcp_6_accr','prcp_5_accr','prcp_4_accr','prcp_3_accr']].mean()
print dfmrobsmeanprcpaccr

plt.clf()
print '\nMake a Mean Prcp Accuracy plot...'
y_list=['prcp_7_accr','prcp_6_accr','prcp_5_accr','prcp_4_accr','prcp_3_accr']
dfmrobsmeanprcpaccr.plot(kind='bar', y=y_list, ylim=[0,1],rot=0, title='Mean Accuracy in Daily Precipitation Forecast')
plt.ylabel('Fraction Accurate')
plt.savefig('../viz/prcp_accr_by_yr_num_bar.png')

'''
plt.clf()
print '\nMake a Mean Absolute Error plot...'
y_list=['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']
dfmrobsmeanabserr.plot(kind='bar', y=y_list, ylim=[0,9],rot=0, title='Mean Absolute Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_abs_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a short Mean Absolute Error plot...'
y_list=['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']
dfmrobsmeanabserr.plot(kind='bar', y=y_list, ylim=[0,10],rot=0, figsize=(10,5), title='Mean Absolute Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_abs_err_by_yr_num_bar_short.png')

plt.clf()
print '\nMake a Mean (Signed) Error plot...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobsmeanerr.plot(kind='bar', y=y_list, ylim=[-2.5,0],rot=0, title='Mean (Signed) Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a Std Dev Error plot...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobsstddeverr.plot(kind='bar', y=y_list, ylim=[0,12],rot=0, title='Std Dev of Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_stddev_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a Box plot for Error...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobs.boxplot(column=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err'], by='year_num', figsize=(10,6),layout=(1,5))
plt.savefig('../viz/max_temp_err_by_yr_num_box.png')
'''



