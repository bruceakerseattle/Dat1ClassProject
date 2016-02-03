'''
summarize_data.py - Verifies unique identifier: wea_stn_cd/valid_date, summarizes missing data
                    Run after pivot_and_join.py
Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
Developed by Bruce Aker   1/4/16 - 1/28/16
'''
import pandas as pd

pd.set_option('display.width',pd.util.terminal.get_terminal_size()[0]) #default: 80 characters
pd.set_option('display.max_columns',30) #default: 20
maxrows = pd.util.terminal.get_terminal_size()[1]-14 #leave room for some other stuff
#maxrows = 20
pd.set_option('display.max_rows',maxrows) #default: 60

data_dir = '../data/'
data_file_in = 'forecast_and_obs'

print '\nRead in', data_dir+data_file_in+'.csv'
df_fors_obs = pd.read_csv(data_dir+data_file_in+'.csv')
print '\nSome data:\n', df_fors_obs

#print some stats about the unique ID: wea_stn_cd/valid_date
print '\nwea_stn_cd/valid_date combination has duplicates:', df_fors_obs.set_index(['wea_stn_cd','valid_date']).index.has_duplicates
count_unq_wea_stns = df_fors_obs.wea_stn_cd.value_counts().count()
print 'wea_stn_cd count:',df_fors_obs.wea_stn_cd.count(),' count unique:',count_unq_wea_stns, \
    ' min:',df_fors_obs.wea_stn_cd.min(),' max:',df_fors_obs.wea_stn_cd.max()
count_unq_valid_dates = df_fors_obs.valid_date.value_counts().count()
print 'valid_date count:',df_fors_obs.valid_date.count(),' count unique:',count_unq_valid_dates, \
    ' min:',df_fors_obs.valid_date.min(),' max:',df_fors_obs.valid_date.max(), '(YYYYMMDD)'
print 'FYI:', count_unq_wea_stns, 'x', count_unq_valid_dates, '=', count_unq_wea_stns*count_unq_valid_dates

#print counts of missing data for each year_num, year_num = 1 is 20110108 thru 20120107 (YYYYMMDD)
df_fors_obs['year_num'] = (df_fors_obs.valid_date-108)//10000 - 2010
df_f_o_counts_by_year_num = df_fors_obs.groupby('year_num').count()
#convert from counts to number missing ( = count with none missing - counts )
df_f_o_missing_by_year_num = (-df_f_o_counts_by_year_num).add(df_f_o_counts_by_year_num.wea_stn_cd,axis=0) #wea_stn_cd is missing none
df_f_o_missing_by_year_num.drop(['wea_stn_cd','valid_date'],axis=1,inplace=True)
df_f_o_missing_by_year_num = df_f_o_missing_by_year_num.join(df_f_o_counts_by_year_num[['wea_stn_cd']]) #put back the "out of" column (wea_stn_cd)
df_f_o_missing_by_year_num.rename(columns={'wea_stn_cd':'out_of'},inplace=True)
print '\nCounts of missing data by year_num (and "out of"), year_num = 1 is 20110108 thru 20120107 (YYYYMMDD)\n', df_f_o_missing_by_year_num

#print counts of missing data for each month/year
df_fors_obs.drop('year_num',axis=1,inplace=True) #no longer needed
df_fors_obs['year'] = df_fors_obs.valid_date//10000
df_fors_obs['month'] = (df_fors_obs.valid_date-20110000)//100%100
df_f_o_counts_by_year_month = df_fors_obs.groupby(['year','month']).count()
#convert from counts to number missing ( = count with none missing - counts )
df_f_o_missing_by_year_month = (-df_f_o_counts_by_year_month).add(df_f_o_counts_by_year_month.wea_stn_cd,axis=0) #wea_stn_cd is missing none
df_f_o_missing_by_year_month.drop(['wea_stn_cd','valid_date'],axis=1,inplace=True)
df_f_o_missing_by_year_month = df_f_o_missing_by_year_month.join(df_f_o_counts_by_year_month[['wea_stn_cd']]) #put back the "out of" column (wea_stn_cd)
df_f_o_missing_by_year_month.rename(columns={'wea_stn_cd':'out_of'},inplace=True)
print '\nCounts of missing data by year and month (and "out of")\n', df_f_o_missing_by_year_month

#print counts of missing data for each weather station
df_fors_obs.drop(['year','month'],axis=1,inplace=True)
df_f_o_counts_by_wea_stn = df_fors_obs.groupby('wea_stn_cd').count()
#convert from counts to number missing ( = count with none missing - counts )
df_f_o_missing_by_wea_stn = (-df_f_o_counts_by_wea_stn).add(df_f_o_counts_by_wea_stn.valid_date,axis=0) #valid_date is missing none
df_f_o_missing_by_wea_stn.drop('valid_date',axis=1,inplace=True)
df_f_o_missing_by_wea_stn = df_f_o_missing_by_wea_stn.join(df_f_o_counts_by_wea_stn[['valid_date']]) #put back the "out of" column (valid_date)
df_f_o_missing_by_wea_stn.rename(columns={'valid_date':'out_of'},inplace=True)
pd.set_option('display.max_rows',count_unq_wea_stns)
print '\nCounts of missing data by wea_stn_cd (and "out of")\n',df_f_o_missing_by_wea_stn



