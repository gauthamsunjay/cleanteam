from scipy.cluster.vq import kmeans, vq
from get_random_locations import get_locations

locations = get_locations()

centroids, _  = kmeans(locations, 10)
print centroids