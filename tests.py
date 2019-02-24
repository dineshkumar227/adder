from transpiler import *


parsed_code = parse('∀ x, x ∈ A ∩ C → x ∈ A ∪ C', ['A', 'B', 'C'], ['x'], ['x ∈ (A) ∩ (C)'] , ['x ∈ (A) from assumption 1', 'x ∈ (A) ∪ (C) from statement 1'])
print()
print("===================Proof===================")
print()

for i in parsed_code:
	print(i)



parsed_code = parse('∀ x, x ∈ A ∩ C → x ∈ A', ['A', 'B', 'C'], ['x'], ['x ∈ (A) ∩ (C)'] , ['x ∈ (A) from assumption 1'])

print()
print("===================Proof===================")
print()

for i in parsed_code:
	print(i)

# wrong proof
parsed_code = parse('∀ x, x ∈ A → x ∈ A ∩ C', ['A', 'B', 'C'], ['x'], ['x ∈ (A)'] , ['x ∈ (A) ∩ (C) from assumption 1'])

print()
print("===================Proof===================")
print()

for i in parsed_code:
	print(i)
