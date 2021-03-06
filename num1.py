# 0, 1
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
				# [row][column]
				for j in table[i][char]:
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

	for state, next_state_sets in enumerate(nfa):
		print(state, next_state_sets)

	print()
	print()
	new_dfa = [0] * next_state_value
	for state, next_state_sets in enumerate(dfa_2):

		new_dfa[state] = []

		for i, next_states in enumerate(next_state_sets):

			new_dfa[state].append([dfa_2[state][i][0] + next_state_value])


	for state, next_state_sets in enumerate(new_dfa):
		nfa.append(next_state_sets)

	for state, next_state_sets in enumerate(new_dfa):
		print(state + 7, next_state_sets)


	return nfa, [next_state_value]

def makeDFAs(alphabet, n):

	return createArray(alphabet, n), createArray(alphabet, n)

def convertToList(number_as_string):
	return [int(i) for i in number_as_string]

# only accept strings strongly divisible by n
# rejects strings not strongly divisible by n
def stronglyNotDivisible(nfa, string, accepting_states):
	return visitNFA(nfa, string, accepting_states)
dfa_1, dfa_2 = makeDFAs([1, 3], 7)

nfa, accepting_states = makeNFA(dfa_1, dfa_2)
print()
for state, next_state_sets in enumerate(nfa):
	print(state, next_state_sets)

print()
#print(visitNFA(nfa, convertToList('741842607938866199443579680083706254648829519399268'), accepting_states))
#exit()
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
			print(string_test, j)

			for i, a in enumerate(string_test):
				#print(string_test[0:i] + string_test[i+1:])
				if int(string_test[0:i] + string_test[i+1:]) % mod_val == 0:
					strings.append(string_test[0:i] + string_test[i+1:])
			print(len(strings), len(string_test))

			#if
			if len(strings) >= 50:
				print(string_test)
				#exit()
				#[print(a) for a in strings]
				#print('yes')
				#exit()
				break

			#exit()
		irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
		#print()
		j += 1
	print(str(irand))

def checkBadValues(irand, mod_val):
	j = 0
	while True:
		if j == 5:
			exit()
		if irand % mod_val != 0:
			string_test = str(irand)
			strings = []
			print(string_test, j)

			for i, a in enumerate(string_test):
				#print(string_test[0:i] + string_test[i+1:])
				if int(string_test[0:i] + string_test[i+1:]) % mod_val != 0:
					strings.append(string_test[0:i] + string_test[i+1:])
			print(len(strings), len(string_test))
			#if
			#if len(strings) >= 50:
			#print(string_test)

				#[print(a) for a in strings]
				#print('yes')
				#exit()
					#break

			#exit()
		irand = randrange(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
		print()
		j += 1
	print(str(irand))
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

	for state in current_states:
		for next_state in A[state][col]:
			current_col.add(next_state)
	return current_col

def nextComboState(A, combo_state):

	next_combo_states = []

	for col in A[0][0]:
		current_states = currentStates(combo_state)

		current_col = nextStates(A, col, current_states)

		next_combo_states.append(('_'.join([str(j) for j in current_states]),
								'_'.join([str(i) for i in sorted(copy.deepcopy(current_col))])))
	return next_combo_states

def makeRow(B, combo_state, A, next_combo_states):

	row = [0] * len(A[0])
	for i, next_state in enumerate(next_combo_states):
		row[i] = next_state[1]
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


B, F = convertNFAToDFA(NFA, [1, 2])
print('nfa')
for i, row in enumerate(NFA):
	print(i, row)

print('accepting states')
print([1, 2, 3])
print()
print('dfa')
for key in B.keys():
	print(key, B[key])
print('accepting states')
print(F)
#print(makeStrongDivisibleKIsFourDigits(1000))

# these should be true
# given 741842607938866199443579680083706254648829519399268 mod 7, 7777 passes
# 67140565324915476532894093498249241428815633453515 mod 7, 7777 passes
# 60602458739593758801428753207988572826358825383144 mod 7, 7777 passes
# 18798293705262441795908572595974294588427819707030 mod 7, 7777 passes
# 24380419698913736423265066784537597353213515197355 mod 7776 passes
# 8673606822268548135917519151355148533771190385120752633984174147239531311111 mod 7777 passes
# 2032636995801934685454869205005410949798183892863782071019641590732058670784 mod 7776 passes

# these should be false
# 84843010178338875747249268316350454599531414812814 mod 7  passes
# 1207313411301253005613037496458396753532429435750 mod 7 passes
# 47422524109175904866718488445265110400851139717641 mod 7 passes
# 99425368701814469896596121584433242153152636615037 mod 7777
#[print(number) for number in strings]
#print(stronglyNotDivisible(nfa, convertToList('741842607938866199443579680083706254648829519399268'), accepting_states))

# change to python
#nfaToDfa = () =>
#{

	# after converting make a list of all states that are marked accepting_state

	# for each state name that is accepting
		# make a new mark array that records a mark for all string states containing the ith accepting state name
#}
