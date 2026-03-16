## 1. Conceptual Section (Teach Mode)

### A. Permission Logic (Octal Notation)
Linux uses a 3-bit system for three entities: **User (u)**, **Group (g)**, and **Others (o)**.

> [!Property] **Bit Values**
> - Read ($r$) = 4
> - Write ($w$) = 2
> - Execute ($x$) = 1
> Total permission $P = \sum(bits)$.

> [!Definition] **Special Permissions**
> - **SUID (Set User ID):** Represented by octal `4000`. When executed, the process runs with the privileges of the file owner (often root).
> - **SGID (Set Group ID):** Octal `2000`. Runs with group privileges.

### B. SSH Port Forwarding
Red Teamers use SSH to bypass firewalls through "tunnels."

> [!Note] **Tunnel Types**
> 1. **Local Forwarding (`-L`):** `L_port:remote_host:R_port`. Access a remote service as if it were local.
> 2. **Dynamic Forwarding (`-D`):** Creates a SOCKS proxy.

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Permission Calculation
*(Using: Octal Summation)*
**Question:** Set a file so the owner can read/write/execute, the group can read/execute, and others have no access. Provide the command and octal code.
**Solution:**
1. Owner: $4+2+1 = 7$.
2. Group: $4+0+1 = 5$.
3. Others: $0+0+0 = 0$.
4. Command: `chmod 750 filename`.

#### Example 2: Log Analysis with Pipes
*(Using: Text Manipulation)*
**Question:** Write a one-liner to find the top 5 IP addresses that failed to log in via SSH from the file `/var/log/auth.log`.
**Solution:**
`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -n 5`
*Explanation:* `grep` filters, `awk` extracts the IP field, `sort/uniq` counts occurrences.

---

## 3. Summary Section
- **chmod:** 777 is "all access," 600 is "owner read/write only."
- **SUID:** Look for `-rws------`. If owned by root, it's a target for privilege escalation.
- **Environment:** Use `export PATH=$PATH:/new/path` to modify binary search locations.