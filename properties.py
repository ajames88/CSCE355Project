import sys
import queue
fileName = sys.argv[1]

#log = open("propertiesLogFile.txt", "w")
#output = open("propertiesOutput.txt", "w")

#f = open(fileName, "r")

#log.write("Input is printed below:\n")
#log.write(f.read())
#log.write("\n")

#f.close()

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

reachableFromStart = []

needToCheck = []
for x in range(numOfStates):
	needToCheck.append(x)

#log.write("\nNeed to Check: "+str(needToCheck)+"\n\n")

def reachAll(state, reachable):
        needToCheck.remove(int(state))
        for x in adjMatrix[state]:
                if x not in reachable:
                        reachable.append(x)
                if int(x) in needToCheck:
                        reachAll(int(x), reachable)

reachAll(0, reachableFromStart)

#log.write("\nReachable States: "+str(reachableFromStart)+"\n")

empty = True

for x in accepting:
	if x in reachableFromStart:
		empty = False

finite = True

reachables = []

def intersect(lista, listb):
	for x in lista:
		if x in listb:
			return True
	return False

def findReachable(x):
	reachableFromX = []
	toCheck = [x]
	while len(toCheck) > 0:
		state = toCheck[0]
		for y in adjMatrix[int(state)]:
			if y not in reachableFromX:
				reachableFromX.append(y)
				toCheck.append(y)
		toCheck.pop(0)
	return reachableFromX

for x in range(numOfStates):
	reachables.append(findReachable(x))
	if str(x) in reachables[x] and intersect(reachables[x], accepting) and str(x) in reachableFromStart:
		finite = False

if empty == True:
	#output.write("empty finite\n")
	print("empty finite")
if empty == False and finite == False:
	#output.write("nonempty infinite\n")
	print("nonempty infinite")
if empty == False and finite == True:
	#output.write("nonempty finite\n")
	print("nonempty finite")

f.close()
#log.close()
#output.close()
