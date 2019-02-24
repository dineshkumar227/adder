import init.data.set
open set

universe u

variable {U : Type}
variables A B C : set U
variable x : U
variable {α : Type u}

theorem setext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=
funext (assume x, propext (h x))

example : ∀ x, x ∈ A → x ∈ B → x ∈ A ∩ B :=
	assume x,
	assume h1 : x ∈ A,
	assume h2 : x ∈ B,
	show x ∈ A ∩ B, from and.intro this
