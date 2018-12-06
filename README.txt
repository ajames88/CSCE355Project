This project is authored by Austin James and it is the sole property of Austin James for use in CSCE 355 by instructor Duncan Buell. All Rights Reserved.

In order to run the simulator from to command line type 'python3.5 simulator.py' followed by the name of an input file containing the description of the DFA and another input file containing the strings to simulate.

The DFA input file should be in the following format:

Number of states: 5
Accepting states: 1 4
Alphabet: 01
0 1
2 3
4 0
1 2
3 4

The string input file should be in the following format:

00110
110
110100101
010001
1001111

An example of this command line call using the provided demo file is 'python3.5 simulator.py demofile.txt'.
The simulator should run completely and correctly.

In order to run the properties program from to command line type 'python3.5 properties.py' followed by the name of an input file containing the description of the DFA.

The DFA input file should be in the following format:

Number of states: 5
Accepting states: 1 4
Alphabet: 01
0 1
2 3
4 0
1 2
3 4

An example of this command line call using the provided demo file is 'python3.5 properties.py demofile.txt'.
The properties program should run completely and correctly.
