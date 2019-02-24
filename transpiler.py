def extract_statement(sentence):
	return " ".join(sentence.split()[2:len(sentence.split())-3])

def extract_have(sentence):
	return " ".join(sentence.split()[:len(sentence.split())-3])

def get_reason(statement, proof, variable):
	#print("statement " + statement)
	#print("proof " + proof)
	
	ret = ""

	s = []
	count = 0
	countback = 0
	for i in proof:
		if i == '(':
			s.append(1)
		elif i == ')':
			s.pop()
		if len(s) == 0:
			break
		count += 1

	s = []
	for i in statement:
		if i == '(':
			s.append(1)
		elif i == ')':
			s.pop()
		if len(s) == 0:
			break
		countback += 1

	#print("count " + str(count))
	#print("count back" + str(countback))
	
	if count != len(proof) - 1:
		prev  = proof[:count+1]
		#print(" op is and")
		#print("prev is " + prev)
		after = proof[count+3:]
		#print("next is " + after)

		op = proof[count+2]

		if op == "∪":
			#print("op is or")
			ret += "or."
			if statement == prev:
				ret += "inr "
			else:
				ret += "inl "
			ret += "this"
		else:
			#print("op is and")
			ret += "and."
			if statement == prev:
				ret += "left "
			else:
				ret += "right "
			ret += "this"

	else:
		prev  = statement[:countback+1]
		#print("prev is " + prev)
		after = statement[countback+3:]
		#print("next is " + after)

		op = statement[countback+2]

		if op == "∪":
			#print("op is or")
			ret += "or."
			if statement == prev:
				ret += "inr "
			else:
				ret += "inl "
			ret += "this"
		else:
			#print("op is and")
			ret += "and.intro "
			ret += "‹" + variable + " ∈ " + prev  +  "› "
			ret += "‹" + variable + " ∈ " + after +  "› "


	return ret
	

def parse(question, sets, variables, assumptions, statements):	
	code = [
	"import init.data.set",
	"open set",
	"universe u",
	"variable {U: Type}",
	"variable {α : Type u}",
	""]

	if len(sets) == 1:
		set_decl = "variable "
	else:
			set_decl = "variables "
	set_decl += " ".join(sets)
	set_decl += ": set U"
	code.append(set_decl)
	code.append("")

	if len(variables) == 1:
		variable_decl = "variable "
	else:
		variable_decl = "variables "

	variable_decl += " ".join(variables)
	variable_decl += ": U"
	code.append(variable_decl)
	code.append("")

	ext_theorem = [
	"theorem setext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=",
	"funext (assume x, propext (h x))"
	]
	code += ext_theorem
	code.append("")

	to_prove = "example : " + question + " :="
	code.append(to_prove)

	for i in variables:
		code.append("  assume " + i + ",")

	for i in range(len(assumptions)):
		code.append("  assume: " + assumptions[i] + ",")

	full_proof = assumptions + statements

	for j in range(len(statements)):
		i = statements[j]
		tokens = i.split()
		reason_stmt = tokens[-1]
		index_full_proof = int(reason_stmt) - 1

		if tokens[-2] == "statement":
			index_full_proof += len(assumptions)

		if index_full_proof < len(assumptions):
			proof = " ".join(full_proof[index_full_proof].split()[2:])
		else:
			proof = extract_statement(full_proof[index_full_proof])

		reason = get_reason(extract_statement(i), proof, tokens[0])
		if j != len(statements) - 1:
			code.append("  have " + extract_have(i) + ", from " + reason + ", ")
		else:
			code.append("  show " + extract_have(i) + ", from " + reason)


	return code
