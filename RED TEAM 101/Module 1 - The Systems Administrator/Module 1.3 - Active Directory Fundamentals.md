## 1. Conceptual Section (Teach Mode)

### A. Logical Structure
Active Directory (AD) is a database and set of services that connects users with the network resources they need.

> [!Definition] **Hierarchy**
> 1. **Objects:** The smallest unit (User, Computer, Printer).
> 2. **Organizational Units (OU):** Containers used to organize objects.
> 3. **Domains:** A security boundary sharing a central database.
> 4. **Forests:** The top-level container for one or more domains.

### B. Authentication Protocols
AD primarily uses **Kerberos** for authentication.

> [!Property] **The Kerberos Ticket Process**
> 1. **AS-REQ:** User requests Authentication.
> 2. **AS-REP:** Key Distribution Center (KDC) provides a Ticket Granting Ticket (TGT).
> 3. **TGS-REQ:** User presents TGT to request a service ticket.
> 4. **TGS-REP:** KDC provides service ticket (The "Gold" for attackers).

### C. Group Policy Objects (GPO)
GPOs are collections of settings that define what a system looks like and how it behaves for a defined group of users.

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Identifying Attack Surface
*(Using: Port Enumeration)*
**Question:** You run a scan on a Windows host and see ports 88, 389, and 445 open. What is the most likely role of this server?
**Solution:**
- **Port 88:** Kerberos.
- **Port 389:** LDAP.
- **Port 445:** SMB (Server Message Block).
**Conclusion:** This is a **Domain Controller**.

#### Example 2: AD Querying
*(Using: PowerShell Cmdlets)*
**Question:** Provide the PowerShell command to list all users in the "Domain Admins" group.
**Solution:**
`Get-ADGroupMember -Identity "Domain Admins"`

---

## 3. Summary Section
- **DC:** The heart of AD; holds the `NTDS.dit` database (contains all password hashes).
- **GPO:** Applied in order: Local $\rightarrow$ Site $\rightarrow$ Domain $\rightarrow$ OU.
- **Workgroups vs. Domains:** Workgroups are decentralized; Domains are centralized via the DC.