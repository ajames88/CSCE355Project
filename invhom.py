import sys
dfa = sys.argv[1]
homomorphism = sys.argv[2]

log = open("homomorphismLogFile.txt", "w")
output = open("homomorphismOutput.txt", "w")

g = open(dfa, "r")

log.write("Input is printed below:"+"\n")
log.write(g.read())
log.write("\n")

log.write("Output is printed below:")
log.write("\n")

g.close()

g = open(fileName, "r")

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

g.close()

f = open(homomorphism, "r")

log.write("Input is printed below:"+"\n")
log.write(f.read())
log.write("\n")

f.close()

f = open(homomorphism, "r")

log.write("Output is printed below:"+"\n")

inAlphabetString = f.readline()
inAlphabetString = inAlphabetString.strip()
inAlphabetStringTrim = inAlphabetString[16:(len(inAlphabetString))]

inAlphabetLength = len(inAlphabetStringTrim)

inAlphabet = []
for x in inAlphabetStringTrim:
	inAlphabet.append(x)

log.write("Input Alphabet: ")
log.write(str(inAlphabet))
log.write("\n")

outAlphabetString = f.readline()
outAlphabetString = outAlphabetString.strip()
outAlphabetStringTrim = outAlphabetString[17:(len(outAlphabetString))]

outAlphabetLength = len(outAlphabetStringTrim)

outAlphabet = []
for x in outAlphabetStringTrim:
	outAlphabet.append(x)

log.write("Output Alphabet: ")
log.write(str(outAlphabet))
log.write("\n")

pairs = []

for x in inAlphabet:
    map = f.readline()
    if map == "\n":
        map = "epsilon"
    mapTrim = map.strip()
    pairs.append([x, mapTrim])

log.write("Pairs: ")
log.write(str(pairs))
log.write("\n")

f.close()
log.close()
output.close()
