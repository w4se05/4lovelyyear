## 1. Conceptual Section (Teach Mode)

### 1.1 Special Categories of Data (Article 9)

> [!Definition] 🧬 Special Categories of Personal Data
> "Special categories" refer to data types considered more sensitive than standard personal data. Processing this data can significantly impact an individual's fundamental rights and freedoms.
>
> **General Rule (Article 9(1)):** Processing of these categories is **prohibited** unless a specific exception applies .

#### The Exhaustive List (Sensitive Data)
The GDPR explicitly lists the following as special categories :
1.  **Racial or Ethnic Origin:** Ancestry, cultural background (e.g., student placement data).
2.  **Political Opinions:** Views, affiliations, voting intentions.
3.  **Religious or Philosophical Beliefs:** Faith, convictions, spiritual beliefs.
4.  **Trade Union Membership:** Indication of membership status.
5.  **Genetic Data:** Information on genetic makeup/inherited characteristics.
6.  **Biometric Data:** Data used to **uniquely identify** a person (fingerprints, facial recognition).
7.  **Health Data:** Physical or mental health status, medical records, diagnoses.
8.  **Sex Life or Sexual Orientation:** Sexual preferences, gender identity.

> [!Note] 🚫 Prohibition Principle
> You cannot just use a standard lawful basis (like "Contract" or "Legitimate Interest") for these. You need a **Lawful Basis (Art. 6)** AND a **Specific Exception (Art. 9)**.

---

### 1.2 Exceptions: When Can You Process? (Article 9(2))

To overcome the prohibition, one of the following exceptions must apply :

1.  **Explicit Consent:** The data subject gives consent for a specified purpose. It must be voluntary and withdrawable.
2.  **Vital Interests:** Necessary to protect life when the subject is physically or legally incapable of giving consent (e.g., unconscious patient).
3.  **Legal Claims:** Necessary for the **establishment, exercise, or defense of legal claims** (e.g., suing for discrimination).
4.  **Substantial Public Interest:** Based on EU/Member State law with safeguards (e.g., equality monitoring).
5.  **Public Health:** Cross-border threats, high standards of quality and safety.
6.  **Archiving, Research, & Statistics:** For scientific/historical purposes, provided data is anonymized or safeguarded.
7.  **Employment/Social Security Law:** Necessary to comply with labor laws (e.g., trade union dues deduction).

---

### 1.3 Criminal Convictions & Offences (Article 10)

> [!Warning] 👮‍♂️ Article 10 Data
> Data relating to criminal convictions and offences is **NOT** a "Special Category" under Article 9, but it is highly regulated under **Article 10**.

**Rules for Processing:** 
1.  **Official Authority:** Processing must be under the control of official authority (Police, Courts).
2.  **Authorized by Law:** Or authorized by Union/Member State law providing appropriate safeguards.
3.  **Register Limits:** Comprehensive registers of criminal convictions can *only* be kept by official authorities.
    * *implication:* Private companies cannot maintain their own "blacklists" of criminals.

**Permitted Purposes:** 
* Criminal justice (prevention/investigation).
* Public security (terrorism prevention).
* Employment background checks (if authorized by law for vulnerable groups).

---

### 1.4 Additional Safeguards

Processing sensitive data requires higher security standards :
* **Data Encryption:** Scrambling data so only key-holders can read it.
* **Pseudonymization:** Replacing identifiers with codes.
* **Access Controls:** Restricting who can view data (e.g., only medical staff).
* **DPIA (Data Protection Impact Assessment):** Mandatory for high-risk processing.

---

## 2. 📘 Examples & Applications (Exam Mode)

### Example 1: Genetic Research & Consent
> **Using:** Genetic Data (Art 9) & Explicit Consent 
>
> **Scenario:** A research institute wants to study genetic predisposition to Alzheimer's. They collect DNA samples from volunteers.
>
> **Analysis:**
> 1.  **Identify Data Type:** DNA samples constitute **Genetic Data**, which is a Special Category (Art 9).
> 2.  **General Rule:** Processing is prohibited.
> 3.  **Exception Applied:** The institute obtains **Explicit Consent** from participants.
> 4.  **Safeguards:** They must explain risks/benefits and allow withdrawal of consent at any time.
>
> **Conclusion:** Processing is lawful because the "Explicit Consent" exception lifts the Article 9 prohibition.

### Example 2: Emergency Treatment (Vital Interests)
> **Using:** Health Data (Art 9) & Vital Interests 
>
> **Scenario:** A patient arrives at the ER unconscious and bleeding. The hospital accesses their electronic health record to check for blood type and allergies.
>
> **Analysis:**
> 1.  **Identify Data Type:** Medical history is **Health Data** (Special Category).
> 2.  **Consent Status:** The patient is unconscious and **incapable** of giving consent.
> 3.  **Exception Applied:** Processing is necessary to protect the **Vital Interests** (life) of the data subject.
>
> **Conclusion:** The hospital can process the sensitive data without consent to save the patient's life.

### Example 3: Legal Defense
> **Using:** Trade Union Membership (Art 9) & Legal Claims 
>
> **Scenario:** A former employee sues a company for "anti-union discrimination." To defend itself in court, the company processes records showing the employee's trade union membership status.
>
> **Analysis:**
> 1.  **Identify Data Type:** **Trade Union Membership** is a Special Category.
> 2.  **Purpose:** The company needs this to prove they did *not* discriminate based on that status.
> 3.  **Exception Applied:** Processing is necessary for the **"establishment, exercise, or defense of legal claims."**
>
> **Conclusion:** The processing is permitted even without the employee's consent.

### Example 4: Employment Background Checks
> **Using:** Criminal Convictions (Art 10) 
>
> **Scenario:** A kindergarten hires a new teacher. They request a criminal record check to ensure the applicant has no history of child abuse.
>
> **Analysis:**
> 1.  **Identify Data Type:** This is **Criminal Conviction Data** (Art 10), not Art 9.
> 2.  **Requirement:** Must be authorized by law or official authority.
> 3.  **Justification:** Employment laws often mandate checks for those working with **vulnerable individuals** (children).
> 4.  **Constraint:** The school cannot keep this record forever; it must be deleted once the hiring decision is made/recorded (Data Minimization) .

---

## 3. Summary

* **Article 9 (Special Categories):** RACE, POLITICS, RELIGION, TRADE UNION, GENETICS, BIOMETRICS (for ID), HEALTH, SEXUAL ORIENTATION.
* **The Rule:** Processing is **banned** by default.
* **The Fix (Exceptions):** You need **Explicit Consent**, **Vital Interests** (life or death), **Legal Claims** (court cases), or **Substantial Public Interest** (statutory authority).
* **Article 10 (Criminal Data):** Separate from Art 9. Controlled by Official Authority (Police) or specific laws (e.g., background checks for teachers). Private "criminal registers" are illegal.
* **Safeguards:** Encryption, Pseudonymization, and strict Access Control are mandatory when handling these high-risk data types.
