import pandas as pd
def filter_jobs_with_salaries(df,salary_col):
    #must have salary range
    tempdf=df[df[salary_col].notnull()]
    #must not be hourly, shortcut look for 'K'
    tempdf=tempdf[tempdf['salary_range'].str.find('K')>0]
    tempdf=tempdf[tempdf['salary_range'].str.find('Employer Provided Salary:')<0]
    return tempdf
def create_salaries_cols(df,salary_col):
    '''
    parses salary range column, removes formatting, and splits to upper, lower bounds, and salary estimate type
    returns dataframe with cleansed salary format
    '''
    tempdf = df['salary_range'].str.replace('$','')
    tempdf = tempdf.str.split('K', expand=True)
    tempdf.columns = ['salary_lower','salary_upper','salary_estimator']
    tempdf['salary_upper'] = tempdf['salary_upper'].str.replace('-','')
    numeric_cols = ['salary_lower','salary_upper']
    tempdf[numeric_cols]=tempdf[numeric_cols].apply(pd.to_numeric)
    df=pd.concat([df,tempdf],axis=1)
    df=df.drop(columns=[salary_col])
    return df
