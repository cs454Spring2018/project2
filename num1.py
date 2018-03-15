# 0, 1
table = [
		[[0, 1], [0, 2]],
		[[2, 1], [3, 0]],
		[[1], [0]],
		[[3], [1, 2]]
]
accepting_states = [2, 3]
def visitNFA(table, input_, accepting_states):

	as_ = [1] + [0 for i in table]
	#print(table)
	for char in input_:
		temp = [0 for i in table]
		ns = []
		for i, a in enumerate(as_):
			if a == 1:
				# [row][column]
				for j in table[i][char]:
					ns.append(j)
		for k in ns:
			#print(k)
			temp[k] = 1
		as_ = temp
		#print(as_)

	for s in accepting_states:
		if as_[s] == 1:
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
