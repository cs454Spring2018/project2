
from random import randrange, uniform
from collections import OrderedDict as od



def visitNFA(table, input_, accepting_states):

    number_of_states = len(table)
    #print(len(table))
    active_states = [1] + ([0] * number_of_states)
#    #print(input_)
    for char in input_:
        temp = [0] * number_of_states
        next_states = []
        for i, state in enumerate(active_states):
            if state:
                # [row][column]
                #[#print(i) for i in table]
               # #print(i, char)
                for j in table[i][char]:
                    #print(table[i][char])
                    next_states.append(j)
        for k in next_states:
            temp[k] = 1
        active_states = temp

    for s in accepting_states:
        if active_states[s]:
            return True
    return False

table = [
        [[0, 1], [0, 2]],
        [[2, 1], [3, 0]],
        [[1], [0]],
        [[3], [1, 2]]
]

accepting_states = [2, 3]
#print(visitNFA(table, [0, 1], accepting_states))

table2 = [

        [[0], [0, 1]],
        [[2], [2]],
        [[3], [1]],
        [[3], [3, 4]],
        [[4], [4]]
    ]
accepting_states2 = [4]
#print(visitNFA(table2, [1, 1, 1, 0, 1, 1, 1, 1, 0, 1], accepting_states2))

def createArray(alphabet, n):

    #test = alphabet
    #print("Shortest multiple of " + str(n) + " using digits {" + ' '.join(map(str,alphabet)) + "}:")

    return [ [ [( remainder * 10 + letter ) % n] for letter in alphabet ] for remainder in range(n) ]

def makeNFA(dfa_1, dfa_2):

    # possible accepting state because the second dfa accepts at this state, as it is the first state for the second dfa
    next_state_value = len(dfa_1)

    nfa = [0] * next_state_value
    for state, next_state_sets in enumerate(dfa_1):
        nfa[state] = next_state_sets
        for i, next_states in enumerate(next_state_sets):
            nfa[state][i].append(state + next_state_value)
    #for state, next_state_sets in enumerate(nfa):
        #print(state, next_state_sets)
   # #print()
   # #print()
    new_dfa = [0] * next_state_value
    for state, next_state_sets in enumerate(dfa_2):

        new_dfa[state] = []

        for i, next_states in enumerate(next_state_sets):

            new_dfa[state].append([dfa_2[state][i][0] + next_state_value])


    for state, next_state_sets in enumerate(new_dfa):
        nfa.append(next_state_sets)
    #for state, next_state_sets in enumerate(new_dfa):
        #print(state + 7, next_state_sets)

    return nfa, [next_state_value, 0]

def makeDFAs(alphabet, n):
    return createArray(alphabet, n), createArray(alphabet, n)

def convertToList(number_as_string):
    return [int(i) for i in number_as_string]

# only accept strings strongly divisible by n
# rejects strings not strongly divisible by n
def stronglyNotDivisible(nfa, string, accepting_states):
    return not visitNFA(nfa, string, accepting_states)

# randrange gives you an integral value
#irand = randrange(0, 100000000000000000000000000000000000000000000000000)
def checkGoodValues(irand, mod_val):
    j = 0
    while True:
        #if j == 5:
            #exit()
        if irand % mod_val == 0:
            string_test = str(irand)
            strings = []
            #print(string_test, j)

            for i, a in enumerate(string_test):
                #print(string_test[0:i] + string_test[i+1:])
                if int(string_test[0:i] + string_test[i+1:]) % mod_val == 0:
                    strings.append(string_test[0:i] + string_test[i+1:])
            #print(len(strings), len(string_test))

            #if
            if len(strings) >= 50:
                #print(string_test)
                #exit()
                #[#print(a) for a in strings]
                #print('yes')
                #exit()
                break

            #exit()
        irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
        #print()
        j += 1
    #print(str(irand))

def checkBadValues(irand, mod_val):
    j = 0
    while True:
        if j == 5:
            exit()
        if irand % mod_val != 0:
            string_test = str(irand)
            strings = []
            #print(string_test, j)

            for i, a in enumerate(string_test):
                #print(string_test[0:i] + string_test[i+1:])
                if int(string_test[0:i] + string_test[i+1:]) % mod_val != 0:
                    strings.append(string_test[0:i] + string_test[i+1:])
            #print(len(strings), len(string_test))
            #if
            #if len(strings) >= 50:
            #print(string_test)

                #[#print(a) for a in strings]
                #print('yes')
                #exit()
                    #break

            #exit()
        irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
        #print()
        j += 1
    #print(str(irand))
#checkGoodValues(randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000), 7776)

#checkBadValues(randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000), 77776)

def makeStrongDivisibleKIsFourDigits(k):

    scalar = 1
    possible_value = scalar * k
    while True:
        if possible_value % k == 0:

            string_test = str(possible_value)
            strings = []
            #print(string_test, j)

            for i, a in enumerate(string_test):
                #print(string_test[0:i] + string_test[i+1:])
                if int(string_test[0:i] + string_test[i+1:]) % mod_val == 0:
                    strings.append(string_test[0:i] + string_test[i+1:])
            if len(strings) == len(string_test):
                return string_test
            else:
                scalar += 1
                possible_value = scalar * k

NFA = [
    [[0, 1], [0, 3]],
    [[0, 2], [1, 2]],
    [[3, 0], [0]],
    [[], []],

]

import copy
def currentStates(current_state):

    if len(current_state.split('_')) > 1:
        return [int(j) for j in current_state.split('_')]
    else:
        return [int(current_state)]
    #return next_states

def nextStates(A, col, current_states):

    current_col = set()
    
    #print("HERE")
    for state in current_states:
        #print(state, " " , col)
        for next_state in A[state][col]:
            current_col.add(next_state)
    #print("HERE")
    return current_col

def nextComboState(A, combo_state):

    next_combo_states = []
    #print(A[0][0])
 #  #print(A[0])
    for col, next_states in enumerate(A[0][0]):
        current_states = currentStates(combo_state)

        current_col = nextStates(A, col, current_states)

        next_combo_states.append(('_'.join([str(j) for j in current_states]),
                                '_'.join([str(i) for i in sorted(copy.deepcopy(current_col))])))
        #print("SUPERHERE")
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
# next_remainder in F and counter == n


'''
i = 4 number of children from root
j = 0
count down i while recording chilfren
in for loop
count up children = j
j += 1
i -= 1
if i == 0

    
    append children at current node to counter(add to a sum and then append the sum)
    level += 1
    i = j
    j = 0
i = 4
i = 12
level = counter

count children
after first node is done
    append count

'''
def testing(F):
    counter = 0
    for i in F:
        if '7' in i.split('_'):
            counter += 1
    return counter
'''
def convertToRead(dfa, f):
        new_dfa = []
        for key in dfa.keys():
            next_states = []
            for next_state in dfa[key]:
                next_states.append(int(''.join(list(reversed(next_state.split('_'))))))
                #print(next_state)
            new_dfa.append(next_states)

        new_F = [int(''.join(list(reversed(key.split('_'))))) for key in f]  
        #[#print(i) for i in new_dfa]
        #print(new_F)
        return new_dfa, new_F
'''

def convertToProperllyConvertedDFA(dfa, f, dictionary):
        new_dfa = []
        for i, key in enumerate(dfa.keys()):
            next_states = []
            #print(dfa[key])
            for next_state in dfa[key]:
                #for value in next_state:
                next_states.append(dictionary[next_state] )

                #print(next_state)
            new_dfa.append(next_states)

        new_F = [dictionary[key] for key in f]  
        #print(new_F)
        return new_dfa, new_F

def testConvertDFAEquivalence(nfa, accepting_states):
    quitloop = False
    for i in range(1):
        b, f = convertNFAToDFA(nfa, accepting_states)
        c, d = convertNFAToDFA(nfa, accepting_states)
        for key_1, key_2 in zip(b.keys(), c.keys()):
            print(key_1, " ", key_2)
            if key_1 != key_2:
                print(key_1, " ", key_2, " SHOULD BE THE SAME")
                quitloop = True
            else:
                for i, next_state in enumerate(b[key_1]):
                    if next_state != c[key_2][i]:
                        print("WE SCREWED")
                        
        if quitloop:
            exit()
        print("all keys were the same")
 
def testConvertToProperllyConvertedDFA(dfa1, dfa2):
    for i, row in enumerate(dfa1):
        for j, col in enumerate(row): 
            if col != dfa2[i][j]:
                print("WE ARE SCREWED AGAIN")
    print("WE ARE GOOD IF SCREWED DIDNT SHOW")

 
def convertTest(B, F):

 #   keyArray = list(sorted([ int(''.join(list(reversed(key.split('_'))))) for key in B.keys()]))

    #convertedDFA, convertedAcceptingStates = convertToRead(B, F)
    converted_state_number = { number : i for i, number in enumerate(B.keys()) }

    properlyConvertedDFA, properlyConvertedAcceptingStates = convertToProperllyConvertedDFA(B, F, converted_state_number)

    new_accepting_states = set([i for i, row in enumerate(properlyConvertedDFA)]) - set(properlyConvertedAcceptingStates)
    
    return properlyConvertedDFA
               
#dfa_1, dfa_2 = makeDFAs([i for i in range(10)], 100)
#nfa, accepting_states = makeNFA(dfa_1, dfa_2)
#b, f = convertNFAToDFA(nfa, accepting_states)
#c, d = convertNFAToDFA(nfa, accepting_states)

dfa_1, dfa_2 = makeDFAs([i for i in range(10)], 7)
nfa, accepting_states = makeNFA(dfa_1, dfa_2)

B, F = convertNFAToDFA(nfa, accepting_states)

convertTest(B, F)
'''
for i in range(20):
    s = i
    if stronglyNotDivisible(nfa, convertToList(str(i)), accepting_states):
        print("yes is strongly not divisible by 7")
    else:
        print("is strongly divisible by 7")

for i in range(10):
    finalDFA1 = convertTest(b, f)
    finalDFA2 = convertTest(c, d)
    testConvertToProperllyConvertedDFA(finalDFA1, finalDFA2)
''' 


testConvertDFAEquivalence(nfa, accepting_states)


'''
B, F = convertNFAToDFA(nfa, accepting_states)

convertedDFA, convertedAcceptingStates = convertToRead(B, F)

dfa_1, dfa_2 = makeDFAs([i for i in range(10)], 7777)
nfa, accepting_states = makeNFA(dfa_1, dfa_2)

print(stronglyNotDivisible(nfa, convertToList('99425368701814469896596121584433242153152636615037'), accepting_states)) 

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

convertedDFA, convertedAcceptingStates = convertToRead(B, F)



sortedKeys = sorted(B.keys())
keyArray = list(sorted([ int(''.join(list(reversed(key.split('_'))))) for key in B.keys()]))

converted_state_number = { number : i for i, number in enumerate(keyArray) }
properlyConvertedDFA, properlyConvertedAcceptingStates = convertToProperllyConvertedDFA(convertedDFA, convertedAcceptingStates, converted_state_number)

new_accepting_states = set([i for i, row in enumerate(properlyConvertedDFA)]) - set(properlyConvertedAcceptingStates)
#print('compliment accepting states')
#print(new_accepting_states)

#print(nfa)



#[#print(i, converted_state_number[i]) for i in converted_state_number]
#print(sortedKeys)

#print('accepting states')
#print([1, 2, 3])
#print()

#print('dfa')
for key in B.keys():
    #print(B[key])
    


#print('accepting states')
#print(F)
length = len(F)


#print("testing F:", length, testing(F))
keys = B.keys()

keys_left = keys - F
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
'''
