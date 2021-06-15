import sys, os

def checkFile():
	try:
		filePath = sys.argv[1]
		return filePath
	except:
		print("Usage: %s bench_file" %sys.argv[0])
		exit()
	

def processFile(filePath):
	seatsArray = []
	
	f = open(filePath, "r")
			
	dMin,sMin = f.readline().split()
	roomArea,nbSeats = f.readline().split()
	
	while True:
		buffer = f.readline().split()
		if buffer:
			seatsArray.append([buffer[0],buffer[1]])
		else:
			break

	return seatsArray,dMin,sMin,roomArea,nbSeats

def makeSeries(seatsArray,offset):
	seriesArray = [[1,[0.0,0.0],0]]
	xData = 0
	i = 1
	
	# INITIAL CONDITION // SERIES NUMBER ZERO
	while True:
		# print("iteration",i)
		# print("series:",seriesArray[0])
		# print("step 1")
		xData = float(seatsArray[i][0])
		# print("xData:",xData,"xMin:",seriesArray[0][1][0],"xMax:",seriesArray[0][1][1])
		
		if  xData > seriesArray[0][1][1]:
			# print("step 2")
			# print("Found higher xMax")
			seriesArray[0][1][1] = xData
		elif xData == seriesArray[0][1][0]:
			# print("step 3")
			# print("End of series reached")
			seriesArray[0][2] = findNbSeatsSeries(seatsArray,0,seriesArray[0][1][0],seriesArray[0][1][1])
			break
		
		# print("step 4\n")
		i = i+1
		
	print("Series number",seriesArray[0][0])
	print("xMin:",seriesArray[0][1][0])
	print("xMax:",seriesArray[0][1][1])
	print("Number of seats:",seriesArray[0][2])
	print("Raw series data:",seriesArray[0])

	# initial series is predetermined
	# new series = number of series in seriesArray +1
	# new series data based on series n-1
	
	return seriesArray

def findNbSeatsSeries(seatsArray,offset,xMin,xMax):
	for i in range(len(seatsArray[offset:])):	
		if float(seatsArray[i][0]) > xMax:
			break
	return i
	


####################

def main():
	filePath = checkFile()
	print("File path is",filePath)
	seatsArray,dMin,sMin,roomArea,nbSeats = processFile(filePath)
	print("Seats array done\n")
	seriesArray = makeSeries(seatsArray)

####################

main()