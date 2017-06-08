
def scale(dataset, key, value):
	mean = sum(dataset[key]) / dataset['len']
	maxX = max(dataset[key])
	minX = min(dataset[key])

	return ( (value - mean) / (maxX - minX) )
