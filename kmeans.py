

def k_means(dataSet,k):
    '''
    Stop condition is: when the distribution list is not changing
    :param dataSet:
    :param k:
    :return:

    '''
    
    k_points = generate_k(dataSet,k)
    assignments = assign_points(dataSet,k_points)
    old_assignments = None
    times = 0
    while assignments != old_assignments:
        times += 1
        print("times is: ",times)
        new_centers = update_centers(dataSet,assignments)
        old_assignments = assignments
        assignements = assign_points(dataSet,new_centers)

    return (assigments,dataSet)
