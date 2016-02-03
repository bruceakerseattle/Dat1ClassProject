'''
analyze_errors.py - Calculate the mean (signed) errors between forecast and observed numbers (i.e. systematic errors) for a few weather stations
                    Calculate mean absolute errors
                    Run after pivot_and_join.py
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/7/16 - 1/21/16
'''
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width',pd.util.terminal.get_terminal_size()[0]) #default: 80 characters
pd.set_option('display.max_columns',30) #default: 20
maxrows = pd.util.terminal.get_terminal_size()[1]-14 #leave room for some other stuff
#maxrows = 20
pd.set_option('display.max_rows',maxrows) #default: 60

print '\nRead data file into pandas dataframe'
dfmrobs=pd.read_csv('../data/forecast_and_obs.csv')
print dfmrobs

print '\nA sample of data'
print dfmrobs.sample(30)

print '\nCreate new column numbering each of the five 365 day periods (1-5)' # from 20110108 - 20160107 (YYYYMMDD)
dfmrobs['year_num'] = (dfmrobs.valid_date-108)//10000 - 2010

print '\nCreate new columns that are the max temp forecast errors'
dfmrobs['max_7_err'] = dfmrobs.max_7 - dfmrobs.tmax
dfmrobs['max_6_err'] = dfmrobs.max_6 - dfmrobs.tmax
dfmrobs['max_5_err'] = dfmrobs.max_5 - dfmrobs.tmax
dfmrobs['max_4_err'] = dfmrobs.max_4 - dfmrobs.tmax
dfmrobs['max_3_err'] = dfmrobs.max_3 - dfmrobs.tmax

print '\nFor example, for each day\'s high temperature, a random sample of errors...'
col_list=['wea_stn_cd','valid_date','year_num',
          'max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
print dfmrobs[col_list].sample(30)
print 'Positive number for error means forecast was too high'

print '\nCreate new columns that are the min temp forecast errors'
dfmrobs['min_7_err'] = dfmrobs.min_7 - dfmrobs.tmin
dfmrobs['min_6_err'] = dfmrobs.min_6 - dfmrobs.tmin
dfmrobs['min_5_err'] = dfmrobs.min_5 - dfmrobs.tmin
dfmrobs['min_4_err'] = dfmrobs.min_4 - dfmrobs.tmin
dfmrobs['min_3_err'] = dfmrobs.min_3 - dfmrobs.tmin

print '\nCreate new column for month of the year'
dfmrobs['month'] = (dfmrobs.valid_date-20110000)//100%100

print '\nCreate new columns for accuracy of precipitation forecast'
dfmrobs['prcp_7_accr'] = (((dfmrobs.pop1_7+dfmrobs.pop2_7)/2.0<=50.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_7+dfmrobs.pop2_7)/2.0>50.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_6_accr'] = (((dfmrobs.pop1_6+dfmrobs.pop2_6)/2.0<=50.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_6+dfmrobs.pop2_6)/2.0>50.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_5_accr'] = (((dfmrobs.pop1_5+dfmrobs.pop2_5)/2.0<=50.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_5+dfmrobs.pop2_5)/2.0>50.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_4_accr'] = (((dfmrobs.pop1_4+dfmrobs.pop2_4)/2.0<=50.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_4+dfmrobs.pop2_4)/2.0>50.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
dfmrobs['prcp_3_accr'] = (((dfmrobs.pop1_3+dfmrobs.pop2_3)/2.0<=50.0)&(dfmrobs.prcp+dfmrobs.snow==0.0))|(((dfmrobs.pop1_3+dfmrobs.pop2_3)/2.0>50.0)&(dfmrobs.prcp+dfmrobs.snow>0.0))
#for =50% could score 1 (or .5?) for rainy day and -1 (or -.5?) for no rain, calc abs value of sum (sum=0 if equal rain/dry days), calc average, then subtract from 1 (perfect score)

dfmrobs['max_7_abs_err'] = dfmrobs['max_7_err'].abs()
dfmrobs['max_6_abs_err'] = dfmrobs['max_6_err'].abs()
dfmrobs['max_5_abs_err'] = dfmrobs['max_5_err'].abs()
dfmrobs['max_4_abs_err'] = dfmrobs['max_4_err'].abs()
dfmrobs['max_3_abs_err'] = dfmrobs['max_3_err'].abs()

print'\nGroup by year_num, mean abs error of max temp'
dfmrobsmeanabserr=dfmrobs.groupby('year_num')[['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']].mean()
print dfmrobsmeanabserr

print'\nGroup by year_num, mean (signed) error of max temp'
dfmrobsmeanerr=dfmrobs.groupby('year_num')[['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].mean()
print dfmrobsmeanerr

print'\nGroup by year_num, std dev of max temp error'
dfmrobsstddeverr=dfmrobs.groupby('year_num')[['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']].std()
print dfmrobsstddeverr

print'\nGroup by year_num, mean prcp accuracy'
dfmrobsmeanprcpaccr=dfmrobs[dfmrobs.year_num>2].groupby('year_num')[['prcp_7_accr','prcp_6_accr','prcp_5_accr','prcp_4_accr','prcp_3_accr']].mean()
print dfmrobsmeanprcpaccr

print'\nGroup by year_num, mean (signed) error of min temp'
dfmrobsmeanminerr=dfmrobs.groupby('year_num')[['min_7_err','min_6_err','min_5_err','min_4_err','min_3_err']].mean()
print dfmrobsmeanminerr

plt.clf()
print '\nMake a Mean Absolute Max Temp Error plot...'
y_list=['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']
dfmrobsmeanabserr.plot(kind='bar', y=y_list, ylim=[0,11],rot=0, title='Mean Absolute Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_abs_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a short Mean Absolute Max Temp Error plot...'
y_list=['max_7_abs_err','max_6_abs_err','max_5_abs_err','max_4_abs_err','max_3_abs_err']
dfmrobsmeanabserr.plot(kind='bar', y=y_list, ylim=[0,10],rot=0, figsize=(10,5), title='Mean Absolute Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_abs_err_by_yr_num_bar_short.png')

plt.clf()
print '\nMake a Mean (Signed) Max Temp Error plot...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobsmeanerr.plot(kind='bar', y=y_list, ylim=[-11,0],rot=0, title='Mean (Signed) Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a Std Dev Max Temp Error plot...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobsstddeverr.plot(kind='bar', y=y_list, ylim=[0,11],rot=0, title='Std Dev of Error in Daily Max Temperature Forecast')
plt.ylabel('Degrees Fahrenheit')
plt.savefig('../viz/max_temp_stddev_err_by_yr_num_bar.png')

plt.clf()
print '\nMake a Mean Prcp Accuracy plot...'
y_list=['prcp_7_accr','prcp_6_accr','prcp_5_accr','prcp_4_accr','prcp_3_accr']
dfmrobsmeanprcpaccr.plot(kind='bar', y=y_list, ylim=[0,1.12],rot=0, title='Mean Accuracy in Daily Precipitation Forecast')
plt.ylabel('Fraction Accurate')
plt.savefig('../viz/prcp_accr_by_yr_num_bar.png')

plt.clf()
print '\nMake a Box plot for Max Temp Error by year_num...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobs.boxplot(column=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err'], by='year_num', figsize=(10,6),layout=(1,5))
plt.savefig('../viz/max_temp_err_by_yr_num_box.png')

plt.clf()
print '\nMake a Box plot for Max Temp Error by month...'
y_list=['max_7_err','max_6_err','max_5_err','max_4_err','max_3_err']
dfmrobs.boxplot(column=y_list, by='month', figsize=(11,6),layout=(1,5))
plt.savefig('../viz/max_temp_err_by_month_box.png')

plt.clf()
print '\nMake a Box plot for Min Temp Error by year_num...'
y_list=['min_7_err','min_6_err','min_5_err','min_4_err','min_3_err']
#skip the few really far outliers (so get same scale as other boxplots)
dfmrobs[(dfmrobs.min_7_err<40)&(dfmrobs.min_7_err>-40)&(dfmrobs.min_6_err<40)&(dfmrobs.min_6_err>-40)&(dfmrobs.min_5_err<40)&(dfmrobs.min_5_err>-40)& \
    (dfmrobs.min_4_err<40)&(dfmrobs.min_4_err>-40)&(dfmrobs.min_3_err<40)&(dfmrobs.min_3_err>-40)].boxplot(column=y_list, by='year_num',figsize=(10,6),layout=(1,5))
plt.savefig('../viz/min_temp_err_by_yr_num_box.png')





