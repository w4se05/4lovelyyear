## 1. Conceptual Section (Teach Mode)

### 1.1 The Concept of Personal Data

> [!Definition] 👤 Personal Data
> "Personal data" refers to any kind of information **relating to** an **identified** or **identifiable natural person** .

#### Identified vs. Identifiable
The distinction lies in the immediate capability to recognize the individual.

* **Identified Person:** An individual who is distinguishable from all other persons and recognizable as an individual based on the data provided .
* **Identifiable Person:** A person who has not yet been identified but can be, directly or indirectly.
    * **Determinants:** One must take into account **all reasonable means** likely to be used to identify the individual, such as "singling out" a person to treat them differently .

> [!Note] 📋 Non-Exhaustive List of Identifiers
> * **Direct Identifiers:** Name, Identification number (SSN) .
> * **Location Data:** Home address.
> * **Online Identifiers:** Email address, screen names, IP address, device IDs.
> * **Biological Data:** Genetic samples, biometric data (fingerprints, facial recognition).

#### The Meaning of "Relates To"
Information is only personal data if it "relates to" the individual. This is determined by three factors :
1.  **Content:** Is the data directly about the individual or their activities?
2.  **Purpose:** Is the data processed to evaluate or influence the individual?
3.  **Result/Effect:** Does the processing have a result or effect on the individual?

---

### 1.2 Data Processing Concepts

#### Forms of Storage
Personal data encompasses various formats, including:
* Written or spoken communications.
* Images and CCTV footage/sound.
* Electronically recorded info and paper records.
* Biological samples (DNA) recording inherited/acquired characteristics .

#### Anonymization vs. Pseudonymization
This is a critical distinction in GDPR compliance regarding whether data protection laws apply.


| Feature | **Anonymization** | **Pseudonymization** |
| :--- | :--- | :--- |
| **Definition** | Process of removing private info so the data subject is **no longer identifiable** . | Process of replacing identifiers with a key/code (reversible). |
| **Reversibility** | **Irreversible**. It is impossible to re-identify the person. | **Reversible**. Data can be re-identified using the key. |
| **Legal Status** | **Not Personal Data**. GDPR does not apply. | **Is Personal Data**. GDPR applies . |
| **Use Case** | Storing data after it is no longer needed for the initial purpose . | Security measure to protect data while retaining utility. |

> [!Warning] Re-identification Risk
> If a data subject provides additional info (e.g., to exercise rights like rectification) that allows an "anonymized" dataset to be linked back to them, the data becomes **personal data** again .

---

### 1.3 Authentication

> [!Definition] 🔐 Authentication
> A procedure by which a person proves they possess a certain identity or are authorized to perform specific acts (e.g., entering a secure area, withdrawing money) .

**Methods of Authentication:**
1.  **Biometric Comparison:** Comparing a live person to stored data (photo, fingerprint) .
2.  **Knowledge-Based:** Information known only to the user (PIN, password).
3.  **Token-Based:** Possession of a physical object (chip card, key).
4.  **Electronic Signatures:** Often combined with PINs for electronic communications .

---

### 1.4 Special Categories of Data (Sensitive Data)

Certain data types are considered more sensitive because their processing can cause harm or embarrassment.

#### Article 9: Special Categories
The GDPR places stricter limits on processing data revealing:
* Racial or ethnic origin.
* Political opinions, religious, or philosophical beliefs .
* Trade union membership.
* Genetic data and biometric data (when used for ID).
* Health data, sexual life, or sexual orientation.

#### Article 10: Criminal Convictions
Data relating to criminal convictions and offences is **not** under Article 9 but has its own regulation .
* **Requirement:** Must be processed under the control of **official authority** or authorized by specific laws providing appropriate safeguards .

#### Exclusions (What is NOT Personal Data)
1.  **Truly Anonymized Data:**.
2.  **Deceased Persons:** Information about the dead is generally not subject to GDPR.
3.  **Legal Entities:** Information about companies or public authorities (unless it relates to an identified natural person within them).

---

## 2. 📘 Examples & Applications (Exam Mode)

### Example 1: Identified vs. Identifiable
> **Using:** Concept of Personal Data & Identifiers 
>
> **Scenario:** A database contains the following entries:
> 1.  `User_A: "John Smith, 123 Main St, London"`
> 2.  `User_B: "Cookie_ID: 889528127905"`
>
> **Analysis:**
> * **User_A:** This is an **Identified Person**. The name combined with an address distinguishes John Smith from others immediately .
> * **User_B:** This relates to an **Identifiable Person**. While the name is not present, the `Cookie_ID` is an "online identifier". By using "reasonable means" (e.g., cross-referencing with server logs), the controller can likely single out or identify the natural person behind the device .
>
> **Conclusion:** Both entries constitute Personal Data under GDPR.

### Example 2: Pseudonymization vs. Anonymization
> **Using:** Anonymization/Pseudonymization Distinctions 
>
> **Scenario:** A hospital is sharing patient data for research.
> * **Method A:** They replace names with a code (e.g., Patient #101) and keep a spreadsheet in a secure safe linking #101 to "Alice".
> * **Method B:** They delete all names, dates of birth, and addresses, and aggregate age into 10-year ranges (e.g., "Age 30-40"), making it statistically impossible to pinpoint any specific individual.
>
> **Analysis:**
> * **Method A (Pseudonymization):** The process is reversible using the "key" (the spreadsheet). The data enables re-identification. Therefore, **GDPR applies**.
> * **Method B (Anonymization):** Private info is removed, and re-identification is no longer possible . The data no longer serves the initial purpose of identifying patients. Therefore, **GDPR does NOT apply**.

### Example 3: Handling Sensitive Business Data
> **Using:** Sensitive Data vs. Personal Data 
>
> **Scenario:** A hacker steals a file containing "Project X Acquisition Plans" and "Financial Reports of TechCorp Inc."
>
> **Analysis:**
> * This data includes trade secrets and financial data which poses a risk to the company.
> * However, does this trigger GDPR "Personal Data" rules? **No.**
> * **Reasoning:** Personal data must relate to a *natural person*. Information purely about companies (legal entities), such as financial reports or acquisition plans, is excluded from the definition of personal data.

---

## 3. Summary

* **Core Definition:** Personal Data is any info relating to an identified or identifiable natural person (living individual).
* **Identifiability:** Includes direct IDs (Name, SSN) and indirect IDs (IP address, Cookies, device IDs). If you can "single out" the person, it's personal data.
* **Anonymization vs. Pseudonymization:**
    * **Anonymized** = Irreversible = Not Personal Data (GDPR Free).
    * **Pseudonymized** = Reversible (Key exists) = Personal Data (GDPR Applies).
* **Sensitive Data (Art. 9):** Higher protection for Race, Religion, Politics, Health, Biometrics, etc.
* **Criminal Data (Art. 10):** Restricted to official authority processing.
* **Non-Personal Data:** Deceased persons, corporate/company data, and truly anonymized data.