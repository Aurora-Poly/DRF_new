import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

movie = pd.read_csv('activity/full.csv')
count_v = CountVectorizer(ngram_range=(1,3))
all_v = count_v.fit_transform(movie['all'])
# 코사인 유사도 구하기
all_csine = cosine_similarity(all_v, all_v)


# 장르 기반 추천 함수
def find_sim_num(title_index):
  # print(movie.iloc[title_index])
  #   # 영화 제목 일치 행 찾기
  #   title_movie = df[df['title'] == title_name]
  #  # print(title_movie)

  #   # 영화의 인덱스 찾기
  #   title_index = title_movie.index.values
  #   # title_index = title_movie.index.values
  #   print(title_index)

  # 입력한 영화 제목과 영화 목록의 코사인 유사도
  # df['similarity'] = genre_csine[title_index, :].reshape(-1,1)
  # df['similarity_office'] = office_csine[title_index, :].reshape(-1,1)
  # df['similarity_money'] = office_csine[title_index, :].reshape(-1,1)
  movie['similarity_all'] = all_csine[title_index, :].reshape(-1, 1)

  # 유사도 기반 내림차순 정렬
  # temp = df.sort_values(by=['similarity','similarity_office','similarity_money'], ascending=False)
  temp = movie.sort_values(by='similarity_all', ascending=False)

  # 입력한 영화 제외
  temp = temp[temp.index.values != title_index]

  # 상위 10개 영화의 인덱스
  final_index = temp.index.values[:1]
  # print('final_index', final_index)
  # print(movie['id'].iat[final_index[0]])
  # print(movie[['id']].iloc[final_index])

  # return movie[['id', 'title', 'field', 'all', 'similarity_all']].iloc[final_index]

  # return movie[['id', 'title', 'juchae', 'jukwan', 'apply_period',
  #               'prize_1st', 'apply_url', 'image_url', 'prize', 'office', 'field', 'target']].iloc[final_index]
  # return movie[['id']].iloc[final_index[0]]
  return movie['id'].iat[final_index[0]]



