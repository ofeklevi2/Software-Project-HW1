
def kmeans (K, iter, input_data):

    data = open(input_data, "r")

    def vMaker(data):
        vArr = [] 
        for line in data: 
            vArr.append([eval(i) for i in line.split()[0].split(",")])
        return vArr
    
    def d(v1,v2):
        res = 0 
        for i in range(len(v1)):
            res += (v1[i] - v2[i]) ** 2
        res = res**(0.5)
        return res
    
    def findClosest(v, centroids):
        minDist = d(v, centroids[0])
        minNum = 0
        for i in range(1, len(centroids)):
            currDist = d(v,centroids[i])
            if  currDist < minDist:
                minDist = currDist 
                minNum = i 
        return minNum

    def compute_centroid_by_cluster (cluster):
        clustLen = len(cluster)
        updated = [0 for i in range(K)]
        for i in range(clustLen):
            for n in range(K):
                updated[n] += cluster[i][n]
        for i in range(len(updated)):
            updated[i] = updated[i]/clustLen
        return updated

    def compute_new_centroids(vArr, centroids):
        clusters = [[] for i in range(K)]
        for i in range(len(vArr)):
            closest = findClosest(vArr[i],centroids)
            clusters[closest].append(vArr[i])
        updatedCentroids = []
        for i in range(K):
            updatedCentroids.append(compute_centroid_by_cluster(clusters[i]))
        delta = findMaxDelta(centroids, updatedCentroids)

        return (updatedCentroids, delta)

    def findMaxDelta(centroids, updatedCentroids):
        deltas = []
        for i in range(K):
            deltas.append(d(centroids[i], updatedCentroids[i]))
        return max(deltas)

            
    vArr = vMaker(data)
    
    if (K >= len(vArr)):
        print("Invalid number of clusters!")
        exit()
    else:
        centroids = []
        for i in range(K):
            centroids.append(vArr[i])

    iteration_number = 0
    delta = 1

    while (delta >= 0.001 and iteration_number < iter):
        centroids, delta = compute_new_centroids(vArr, centroids)
        iteration_number += 1
    
    print(centroids)

kmeans(3,600,"/Users/USER/Downloads/tests/input_1.txt")
    

        
    



    