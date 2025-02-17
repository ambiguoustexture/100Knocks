# Author：ambiguoustexture
# Date: 2020-02-13

from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"

verbs = set()
verbs_order = []

words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '動詞':
        verbs.add(word['base'])
        verbs_order.append(word['base'])

verbs = sorted(verbs, key=verbs_order.index)
for verb in verbs:
    print(verb)
