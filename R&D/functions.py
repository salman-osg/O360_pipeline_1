import numpy as np
import pandas as pd
import re
from fuzzywuzzy import fuzz



def txt_file_to_list(txt_file_path):
    f = open(txt_file_path, "r",encoding='utf-8')
    r_keys = f.readlines()
    keys =[]
    for i in r_keys:
        keys.append(i[:-1])
    return keys

def Domains(x):
    try:
        return x.split('www.')[1]
    except:
        return x
    
def Get_Search_Type(row, fourMoreThreshold , fourThreshold):
    search_Map_File = pd.read_excel("SearchTypeMap_New.xlsx")
    
    brandsearchTypeList = list(set(search_Map_File['Brand '].tolist()))
    brandsearchTypeList =  [x for x in brandsearchTypeList if type(x) == str]
   
    categorysearchTypeList = list(set(search_Map_File['Category'].tolist()))
    categorysearchTypeList =  [x for x in categorysearchTypeList if type(x) == str]
    
    keyword = row['Keyword Used']
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



def check_box_filter(check_box_lst, url):
    for i in check_box_lst:
        #print(i)
        if i in url:
            return 1
    else:
        return 0