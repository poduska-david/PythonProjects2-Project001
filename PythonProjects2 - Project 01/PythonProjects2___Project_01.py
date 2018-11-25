running = True
calculationStack = []
result = 0
while running:
	#Ask for input
	print("Type in space delimited operation(s) in Reverse Polish Notation")
	calculation = input()
	#parse input
	tokens = calculation.split(" ")
	#caluculate
	for token in tokens:
		if token in "+-*/%^":
			#Pop operands from stack
			operandA = calculationStack.pop()
			operandB = calculationStack.pop()
			if token == "+":
				result = operandA + operandB
			elif token == "-":
				result = operandA - operandB
			elif token == "*":
				result = operandA * operandB
			elif token == "/":
				result = operandA - operandB
			elif token == "%":
				result = operandA % operandB
			elif token == "^":
				result = pow(operandA, operandB)
			#push result to stack
			calculationStack.append(result)
		elif token == "q":
			running = False
			continue;
		else:
			try:
				calculationStack.append(float(token))
			except ValueError:
				print("Token is not a valid operator or is not a number")
				continue;
	result = calculationStack.pop()
	#output answer
	print("Calculation result")
	print(result)