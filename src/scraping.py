import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import argparse

browser = webdriver.Chrome()
browser.get('http://seleniumhq.org/')

css_mappings = {'job_title': 'h1.jobTitle.h2.strong',
            'job_description': 'div.jobDescriptionContent.desc',
            'company': 'a.plain.strong.empDetailsLink',
            'stars': 'span.compactRating.lg.margRtSm',
            'salary_range': 'span.green.small.salary'}

def get_element_from_selector(browser, css_key, css_value):
    try:
        res = browser.find_element_by_css_selector(css_value).text
    except:
        res = np.nan
    return res

def get_info_from_job(css_mappings, browser, attributes):
    for k,v in css_mappings.items():
        result = get_element_from_selector(browser,k,v)
        attributes[k].append(result)
    return attributes

def get_page_of_attributes(css_mappings, browser, attributes):
    Jobs = browser.find_elements_by_css_selector('li.jl')
    for Job in Jobs:
        time.sleep(.75)
        try:
            Job.click()
            attributes = get_info_from_job(css_mappings, browser, attributes)
        except:
            pass
    return attributes

def scrape_ds():
    attributes = {}
    for k,v in css_mappings.items():
        attributes[k] = []
    for i in range(1,31):
        dsurl = 'https://www.glassdoor.com/Job/seattle-data-scientist-jobs-SRCH_IL.0,7_IC1150505_KO8,22_IP' + str(i) + '.htm'
        browser.get(dsurl)
        attributes=get_page_of_attributes(css_mappings, browser, attributes)
        ds=pd.DataFrame(attributes)
        ds.to_csv('ds_'+str(i)+'.csv', sep='|')
    return ds

def scrape_glassdoor_url(base_url, url_filters, job_type):
    '''
    base url example
    https://www.glassdoor.com/Job/seattle-data-scientist-jobs-SRCH_IL.0,7_IC1150505_KO8,22_IP
    url filters example
    .htm?minSalary=18000
    '''
    attributes = {}
    for k,v in css_mappings.items():
        attributes[k] = []
    for i in range(1,31):
        dsurl = base_url + str(i) + url_filters
        browser.get(dsurl)
        attributes=get_page_of_attributes(css_mappings, browser, attributes)
        ds=pd.DataFrame(attributes)
        ds.to_csv(job_type + '_' + str(i)+'.csv', sep='|')
    return ds

if __name__ == '__main__':
    base_url = 'https://www.glassdoor.com/Job/seattle-chemical-jobs-SRCH_IL.0,7_IC1150505_KO8,22_IP'
    url_filters = '.htm?minSalary=18000'
    job_type = 'chemical'
    scrape_glassdoor_url(base_url, url_filters, job_type)
