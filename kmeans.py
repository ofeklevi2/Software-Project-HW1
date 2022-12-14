def str_to_int(f):
    cluster = []
    for v in f:
        v = v.split(",")
        for i in range(len(v)):
            v[i] = float(v[i])
        cluster.append(v)
    return cluster

def distance(v, u):
    d = 0
    for i in range(len(v)):
        d += (v[i]-u[i])**2
    return d**0.5

def assignToClosestCluster(xi, centroids,clusters):
    minD = distance(xi, centroids[0])
    index = 0
    for i in range(1, len(centroids)):
        d = distance(xi, centroids[i])
        if(d < minD):
            minD = d
            index = i
    clusters[index].append(xi)

def calcNewCentroid(cluster):
    newCentroid = [0 for i in range(len(cluster[0]))]
    for xi in cluster:
        for cord in range(len(xi)):
            newCentroid[cord] += xi[cord]
    for cord in range(len(newCentroid)):
        newCentroid[cord] = newCentroid[cord] / len(cluster)
    return [newCentroid]

def printCentroids(centroids):
    for centroid in centroids:
        c = []
        for cord in range(len(centroid)):
            c.append(round(centroid[cord], 4))
        print(c)




def kmeans(k, iter, input_data):
    if(input_data.endswith('.txt') == False):
        print("NA")
        exit()
    try:
        f = open(input_data, "r")
    except:
        print("An Error Has Occurred")
        exit()

    dataPoints = str_to_int(f)
    f.close()
    if (k >= len(dataPoints)):
        print("Invalid number of clusters!")
        exit()
    if(iter >=1000 or iter<=1):
        print("Invalid maximum iteration!")
        exit()



    clusters = [[] for i in range(k)]
    centroids = [0 for i in range(k)]
    prevCentroids = []

    # Initialize centroids as first k datapoints
    for i in range(k):
        centroids[i] = dataPoints[i]

    for iterNum in range(iter):
        # make all clusters
        for xi in dataPoints:
            assignToClosestCluster(xi, centroids, clusters)
        prevCentroids = centroids.copy()
        # update clusters, and centroids[] will be the populated with the new centroids
        for i in range(len(clusters)):
            clusters[i] = calcNewCentroid(clusters[i])
            centroids[i] = clusters[i][0]
        #check epsilon for each centroid
        allUnderEps = True
        for i in range(len(centroids)):
            d = distance(centroids[i], prevCentroids[i])
            if(d >= 0.001):
                allUnderEps = False
        if(allUnderEps == True):
            # print(centroids)
            # print(iterNum)
            printCentroids(centroids)
            return
    printCentroids(centroids)
    # print(iterNum)
    # print(centroids)
kmeans(11,2,"test_data/tests/input_1.txt")






