# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
import numpy as np 
from scipy import io
from similarity_cosine_w2v import sim_cos 

file_context_matrix_X_w2v = './context_matrix_X_w2v'
file_t_index_dict_w2v        = './t_index_dict_w2v'

with open(file_t_index_dict_w2v, 'rb') as t_index_dict_w2v:
    t_index_dict_w2v = pickle.load(t_index_dict_w2v)

context_matrix_X_w2v = io.loadmat(file_context_matrix_X_w2v)['context_matrix_X_w2v']

words_additive = context_matrix_X_w2v[t_index_dict_w2v['Spain']] \
        - context_matrix_X_w2v[t_index_dict_w2v['Madrid']] \
        + context_matrix_X_w2v[t_index_dict_w2v['Athens']]
words_similarities = [sim_cos(words_additive, context_matrix_X_w2v[i])
        for i in range(len(t_index_dict_w2v))]
words_similarities_sorted = np.argsort(words_similarities)
words = list(t_index_dict_w2v.keys())

for index in words_similarities_sorted[:-11:-1]:
    print(words[index].ljust(14, ' '), words_similarities[index])    
