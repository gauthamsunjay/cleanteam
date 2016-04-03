import random

def get_locations(west=13.109716,north=77.494253,east=12.874204,south=77.554698):
	locations = []
	for i in range(1000):
		lat = round(random.uniform(west, east), 6)
		lng = round(random.uniform(north, south), 6)
		locations.append((lat, lng))

	return locations