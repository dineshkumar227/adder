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
		code.append("  assume h" + str(i+1) + assumptions[i] + ",")
	
	full_proof = assumptions + statements
	
	for i in statements:
		 tokens = i.split()
		 reason = tokens[-1]
		 

	
	return code

parsed_code = parse('∀ x, x ∈ A ∩ C → x ∈ A ∪ C', ['A', 'B', 'C'], ['x'], ['x \in A \i C'] , ['x \in A from 1', 'thus x \in A from 2'])
for i in parsed_code:
	print(i)
