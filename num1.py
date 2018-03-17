# 0, 1
table = [
		[[0, 1], [0, 2]],
		[[2, 1], [3, 0]],
		[[1], [0]],
		[[3], [1, 2]]
]
accepting_states = [2, 3]
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

print(visitNFA(table, [0, 1], accepting_states))

table2 = [

		[[0], [0, 1]],
		[[2], [2]],
		[[3], [1]],
		[[3], [3, 4]],
		[[4], [4]]
	]
accepting_states2 = [4]
print(visitNFA(table2, [1, 1, 1, 0, 1, 1, 1, 1, 0, 1], accepting_states2))

def createArray(alphabet, n):

    #test = alphabet
    print("Shortest multiple of " + str(n) + " using digits {" + ' '.join(map(str,alphabet)) + "}:")

    return [ [ [( remainder * 10 + letter ) % n] for letter in alphabet ] for remainder in range(n) ]
def makeNFA(dfa_1, dfa_2):
	print()
	#[print(i, j) for i, j in enumerate(dfa_1)]
	#print()
	#[print(i, j) for i, j in enumerate(dfa_2)]

	next_state_value = len(dfa_1)
	#print(next_state_value)
	#print()
	nfa = [0] * next_state_value
	for state, next_state_sets in enumerate(dfa_1):
		nfa[state] = next_state_sets
		for i, next_states in enumerate(next_state_sets):
			nfa[state][i].append(state + next_state_value)
		#print(state, nfa[state])


	#print()
	new_dfa = [0] * next_state_value
	for state, next_state_sets in enumerate(dfa_2):

		new_dfa[state] = []

		for i, next_states in enumerate(next_state_sets):
			#print(dfa_2[state][i][0] + next_state_value)
			new_dfa[state].append([dfa_2[state][i][0] + next_state_value])
		#print(state + next_state_value, new_dfa[state])

	for state, next_state_sets in enumerate(new_dfa):
		nfa.append(next_state_sets)

	print()
	for state, next_state_sets in enumerate(nfa):

		print(state, next_state_sets)

		#nfa[state] = next_state_sets

dfa_1 = createArray([1, 3], 7)
dfa_2 = createArray([1, 3], 7)

makeNFA(dfa_1, dfa_2)
# change to python
#nfaToDfa = () =>
#{

	# after converting make a list of all states that are marked accepting_state

	# for each state name that is accepting
		# make a new mark array that records a mark for all string states containing the ith accepting state name
#}
