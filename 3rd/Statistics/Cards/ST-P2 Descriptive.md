---
course: Statistics
source: "[[P2 Descriptive Statistics]]"
---
#flashcards/stats/p2-descriptive

# ST-P2 Descriptive Statistics — Cards (Lecture Notes Part II)

> [!info] How to use
> Fill the ✍️ answers in RStudio first (real data, real code). Core sheet: [[P2 Descriptive Statistics]]. Plan: [[00 Statistics Plan]]

## One variable

Absolute vs. relative frequency?::Absolute: count h of a value. Relative: proportion f = h / n.

Bar chart vs. histogram?::Bar chart: categorical (nominal/ordinal) data, separate bars. Histogram: numeric data grouped into bins, adjacent bars.

Why should pie charts be used carefully?::People compare angles and areas badly; bar charts are easier to read.

Rules for the number of bins k?::Basic: k = √n (n ≤ 1000) or 10·lg n (n > 1000). Sturges: k = 1 + log2(n). Rice: k = 2·n^(1/3).

What is the ECDF?::Fn(x) = (number of observations ≤ x) / n — a step function from 0 to 1.

Interpret Fn(50) = 0.65.::65 % of all observations are less than or equal to 50.

Mean, median, mode?::Arithmetic average; middle value of the sorted data; most frequent value.

Which measures are robust against outliers?::Median and IQR are robust; mean, range, variance and standard deviation are not.

Quartiles?::Q1 = 0.25-quantile, median = 0.5-quantile, Q3 = 0.75-quantile.

Six-number summary (as in the notes)?::Minimum, Q1, median, mean, Q3, maximum — the basis for the boxplot.

Range and IQR?::Range = max − min (very sensitive to outliers). IQR = Q3 − Q1, the spread of the middle 50 %.

Sample variance — formula and why n − 1?::s² = Σ(xi − x̄)² / (n − 1); dividing by n − 1 makes it an unbiased estimator of the population variance.

Boxplot elements?::Box from Q1 to Q3, thick line = median, whiskers to the most extreme non-outliers, points beyond 1.5·IQR from the box = outliers.

Skewness rule of thumb?::Right-skewed: usually mean > median. Left-skewed: usually mean < median. Symmetric: mean ≈ median. Only a rule of thumb, not always true.

Density plot and violin plot?::Density plot: smoothed histogram. Violin plot: density shape mirrored, good for comparing groups.

## Two variables

Sample covariance?::sxy = Σ(xi − x̄)(yi − ȳ) / (n − 1). Sign = direction of the linear relation; size depends on the units.

Pearson correlation r?::r = sxy / (sx · sy), between −1 and 1; measures only LINEAR relationships; unaffected by linear transformations.

When to use Spearman instead of Pearson?::Ordinal variables, monotonic but non-linear relationships, or extreme outliers — Spearman uses ranks.

Expected count in a contingency table (independence)?::E = (row total × column total) / n.

Chi-square statistic?::χ² = Σ (observed − expected)² / expected; large values speak against independence.

Relative risk in a 2×2 table?::RR = (f11 / f1·) / (f21 / f2·): the risk in group 1 divided by the risk in group 2.

Odds ratio and its interpretation?::OR = (f11 · f22) / (f12 · f21). OR = 1: no association; OR > 1: higher odds in group 1; OR < 1: protective effect.

## Data workflow

Tidy data — three rules?::Each variable is a column, each observation a row, each value a cell.

Main dplyr verbs?::filter (rows), select (columns), mutate (new columns), group_by + summarise (aggregates per group), arrange (sort), joins.

## R reflexes

R: frequency table and relative frequencies?::t <- table(x); prop.table(t); addmargins(t) for totals.

R: quartiles, IQR, summary?::quantile(x, c(0.25, 0.5, 0.75)); IQR(x); summary(x) or fivenum(x).

R: Pearson and Spearman correlation?::cor(x, y) and cor(x, y, method = "spearman").

R: expected counts and chi-square test of a table?::chisq.test(tab)$expected and chisq.test(tab).

R: histogram with ggplot2?::ggplot(df, aes(x = var)) + geom_histogram(binwidth = 3)

R: ECDF value at 50?::Fn <- ecdf(x); Fn(50)

R: boxplot per group with ggplot2?::ggplot(df, aes(x = group, y = value)) + geom_boxplot()

## Understanding — write your own answers ✍️

✍️ True or false: "In right-skewed data the mean is always larger than the median." Explain with an example.
?
✍️ your answer — then check [[P2 Descriptive Statistics]]

✍️ Titanic: compute the odds ratio of survival for women vs. men in R and interpret it in one sentence.
?
✍️ your code + sentence — then check [[P2 Descriptive Statistics]] gold example 2

✍️ The DWD workflow (sheet 5): name the 4 steps and one typical pitfall in each.
?
✍️ your answer — then check [[P2 Descriptive Statistics]] gold example 4

✍️ faithful$waiting has n = 272. How many bins do the basic rule, Sturges and Rice suggest? Which do you choose and why?
?
✍️ your answer — then check [[P2 Descriptive Statistics]] gold example 1
