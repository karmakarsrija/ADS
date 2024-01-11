# def mapper_all_pair_jaccard(doc_):
#     list_output = []
#     (i,j,doc_i,doc_j) = doc_
#     similarity_ = jaccard(doc_i,doc_j)
#     list_output.append(((i,j),similarity_))
#     return list_output

# def reducer_all_pair(item):
    
#     (keys,values) = item
#     output_reducer = [(keys,values)]
#     return (output_reducer)
# def maketotal(dict1):
#     total = 0
#     for item in dict1.values():
#         total += item
#     return total

# def jaccard(dict1, dict2):
#     intersection = {}
#     for item in dict1.keys():
#         if item in dict2.keys():
#             intersection[item] = min(dict1[item], dict2[item])

#     intersectiontot = maketotal(intersection)
#     union = maketotal(dict1) + maketotal(dict2) - intersectiontot
#     return intersectiontot / union 

def maketotal(dict1):
    total = 0
    for item in dict1.values():
        total += item
    return total

def jaccard(dict1, dict2):
    intersection = {}
    for item in dict1.keys():
        if item in dict2.keys():
            intersection[item] = min(dict1[item], dict2[item])

    intersectiontot = maketotal(intersection)
    union = maketotal(dict1) + maketotal(dict2) - intersectiontot
    return intersectiontot / union 


def all_pairs_similarities(docs,similarity):
    aps = []
    if similarity == 'jaccard':
        sim = jaccard
    elif similarity == 'cosine':
        sim = cosine
        docs = make_matrix(docs)
    elif similarity == 'cosine_similarity_numpy':
        sim = cosine_similarity_numpy
        docs = make_matrix(docs)
    else:
        return print('Invalid similarity')

    for doc1 in docs:
        for doc2 in docs:
              aps.append(sim(doc1,doc2))
    return aps
def all_pairs_similarities_wrapper(x):
    docs_list, similarity = x
    return all_pairs_similarities(docs_list, similarity='jaccard')