def IncreasingSequences(V):
	n = list(range(0,len(V)))
	L = [1] * len(V)

	for i in range(1, len(V)):
		for j in range(1, i+1):
			if V[i-j] < V[i] and L[i] <= L[i-j]:
				L[i] = L[i-j] + 1

	longest_length = 0
	id_of_longest = 0

	for i in range(len(V)):
		if L[i] > longest_length:
			longest_length = L[i]
			id_of_longest = i

	sequence = [V[id_of_longest]]
	length_sequence = [longest_length]

	for i in range(id_of_longest-1, -1, -1):
		if V[i] < sequence[0] and L[i] == length_sequence[0] - 1:
			sequence.insert(0, V[i])
			length_sequence.insert(0, L[i])

	return sequence, longest_length

if __name__ == '__main__':
	V = [2, 22, 32, 35, 66, 59, 79, 64, 48, 96, 7, 39, 18, 15, 45, 89, 3, 81, 26, 26, 31, 55, 10, 91, 70, 61, 12, 87, 13, 31, 27, 58, 71, 75, 32, 63, 98, 77, 92, 43, 66, 32, 11, 65, 1, 80, 14, 99, 29, 91]
	A = IncreasingSequences(V)
	print(A)