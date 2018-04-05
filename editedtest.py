import sys
from random import randrange, uniform
from collections import OrderedDict as od



def visitNFA(table, input_, accepting_states):

    number_of_states = len(table)
    active_states = [1] + ([0] * number_of_states)

    for char in input_:
        temp = [0] * number_of_states
        next_states = []
        for i, state in enumerate(active_states):
            if state:
                for j in table[i][char]:
                    next_states.append(j)
        for k in next_states:
            temp[k] = 1
        active_states = temp

    for s in accepting_states:
        if active_states[s]:
            return True
    return False


def createArray(alphabet, n):
    return [ [ [( remainder * 10 + letter ) % n] for letter in alphabet ] for remainder in range(n) ]

def makeNFA(dfa_1, dfa_2):

    # possible accepting state because the second dfa accepts at this state, as it is the first state for the second dfa
    next_state_value = len(dfa_1)

    nfa = [0] * next_state_value
    for state, next_state_sets in enumerate(dfa_1):
        nfa[state] = next_state_sets
        for i, next_states in enumerate(next_state_sets):
            nfa[state][i].append(state + next_state_value)

    new_dfa = [0] * next_state_value
    for state, next_state_sets in enumerate(dfa_2):

        new_dfa[state] = []

        for i, next_states in enumerate(next_state_sets):

            new_dfa[state].append([dfa_2[state][i][0] + next_state_value])


    for state, next_state_sets in enumerate(new_dfa):
        nfa.append(next_state_sets)

    return nfa, [next_state_value, 0]

def makeDFAs(alphabet, n):
    return createArray(alphabet, n), createArray(alphabet, n)

def convertToList(number_as_string):
    return [int(i) for i in number_as_string]

# only accept strings strongly divisible by n
# rejects strings not strongly divisible by n
def stronglyNotDivisible(nfa, string, accepting_states):

    return not visitNFA(nfa, string, accepting_states)

def checkGoodValues(irand, mod_val):
    j = 0
    while True:
        if irand % mod_val == 0:
            string_test = str(irand)
            strings = []
            for i, a in enumerate(string_test):
                if int(string_test[0:i] + string_test[i+1:]) % mod_val == 0:
                    strings.append(string_test[0:i] + string_test[i+1:])

            if len(strings) >= 50:
                break

        irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
        j += 1

def checkBadValues(irand, mod_val):
    j = 0
    while True:
        if j == 5:
            exit()
        if irand % mod_val != 0:
            string_test = str(irand)
            strings = []

            for i, a in enumerate(string_test):
                if int(string_test[0:i] + string_test[i+1:]) % mod_val != 0:
                    strings.append(string_test[0:i] + string_test[i+1:])
            
        irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
        j += 1
    
def makeStrongDivisibleKIsFourDigits(k):

    scalar = 1
    possible_value = scalar * k
    while True:
        if possible_value % k == 0:

            string_test = str(possible_value)
            strings = []

            for i, a in enumerate(string_test):
                if int(string_test[0:i] + string_test[i+1:]) % mod_val == 0:
                    strings.append(string_test[0:i] + string_test[i+1:])
            if len(strings) == len(string_test):
                return string_test
            else:
                scalar += 1
                possible_value = scalar * k

import copy
def currentStates(current_state):

    if len(current_state.split('_')) > 1:
        return [int(j) for j in current_state.split('_')]
    else:
        return [int(current_state)]

def nextStates(A, col, current_states):

    current_col = set()


    for state in current_states:
        for next_state in A[state][col]:
            current_col.add(next_state)
    return current_col

def nextComboState(A, combo_state):

    next_combo_states = []

    for col, next_states in enumerate(A[0][0]):
        current_states = currentStates(combo_state)

        current_col = nextStates(A, col, current_states)

        next_combo_states.append(('_'.join([str(j) for j in current_states]),
                                '_'.join([str(i) for i in sorted(copy.deepcopy(current_col))])))
    return next_combo_states

def makeRow(B, combo_state, A, next_combo_states):
    row = []
    for i, next_state in enumerate(next_combo_states):
        row.append(next_state[1])
    return row

def addAcceptingStatesToF(current_combo_state, F, combo_state, accepting_states):

    for number in [int(k) for k in combo_state.split('_')]:
        if number in accepting_states:
            F.add(current_combo_state)
    return F

def appendNextComboStates(unadded_states, next_combo_states):
    for j in next_combo_states:
        unadded_states.append(j[1])
    return unadded_states



def convertNFAToDFA(A, accepting_states):

    unadded_states = ['0']

    F = set()
    B = od([])
    while unadded_states != []:


        combo_state = unadded_states[0]
        del unadded_states[0]

        next_combo_states = nextComboState(A, combo_state)

        current_combo_state = next_combo_states[0][0]

        F = addAcceptingStatesToF(current_combo_state, F, combo_state, accepting_states)

        B[combo_state] = makeRow(B, combo_state, A, next_combo_states)

        unadded_states = appendNextComboStates(unadded_states, next_combo_states)

        x = set(unadded_states)
        y = set(B.keys())
        if list(x & y) != []:

            unadded_states = list(x - y)

    return B, F

def testing(F):
    counter = 0
    for i in F:
        if '7' in i.split('_'):
            counter += 1
    return counter

def convertToProperllyConvertedDFA(dfa, f, dictionary):
        new_dfa = []
        for i, key in enumerate(dfa.keys()):
            next_states = []

            
            for next_state in dfa[key]:
                
                next_states.append(dictionary[next_state] )

                
            new_dfa.append(next_states)


        new_F = [dictionary[key] for key in f]
        #print(new_F)
        return new_dfa, new_F

def Pop(queue):
	item = queue[0]
	del queue[0]
	return item

def Push(queue, item):

	queue.append(item)
	return queue

# 9 is not strongly divisible by 7
def bfs(state_transition_table, start_state, alphabet, accepting_states, n):

	edge_input = {i:letter for i, letter in enumerate(alphabet)}
	visited = [0] * len(state_transition_table)
	sequences_found_so_far = [(-1, -1)] * len(state_transition_table)
	queue = []
	visited[start_state] = 1
	queue = Push(queue, start_state)
	n += 1
	level_counter = 1
	i = 1
	j = 0

	while (queue != []):
	   current_remainder = Pop(queue)
	   next_remainders = [(edge_input[i], NextRemainder) for i, NextRemainder in enumerate(state_transition_table[current_remainder])]

       for y in next_remainders:
'''
            (letter, next_remainder) = y

            
            if visited[next_remainder] == 0:
			    visited[next_remainder] = 1
				sequences_found_so_far[next_remainder] = (current_remainder, letter)
				queue = Push(queue, next_remainder)
				j += 1

			if next_remainder in accepting_states and level_counter == n:
				print(level_counter - 1)

				sequences_found_so_far[next_remainder] = (current_remainder, letter)
				return recover(sequences_found_so_far, next_remainder)
		i -= 1

		if i == 0:
            level_counter += 1
            i = j
            j = 0
    #print("wtf")
'''


def recover(sequences_found_so_far, next_remainder):
    sequence = []
    (prev_state, input_index) = sequences_found_so_far[next_remainder]

    sequence.insert(0, str(input_index))
    while prev_state != 0:
        (prev_state, input_index) = sequences_found_so_far[prev_state]
        sequence.insert(0, str(input_index))

    return ''.join(sequence)
def createArray2(alphabet, n):
    return [ [ ( remainder * 10 + letter ) % n for letter in alphabet ] for remainder in range(n) ]


def testConvertDFAEquivalence(nfa, accepting_states):
    quitloop = False
    for i in range(1):
        b, f = convertNFAToDFA(nfa, accepting_states)
        c, d = convertNFAToDFA(nfa, accepting_states)
        for key_1, key_2 in zip(b.keys(), c.keys()):
            #print(key_1, " ", key_2)
            if key_1 != key_2:
                print(key_1, " ", key_2, " SHOULD BE THE SAME")
                quitloop = True
            else:
                for i, next_state in enumerate(b[key_1]):
                    if next_state != c[key_2][i]:
                        print("THIS IS WRONG, next state should equal c[key_2][i]")

        if quitloop:
            exit()
        print("all keys were the same in the converted DFA's")

def testConvertToProperllyConvertedDFA(dfa1, dfa2):
    quitloop = false
    for i, row in enumerate(dfa1):
        for j, col in enumerate(row):
            if col != dfa2[i][j]:
                print("our col in dfa1 did not equal dfa2, somethings wrong!")
                quitloop = true
    if quitloop:
            exit()
    print("Convert to properlly converted dfa worked!")


def convertTest(B, F):

    converted_state_number = { number : i for i, number in enumerate(B.keys()) }

    properlyConvertedDFA, properlyConvertedAcceptingStates = convertToProperllyConvertedDFA(B, F, converted_state_number)

    new_accepting_states = set([i for i, row in enumerate(properlyConvertedDFA)]) - set(properlyConvertedAcceptingStates)

    return properlyConvertedDFA

def testExtraCredit(nfa, accepting_states, n, k):
    for i in range(10):
        dfa_1, dfa_2 = makeDFAs([i for i in range(10)], k)

    #nfa, accepting_states = makeNFA(dfa_1, dfa_2)
    
    B, F = convertNFAToDFA(nfa, accepting_states)
    

    converted_state_number = { number : i for i, number in enumerate(B.keys()) }
    properlyConvertedDFA, properlyConvertedAcceptingStates = convertToProperllyConvertedDFA(B, F, converted_state_number)

    new_accepting_states = set([i for i, row in enumerate(properlyConvertedDFA)]) - set(properlyConvertedAcceptingStates)
    test_dfa = createArray2([i for i in range(1, 10)], k)
    
    #int(len(str(n)))
    #when 17 gets put in it fucks up
    sequence = int(bfs(properlyConvertedDFA, 0, [i for i in range(10)], new_accepting_states, 17))
    if  sequence == -1:
        print("Could not find any integer with ", int(len(str(n))), " digits that is strongly not divisible by ", k,)
    else:
        print("The smallest integer with ", int(len(str(n))), " digits that is strongly not divisible by ", k, " is: ", sequence)

    
    #print(len(str(n)))

    #for key in B.keys():
     #   print(B[key])

def main():
    if sys.version_info <= (3, 0):
       sys.exit('You need python 3.0>')

    k = int(input("Enter your k (at most 4 digits): "))
    if k > 9999:
        while k > 9999:
            k = int(input("Your k is more then 4 digits, try again: "))

    dfa_1, dfa_2 = makeDFAs([i for i in range(10)], k)
    nfa, accepting_states = makeNFA(dfa_1, dfa_2)

    [print(i) for i in nfa]
    n = input("Enter an integer N (up to 100 digits: ")

# 60602458739593758801428753207988572826358825383144 mod 7, 7777 passes

    if stronglyNotDivisible(nfa, convertToList(n), accepting_states):
        print("yes ", n, " is strongly not divisible by ", k)
    else:
        print("no ", n, " is strongly not divisible by ", k)

    #fails after n is more then 16 digits long? wtf? 
    testExtraCredit(nfa, accepting_states, n, k)


main()
#print(nfa);
'''
B, F = convertNFAToDFA(nfa, accepting_states)

convertTest(B, F)

testConvertDFAEquivalence(nfa, accepting_states)
'''




#dfa_1, dfa_2 = makeDFAs([1, 3], 7)

#nfa, accepting_states = makeNFA(dfa_1, dfa_2)
#print()
#for state, next_state_sets in enumerate(nfa):
    #print(state, next_state_sets)

#print()
#B, F = convertNFAToDFA(NFA, [1, 2])
#k = int(input("Enter an integer K: "))
'''
dfa_1, dfa_2 = makeDFAs([i for i in range(10)], 7777)
nfa, accepting_states = makeNFA(dfa_1, dfa_2)
[print(i) for i in nfa]
#n = input("Enter an integer N: ")

# 60602458739593758801428753207988572826358825383144 mod 7, 7777 passes

if stronglyNotDivisible(nfa, convertToList('99425368701814469896596121584433242153152636615037'), accepting_states):
    print("yes is strongly not divisible by 7777")
else:
    print("is strongly divisible by 7777")
'''












'''
if stronglyNotDivisible(nfa, convertToList(741842607938866199443579680083706254648829519399268), accepting_states):
    print("yes ", n, " is strongly not divisible by ", k)
else:
    print("no ", n, " is not strongly not divisible by ", k)
'''
#if stronglyNotDivisible(nfa, convertToList('741842607938866199443579680083706254648829519399268'), accepting_states)):
#print(stronglyNotDivisible(nfa, convertToList('84843010178338875747249268316350454599531414812814'), accepting_states))

#print(stronglyNotDivisible(nfa, convertToList('99425368701814469896596121584433242153152636615037'), accepting_states))


#print(stronglyNotDivisible(nfa, convertToList(''), accepting_states))


'''
def main():
    if sys.version_info <= (3, 0):
       sys.exit('You need python 3.0>')

    int(input("enter



B, F = convertNFAToDFA(nfa, accepting_states)

#nfa, accepting_states = makeNFA(dfa_1, dfa_2)
'''
NFA = [
    [[0, 1], [0, 3]],
    [[0, 2], [1, 2]],
    [[3, 0], [0]],
    [[], []],

]

# extra credit
'''
for i in range(10):
	dfa_1, dfa_2 = makeDFAs([i for i in range(10)], 7)

	nfa, accepting_states = makeNFA(dfa_1, dfa_2)
	
	B, F = convertNFAToDFA(nfa, accepting_states)
	

	converted_state_number = { number : i for i, number in enumerate(B.keys()) }
	properlyConvertedDFA, properlyConvertedAcceptingStates = convertToProperllyConvertedDFA(B, F, converted_state_number)

	new_accepting_states = set([i for i, row in enumerate(properlyConvertedDFA)]) - set(properlyConvertedAcceptingStates)
	test_dfa = createArray2([i for i in range(1, 10)], 7)
	
	sequence = int(bfs(properlyConvertedDFA, 0, [i for i in range(10)], new_accepting_states, 5))

	print(sequence)


for key in B.keys():
    print(B[key])
'''


#print('accepting states')
#print(F)
#length = len(F)


#print("testing F:", length, testing(F))
#keys = B.keys()

#keys_left = keys - F
#print(testing(keys_left))


#print(stronglyNotDivisible(nfa, convertToList('741842607938866199443579680083706254648829519399268'), accepting_states))


#print(makeStrongDivisibleKIsFourDigits(1000))

# these should be true(strongly not divisible)
# given 741842607938866199443579680083706254648829519399268 mod 7, 7777 passes
# 67140565324915476532894093498249241428815633453515 mod 7, 7777 passes
# 60602458739593758801428753207988572826358825383144 mod 7, 7777 passes
# 18798293705262441795908572595974294588427819707030 mod 7, 7777 passes
# 24380419698913736423265066784537597353213515197355 mod 7776 passes
# 8673606822268548135917519151355148533771190385120752633984174147239531311111 mod 7777 passes
# 2032636995801934685454869205005410949798183892863782071019641590732058670784 mod 7776 passes

# these should be false(strongly divisible)
# 84843010178338875747249268316350454599531414812814 mod 7  passes
# 1207313411301253005613037496458396753532429435750 mod 7 passes
# 47422524109175904866718488445265110400851139717641 mod 7 passes
# 99425368701814469896596121584433242153152636615037 mod 7777
#[#print(number) for number in strings]
#print(stronglyNotDivisible(nfa, convertToList('741842607938866199443579680083706254648829519399268'), accepting_states))

# change to python
#nfaToDfa = () =>
#{

    # after converting make a list of all states that are marked accepting_state

    # for each state name that is accepting
        # make a new mark array that records a mark for all string states containing the ith accepting state name
#}
