---
course: Databases
source: "[[1.Relations]]"
---
#flashcards/db/1-relational

# DB-1 Relational Model, Relational Algebra, Tuple Calculus — Cards

> [!info] How to use
> Fill every ✍️ answer on paper first, then check in [[1.Relations|DB-1]] or the slides. The tuple-calculus cards fill the gap in your note (it stops before tuple calculus). Plan: [[00 DB Plan]]

## Introduction (lectures 1–2)

Three views (levels) of a database system?::External view: how users perceive the data. Conceptual/logical view: how the data is structured from the application's point of view. Internal/physical view: how the data is stored.

Logical data independence?::Changes in the logical view do not influence the external views — depends on the database design.

Physical data independence?::Changes in the internal (storage) view do not influence the logical view — realized in all modern DBMS.

The DBA changes the storage structure and all applications must be adapted. Which principle is violated?::Physical data independence.

Declarative vs. imperative query?::Declarative: the user says what data to fetch (e.g. SQL). Imperative: the user says how (open file, loop over records, check, output).

How does a DBMS recover after a crash?::It manages log files of all modifications and reconstructs the consistent state that existed before the crash (e.g. no half-done money transfer).

What is a lost update?::Two concurrent transactions read the same value and both write it back; one update is lost (100 + 10 and + 20 gives 110 or 120 instead of 130).

Integrity constraints: purpose and examples?::Rules the data must follow, checked by the DBMS to avoid errors by users and programs — e.g. salary is an integer, salary between 10,000 and 100,000, every department member is an employee.

Database user categories and their tasks?::End users (naive users via forms/apps; sophisticated users write ad hoc queries), application programmers (build applications), database administrator (schema, views, performance tuning of the internal schema, loading, security and reliability).

Data model vs. schema?::Data model: how data is described (e.g. relational model). Schema: concrete description of a particular collection of data using a data model.

Conceptual vs. logical data models (examples)?::Conceptual: ER model, UML. Logical: hierarchical, network, relational, object-oriented, object-relational, semi-structured.

## Basics

Relation: schema vs. instance?::Schema: relation name and attributes (with domains). Instance: the current set of tuples.

Tuple / attribute / domain / cardinality?::Tuple = row. Attribute = column. Domain = set of allowed values (type) of an attribute. Cardinality = number of tuples.

Formal definition of a relation?::A subset of the Cartesian product of the domains: R ⊆ D1 × D2 × … × Dn.

Key / candidate key / primary key?::Key: minimal set of attributes whose values identify a tuple uniquely. A relation can have several candidate keys; one is chosen as primary key.

Why can a relation contain no duplicates?::A relation is a set of tuples (the relational model is set-oriented).

DDL — what is it used for?::Data Definition Language: define the schema (create table) and integrity constraints.

## Relational algebra

Closure of the relational algebra?::Every operator takes relations as input and returns a relation, so operators can be nested freely.

Projection π?::Keeps only the listed attributes; duplicates are eliminated (set semantics).

Selection σ?::Keeps the tuples that fulfil predicate p (comparisons combined with and, or, not).

Cardinality of R1 × R2?::|R1| · |R2|.

Join in terms of basic operators?::A cross product followed by a selection: R1 ⋈θ R2 = σθ(R1 × R2).

θ-join vs. equi-join vs. natural join?::θ-join: arbitrary comparison predicate. Equi-join: only equality comparisons. Natural join: equality on all attributes with the same name; these appear only once in the result.

Why rename (ρ)?::To avoid name collisions between attributes, e.g. when joining a relation with itself.

Left outer join?::Result of the inner join plus the left tuples without a partner, padded with NULL.

Precondition for union, intersection, difference?::Both relations must have compatible schemas (same number of attributes with compatible domains).

What is relational division used for?::Queries with an "all" statement, e.g. students who attend all lectures.

Element-wise definition of R1 ÷ R2?::t is in the result iff for each v in R2 there is a u in R1 whose non-R2 part equals t and whose R2 part equals v.

Division expressed with basic operators (X = sch(R1) − sch(R2))?::R1 ÷ R2 = πX(R1) − πX((πX(R1) × R2) − R1).

Relational algebra vs. SQL semantics?::Relational algebra works on sets (no duplicates); SQL works on bags (duplicates possible, use DISTINCT).

## Tuple calculus (gap fill — not in your note)

General form of a tuple-calculus query?::{ t | P(t) } — t is a tuple variable, P a formula.

Atoms of the tuple calculus?::s ∈ R; s.A θ t.B; s.A θ c (θ is a comparison operator, c a constant).

Free vs. bound variable?::Bound: bound by a quantifier ∃ or ∀. Free: not bound — the result variable t must be free.

Replace ∀ by ∃?::∀t ∈ R (P(t)) ≡ ¬∃t ∈ R (¬P(t)).

Replace an implication?::P ⇒ Q ≡ ¬P ∨ Q.

De Morgan in formulas?::¬(P ∧ Q) ≡ ¬P ∨ ¬Q and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q.

What is a safe expression? Unsafe example?::The result must be a subset of the domain of the formula (constants in the formula + attribute values of the relations used) → finite. Unsafe: { n | ¬(n ∈ Professor) }.

Power of expression of the three languages?::Relational algebra, safe tuple calculus and safe domain calculus have the same power (domain calculus is not part of this course).

All professors in room 201 (tuple calculus)?::{ p | p ∈ Professor ∧ p.RoomNr = 201 }

## Understanding — write your own answers ✍️

✍️ MatrNr of students who attend all lectures — relational algebra. (sheet 4, 1d)
?
✍️ your answer — then check with the division formula above and the solution of sheet 4

✍️ Names of students who attend all lectures — tuple calculus. (sheet 5, 1c)
?
✍️ your answer — then check: ∀l ∈ Lecture ∃a ∈ attends (…)

✍️ Names that belong both to a professor and to a student, as a one-attribute relation — relational algebra. (sheet 4, 1c)
?
✍️ your answer — then check sheet 4 solution (rename + intersection)

✍️ Students who attend at least one lecture of Prof. Schmitt — tuple calculus.
?
✍️ your answer — then check the slide example in the Relational Model slides

✍️ Why must the projection in relational algebra remove duplicates, but SQL's SELECT does not? What do you write in SQL?
?
✍️ your answer — then check [[1.Relations|DB-1]] §4.1
