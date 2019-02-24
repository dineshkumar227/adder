import nltk
from nltk.tokenize import word_tokenize

def get_assumptions(statement):
	return " ".join(statement.split(" ")[1:])

def parser(proof):
	sent_token = proof.split('\n', proof.count('\n'))
	variables = []; sets = []; assumptions = []; statements = []; question=""

	for statement in sent_token:
		words = statement.split(" ")
		for i in words:
			if len(i) == 1:
				if i.isupper():
					sets.append(i)
				elif i.islower():
					variables.append(i)


		if len(statement) < 2:
			continue

		if "Question:" in statement:
			question = statement.split("Question:")[1].strip()

		word_token = word_tokenize(statement)
		if word_token[0] == "Let":
			assumptions.append(get_assumptions(statement).rstrip())
		elif statement[0] == "⇒" or statement[0] == "∴":
			statements.append(statement[1:].rstrip())

	variables = list(set(variables))
	sets = list(set(sets))


	return question, sets, variables, assumptions, statements
