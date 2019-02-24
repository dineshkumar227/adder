import init.data.set
open set

universe u

variable {U : Type}
variables A B C : set U
variable x : U
variable {α : Type u}

theorem setext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=
funext (assume x, propext (h x))

example : ∀ x, x ∈ A ∩ C → x ∈ A ∪ C :=
  assume x,
  assume h2 : x ∈ A ∩ C,
  have h3: x ∈ A, from and.left h2,
  show x ∈ A ∪ C, from or.inl h3
