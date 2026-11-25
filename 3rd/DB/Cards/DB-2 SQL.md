---
course: Databases
source: "[[2.SQL]]"
---
#flashcards/db/2-sql

# DB-2 SQL — Cards (SQL 1–8)

> [!info] How to use
> Write the ✍️ queries on paper first (the exam is on paper!), then run them in HSQLDB and compare. Core sheet: [[2.SQL]]. Plan: [[00 DB Plan]]

## Basic queries

Basic SQL query and its relational-algebra meaning?::SELECT = projection, FROM = cross product, WHERE = selection.

Does SELECT remove duplicates?::No. SQL works on bags; use SELECT DISTINCT.

LIKE wildcards?::_ = exactly one arbitrary character; % = any sequence of characters (also empty).

How do you test for NULL?::IS NULL / IS NOT NULL — a comparison "= NULL" is never true.

NULL in arithmetic expressions?::If at least one operand is NULL, the result is NULL.

Logic used for conditions with NULL, and what does WHERE keep?::Three-valued logic: true, false, unknown. WHERE keeps only the tuples whose condition is true.

Several relations in the FROM clause?::They are combined by a cross product; the join condition goes into WHERE.

UNION vs. UNION ALL?::UNION removes duplicates; UNION ALL keeps them.

Set difference and intersection in SQL?::EXCEPT and INTERSECT.

ORDER BY: default and descending; example with two keys?::Ascending by default, DESC for descending. order by Birthday desc, SName

## Subqueries and quantifiers

Uncorrelated vs. correlated subquery?::Uncorrelated: does not depend on the outer query, evaluated once. Correlated: refers to the outer tuple, evaluated per outer tuple.

EXISTS R?::True iff the subquery result R is not empty.

s IN R?::True iff tuple s equals one of the tuples of R.

s θ ANY R and s θ ALL R?::ANY: the comparison holds for at least one tuple of R. ALL: it holds for all tuples of R — and is true if R is empty.

Is "θ ALL" a universal quantifier?::No (slides): it only compares with the values of a subquery result. SQL has no universal quantifier.

IN vs. EXISTS — expressive power?::Every condition with IN can be replaced by an equivalent (correlated) condition with EXISTS.

Two ways to express "for all" in SQL?::Double negation with NOT EXISTS ("there is no lecture the student does not attend") — or counting: GROUP BY … HAVING count(*) = (select count(*) from Lecture).

## Aggregation

Aggregate functions?::count, sum, avg, min, max — they reduce a column to one value.

count(*) vs. count(A) vs. count(distinct A)?::All tuples vs. non-NULL values of A vs. different non-NULL values of A.

Rule for the SELECT list with GROUP BY?::Attributes that are not in the GROUP BY clause may only appear inside aggregate functions.

WHERE vs. HAVING?::WHERE filters tuples before grouping; HAVING decides which groups are in the result (may use aggregates).

Why is "where Grade = min(Grade)" wrong, and what is right?::Aggregates are not allowed in WHERE. Use a subquery: where Grade = (select min(Grade) from …).

## Recursion, modification, schema, views

Template of a recursive query?::with recursive tmp(…) as ( base query union recursive query that uses tmp ) select … from tmp

DELETE and UPDATE syntax?::delete from R where condition · update R set A = value where condition

Danger of DELETE without WHERE?::It deletes all tuples of the relation.

Why are modifications executed in two steps?::1. determine all tuples to modify, 2. apply the change — so the result does not depend on the order in which tuples are processed.

char(n) vs. varchar(n); numeric(p, s)?::char: fixed number of characters; varchar: maximum number of characters. numeric: p total digits, s digits after the decimal point (default 0).

Why cast(a.number as real) / cast(b.number as real)?::To avoid integer division when both columns are integers.

What is a view?::A virtual relation defined by a query: create view Name as query.

Uses and drawback of views?::Structure complex queries, data privacy (users see only their part), data independence, simpler access. Drawback: modifications through views are often impossible.

## Understanding — write your own answers ✍️

✍️ Names of students who attend all lectures — with double NOT EXISTS.
?
✍️ your query (paper) — then run it in HSQLDB and compare with [[2.SQL]] gold example 1

✍️ The same query with GROUP BY and HAVING count(*).
?
✍️ your query (paper) — then compare with [[2.SQL]] gold example 1

✍️ Ranking of professors by the average grade of their exams, only passed exams (grade < 5), ascending. (sheet 5, d+e)
?
✍️ your query (paper) — then run it

✍️ Names of all students who do NOT attend a lecture titled 'databases' (use a subquery). (sheet 5, g)
?
✍️ your query (paper) — then run it

✍️ Why does "x NOT IN (subquery)" return no rows at all if the subquery result contains a NULL?
?
✍️ your answer — then check the three-valued logic in [[2.SQL]]

✍️ T(A, B), A key, no NULLs. Q1: select B from T where B >= all (select B from T). Q3: select max(B) from T. Equivalent? If not, give an instance of T. (sheet 7, 2)
?
✍️ your answer — then check [[2.SQL]] gold example 3

✍️ All students "lecture-connected" to Smith (chain of shared lectures) with WITH RECURSIVE. (sheet 7, 1c)
?
✍️ your query (paper) — then run it
