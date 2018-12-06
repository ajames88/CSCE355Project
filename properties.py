import sys
fileName = sys.argv[1]

log = open("propertiesLogFile.txt", "w")
output = open("propertiesOutput.txt", "w")

f = open(fileName, "r")

log.write("Input is printed below:")
log.write(f.read())
log.write("\n")

log.write("Output is printed below:")
log.write("\n")

f = open(fileName, "r")

numOfStatesString = f.readline()
numOfStatesString = numOfStatesString.strip()
numOfStatesTrim = numOfStatesString[18:(len(numOfStatesString))]
numOfStates = int(numOfStatesTrim)

log.write("Number of States: ")
log.write(str(numOfStates))
log.write("\n")

acceptingStatesString = f.readline()
acceptingStatesString = acceptingStatesString.strip()
acceptingStatesTrim = acceptingStatesString[18:(len(acceptingStatesString))]

accepting = acceptingStatesTrim.split(" ")


log.write("Accepting States: ")
log.write(str(accepting))
log.write("\n")

alphabetString = f.readline()
alphabetString = alphabetString.strip()
alphabetStringTrim = alphabetString[10:(len(alphabetString))]

alphabetLength = len(alphabetStringTrim)

alphabet = []
for x in alphabetStringTrim:
	alphabet.append(x)

log.write("Alphabet: ")
log.write(str(alphabet))
log.write("\n")

adjMatrix = []
for x in range(numOfStates):
	adjMatrix.append([])

for x in range(numOfStates):
	paths = f.readline()
	paths = paths.strip()
	matrix = paths.split(" ")
	adjMatrix[x] = matrix

log.write("Adjacency Matrix:: ")
log.write(str(adjMatrix))
log.write("\n")

reachable = []

needToCheck = []
for x in range(numOfStates):
    needToCheck.append(x)

log.write("\nNeed to Check: "+str(needToCheck)+"\n\n")

def reachAll(state):
    log.write("The following states are reachable directly from state "+str(state)+": ")
    for x in adjMatrix[state]:
        if x not in reachable:
            reachable.append(x)
        log.write(x+" ")
    log.write("\n")

for x in range(numOfStates):
    reachAll(x)

log.write("\nReachable States: "+str(reachable)+"\n")

empty = True

for x in accepting:
    if x in reachable:
        output.write("nonempty\n")
        empty = False
    break

if empty == True:
    output.write("empty\n")

f.close()
log.close()
output.close()
