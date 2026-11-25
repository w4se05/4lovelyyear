## 1. Conceptual Section (Teach Mode)

### 1.1 What is a DPIA?

> [!Definition] 🛡️ Data Protection Impact Assessment (DPIA)
> A DPIA is a systematic process designed to describe the processing, assess its necessity and proportionality, and assist in managing the risks to the rights and freedoms of natural persons resulting from the processing of personal data .

**Legal Basis:**
* **Article 35 GDPR:** Mandates DPIAs for high-risk processing.
* **Purpose:** Implements the principles of **Accountability** (Art. 5(2)) and **Privacy by Design** (Art. 25).
* **Outcome:** It helps organizations implement measures to mitigate identified risks and demonstrate compliance .

---

### 1.2 When is a DPIA Required? (Screening)

A DPIA is mandatory when processing is likely to result in a **high risk** to the rights and freedoms of natural persons.

**Mandatory Scenarios (Art. 35(3)):** 
1.  **Systematic Evaluation & Profiling:** Automated processing with legal or significant effects (e.g., loan rejection).
2.  **Large-Scale Special Categories:** Processing sensitive data (Art. 9) or criminal conviction data (Art. 10) on a large scale.
3.  **Systematic Public Monitoring:** Large-scale monitoring of public areas (e.g., CCTV).

**EDPB Criteria (The "Rule of Two"):** 
The European Data Protection Board (EDPB) lists 9 criteria. Generally, if a processing operation meets **two or more**, a DPIA is required.

1.  **Evaluation/Scoring:** Credit scoring, health risk assessments.
2.  **Automated Decision-Making:** e.g., e-recruiting without human intervention.
3.  **Systematic Monitoring:** Workplace monitoring, internet surveillance.
4.  **Sensitive Data:** Medical records, political views.
5.  **Large-Scale Processing:** Considering volume, duration, and geography.
6.  **Matching/Combining Datasets:** Merging data from sources in unexpected ways.
7.  **Vulnerable Data Subjects:** Children, employees, patients, asylum seekers.
8.  **Innovative Technology:** AI, facial recognition, IoT.
9.  **Prevents Exercise of Rights:** Screening against fraud databases before providing service.

---

### 1.3 The 8-Step DPIA Methodology

> [!Process] ⚙️ The Cycle of Assessment
> The DPIA is not a one-time box-ticking exercise but a continuous process .

#### Step 1: Screening
Determine if a DPIA is required based on the criteria above (National lists, Art. 35(3), EDPB criteria) .

#### Step 2: Description
Systematically describe the processing operation:
* **Nature:** How data is collected/stored.
* **Scope:** Volume and variety of data.
* **Context:** Relationship with subjects and their expectations.
* **Purpose:** The specific reason for processing.
* **Data Flows:** Visual representation of data movement.

#### Step 3: Necessity & Proportionality
Assess adherence to fundamental principles:
* **Purpose Limitation:** Is the purpose specific and legitimate?
* **Data Minimization:** Is only essential data collected?
* **Storage Limitation:** Is the retention period justified?

#### Step 4: Risk Identification
Identify risks to data subjects (not just the organization) .
* **Physical Harm:** Bodily harm (e.g., from data breaches leading to stalking).
* **Material Harm:** Financial loss, fraud, denial of service.
* **Non-Material Harm:** Distress, reputational damage, loss of confidentiality.
* **Risk Events:** Unauthorized access, modification, loss, or function creep .

#### Step 5: Mitigation Measures
Propose measures to address the risks :
* **Technical:** Encryption, pseudonymization, access controls.
* **Organizational:** Policies, staff training, incident response plans.
* **Legal:** Data processing agreements (Art. 28).
* **Physical:** Secure facilities, hardware disposal.

#### Step 6: Consultation
* **DPO:** Mandatory advice (if designated).
* **Stakeholders:** IT/Security teams.
* **Data Subjects:** Seek views where appropriate.
* **Supervisory Authority (Art. 36):** **Prior Consultation** is required if high risks *cannot* be mitigated .

#### Step 7: Documentation
Record all findings, rationale, and the final decision. This is crucial for accountability.

#### Step 8: Review
Monitor and review the DPIA, especially when there are changes in operations or risks .

---

## 2. 📘 Examples & Applications (Exam Mode)

### Example 1: Assessing the Need for a DPIA
> **Using:** EDPB Criteria (Rule of Two) 
>
> **Scenario:** A hospital plans to implement a new AI system (Innovative Tech) to analyze patient genetic data (Sensitive Data/Vulnerable Subjects) to predict hereditary diseases.
>
> **Analysis:**
> 1.  **Criterion 1:** Sensitive Data (Health/Genetic data).
> 2.  **Criterion 2:** Vulnerable Subjects (Patients).
> 3.  **Criterion 3:** Innovative Use (AI prediction).
>
> **Conclusion:** The project meets at least 3 criteria. A **DPIA is mandatory**.

### Example 2: Risk Mitigation Strategy
> **Using:** Step 5 Mitigation Measures 
>
> **Scenario:** An HR department stores employee performance reviews (High Risk: Vulnerable subjects/Evaluation).
> **Risk identified:** Unauthorized access by other employees could lead to reputational damage (Non-material harm) or discrimination.
>
> **Solution:**
> * **Technical:** Implement strict **Access Control Lists (ACLs)** so only Line Managers can view specific records. Use **Encryption at rest** for the database.
> * **Organizational:** Conduct **Staff Training** on confidentiality and enforce a **Clean Desk Policy**.

### Example 3: Prior Consultation (Art. 36)
> **Using:** Step 6 Consultation 
>
> **Scenario:** A company conducts a DPIA for a facial recognition system in a public mall.
> * **Result:** Even with encryption and signage, the residual risk to passersby remains "High" due to the inability to capture valid consent from everyone.
>
> **Action:** Since the high risk cannot be sufficiently mitigated, the company **must consult the Supervisory Authority** (Article 36) *before* starting the processing.

---

## 3. Summary

* **Definition:** DPIA is a risk assessment tool for rights and freedoms, required by Art. 35 GDPR.
* **Triggers:** Required for "High Risk" scenarios, specifically: Systematic Profiling, Large-Scale Sensitive Data, and Public Monitoring.
* **EDPB Guidelines:** Use the "2 out of 9" criteria rule to decide if a DPIA is needed.
* **Methodology:** Follow the 8 steps: Screening $\rightarrow$ Description $\rightarrow$ Necessity $\rightarrow$ Risk $\rightarrow$ Mitigation $\rightarrow$ Consultation $\rightarrow$ Documentation $\rightarrow$ Review.
* **Accountability:** If you can't mitigate high risks, you must ask the Regulator (Prior Consultation).