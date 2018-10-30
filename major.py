from collections import defaultdict
from random import uniform


def assign_points(dataSet,centers):
    '''
    Given a data set and a centroid set;
    Assign each point to the closest centroid to that point.
    Finally, return the distribution list of all points in the center of mass.
    :param dataSet:
    :param centers:
    :return:
    
    '''
    assignments = []
    for point in dataSet:
        shortest = float('Inf')
        shortest_index = 0
        for i in range(len(center)):
            distance = distance(point,center[i])
            if distance < shortest:
                shortest = distance
                shortest_index = i
        assigments.append(shortest_index)

    return assignments


def generate_k(dataSet,k):
    '''
    Give a data set and K value.
    Find the maximum and minimum values of each dimension.
    The initial centroid position is randomly generated,
    according to the number of k and maximum and minimum
    :param dataSet:
    :param k:
    :return:
    
    '''
    centers = []
    dimensions = len(dataSet[0])
    min_max = defaultdict(int)

    for point in dataSet:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' %i
            max_key = 'max_%d' %i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for k in range(k):
        rand_points = []
        for i in range(dimensions):
            min_val = min_max['min_%d' %i]
            max_val = min_max['max_%d' %i]
            
            rand_points.append(uniform(min_val,max_val))

        centers.append(rand_points)

    return centers

