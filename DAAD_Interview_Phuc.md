# DAAD Interview — Hồng Nguyên Phú
## April 20, 2026 · 15:40–15:50 · Zoom

> **10 minutes. Candidate 14 of 15. The committee is tired. Wake them up.**

---

## 🔴 LOGISTICS — DO THESE BEFORE APRIL 20

- [ ] Confirm attendance by replying to the email
- [ ] Zoom link for April 20: `https://zoom.us/j/98067146736`
- [ ] Join with **VGU email** and **full name: Hồng Nguyên Phúc** — not nickname
- [ ] Join **10 minutes early** — have the link saved on your phone as backup
- [ ] Camera at **eye level** — not looking up at you
- [ ] **Light in front of your face**, not behind
- [ ] Test microphone the night before
- [ ] Dress formally — shirt, formal trousers
- [ ] One physical **cheat sheet** on paper next to the screen (not on screen)

### Cheat sheet (print this, put it next to your camera):
```
OPENING: eliminate → red team → Layer 7 gap → FRA-UAS → Baun
RLS: policy evaluated BEFORE query returns → API cannot bypass it
PRESIGNED: HMAC signed capability token → TTL + scoped key → server never touches file
TCP: SYN → SYN-ACK → ACK
COSINE: cos θ = a·b / (||a|| × ||b||)   ← denominator is TWO separate magnitudes
BAUN: Computer Networks + OS + Cloud · Rechnernetzelabor · Honeypot · ossperf · Virtual Network Lab
DE-CIX: largest internet exchange in the world · 10+ Tbps peak · Frankfurt
```

---

## 🎯 SCORING FORMULA — YOUR ACTUAL COMPETITION

| Component | Weight | Your Position |
|-----------|--------|---------------|
| GPA | 50% | **Strong — 1.7 German scale** |
| Motivation | 20% of interview = 10% total | **Strong — if you tell YOUR story** |
| English | 15% of interview = 7.5% total | Risk — 5.5 speaking, override with live performance |
| German | 15% of interview = 7.5% total | Potential — strong grades, prepare 3 sentences |

**25 scholarships. 29 shortlisted. You need to beat ~4 people.**

---

## 🗣️ THE OPENING — 60 SECONDS MAXIMUM

This is the most important moment. The committee has heard 13 identical answers. Start differently.

**The structure:**
1. The elimination (I tried everything, crossed it out)
2. Why security, specifically red team (attacker instinct, not strategy)
3. The gap (Layer 7 ceiling)
4. Why FRA-UAS, specifically (Baun's lab, not just "good curriculum")

**Your logic in plain language:**
> "First of all, thank you for having me. My name is [Your Name], and I am currently [your current degree/job, e.g., a second-year computer science student].

Over the past year, I actually spent time trying every domain—full-stack, AI, cloud, mobile. I crossed each one out. What remained was security. Not because it sounded impressive, but because the offensive mindset feels more natural to me. I look for the hole, not the patch—because you cannot defend what you don't know how to break.
The problem I'm facing now is that I have only ever operated above Layer 7. I can build systems, but I cannot yet see what is beneath them. Professor Baun's work on computer networks and operating systems here at FRA-UAS targets that exact foundational layer. That is why I am applying for this scholarship today."

**Do NOT memorize those words. Own the structure. Say it in your voice.**

---

## ❓ INTERVIEW QUESTIONS + YOUR ANSWERS

### Q1: "Tell me about yourself and why you are applying."
→ Use the opening structure above. 60 seconds. End with FRA-UAS.

---

### Q2: "Why are you the right candidate? Why should we choose you?"
Three claims, no stories:
1. GPA reflects genuine CS engagement — 1.0 in Intro to CS, 1.3 in Programming 1
2. I built a production system with real users — vgushare.org, 140+ monthly downloads
3. I know exactly what I am missing and exactly which courses fill that gap

---

### Q3: "What do you know about FRA-UAS / Frankfurt?"

**The Dr. Baun card — deploy here:**
> "When I researched FRA-UAS, I did not just look at the curriculum. I looked at who teaches it. Professor Baun's three research areas are computer networks, distributed systems, and operating systems — exactly the layers beneath everything I have built. He runs the Computer Networks Laboratory. He supervised a student project building a honeypot — that is offensive security applied to real hardware. He built a virtual network platform specifically for teaching complex IT structures including IT Security courses. I build systems at the application layer. He works at the layer beneath them. That alignment is why FRA-UAS is the right place for me specifically."

**DE-CIX line:**
> "Frankfurt is also home to DE-CIX — the largest internet exchange point in the world by throughput, handling over 10 terabits per second. For someone studying network security, that is not symbolic proximity. That is literal proximity to the infrastructure I want to understand."

---

### Q4: "Which courses will you take?"
Name specific courses. Research these on frankfurt-university.de before April 20:
- Computer Networks 1 (Prof. Dr. Christian Baun)
- Operating Systems (Prof. Dr. Christian Baun)
- Databases
- OOP w Java
- Statistic
- Software Engineering

Say: *"I have already identified the specific modules. The Computer Networks and Operating Systems courses taught by Professor Baun are the primary reason I chose FRA-UAS over other partner universities."*

---

### Q5: "What are your plans after graduation?"
> "I want to work in cloud and infrastructure security — penetration testing and red team work. Frankfurt's concentration of financial institutions and cloud infrastructure is the environment I want to enter. The knowledge I build at FRA-UAS I bring back to Vietnam. That is the point of this scholarship."

**Do NOT say you want to stay in Germany.**

---

### Q6: "What do you know about your projects?" / Technical questions

**The AST debugging story — your strongest owned technical moment:**
> "When integrating the markdown renderer into vgushare.org, I trusted the abstraction. I let an AI assistant configure it. The build failed. I gave the error back to the AI — it made things worse. That was the moment I stopped trusting the abstraction and went one level down. I read the Turbopack build trace directly. The problem was not a library bug — it was a version conflict between Tailwind v4 and React-Markdown at the compiler layer. The AI was reasoning about the API layer. The real problem was lower. Going to the correct layer fixed it in ten minutes."

**RLS — what you actually know:**
> "Documents enter the system with is_active = false. Postgres Row Level Security evaluates a policy before the query result is returned — which means the API never receives the inactive rows. It is impossible to bypass at the API layer because the database itself filters them out first."

**Presigned URLs — what you can honestly claim:**
> "The architecture routes file uploads through Cloudflare Workers instead of the Next.js server. The Worker generates a time-limited, cryptographically signed URL scoped to a specific object key and content type. The file goes directly from the user to R2 storage — the server never handles the payload. I implemented this from a team specification and came to understand why it matters: it eliminates server-side attack surfaces entirely."

**Cosine similarity — you own this:**
> "Each text is vectorized based on context from training. Cosine similarity measures the angle between two vectors using cos θ = a·b divided by the product of their individual magnitudes. The denominator normalizes for document length — so a 10-word query and a 10,000-word document can still match on meaning. In our RAG pipeline, casual student queries like 'exam notes' pointed in a different direction in vector space than formal document titles like 'Assessment Materials.' The fix was a translation layer before the vector search."

---

### Q7: "What are your extracurricular activities?"
> "I am Vice President of the Redner-VGU Debate Club. I manage 30+ members, design the sessions, and facilitate structured arguments in English under time pressure every week. I also served as an IT intern at VGU's IT department for 6 months — I built and maintained the internal wiki platform. I compete in basketball and volleyball."

**This covers your entire social skills score. Do not rush through it.**

---

### Q8: German language switch — it will happen

**Self-introduction in German (memorize this):**
> "Ich heiße Hồng Nguyên Phúc. Ich studiere Informatik an der Vietnamesisch-Deutschen Universität im zweiten Jahr. Mein Notendurchschnitt ist 1,7. Ich interessiere mich besonders für Cloud-Sicherheit und Penetrationstests. In meiner Freizeit bin ich Vizepräsident des Debattierclubs an der VGU."

**Why Frankfurt in German (memorize this one sentence):**
> "Frankfurt ist der Sitz von DE-CIX, dem größten Internetknoten der Welt. Für mein Ziel in der Netzwerksicherheit ist das sehr relevant."

**Survival phrase if you do not understand:**
> "Könnten Sie die Frage bitte wiederholen?" *(Could you repeat the question please?)*

**If you must switch back to English:**
> "Entschuldigung, ich antworte auf Englisch, weil mein Deutsch noch nicht ausreicht."

---

## 🧠 PSYCHOLOGY — THE 3-STEP FREEZE PROTOCOL

When your mind goes blank — execute in order:

**Step 1:** Exhale. Nod once. Say: *"Let me think about that precisely."* (buys 3 seconds)

**Step 2 — Acknowledge-Anchor-Bridge:**
> "I haven't worked with that at implementation depth. What I understand at the principle level is [X]. The specific mechanics are exactly why I am applying to FRA-UAS's [course name]."

**Step 3 — Identity anchor (say this inside, not out loud):**
> "I built a production system that serves real users. I found a real bug by reading a build trace. I know what I do not know and I know where to learn it."

**Rule:** Never say "I don't know" and stop. Always bridge. Always redirect to FRA-UAS.

---

## 📚 CONCEPTS — WHAT YOU ACTUALLY OWN

### Cosine Similarity ✅ OWNED
- Words vectorized by context in training data
- `cos θ = a·b / (||a|| × ||b||)` — denominator is TWO separate magnitudes
- Measures angle (direction), not magnitude (length)
- Vocabulary gap: "cheat" and "academic misconduct" point in different vector directions
- Fix: query reconciliation layer translates slang → formal terms before search
- Euclidean distance measures distance; cosine measures direction — direction = meaning

### RLS (Row Level Security) ✅ OWNED
- Postgres policy evaluated **before** query result is returned
- `is_active = false` rows are invisible to any public API query
- Cannot be bypassed at the API layer — database filters first
- SQL: `CREATE POLICY "public sees active only" ON documents FOR SELECT USING (is_active = true);`

### Presigned URLs ⚠️ PARTIAL — BE HONEST
- HMAC-signed capability token with TTL and scoped object key
- Server never handles file payload → eliminates DoS and payload injection vectors
- Blast radius of leaked URL: bounded by TTL + scope + downstream RLS
- You **implemented** from a spec — say that honestly if pushed

### TCP Handshake ✅ OWNED (from your study)
- SYN → SYN-ACK → ACK
- Connection established before any data flows
- Port + IP = socket
- TLS encrypts everything above the TCP layer

### OSI Model ✅ KNOW YOUR LAYERS
- Layer 7 (Application): HTTP, your APIs, SQL injection
- Layer 4 (Transport): TCP, SYN flood attacks
- Layer 3 (Network): IP, IP spoofing
- Layer 2 (Data Link): ARP spoofing
- **Your entire career so far: Layer 7. Your gap: Layers 1-6.**

### AST Debugging ✅ FULLY OWNED
- Tailwind v4 changed how it processed component props at build level
- React-Markdown was passing className in a way the new version rejected
- AI reasoned at API layer → wrong answer
- You read Turbopack build trace → found compiler layer conflict
- Fixed by restructuring component wrappers

---

## 👨‍🏫 DR. CHRISTIAN BAUN — YOUR WEAPON

**Position:** Professor of Computer Science, FRA-UAS, FB2
**Research areas:** Computer Networks · Distributed Systems (Cloud Computing) · Operating Systems
**Role:** Head of the Computer Networks Laboratory (Rechnernetzelabor)
**Books:** Textbooks on Operating Systems and Computer Networks (Springer, bilingual)
**Security work:** Supervised honeypot project on Raspberry Pi (won VDE prize 2021)
**Virtual Lab:** Built virtual platform for teaching complex network structures — specifically designed for Computer Networks, Distributed Systems, and **IT Security** courses
**GitHub:** `ossperf` — tool for analyzing performance and **data integrity** of object storage services
**Citations:** 1,000+ academic citations
**Email:** christianbaun@fb2.fra-uas.de

**The connection sentence:**
> "I build systems at the application layer. Professor Baun works at the layer beneath everything I have built. That is not a coincidence — that is why FRA-UAS is the right place for me specifically."

---

## 💰 SCHOLARSHIP DETAILS — KNOW THIS IF ASKED

- **Living allowance:** 992 EUR/month × 5 months (Oct 2026 – Feb 2027)
- **German language course:** 992 EUR (September 2026, funded)
- **Flight contribution:** 1,500 EUR (reimburse AFTER arrival — need money upfront)
- **Total value:** ~7,452 EUR
- **Housing:** DAAD students get priority at Studentenwerk Frankfurt, Stralsunder Straße 28, ~160 EUR/month shared room

---

## ⚠️ THINGS NEVER TO SAY

- ~~"vibe coded"~~ — never, ever, in any interview
- ~~"my narrative is cybersecurity"~~ — too vague, says nothing
- ~~"I want to stay in Germany"~~ — you are funded to return to Vietnam
- ~~"basically"~~ / ~~"kind of"~~ / ~~"I think"~~ — hedging words kill credibility
- Never guess and present it as fact — a German professor will probe every claim
- Never apologize for not knowing something — bridge instead

---

## 🔑 THE REAL STORY — YOUR ANCHOR

When pressure hits, come back to this:

> I was always the person who asked why. Not why as curiosity — why as necessity. I tried every domain, crossed each one out. Security was what remained, and red teaming was what fit — because I look for holes, not patches. That is not a career calculation. That is a personality trait expressing itself as a direction.
>
> vgushare.org did not create this. It confirmed it. When the build broke, I did not accept the AI's answer. I went to the source. When the RAG pipeline failed, I built a layer to fix the assumption. Those instincts were already there.
>
> What I am missing is everything beneath Layer 7. I cannot yet see the packet. I cannot reason about the TCP state machine or how a distributed system's trust assumptions interact with its network topology. Professor Baun's lab is exactly where I learn to see that layer.
>
> That is the honest version. That is the one I defend.

---

*Built across multiple sessions, April 2026. Interview: April 20, 15:40–15:50, Zoom.*
