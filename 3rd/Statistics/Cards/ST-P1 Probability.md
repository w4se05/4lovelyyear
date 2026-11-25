---
course: Statistics
source: "[[P1 Probability]]"
---
#flashcards/stats/p1-probability

# ST-P1 Probability — Cards (Lecture Notes Part I)

> [!info] How to use
> In the exam you have the lecture notes on the PC, so these cards train what the notes can't give you under time pressure: recognizing the right model, R syntax, and interpretation. Fill the ✍️ answers in R/on paper first. Core sheet: [[P1 Probability]]. Plan: [[00 Statistics Plan]]

## Probability models

Three parts of a probability model?::Sample space Ω, a σ-algebra F of events, a probability measure P on F.

Inclusion–exclusion for two events?::P(A ∪ B) = P(A) + P(B) − P(A ∩ B).

Complement and monotonicity?::P(A^c) = 1 − P(A); if B ⊆ A then P(B) ≤ P(A) and P(A ∩ B^c) = P(A) − P(B).

Uniform probability on a finite sample space?::P(A) = |A| / |Ω| (count favorable outcomes / all outcomes).

Conditional probability?::P(A | B) = P(A ∩ B) / P(B), for P(B) > 0.

Law of total probability?::P(A) = Σ P(A | Bi) · P(Bi) for a partition B1, B2, … of Ω.

Bayes' theorem?::P(Bj | A) = P(A | Bj) · P(Bj) / Σ P(A | Bi) · P(Bi).

Independence of A and B?::P(A ∩ B) = P(A) · P(B) (equivalently P(A | B) = P(A)).

## Random variables and distributions

What is a random variable?::A function X: Ω → ℝ.

pmf vs. density vs. cdf?::pmf: p(x) = P(X = x) (discrete). Density f: P(a < X ≤ b) = ∫ from a to b of f (absolutely continuous). cdf: F(x) = P(X ≤ x) (always).

Properties of every cdf?::0 ≤ F ≤ 1, nondecreasing, F → 0 for x → −∞, F → 1 for x → ∞, right-continuous.

Binomial(n, p): model, mean, variance?::Number of successes in n independent Bernoulli(p) trials. E = np, Var = np(1 − p).

Geometric(θ) as in the notes (and in R)?::Number of failures before the first success: P(X = k) = θ(1 − θ)^k, k = 0, 1, … ; mean (1 − θ)/θ.

Poisson(λ): use, mean, variance?::Count of rare events in a fixed interval; E = Var = λ.

Exponential(λ): density, mean, variance, special property?::f(x) = λe^(−λx) for x ≥ 0; E = 1/λ; Var = 1/λ²; memoryless.

Normal: standardization?::Z = (X − μ)/σ ~ N(0, 1).

Marginal from a joint density?::f_X(x) = ∫ f_X,Y(x, y) dy (sum over y in the discrete case).

## Expectation and dependence

Linearity of expectation?::E[aX + bY] = a·E[X] + b·E[Y] — always, independence not needed.

Variance: shortcut and effect of aX + b?::Var(X) = E[X²] − (E[X])²; Var(aX + b) = a²·Var(X); Sd(aX + b) = |a|·Sd(X).

Var(X + Y)?::Var(X) + Var(Y) + 2·Cov(X, Y); if X, Y are independent: Var(X) + Var(Y).

Covariance and correlation?::Cov(X, Y) = E[XY] − E[X]E[Y]; Corr = Cov / (Sd(X)·Sd(Y)), between −1 and 1.

Independent ⇒ uncorrelated? And the converse?::Independent ⇒ Cov = 0. But Cov = 0 does not imply independence.

Markov and Chebyshev inequalities?::Markov: P(X ≥ a) ≤ E[X]/a for X ≥ 0. Chebyshev: P(|X − μ| ≥ a) ≤ Var(X)/a².

## Limits and simulation

Weak law of large numbers?::The sample mean converges in probability to μ as n → ∞.

Central Limit Theorem?::For i.i.d. Xi with mean μ and variance σ²: (X̄n − μ)/(σ/√n) → N(0, 1) in distribution; a sum of n is approximately N(nμ, nσ²).

Rule of thumb for the normal approximation of Binomial(n, p)?::np ≥ 10 and n(1 − p) ≥ 10.

Order of the convergence types?::Almost sure ⇒ in probability ⇒ in distribution (the converses are false in general).

Inversion method?::If U ~ Uniform[0, 1] then F⁻¹(U) has cdf F. Exponential(λ): −ln(1 − U)/λ.

Monte Carlo estimate of a probability?::Simulate many independent repetitions and use the fraction of runs in which the event happened.

χ² and t distribution from normals?::χ²(n) = sum of n squared i.i.d. N(0,1). t(ν) = Z / √(V/ν) with Z ~ N(0,1), V ~ χ²(ν) independent.

## R reflexes

R: the four functions for a distribution (Binomial example)?::dbinom(k, n, p) = P(X = k); pbinom(k, n, p) = P(X ≤ k); qbinom(q, n, p) = quantile; rbinom(m, n, p) = m random values.

R: P(X ≥ 50) for X ~ Binomial(200, p)?::1 - pbinom(49, 200, p)  — or pbinom(49, 200, p, lower.tail = FALSE). Off-by-one: ≥ 50 means 1 − P(X ≤ 49).

R: P(X > 2) for X ~ N(mean 1, variance 9)?::1 - pnorm(2, mean = 1, sd = 3) — R wants the standard deviation, not the variance.

R: random values from an exponential distribution with mean 4?::rexp(n, rate = 1/4) — R uses the rate λ = 1/mean.

R: Monte Carlo estimate of P(sum of two dice = 7)?::mean(replicate(1e5, sum(sample(1:6, 2, replace = TRUE))) == 7)

R: make a simulation reproducible?::set.seed(123) before simulating.

## Understanding — write your own answers ✍️

✍️ Test: prevalence 1 %, sensitivity 99 %, false-positive rate 5 %. P(sick | positive)? Solve with Bayes, then check by simulation in R, and interpret.
?
✍️ your answer — then check [[P1 Probability]] gold example 1

✍️ Mock exam Q1: P(X ≥ 50) exactly, via CLT, and by simulation. Why do the three numbers differ?
?
✍️ your answer — then check [[P1 Probability]] gold example 2 and the mock exam Rmd

✍️ Poisson vs. Binomial vs. Geometric vs. Exponential: when do you use which? One CS example each.
?
✍️ your answer — then check [[P1 Probability]] decision table

✍️ Explain the CLT in 3 sentences to a friend, and why it matters for statistics.
?
✍️ your answer — then check Lecture Notes Part I, section 4.4

✍️ Write the 5-line Monte Carlo recipe in R for any probability (as in the R guide, §12).
?
✍️ your answer — then check [[R Guide for Statistics Part 1]] §12
