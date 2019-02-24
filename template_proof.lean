import init.data.set
open set

universe u

variable {U : Type}
variables A B C : set U
variable x : U
variable {α : Type u}

theorem setext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=
funext (assume x, propext (h x))

example : ∀ x, x ∈ A ∩ C → x ∈ A :=
  assume x,
  assume h : x ∈ A ∩ C,
  show x ∈ A, from and.left h
