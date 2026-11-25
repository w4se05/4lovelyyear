## 1. Conceptual Section (Teach Mode)

### 1.1 Overview of GDPR Principles

> [!Definition] 📜 Article 5 Principles
> Article 5 of the GDPR establishes seven key principles that form the foundation of the data protection regime. Infringements of these principles are subject to the highest tier of fines (up to €20 million or 4% of global turnover).

**The 7 Principles:** 
1.  **Lawfulness, Fairness, and Transparency**
2.  **Purpose Limitation**
3.  **Data Minimization**
4.  **Accuracy**
5.  **Storage Limitation**
6.  **Integrity and Confidentiality (Security)**
7.  **Accountability**

---

### 1.2 Principle 1: Lawfulness, Fairness, and Transparency

> [!Property] ⚖️ Lawfulness
> Data must be processed based on one of the **6 specific grounds** (lawful bases) defined in Article 6. At least one must be met:
> 1.  **Consent:** Clear, affirmative action for a specific purpose.
> 2.  **Contract:** Necessary for the performance of a contract (e.g., shipping goods bought online) .
> 3.  **Legal Obligation:** Compliance with a law (e.g., keeping tax records).
> 4.  **Vital Interests:** Protecting life in emergencies (e.g., unconscious patient data) .
> 5.  **Public Task:** Exercising official authority or public interest tasks (e.g., vehicle registration).
> 6.  **Legitimate Interests:** Necessary for the controller's interest, unless overridden by individual rights (e.g., CCTV for safety).

**Requirements for Valid Consent:** 
* **Freely Given:** Voluntary, no pressure/influence .
* **Specific:** Clear about identity, data types, and purpose. Blanket consent (e.g., "for partners") is invalid .
* **Informed:** User knows their rights, including the right to withdraw .
* **Unambiguous:** Requires affirmative action (Opt-in). Pre-ticked boxes or silence are **not** consent .

> [!Property] 🎭 Fairness
> Processing must align with **Reasonable Expectations** and not cause unjustified adverse effects.
> * **Fair:** A delivery app tracking location for delivery.
> * **Unfair:** A flashlight app selling contact lists to marketers (unexpected).

> [!Property] 🔍 Transparency
> Controllers must be open and honest about who they are and how they use data.
> * Information must be easily accessible and understandable.
> * Data subjects must be informed of risks (e.g., re-identification risks in research).

---

### 1.3 Principle 2: Purpose Limitation

> [!Definition] 🎯 Purpose Limitation
> Data must be collected for **specified, explicit, and legitimate purposes** and **not further processed** in a manner incompatible with those purposes .

**Compatibility Assessment:** 
New purposes are only allowed if they are "compatible" with the original one. Factors include:
* Link between original and new purpose.
* Context and reasonable expectations.
* Nature of data (sensitive?).
* Existence of safeguards (encryption/pseudonymization).

*Note: Research, statistical, and archiving purposes are generally considered compatible*.

---

### 1.4 Principle 3: Data Minimization

> [!Definition] 🤏 Data Minimization
> Personal data must be **adequate, relevant, and limited** to what is necessary for the purposes .

* **Adequate:** Sufficient to fulfill the purpose.
* **Relevant:** clearly linked to the purpose.
* **Limited:** No more than you need. Do not collect data "just in case" for the future.

---

### 1.5 Principle 4: Accuracy

> [!Definition] ✅ Accuracy
> Data must be accurate and, where necessary, kept up to date. Inaccurate data must be erased or rectified without delay.

* **Historical Data:** Updates to historical records (e.g., medical operation notes) are often prohibited to preserve the record's integrity, though additions/remarks can be made .
* **Impact:** Inaccurate data (e.g., in credit databases) can cause harm, so regular checks are vital .

---

### 1.6 Principle 5: Storage Limitation

> [!Definition] ⏳ Storage Limitation
> Data must be kept **no longer than necessary** for the purpose.

* **Exceptions:** Longer storage is permitted for archiving in the public interest, scientific/historical research, or statistical purposes (with safeguards).
* **Retention:** Organizations must define retention periods based on necessity.

---

### 1.7 Principle 6: Integrity and Confidentiality (Security)

> [!Definition] 🔒 Security
> Data must be processed ensuring appropriate security, including protection against unauthorized processing, accidental loss, destruction, or damage.

* **Measures:** Includes cybersecurity (system/network security) and physical/organizational measures .
* **Techniques:** Pseudonymization and Encryption are recommended depending on risk.
* **Harms to Avoid:** Identity fraud, financial loss, witness intimidation, distress .

---

### 1.8 Principle 7: Accountability

> [!Definition] 🧾 Accountability
> The controller is responsible for complying with the principles and must be **able to demonstrate compliance**.

* **Requirement:** Actively implement risk-based technical and organizational measures.
* **Demonstration:** Must prove compliance to authorities and the public at any time.

---

## 2. 📘 Examples & Applications (Exam Mode)

### Example 1: Consent Validity
> **Using:** Lawfulness (Consent) 
>
> **Scenario:** An online store has a checkout box that is pre-ticked saying "I agree to share my data with partners."
>
> **Analysis:**
> 1.  **Specific?** No. "Partners" is vague; the user doesn't know who receives the data.
> 2.  **Unambiguous?** No. Pre-ticked boxes constitute inactivity/silence, not a clear affirmative act (Opt-in).
>
> **Conclusion:** The consent is **invalid**. The processing is unlawful.

### Example 2: Purpose Limitation & Compatibility
> **Using:** Purpose Limitation 
>
> **Scenario:** A doctor (GP) collects patient data for medical treatment. He shares this list with his wife, a travel agent, to offer "recuperation holiday deals" to patients.
>
> **Analysis:**
> * **Original Purpose:** Medical diagnosis and treatment.
> * **New Purpose:** Commercial marketing of travel services.
> * **Compatibility:** Is there a link? No. Would patients reasonably expect this? No.
>
> **Conclusion:** The new purpose is **incompatible**. The disclosure is a breach of the purpose limitation principle.

### Example 3: Data Minimization vs. Security
> **Using:** Minimization & Security 
>
> **Scenario:** A town council issues travel cards.
> * **System A:** The card stores the user's name on a chip. When scanned on a bus, the reader checks a central database of all users to verify validity. The system logs who traveled where and when.
> * **System B:** The card stores a simple "validity code" or barcode. The reader just checks if the code is valid (Green light). No central database lookup or movement tracking is recorded.
>
> **Analysis:**
> * **System A:** Collects movement data (who/where/when). This is **excessive** if the only goal is to check "did they pay?".
> * **System B:** Achieves the purpose (validation) without collecting movement data.
>
> **Conclusion:** System B aligns with **Data Minimization**. System A violates it by collecting more than necessary.

### Example 4: Unlawful Processing (Unfairness)
> **Using:** Lawfulness (Unlawful Processing) 
>
> **Scenario:** A training company photocopies a copyrighted book, scans it, and emails it to 500 students using their personal email addresses.
>
> **Analysis:**
> * While they may have a contract with students, the processing involves an **infringement of copyright**.
> * Processing that results in a breach of other laws (like copyright or confidence) is considered unlawful under GDPR.
>
> **Conclusion:** The processing is **unlawful**.

---

## 3. Summary

* **Article 5 is King:** Adherence to the 7 principles is mandatory; failure leads to maximum fines.
* **Lawful Basis (Art 6):** You need one of six bases (Consent, Contract, Legal Obligation, Vital Interest, Public Task, Legitimate Interest) to process data legally.
* **Consent:** Must be specific, informed, and an active "Opt-in".
* **Purpose:** Stick to the original reason for collection. Don't repurpose data unexpectedly.
* **Minimization:** "Less is more." Only collect what you strictly need.
* **Accuracy:** Keep it correct.
* **Storage:** Delete it when you're done.
* **Security:** Protect it (Cybersecurity + Physical measures).
* **Accountability:** Don't just *do* it; be able to *prove* you did it.