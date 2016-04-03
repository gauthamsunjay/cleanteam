from scipy.cluster.vq import kmeans, vq
import sys


def get_means(data, num_centers):
    centroids, _ = kmeans(data, num_centers)
    indexes, _ = vq(data, centroids)
    return centroids, indexes

if __name__ == "__main__":
    import csv
    if len(sys.argv) != 3:
        print sys.argv
        print 'USAGE : ./pgm <num_centers> <output file>'
        print 'EXAMPLE : ./kmeans.py 10 centers'
        exit(1)

    num_centers = int(sys.argv[1])
    locations = []
    volume = []
    with open("res", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            locations.append(list(map(float, row[:2])))
            volume.append(float(row[2]))

    centroids, indexes = get_means(locations, num_centers)
    volume_in_centers = [0] * num_centers
    for i, v in enumerate(volume):
        center = indexes[i]
        volume_in_centers[center] += v

    with open(sys.argv[2], "wb") as f:
        writer = csv.writer(f)
        for i in range(len(volume_in_centers)):
            writer.writerow(list(centroids[i]) + [volume_in_centers[i]])
