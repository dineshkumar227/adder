import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def get_variables(statement):
    variables = []
    for word in statement:
        if word == "be":
            break
        elif word != ",":
            variables.append(word)

    return variables

def get_sets(statement):
    sets = []
    for word in statement:
        for l in word:
            if l.isupper():
                sets.append(l)
    sets = list(set(sets))

    return sets

def get_assumptions(statement):
    assumptions = [t.strip() for t in statement.split("such that")[1].split(',')]
    return assumptions

def parser(proof):
    sent_token = proof.split('\n', proof.count('\n'))
    variables = []; sets = []; assumptions = []; statements = []; question=""

    for statement in sent_token:
        if len(statement) < 2:
            continue

        if "Question:" in statement:
            question = statement.split("Question:")[1].strip()

        word_token = word_tokenize(statement)
        if word_token[0] == "Let":
            variables = get_variables(word_token[1:])
            sets = get_sets(word_token[1:])
            assumptions = get_assumptions(statement)
        elif statement[0] == "⇒" or statement[0] == "∴":
            statements.append(statement[1:].rstrip())

    return question, variables, sets, assumptions, statements
