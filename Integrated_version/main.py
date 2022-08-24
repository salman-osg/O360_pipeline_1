# import numpy as np
import pandas as pd
import re
import json
from functions import check_box_filter,Get_Search_Type,get_domain_type,sort_by_filter

# data = pd.read_csv('Data/data1859.csv')
search_domain  = 'www.carrefourqatar.com'
keyword = 'Tide'
url = "https://www.carrefourqatar.com/mafqat/en/v4/search?currentPage=0&filter=product_category_level_1_en%3A%27FQAT1000000%27&keyword=children%27s%20food&nextPageOffset=0&pageSize=60&sortBy=relevance"

################### Features ###########################
domain_type = get_domain_type(search_domain)
search_type = Get_Search_Type(keyword, fourMoreThreshold = 80 , fourThreshold = 75)
check_box_filter_flag = check_box_filter(url)
sort_filter = sort_by_filter(url)

print('DOMAIN_TYPE: {}'.format(domain_type))
print('SEARCH_TYPE: {}'.format(search_type))
print('CHECK_BOX_FILTER: {}'.format(check_box_filter_flag))
print('SORT_FILTER: {}'.format(sort_filter))





# data.to_csv('data_after_pipeline_1_v2.csv',index= False)




