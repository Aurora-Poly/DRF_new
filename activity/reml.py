import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

reco = pd.read_csv('activity/re_act1031.csv')
reco['fo'] = reco['field'].astype(str)+ str(' ') + reco['office'].astype(str)
count_v = CountVectorizer(ngram_range=(1,3))
all_v = count_v.fit_transform(reco['all'])
all_csine = cosine_similarity(all_v, all_v)

field_v = count_v.fit_transform(reco['field_d'])
field_csine = cosine_similarity(field_v, field_v)


fo_v = count_v.fit_transform(reco['fo'])
fo_csine = cosine_similarity(fo_v, fo_v)

# 스크랩 기반 추천 함수
def find_sim_num(title_index):
  title_index=title_index-1
  # 스크랩한 활동과 활동 목록의 코사인 유사도
  # df['similarity'] = genre_csine[title_index, :].reshape(-1,1)
  # df['similarity_office'] = office_csine[title_index, :].reshape(-1,1)
  # df['similarity_money'] = office_csine[title_index, :].reshape(-1,1)
  reco['similarity_all'] = all_csine[title_index, :].reshape(-1, 1)
  reco['similarity_field'] = field_csine[title_index, :].reshape(-1, 1)
  reco['similarity_fo'] = fo_csine[title_index, :].reshape(-1, 1)
  # print("all_csine", all_csine[-1])


  # 유사도 기반 내림차순 정렬
  temp = reco.sort_values(by=['similarity_field', 'similarity_fo', 'similarity_all'], ascending=False)
  print(title_index, 'temp', temp.index.values)
  temp = temp[temp.index.values != title_index]
  temp = temp[temp.index.values != 1140]

  final_index = temp.index.values[:1]
  # return reco['id'].iat[final_index[0]]
  # print(title_index, reco['act_id'].iat[final_index[0]])
  print(reco[['title', 'act_id', 'all']].iloc[title_index])
  print(reco[['title','act_id', 'all']].iloc[final_index])
  return reco['act_id'].iat[final_index[0]]



