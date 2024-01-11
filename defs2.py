# def compute_jaccard_similarity_parallel(pair):
#     dict1, dict2 = pair
#     return jaccard(dict1, dict2)

def work_that_CPU(num_loops):
    import random
    import multiprocessing
    import time

    startTime = time.time()
    
    for w in range(num_loops):
        random.random()

    #print(multiprocessing.current_process()," took ", time.time()-startTime," seconds")
    
