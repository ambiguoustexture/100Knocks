# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
import numpy as np 
from scipy import io
from collections import OrderedDict
import word2vec 

file_corpus_shaped    = '../../ch09-Vector-space-method-01/compound_words_process_result.txt'
file_word2vec         = './word2vec.txt'
file_matrix_w2v       = './matrix_w2v.mat'
file_t_index_dict_w2v = './t_index_dict_w2v'

word2vec.word2vec(train=file_corpus_shaped, output=file_word2vec, size=300, threads=4, binary=0)

with open(file_word2vec) as vectors:
    vector = vectors.readline().split(' ')
    dict_size = int(vector[0])
    matrix_w2v_size = int(vector[1])

    t_index_dict_w2v = OrderedDict()
    matrix_w2v = np.zeros([dict_size, matrix_w2v_size], dtype=np.float64)

    for index, vector in enumerate(vectors):
        vector = vector.strip().split(' ')
        t_index_dict_w2v[vector[0]]    = index
        matrix_w2v[index] = vector[1:]

io.savemat(file_matrix_w2v, {'matrix_w2v': matrix_w2v})

with open(file_t_index_dict_w2v, 'wb') as t_index:
    pickle.dump(t_index_dict_w2v, t_index)
