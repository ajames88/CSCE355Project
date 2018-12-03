import sys
fileName = sys.argv[1]

f = open(fileName, "r")
print("Input is printed below:")
print(f.read())

print("Output is printed below:")
f = open(fileName, "r")

numOfStatesString = f.readline()
numOfStatesString = numOfStatesString.strip()
numOfStatesTrim = numOfStatesString[18:(len(numOfStatesString))]
numOfStates = int(numOfStatesTrim)
print("Number of States: ", numOfStates)

acceptingStatesString = f.readline()
acceptingStatesString = acceptingStatesString.strip()
acceptingStatesTrim = acceptingStatesString[18:(len(acceptingStatesString))]

accepting = acceptingStatesTrim.split(" ")


print("Accepting States: ", accepting)

alphabetString = f.readline()
alphabetString = alphabetString.strip()
alphabetStringTrim = alphabetString[10:(len(alphabetString))]

alphabetLength = len(alphabetStringTrim)

alphabet = []
for x in alphabetStringTrim:
	alphabet.append(x)

print("Alphabet: ", alphabet)

adjMatrix = []
for x in range(numOfStates):
	adjMatrix.append([])

for x in range(numOfStates):
	paths = f.readline()
	paths = paths.strip()
	matrix = paths.split(" ")
	adjMatrix[x] = matrix

print("Adjacency Matrix:: ", adjMatrix)

inputFile = sys.argv[2]
inReader = open(inputFile, "r")

input = []
for x in inReader:
	x = x.strip()
	input.append(x)

print(numOfStates, len(adjMatrix))

print("Input: ", input)

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
		print(current, "accept")
	else:
		print(current, "reject")
