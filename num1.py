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

# change to python
#nfaToDfa = () =>
#{

	# after converting make a list of all states that are marked accepting_state

	# for each state name that is accepting
		# make a new mark array that records a mark for all string states containing the ith accepting state name
#}
