import numpy as np
import pandas as pd
import re
import configparser
from fuzzywuzzy import fuzz

config_file = 'config.ini'
def read_config():
  config = configparser.ConfigParser()
  config.read(config_file, encoding='utf-8')
  return config

# def txt_file_to_list(txt_file_path):
#     f = open(txt_file_path, "r",encoding='utf-8')
#     r_keys = f.readlines()
#     keys =[]
#     for i in r_keys:
#         keys.append(i[:-1])
#     return keys

def get_domain_type(search_domain):
    config = read_config()
    domain_Map_File = eval(config['DOMAIN_MAP']['domain_map_dict'])
    # try:
    #     domain = x.split('www.')[1]
    # except:
    #     domain =  x
    for key,value in domain_Map_File.items():
        for v in value:
            if v in search_domain:
                return key
    return ''
    
def Get_Search_Type(keyword, fourMoreThreshold , fourThreshold):
    config = read_config()
    search_Map_File = eval(config['SEARCH_TYPE_MAP']['category_brand_dict'])
    brandsearchTypeList= []
    categorysearchTypeList = []
    for key, values in search_Map_File.items():
        categorysearchTypeList.append(key)
        brandsearchTypeList.extend(values)
    
    categorysearchTypeList = list(set(categorysearchTypeList))
    brandsearchTypeList = list(set(brandsearchTypeList))

    if type(keyword) == str:
        if len(keyword) > 4:
            for b in brandsearchTypeList:
                term_Index = brandsearchTypeList.index(b)

                if fuzz.partial_ratio(keyword.lower(),b.lower()) > fourMoreThreshold:
                    return 'Brand Search'
                
                elif fuzz.token_set_ratio(keyword.lower(),b.lower()) > fourMoreThreshold:
                    return 'Brand Search'
                

            for c in categorysearchTypeList:
                term_Index = categorysearchTypeList.index(c)

                if fuzz.partial_ratio(keyword.lower(),c.lower()) > fourMoreThreshold:
                    return 'Category Search'
                
                elif fuzz.token_set_ratio(keyword.lower(),c.lower()) > fourMoreThreshold:
                    return 'Category Search'
                
        elif len(keyword) == 4:
            for b in brandsearchTypeList:
                term_Index = brandsearchTypeList.index(b)

                if fuzz.ratio(keyword.lower(),b.lower()) >= fourThreshold:
                    return 'Brand Search'
                
            for c in categorysearchTypeList:
                term_Index = categorysearchTypeList.index(c)

                if fuzz.ratio(keyword.lower(),c.lower()) >= fourThreshold:
                    return 'Category Search'   
            
                
        else:
            for b in brandsearchTypeList:
                term_Index = brandsearchTypeList.index(b)

                if keyword.lower() == b.lower():
                    return 'Brand Search'
            
            for c in categorysearchTypeList:
                term_Index = categorysearchTypeList.index(c)

                if keyword.lower() == c.lower():
                    return 'Category Search' 
                
        return 'Other'
    else:
        return ''



def check_box_filter(url):
    config = read_config()
    check_box_lst = eval(config['CHECK_BOX_FILTER']['check_filter_keys'])
    for i in check_box_lst:
        #print(i)
        if i in url:
            return 1
    else:
        return 0

def sort_by_filter(url):
    config = read_config()
    sort_filter_dict = eval(config['SORT_FILTER']['sort_filter_dict'])
    for k in sort_filter_dict:
        if re.match(k, url):
            return sort_filter_dict[k]