import sys
fileName = sys.argv[1]

#log = open("simulatorLogFile.txt", "w")
#output = open("simulatorOutput.txt", "w")

f = open(fileName, "r")

#log.write("Input is printed below:")
#log.write(f.read())
#log.write("\n")

#log.write("Output is printed below:")
#log.write("\n")

f = open(fileName, "r")

numOfStatesString = f.readline()
numOfStatesString = numOfStatesString.strip()
numOfStatesTrim = numOfStatesString[18:(len(numOfStatesString))]
numOfStates = int(numOfStatesTrim)

#log.write("Number of States: ")
#log.write(str(numOfStates))
#log.write("\n")

acceptingStatesString = f.readline()
acceptingStatesString = acceptingStatesString.strip()
acceptingStatesTrim = acceptingStatesString[18:(len(acceptingStatesString))]

accepting = acceptingStatesTrim.split(" ")


#log.write("Accepting States: ")
#log.write(str(accepting))
#log.write("\n")

alphabetString = f.readline()
alphabetString = alphabetString.strip()
alphabetStringTrim = alphabetString[10:(len(alphabetString))]

alphabetLength = len(alphabetStringTrim)

alphabet = []
for x in alphabetStringTrim:
	alphabet.append(x)

#log.write("Alphabet: ")
#log.write(str(alphabet))
#log.write("\n")

adjMatrix = []
for x in range(numOfStates):
	adjMatrix.append([])

for x in range(numOfStates):
	paths = f.readline()
	paths = paths.strip()
	matrix = paths.split(" ")
	adjMatrix[x] = matrix

#log.write("Adjacency Matrix:: ")
#log.write(str(adjMatrix))
#log.write("\n")

inputFile = sys.argv[2]
inReader = open(inputFile, "r")

input = []
for x in inReader:
	x = x.strip()
	input.append(x)

#log.write("Input: ")
#log.write(str(input))
#log.write("\n")

for x in input:
	current = 0
	for y in range(len(x)):
		nextIn = x[y]
		currentAdj = adjMatrix[int(current)]
		#print(currentAdj)
		alphaInd = alphabet.index(nextIn)
		current = currentAdj[alphaInd]
		#print(current)
	if str(current) in accepting:
		#log.write("Ending State: "+str(current)+" -> ")
		#log.write("accept\n")
		print("accept")
	else:
		#log.write("Ending State: "+str(current)+" -> ")
		#log.write("reject\n")
		print("reject")

f.close()
#log.close()
#output.close()
