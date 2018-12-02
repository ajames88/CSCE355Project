import sys
fileName = sys.argv[1]

f = open(fileName, "r")
print("Input is printed below:")
print(f.read())

print("Output is printed below:")
f = open(fileName, "r")

numOfStatesString = f.readline()
numOfStatesString = numOfStatesString.strip()
numOfStatesTrim = numOfStatesString[(len(numOfStatesString) - 1)]
numOfStates = int(numOfStatesTrim)
print("Number of States: ", numOfStates)

acceptingStatesString = f.readline()
acceptingStatesString = acceptingStatesString.strip()
acceptingStatesTrim = acceptingStatesString[18:(len(acceptingStatesString))]
acceptingStatesNoSpaces = acceptingStatesTrim.replace(" ", "")

accepting = []
for x in acceptingStatesNoSpaces:
	accepting.append(x)

print("Accepting States:", accepting)

alphabetString = f.readline()
alphabetString = alphabetString.strip()
alphabetStringTrim = alphabetString[10:(len(alphabetString))]

alphabetLength = len(alphabetStringTrim)

alphabet = []
for x in alphabetStringTrim:
	alphabet.append(x)

print("Alphabet:", alphabet)

adjMatrix = []
for x in range(numOfStates):
	adjMatrix.append([])

for x in range(numOfStates):
	paths = f.readline()
	paths = paths.strip()
	pathsTrim = paths.replace(" ","")
	for y in pathsTrim:
		adjMatrix[x].append(y)

print("Adjacency Matrix: :", adjMatrix)
