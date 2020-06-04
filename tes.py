import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

A = pd.read_excel('A.xlsx', sheet_name='PartA')
B = pd.read_excel('A.xlsx', sheet_name='PartB')
C = pd.read_excel('A.xlsx', sheet_name='PartC')

B['multi'] = (pd.Series(A[['Cuisines', 'Features', 'Restaurant_Type']].values.tolist()).str.join(','))
C['multi'] = (pd.Series(A[['Cuisines', 'Features', 'Restaurant_Type']].values.tolist()).str.join(','))

D = pd.concat([A, B, C])

def favorite_restaurant(resto):
    return D[D['Restaurant_Name'] == resto]

def restaurant_recommendation(resto):
    ext = CountVectorizer(tokenizer= lambda x: x.split(','))
    zmulti = ext.fit_transform(D['multi'].head(1316))
    zmulti.toarray()
    cos_score = cosine_similarity(zmulti)

    resto_index = D[D['Restaurant_Name'] == resto].index[0]
    a = list(enumerate(cos_score[resto_index]))
    resto_sug = sorted(a, key=lambda x:x[1], reverse=True)
    resto_sug.remove(a[resto_index])

    list_dict = []
    dict_rank = {}
    
    for i in resto_sug[:10]:
        dict_rank['cost'] = D.iloc[i[0]]['Cost_for_two']
        dict_rank['cuisines'] = D.iloc[i[0]]['Cuisines']
        dict_rank['features'] = D.iloc[i[0]]['Features']
        dict_rank['hours'] = D.iloc[i[0]]['Operational_hours']
        dict_rank['rating'] = D.iloc[i[0]]['Rating_votes']
        dict_rank['location'] = D.iloc[i[0]]['Restaurant_Location']
        dict_rank['name'] = D.iloc[i[0]]['Restaurant_Name']
        dict_rank['type'] = D.iloc[i[0]]['Restaurant_Type']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)

def cuisines_recommendation(resto):
    ext = CountVectorizer(tokenizer= lambda x: x.split(','))
    zcuisines = ext.fit_transform(D['Cuisines'].head(1316))
    zcuisines.toarray()
    cos_score = cosine_similarity(zcuisines)

    resto_index = D[D['Restaurant_Name'] == resto].index[0]
    a = list(enumerate(cos_score[resto_index]))
    resto_sug = sorted(a, key=lambda x:x[1], reverse=True)
    resto_sug.remove(a[resto_index])

    list_dict = []
    dict_rank = {}
    
    for i in resto_sug[:10]:
        dict_rank['cost'] = D.iloc[i[0]]['Cost_for_two']
        dict_rank['cuisines'] = D.iloc[i[0]]['Cuisines']
        dict_rank['features'] = D.iloc[i[0]]['Features']
        dict_rank['hours'] = D.iloc[i[0]]['Operational_hours']
        dict_rank['rating'] = D.iloc[i[0]]['Rating_votes']
        dict_rank['location'] = D.iloc[i[0]]['Restaurant_Location']
        dict_rank['name'] = D.iloc[i[0]]['Restaurant_Name']
        dict_rank['type'] = D.iloc[i[0]]['Restaurant_Type']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)

def features_recommendation(resto):
    ext = CountVectorizer(tokenizer= lambda x: x.split(','))
    zfeatures = ext.fit_transform(D['Features'].head(1316))
    zfeatures.toarray()
    cos_score = cosine_similarity(zfeatures)

    resto_index = D[D['Restaurant_Name'] == resto].index[0]
    a = list(enumerate(cos_score[resto_index]))
    resto_sug = sorted(a, key=lambda x:x[1], reverse=True)
    resto_sug.remove(a[resto_index])

    list_dict = []
    dict_rank = {}
    
    for i in resto_sug[:10]:
        dict_rank['cost'] = D.iloc[i[0]]['Cost_for_two']
        dict_rank['cuisines'] = D.iloc[i[0]]['Cuisines']
        dict_rank['features'] = D.iloc[i[0]]['Features']
        dict_rank['hours'] = D.iloc[i[0]]['Operational_hours']
        dict_rank['rating'] = D.iloc[i[0]]['Rating_votes']
        dict_rank['location'] = D.iloc[i[0]]['Restaurant_Location']
        dict_rank['name'] = D.iloc[i[0]]['Restaurant_Name']
        dict_rank['type'] = D.iloc[i[0]]['Restaurant_Type']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)

def type_recommendation(resto):
    ext = CountVectorizer(tokenizer= lambda x: x.split(','))
    ztype = ext.fit_transform(D['Restaurant_Type'].head(1316))
    ztype.toarray()
    cos_score = cosine_similarity(ztype)

    resto_index = D[D['Restaurant_Name'] == resto].index[0]
    a = list(enumerate(cos_score[resto_index]))
    resto_sug = sorted(a, key=lambda x:x[1], reverse=True)
    resto_sug.remove(a[resto_index])

    list_dict = []
    dict_rank = {}
    
    for i in resto_sug[:10]:
        dict_rank['cost'] = D.iloc[i[0]]['Cost_for_two']
        dict_rank['cuisines'] = D.iloc[i[0]]['Cuisines']
        dict_rank['features'] = D.iloc[i[0]]['Features']
        dict_rank['hours'] = D.iloc[i[0]]['Operational_hours']
        dict_rank['rating'] = D.iloc[i[0]]['Rating_votes']
        dict_rank['location'] = D.iloc[i[0]]['Restaurant_Location']
        dict_rank['name'] = D.iloc[i[0]]['Restaurant_Name']
        dict_rank['type'] = D.iloc[i[0]]['Restaurant_Type']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)