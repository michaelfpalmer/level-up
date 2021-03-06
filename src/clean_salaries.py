import pandas as pd
blacklisted_occupations = ['physician', 'dentist', 'psychiatrist', 'pediatrician', 'oncologist', 'crna', 'surgeon', 'anesthesiologist', 'neurologist', 'hospitalist']

def filter_jobs_with_salaries(df,salary_col):
    '''
    takes in a dataframe of job postings along with its salary column
    lowercases the data for easier manipulation
    returns a subset of the dataframe that only has salaried job postings
    at the moment also excludes employer provided salaries
    '''
    tempdf=df[df[salary_col].notnull()]
    tempdf[salary_col] = tempdf[salary_col].str.lower()
    #must not be hourly, shortcut look for 'K'
    tempdf=tempdf[tempdf[salary_col].str.find('k')>0]
    tempdf=tempdf[tempdf[salary_col].str.find('employer provided salary:')<0]
    return tempdf
def create_salaries_cols(df,salary_col):
    '''
    parses salary range column, removes formatting, and splits to upper, lower bounds, and salary estimate type
    returns dataframe with cleansed salary format
    '''
    tempdf = df[salary_col].str.replace('$','')
    tempdf = tempdf.str.split('k', expand=True)
    tempdf.columns = ['salary_lower','salary_upper','salary_estimator']
    tempdf['salary_upper'] = tempdf['salary_upper'].str.replace('-','')
    numeric_cols = ['salary_lower','salary_upper']
    tempdf[numeric_cols]=tempdf[numeric_cols].apply(pd.to_numeric)
    df=pd.concat([df,tempdf],axis=1)
    df=df.drop(columns=[salary_col])
    return df

def convert_salaries_hourly(df,salary_col):
    '''
    takes in a dataframe with its salary column
    finds postings with per hour in the estimate
    strips out formatting
    right now just returns original df
    '''
    hourly=df[df[salary_col].str.lower().str.find('per hour')>0][salary_col]
    hourly=hourly.str.replace('employer provided Salary:','')
    hourly=hourly.str.replace('per hour','')
    hourly=hourly.str.replace("glassdoor Est.",'')
    hourly=hourly.str.replace("\(\)","")
    hourly=hourly.str.replace('$','')
    hourly=hourly.str.split('-',expand=True)
    hourly.columns=['salary_lower','salary_upper']
    numeric_cols = ['salary_lower','salary_upper']
    hourly[numeric_cols]=hourly[numeric_cols].apply(pd.to_numeric)
    return df
