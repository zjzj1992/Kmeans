from collections import defaultdict
from math import sqrt


'''
Read data from text file
:param fileName:
:return:

'''
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat


def point_avg(points):
    '''
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2
    Returns a new points which is the center of all the points
    :param points:
    :return:
    
    '''
    dimensions = len(points[0])
    
    new_center = []
    
    for  dimension in range(dimensions):
        dim_sum = 0
        for point in points:
            dim_sum += point[dimension]
            
        #average of each dimension
        new_center.append(dim_sum/float(len(points[0])))
        
    return new_center


def update_centers(dataSet,assignments):
    '''
    Accepts a dataset and a list of assignments;
    the indexes of both lists correspond to each other.
    compute the center for each of the assigned groups.
    :param dataSet
    :param assignments
    :return:
    
    '''
    new_points = defaultdict(list)
    centers = []
    for assignments,dataSet in zip(assignments,dataSet):
        new_points[assignments].append(dataSet)

    for points in new_points.values():
        centers.append(point_avg(points))

    return centers


def distance(a,b):
    dimensions = len(a)

    dim_sum = 0
    for dimension in range(dimensions):
        distance = (a[dimension] - b[dimension]) ** 2
        dim_sum += distance

    return sqrt(dim_sum)
