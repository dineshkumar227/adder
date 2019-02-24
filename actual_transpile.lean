import init.data.set
open set
universe u
variable {U: Type}
variable {α : Type u}

variables A B C: set U

variable x: U

theorem setext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=
funext (assume x, propext (h x))

example : ∀ x, x ∈ A ∩ C → x ∈ A ∪ C :=
  assume x,
  assume: x ∈ (A) ∩ (C),
  have x ∈ (A), from and.left this, 
  show x ∈ (A) ∪ (C), from or.inl this

