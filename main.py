import numpy as np
import pandas as pd
import re
import json
from tqdm import tqdm
from functions import check_box_filter,txt_file_to_list,Domains,Get_Search_Type
from URL_Categorization import check_pages

## Make a text file of this
#check_box_lst = ['&rh','?filter','&rootdimension','&n=','?f[','&filter','rt=nc','explicit=1','=facets','facet']

sort_filter_dict = json.load(open('sort_filter.json','r'))
#print(sort_filter_dict)
# pdp_key = txt_file_to_list('pdp_keys.txt')
# cart_key = txt_file_to_list('Cart.txt')
# search_key = txt_file_to_list('search_page.txt')
check_filter_keys = txt_file_to_list('check_filter_keys.txt')
# tqdm.pandas()
# tqdm_pandas(tqdm())

#data = pd.read_csv('Braun_data_with_filter_and_page_cat_with_html_v4.csv')

data = pd.read_csv('Data/data1859.csv')
# data = pd.read_csv('Data/ClickStream+PurchasesCombined_FINAL_15Feb (1).csv')
#data.rename(columns = {'Path Analysis':'URL'}, inplace = True)

################################### Domain Type #####################################
data['Domain'] = data["Search Domain"].apply(lambda x : Domains(x))
domain_MapFile = pd.read_excel("domain_Map.xlsx")
data = data.merge(domain_MapFile, how = 'left', left_on = 'Domain', right_on = 'domain')

################################## Search Type ########################################
# search_Map_File = pd.read_excel("SearchTypeMap_New.xlsx")
fourMoreThreshold = 80
fourThreshold = 75
data["Search Type"] = data.apply(lambda x : Get_Search_Type(x,fourMoreThreshold,fourThreshold), axis=1)

############################## Check box filter flag #######################################
data['check_box_flag'] = data['URL'].apply(lambda x:check_box_filter(check_filter_keys,x))

################################## Sort filter #############################################
data['sort_filter'] = data['URL'].astype(str).str.lower().replace(sort_filter_dict,regex=True)
data.loc[data[~data['sort_filter'].isin(list(sort_filter_dict.values()))].index,'sort_filter'] = np.NaN

tqdm.pandas()
# data['URL_Category_new'] = data.apply(lambda x : check_pages(x,pdp_key,search_key,cart_key), axis=1)

data.to_csv('data_after_pipeline_1_v2.csv',index= False)
#data.to_csv('Braun_data_with_filter_and_page_cat_with_html_v5.csv',index= False)




