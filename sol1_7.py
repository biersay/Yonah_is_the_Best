import numpy as np
def rotate(arr):
	try:
		arr = np.array(arr)
	except:
		quit("You done screwed up")
	n = np.shape(arr)[0]
	if(n != np.shape(arr)[1] or len(np.shape(arr)) != 2):
		print("You suck! Asshole")
		return(-1)
	return(np.array([[arr[n-1-j,i] for j in range(n)] for i in range(n)]))
	
		
