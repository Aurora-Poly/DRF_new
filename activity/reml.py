import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

reco = pd.read_csv('activity/full.csv')
count_v = CountVectorizer(ngram_range=(1,3))
all_v = count_v.fit_transform(reco['all'])
all_csine = cosine_similarity(all_v, all_v)


# 스크랩 기반 추천 함수
def find_sim_num(title_index):
  # 스크랩한 활동과 활동 목록의 코사인 유사도
  # df['similarity'] = genre_csine[title_index, :].reshape(-1,1)
  # df['similarity_office'] = office_csine[title_index, :].reshape(-1,1)
  # df['similarity_money'] = office_csine[title_index, :].reshape(-1,1)
  reco['similarity_all'] = all_csine[title_index, :].reshape(-1, 1)

  # 유사도 기반 내림차순 정렬
  temp = reco.sort_values(by='similarity_all', ascending=False)
  temp = temp[temp.index.values != title_index]
  final_index = temp.index.values[:1]
  return reco['id'].iat[final_index[0]]



