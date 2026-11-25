# R Guide for Statistics Part 1

*Companion to Ex01 (Intro to R), Ex02 and Ex03 (Probability Theory) and the Part 1 lecture-notes exercises*

This guide covers the R you need for your course: the core language (Ex01), the simulation toolkit (Ex02/Ex03), exact computation in R, a hint for every exercise on your sheets, and the linear-model preview. Every code block runs as written (use `set.seed()` first if you want identical numbers).

## 1. Workflow and getting help

- **Console** is for quick tests, a **script** (.R) is for code you keep, and an **R Markdown** file (.Rmd) mixes text, LaTeX and code chunks. A chunk starts with three backticks and `{r}` and ends with three backticks. Run a chunk with Ctrl/Cmd+Shift+Enter, and render the whole file with Knit.
- Put `set.seed(1)` at the top of a document so random results are reproducible.
- Comments start with `#`.
- `?mean` opens the help page for a function, `example(mean)` runs its examples, and `??keyword` searches all help pages.
- Inspecting objects: `str(x)` (structure), `class(x)`, `length(x)`, `dim(m)`, `head(df)`, `summary(df)`, `ls()` (list objects), `rm(x)` (delete).

## 2. Objects, assignment, arithmetic

```r
a <- 7.5            # assign with <-
b <- 2
a + b; a - b; a * b; a / b
a^b                 # power
a %% b              # remainder (modulo): 1.5
a %/% b             # integer quotient: 3
sqrt(a); exp(a); log(a); abs(-3); round(a); floor(a); ceiling(a)
rm(b)               # remove b
```

- `;` lets you put several statements on one line.
- Special values: `NA` (missing), `Inf`, `NaN`, `TRUE`/`FALSE` (always capitals), `NULL` (nothing).
- Floating-point warning: `0.1 + 0.2 == 0.3` is `FALSE`. Compare with a tolerance, `abs(x - y) < 1e-12`, or use `all.equal(x, y)`. Your Ex02 task 1 does exactly this.

## 3. Vectors

The vector is the basic data type; a single number is a vector of length 1.

```r
x <- c(3, 1, 4, 1, 5)        # combine
1:8                           # range 1,2,...,8
seq(0, 1, by = 0.25)          # 0 0.25 0.5 0.75 1
seq(0, 1, length.out = 5)     # same thing
rep(c('a', 'b'), times = 3)   # a b a b a b
rep(c('a', 'b'), each = 3)    # a a a b b b
length(x); sum(x); prod(x); cumsum(x); rev(x); sort(x); unique(x)
min(x); max(x); range(x); which.max(x); which(x == 1)
mean(x); var(x); sd(x); median(x)
quantile(x, probs = c(0.25, 0.75))
```

**Vectorization.** Arithmetic is applied element by element, so you rarely need a loop:

```r
x <- 1:8
x^2 - 3*x + 2
```

**Recycling.** If two vectors have different lengths, the shorter one is repeated:

```r
y <- c(10, 20, 30, 40, 50)
y + c(1, 2)    # 11 22 31 42 51 (with a warning: 5 is not a multiple of 2)
```

**Indexing.** R counts from **1**, not 0.

```r
y[2]            # one element
y[2:4]          # elements 2 to 4
y[-1]           # everything except the first
y[-(2:4)]       # everything except 2 to 4
y[c(2, 4)]      # elements 2 and 4
y[y > 20]       # logical filter: 30 40 50
y[length(y)]    # last element
```

**Named vectors** (used in Ex02 task 1):

```r
p <- c('1' = 1/2, '2' = 1/3, '3' = 1/6)
p[c('1', '2')]            # subset by name
sum(p[c('1', '2')])       # P({1,2}) = 5/6
names(p)                  # the names
names(p) <- c('a', 'b', 'c')   # rename
```

## 4. Logical vectors and conditions

```r
x <- 1:8
x %% 2 == 0              # TRUE/FALSE for each element
x[x %% 2 == 0]           # the even ones
x > 2 & x < 6            # AND (element-wise)
x < 2 | x > 6            # OR (element-wise)
!(x > 3)                 # NOT
x %in% c(2, 5, 7)        # membership
any(x > 7); all(x > 0)   # collapse a logical vector to one value
sum(x > 3)               # counts the TRUEs
mean(x > 3)              # proportion of TRUEs  <-- the key to simulation
```

- `==` tests equality, `=` and `<-` assign. Mixing them up is the most common beginner bug.
- `&` and `|` work element-wise on vectors. `&&` and `||` only look at single values and are meant for `if` conditions. In your Ex02 task 2 you want `|`.
- `TRUE` counts as 1 and `FALSE` as 0 in arithmetic, which is why `mean()` of a logical vector gives a proportion.

## 5. Factors and tables

```r
sex <- c('male', 'female', 'female', 'male', 'male')
f <- factor(sex)            # categorical variable with levels
levels(f)
table(f)                    # frequency table
table(f) / length(f)        # proportions
prop.table(table(f))        # same
table(sex) |> prop.table()  # same, using the pipe
```

The pipe `x |> f()` means `f(x)`. It lets you read code left to right. `table()` also works on numbers, so `table(rowSums(dice)) / N` gives an empirical pmf.

## 6. Matrices

```r
M <- matrix(1:9, nrow = 3, ncol = 3, byrow = TRUE)  # byrow = TRUE: fill row by row
M <- matrix(1:9, nrow = 3)                          # default: fill column by column
t(M)                  # transpose
M %*% t(M)            # matrix multiplication (M * M is element-wise!)
solve(M2)             # inverse of an invertible matrix M2
diag(3)               # 3x3 identity
colSums(M); rowSums(M); colMeans(M); rowMeans(M)
M[1, 2]               # row 1, column 2
M[, 2]                # whole second column
M[1, ]                # whole first row
M[3, 3] <- 0          # replace an entry
dim(M); nrow(M); ncol(M)
```

The default of filling **by column** matters in simulation: `matrix(sample(1:6, 2*N, replace = TRUE), ncol = 2)` puts the first N draws in column 1 and the next N in column 2, exactly as Ex02 task 3 describes.

## 7. Lists and data frames

A **list** can hold objects of different types and sizes. A **data frame** is a list of equal-length columns, i.e. a table.

```r
l <- list(z = rnorm(5), init = rep('Fa', 5), mat = M)
l$z              # by name
l[['z']]         # same
l[[1]]           # by position (the object itself)
l[1]             # a list of length 1 (not the object!)

df <- data.frame(x = rnorm(10, 5, 2), y = rnorm(10, 10, 3))
df$x             # a column
df[3, ]          # a row
df[df$x > 5, ]   # filter rows
nrow(df); ncol(df); names(df); summary(df)
```

Incompatible shapes: `data.frame()` needs columns of equal length, so the 3x3 matrix in Ex01 task 6 cannot sit next to length-5 vectors. Drop it with `l[-3]`. Rows are recycled only if the lengths divide evenly.

## 8. Functions and control flow

```r
z_score <- function(x) {
  if (sd(x) == 0) warning('sd is 0, z-scores are undefined')
  (x - mean(x)) / sd(x)       # the last expression is returned
}
z_score(c(1, 2, 3, 4))

f <- function(n, p = 0.5) {   # default argument
  rbinom(1, n, p)
}
f(10)           # uses p = 0.5
f(10, p = 0.3)  # named argument
```

```r
for (i in 1:3) print(i^2)
if (x > 0) 'pos' else 'non-pos'      # for single values
ifelse(x > 0, 'pos', 'non-pos')      # for whole vectors
while (cond) { ... }                 # rarely needed here
```

- `ifelse()` is vectorized and is for transforming vectors. Use `if` for deciding what code to run. Your Ex01 task 8 asks for a *warning*, so use `if` plus `warning()` (or `stop()` for an error).
- Anonymous functions are common: `function(A) sum(p[A])`, or the short form `\(A) sum(p[A])`.
- Avoid loops that grow a vector. Prefer `replicate()`, `sapply()` or vectorized code.

## 9. The apply family

```r
sapply(mtcars, mean)                      # mean of every column, returns a vector
vapply(1:5, function(i) i^2, numeric(1))  # like sapply, but checks the output type
lapply(1:3, function(i) i^2)              # returns a list
apply(mtcars, MARGIN = 2, FUN = quantile, probs = c(0.25, 0.75))  # per COLUMN
apply(mtcars, MARGIN = 1, FUN = sum)                              # per ROW
aggregate(. ~ cyl, data = mtcars, FUN = mean)      # group means by cyl
aggregate(mtcars, by = list(cyl = mtcars$cyl), FUN = mean)  # alternative
replicate(1000, mean(rnorm(10)))          # repeat an expression 1000 times
```

`MARGIN = 1` means rows and `MARGIN = 2` means columns. Your Ex01 task 9 asks for column quantiles, so use 2.

## 10. Reading, writing and plotting

```r
f <- tempfile(fileext = '.csv')   # a temporary file path, portable across computers
write.csv(df, f, row.names = FALSE)
df2 <- read.csv(f)

plot(df2$x, df2$y, xlab = 'x', ylab = 'y', main = 'Scatter', pch = 19)
abline(lm(y ~ x, data = df2), col = 'red')       # least-squares line

hist(z, breaks = 30, freq = FALSE)                 # freq = FALSE: density scale
curve(dnorm(x), add = TRUE, col = 'blue')          # overlay a density
plot(ecdf(z))                                      # empirical cdf
barplot(table(f))
boxplot(mpg ~ cyl, data = mtcars)
```

`setwd()` with a hard-coded path breaks on other computers, so prefer `tempfile()` or an RStudio project.

## 11. Probability distributions: the r / d / p / q pattern

Every distribution has four functions that share a prefix letter:

- `r...` **random** draws, `rnorm(n, mean, sd)`
- `d...` **density** (continuous) or **pmf** (discrete), the value of f(x) or P(X = x)
- `p...` **cdf**, P(X <= x). Add `lower.tail = FALSE` for P(X > x).
- `q...` **quantile**, the inverse cdf

| Distribution | Simulate | pmf / density | cdf |
| --- | --- | --- | --- |
| Binomial(n, p) | `rbinom(N, n, p)` | `dbinom(k, n, p)` | `pbinom(k, n, p)` |
| Geometric(p) | `rgeom(N, p) + 1` | `dgeom(k - 1, p)` | `pgeom(k - 1, p)` |
| Hypergeometric | `rhyper(N, m, n, k)` | `dhyper(x, m, n, k)` | `phyper(x, m, n, k)` |
| Uniform\[a, b\] | `runif(N, a, b)` | `dunif(x, a, b)` | `punif(x, a, b)` |
| Exponential(rate) | `rexp(N, rate)` | `dexp(x, rate)` | `pexp(x, rate)` |
| Normal(mu, sd) | `rnorm(N, mu, sd)` | `dnorm(x, mu, sd)` | `pnorm(x, mu, sd)` |

Three traps:

1. **Geometric.** R's `rgeom` counts the *failures before the first success* (values 0, 1, 2, ...). Your Ex03 uses the convention Z in {1, 2, ...}, so add 1 to simulations. For exact values, P(Z = k) is `dgeom(k - 1, p)`.
2. **Normal.** R wants the standard deviation, not the variance. N(5, 9) is `rnorm(N, 5, 3)`.
3. **Exponential.** R's second argument is the *rate* lambda (mean 1/lambda), matching the usual Exponential(lambda) notation.

Hypergeometric `dhyper(x, m, n, k)`: m = number of red balls, n = number of blue balls, k = number drawn, x = reds in the draw.

**Sampling from a finite set** with `sample()`:

```r
sample(1:6, 10, replace = TRUE)     # 10 die rolls (replace = TRUE for independent draws)
sample(1:52, 5)                     # 5 cards without replacement (the default)
sample(c('H', 'T'), 1e5, replace = TRUE, prob = c(0.3, 0.7))   # biased coin
sample(c(5))                        # TRAP: a single number n means sample(1:n)
```

## 12. The simulation (Monte Carlo) recipe

By the law of large numbers, the fraction of trials in which an event happens approaches its probability. Every simulation exercise follows the same steps:

1. Choose a large `N` (try 1e3, 1e4, 1e5, 1e6 and watch the estimate stabilize).
2. Simulate all N trials at once with vectorized code, or with `replicate()` when each trial has a variable number of steps.
3. Turn each trial into `TRUE`/`FALSE` for the event.
4. Estimate the probability with `mean(event)`.
5. Compare with the exact answer from pen and paper, and return both as a named vector.

```r
set.seed(1); N <- 1e5

# Event from a single draw (Ex 1.3.2)
x <- sample(1:100, N, replace = TRUE)
est <- mean(x %% 3 == 0 | x %% 5 == 0)
exact <- (33 + 20 - 6) / 100
c(estimate = est, exact = exact)

# Several dice per trial (Example 1.4.6): rows are trials, columns are dice
d <- matrix(sample(1:6, 2 * N, replace = TRUE), ncol = 2)
s <- rowSums(d)
c(estimate = mean(s == 10), exact = 3 / 36)
```

**Conditional probability** P(A | B): keep only the trials where B happened, then take the share where A happened.

```r
mean(A[B])          # A and B are logical vectors of length N
sum(A & B) / sum(B) # equivalent
```

**Independence check** (Ex 1.5.13): events are independent if P(A and B) = P(A) P(B). Estimate each side and compare, e.g. `mean(A & C)` against `mean(A) * mean(C)`.

**Repeating a multi-step experiment** with `replicate()` (Challenge 1.4.30):

```r
birthday <- function(C, N) {
  replicate(N, any(duplicated(sample(1:365, C, replace = TRUE))))
}
mean(birthday(23, 10000))                       # about 0.507
Cs <- 2:60
est <- sapply(Cs, function(C) mean(birthday(C, 5000)))
Cs[which(est > 0.5)[1]]                         # first group size above 50%
1 - prod((365 - 0:22) / 365)                    # exact for C = 23
```

**Estimating a pmf**: `table(y) / N`, or `prop.table(table(y))`. For continuous variables, estimate P(X > a) with `mean(x > a)`, or look at `hist()` / `ecdf()`.

**Maximizing over a parameter grid** (Ex 2.3.5):

```r
ps <- seq(0.01, 0.99, by = 0.01)
est <- sapply(ps, function(p) mean(rbinom(1e5, 12, p) == 11))
ps[which.max(est)]            # near 11/12 = 0.917
plot(ps, est, type = 'l')
```

**How accurate is the estimate?** The standard error is about `sqrt(p * (1 - p) / N)`, so 10 times more precision costs 100 times more samples.

## 13. Exact answers in R (counting)

```r
choose(52, 5)       # number of 5-card hands = 2,598,960
factorial(5)        # 120
prod(1:5)           # also 120
combn(1:3, 2)       # all 2-element subsets, one per column
combn(c('a', 'b', 'c'), 2, simplify = FALSE)   # as a list
expand.grid(die1 = 1:6, die2 = 1:6)            # all 36 outcomes of two dice
```

**Exercise 1.4.13 (five-card hands), exact:**

```r
H <- choose(52, 5)
c(four_aces_plus_KS = 1 / H,
  all_spades        = choose(13, 5) / H,
  no_pairs          = choose(13, 5) * 4^5 / H,
  full_house        = 13 * choose(4, 3) * 12 * choose(4, 2) / H)
```

**Dice sums by brute force:** `table(outer(1:6, 1:6, '+'))` lists the 36 sums, and `table(outer(1:6, 1:6, '*'))` the 36 products.

**All subsets automatically** (Ex02 task 1):

```r
omega <- c('1', '2', '3')
subs <- c(list(character(0)),
          unlist(lapply(1:3, function(k) combn(omega, k, simplify = FALSE)),
                 recursive = FALSE))
length(subs)   # 2^3 = 8 events
```

## 14. Hints for each exercise on your sheets

### Ex02: Probability Theory I

- **1.2.10.** Build `p`, build `subs`, compute `vals` with `vapply(subs, function(A) if (length(A) == 0) 0 else sum(p[A]), numeric(1))`, name it, and filter with `vals[abs(vals - 0.5) < 1e-12]`.
- **1.3.2.** See the template in Section 12. Exact: 33 multiples of 3, 20 of 5, 6 of 15, so 47/100.
- **Example 1.4.6.** Template in Section 12. Exact: 3/36.
- **1.4.13.** Exact code in Section 13.
- **1.4.30.** Template in Section 12. Parts (a) to (c) by hand: 1/365, (1/365)^(C-1), and 1 - 365 x 364 x ... x (365 - C + 1) / 365^C. The 50% crossover is at C = 23.
- **1.5.4.** Simulate three coins as `flips <- matrix(rbinom(3 * N, 1, 0.5), ncol = 3)`, then `two <- rowSums(flips) == 2` and `mean(flips[two, 1] == 1)`. Exact: 2/3.
- **Example 1.5.1.** Pick the urn first, then the ball colour, and condition on blue. Use the urn contents from your lecture notes:

  ```r
  urn  <- sample(1:2, N, replace = TRUE)
  blue <- runif(N) < ifelse(urn == 1, p_blue_urn1, p_blue_urn2)   # fill in from the notes
  mean(urn[blue] == 2)   # P(urn 2 | blue)
  ```
- **1.5.13.** Draw `red <- sample(1:6, N, TRUE)` and `blue <- sample(1:6, N, TRUE)`. Then `A <- red == blue`, `B <- red + blue == 12`, `C <- red == 4`, `D <- blue == 4`. For (b) compare `mean(A & C)` with `mean(A) * mean(C)`, and for (d) compare `mean(C & D)` with `mean(C) * mean(D)`.
- **1.5.19.** Exact: `dhyper(0:5, 8, 12, 5)`. Simulation: `replicate(N, sum(sample(c(rep(1, 8), rep(0, 12)), 5)))`, then `table(...) / N`.
- **Example 1.5.3 (Monty Hall).**

  ```r
  car  <- sample(1:3, N, TRUE)
  pick <- sample(1:3, N, TRUE)
  # staying wins when pick == car; the host opens a goat door, so switching wins otherwise
  c(stay = mean(pick == car), switch = mean(pick != car))   # about 1/3 and 2/3
  ```

### Ex03: Probability Theory II

- **2.3.3 (product pmf).** `y <- sample(1:6, N, TRUE) * sample(1:6, N, TRUE)`, then `round(table(y) / N, 4)`. Compare with `table(outer(1:6, 1:6, '*')) / 36`.
- **2.3.4 (geometric).** `Z <- rgeom(N, p) + 1`, then `mean(Z >= 5 & Z <= 9)`. Exact: `pgeom(8, p) - pgeom(3, p)`.
- **2.3.5 (binomial maximizer).** Grid search from Section 12. The exact answer is p = 11/12.
- **2.4.3.** `U <- runif(N)`; `mean(U <= 0.5)`, `mean(U >= 1/3 & U <= 2/3)`, `mean(U == 1)`. Exact: 1/2, 1/3, 0.
- **2.4.4.** `Z <- rexp(N, 4)`; `mean(Z > 5)` and `mean(Z > 2 & Z <= 5)`. Exact: `exp(-20)` and `exp(-8) - exp(-20)`. Note that exp(-20) is about 2e-9, so even N = 1e6 will give 0. This is a useful lesson on rare events.
- **2.4.5 (find c).** Since the density must integrate to 1, c = 1 / E\[g(U)\] where g is the shape (x or x^n) and U is uniform on (0,1). So `U <- runif(N); 1 / mean(U)` gives c for (i), exact value 2, and `1 / mean(U^n)` gives c for (ii), exact value n + 1.
- **2.5.3 (scaled die).** `X <- sample(1:6, N, TRUE) / 6`; `Fx <- ecdf(X)`; `plot(Fx)`; check `Fx(0)` (about 0) and `Fx(1)` (equals 1).
- **2.5.4.** `X <- rnorm(N)`; `mean(X > 2 & X < 7)` and `mean(X <= -3)`. Exact: `pnorm(7) - pnorm(2)` and `pnorm(-3)`.
- **2.6.2.** `X <- runif(N, L, R); Y <- c * X + d`. Check `range(Y)`, `hist(Y, freq = FALSE)` with `curve(dunif(x, c*L + d, c*R + d), add = TRUE)`.
- **2.6.3.** `X <- rnorm(N, mu, sigma); Y <- c * X + d`. Check that `mean(Y)` is near `c*mu + d` and `sd(Y)` is near `abs(c) * sigma`.

## 15. Linear model preview (Ex01 tasks 7 and 10)

```r
set.seed(1)
n <- 100
x <- rnorm(n)
y <- 3 + 2 * x + rnorm(n)        # true intercept 3, slope 2
fit <- lm(y ~ x)                  # y ~ x means: model y as a function of x
coef(fit)                         # estimated b0 and b1
summary(fit)$r.squared            # R squared
summary(fit)$sigma                # residual standard error
summary(fit)                      # full table
plot(fitted(fit), resid(fit)); abline(h = 0, lty = 2)   # residuals vs fitted
```

A good residual plot is a shapeless cloud around 0. A U-shape means the relationship is not linear, and a funnel shape means the variance changes with x.

## 16. Common mistakes checklist

- Counting from 0 instead of 1 in indexing.
- `=` where `==` was meant.
- `||` or `&&` where the element-wise `|` or `&` is needed.
- Forgetting `replace = TRUE` in `sample()` for independent trials (dice, coins, birthdays).
- `sample(n)` with a single number gives a permutation of 1:n, not one draw.
- `rgeom` starts at 0, and `rnorm` takes sd, not variance.
- `matrix()` fills by column, `M * M` is not matrix multiplication (use `%*%`), and `apply()` margin 1 is rows while margin 2 is columns.
- Comparing floating-point numbers with `==`.
- Estimating a tiny probability with too small an `N`. If the exact value is about 1/N or smaller, the estimate will be 0.
- Forgetting `set.seed()`, which makes results change on every run.
- Overwriting built-ins such as `c`, `t`, `T` or `data` as variable names. It works, but causes confusing bugs.

## 17. One-page cheat sheet

| Task | Code |
| --- | --- |
| Random draws from a finite set | `sample(x, n, replace = TRUE)` |
| Estimate a probability | `mean(event)` |
| Conditional probability | `mean(A[B])` |
| Repeat an experiment | `replicate(N, expr)` |
| Empirical pmf | `table(y) / N` |
| Empirical cdf | `ecdf(x)` |
| Counting | `choose(n, k)`, `factorial(n)`, `combn()` |
| Exact binomial / normal | `dbinom`, `pbinom`, `pnorm` |
| Maximize over a grid | `which.max(sapply(grid, f))` |
| Matrix of trials | `matrix(draws, ncol = k)`, then `rowSums()` |
| Check duplicates | `any(duplicated(v))` |
| Linear model | `lm(y ~ x)`, `summary(fit)` |
| Reproducibility | `set.seed(1)` |
