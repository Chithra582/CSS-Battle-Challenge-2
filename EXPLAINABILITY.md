# Explainability — css-battle-challenge-agent

This document explains the internal mechanisms, data lineage, and operational boundaries
of **css-battle-challenge-agent** in accordance with the OpenGAP Checkpoint 2 specification.

---

## How the Agent Decides

css-battle-challenge-agent makes decisions through a deterministic, code-grounded
query classification pipeline. All answers are derived strictly from the challenge
source files (index.html, styles.css).

### 1. Decision Architecture
The decision process flows through sequential stages:

```
User Query (text prompt)
    |
    v
[Stage 1: Query Type Classification]
    |  - Classifies intent into 4 types:
    |    Animation Question / Challenge Walkthrough / DOM Interaction / General CSS-JS Help
    v
[Stage 2: Skill and Tool Selection]
    |  - Animation Question    -> css-animation-guide    + animation-inspector
    |  - Challenge Walkthrough -> challenge-walkthrough  + challenge-navigator
    |  - DOM Interaction       -> dom-interaction-explainer + snippet-generator
    |  - General CSS-JS Help   -> css-animation-guide    + snippet-generator
    v
[Stage 3: Source Code Retrieval]
    |  - Reads relevant sections of index.html and styles.css
    |  - Identifies the exact CSS property or JS pattern in question
    v
[Stage 4: Accuracy Gate]
    |  - Confirms the technique exists in the actual source code
    |  - Rejects claims about libraries or features not present in the project
    v
(Branching Decision: Is the answer grounded in source code?)
    |-- False --> Notifies user: technique not present in this challenge solution
    |-- True  --> [Stage 5: Technical Explanation Composition]
                      |  - Composes: concept -> code snippet -> effect
                      v
                  [Stage 6: Response Delivery with Browser Notes]
                      - Delivers explanation with compatibility notes if relevant
```

### 2. Query Classification Rubric
- **Animation Question (45%)**: Questions about CSS 3D transforms, transitions,
  keyframes, perspective, backface-visibility. Triggers css-animation-guide.
- **Challenge Walkthrough (25%)**: Questions about the overall solution structure,
  HTML layout, coin flip result logic. Triggers challenge-walkthrough.
- **DOM Interaction (20%)**: Questions about JavaScript event listeners, class toggling,
  stat tracking, getElementById. Triggers dom-interaction-explainer.
- **General CSS-JS Help (10%)**: Flexbox, centering, button styling questions.
  Answered from source code context.

### 3. Thresholding and Refusal Decision Criteria
- **Source-Only Grounding**: Only techniques present in index.html and styles.css
  are explained as part of this project. Alternative approaches are flagged as suggestions.
- **No Score Fabrication**: CSS Battle platform scores, rankings, or accuracy percentages
  are not fabricated. Users are directed to cssbattle.dev for live data.
- **Library Accuracy Gate**: The agent never claims React, Vue, GSAP, or other libraries
  are used — this project uses vanilla HTML, CSS, and JavaScript only.

### 4. Client-Side Guardrail Decision Gates
- **Destructive Change Gate**: If a query requests removal of core animation logic,
  the agent warns about the visual impact before suggesting changes.
- **Attribution Gate**: Credit for the challenge solution is attributed to Chithra R
  only; no third-party authorship is implied.

### 5. Fallback and Offline Decision Mechanism
- The agent operates on static source code snapshots with no runtime dependencies.
- If live cssbattle.dev scores are requested, the agent explicitly states it cannot
  access the platform and directs the user there directly.
- For browser compatibility questions, the agent cites known CSS specification support
  levels from its training data rather than querying live compatibility tables.

### 6. Human-in-the-Loop Governance
- **No Auto-Modification**: The agent never auto-edits challenge source files.
- **Kill Switch**: Agent session can be terminated instantly with no background state.
- **Audit Logging**: All query classifications and skill invocations are logged in
  structured JSON for compliance review.

---

## The Data It Uses

css-battle-challenge-agent operates strictly on static source code from the
CSS Battle Challenge 2 repository.

### 1. Ingested Input Data
- **index.html**: HTML structure — container, coin element, coin-face divs (heads/tails),
  result display div, flip button, stats section (headsCount, tailsCount, totalFlips).
- **styles.css**: All styling — coin dimensions (width/height), 3D perspective setup,
  transform-style, rotateY transitions, backface-visibility, flexbox layout, button styles,
  stat card design, color theme (gold/silver coin faces).
- **package.json**: Project metadata — name (html-css), version (1.0.0), serve script.
- **.eslintrc.json**: Linting configuration for the JavaScript layer.

### 2. In-Memory Processing and Storage Architecture
- **Static Source Model**: All explanations are derived from the committed source files.
  No dynamic code execution or live DOM inspection occurs at query time.
- **Session-Only Memory**: Query context is held in local session memory and discarded
  at session end. No user queries are stored remotely.
- **0-Byte Raw Egress Guarantee**: Source code is never uploaded to external servers
  beyond what is already public on GitHub.

### 3. External Relay Data and Redaction Patterns
When responses are exported to framework adapters (OpenAI SDK, CrewAI, Claude Code, Lyzr):
- Only structured code summaries and CSS property descriptions are included in payloads.
- No PII is present in the challenge source code. No redaction patterns apply.
- GitHub repository URL is included as public attribution only.

### 4. Data Privacy, Storage, and Retention
- **No Remote Storage**: The agent does not store or transmit challenge source code
  to any external analytics or database service.
- **GDPR Alignment**: No personal data is collected during challenge walkthroughs.
- **Audit Logging**: Structured JSON logs record query type, skill invoked, and tool used.

---

## Limitations

### 1. Data Currency and Source Snapshot Constraints
- **Static Snapshot**: The agent reflects the state of the repository at the time of
  the last clone. Future commits (new challenges, updated styles) require re-cloning.
- **No Live CSS Battle Score Access**: Platform scores, accuracy percentages, and
  challenge rankings on cssbattle.dev are not accessible to the agent.

### 2. Scope and Domain Constraints
- **Project-Scoped Only**: The agent explains this specific challenge solution.
  Generic CSS or JavaScript tutorials outside the project scope are flagged as out-of-scope.
- **No Browser Execution**: The agent cannot render or visually evaluate the coin flip
  animation at runtime; it explains behavior from source code only.
- **No Auto-Fix**: The agent suggests fixes but does not automatically modify source files.

### 3. Connectivity and Synthesis Boundaries
- **No Live CSS Validation**: The agent cannot run the CSS through a live validator
  at query time. It describes expected behavior based on the specification.
- **No Live Compatibility Check**: Browser support data is from training knowledge,
  not a live Can I Use query.

### 4. Animation Complexity Limitations
- **2D Fallback Scenarios**: If a user's browser does not support `transform-style: preserve-3d`
  (rare in modern browsers), the 3D flip effect will not render. The agent can explain
  the fallback behavior but cannot detect the user's browser at runtime.

### 5. Media and Formatting Constraints
- **Text-Only Explanations**: The agent cannot render or animate the coin flip visually.
  It refers users to the live GitHub Pages URL or local file for visual inspection.

### 6. Security and Guardrail Edge Cases
- **Self-Contained Project**: The challenge has no external API calls or authentication,
  so security surface is minimal. The primary guardrail is attribution accuracy.

---

## Summary & Compliance Checklist

| Checkpoint 2 Requirement | Corresponding Section | Status |
| :--- | :--- | :---: |
| **How the agent decides** | [How the Agent Decides](#how-the-agent-decides) | **Covered** |
| - Decision architecture and 6-stage pipeline | Section 1 | Verified |
| - Query classification rubric and domain routing | Section 2 | Verified |
| - Thresholding, refusal and no-fabrication logic | Section 3 | Verified |
| - Guardrail decision gates | Section 4 | Verified |
| - Fallback and offline decision mechanism | Section 5 | Verified |
| - Human-in-the-loop governance | Section 6 | Verified |
| **The data it uses** | [The Data It Uses](#the-data-it-uses) | **Covered** |
| - Ingested source files and attributes | Section 1 | Verified |
| - In-memory processing and 0-byte egress guarantee | Section 2 | Verified |
| - External relay data and redaction | Section 3 | Verified |
| - Data privacy, retention and GDPR alignment | Section 4 | Verified |
| **Its limitations** | [Limitations](#limitations) | **Covered** |
| - Data currency and snapshot constraints | Section 1 | Verified |
| - Scope boundaries and domain constraints | Section 2 | Verified |
| - Connectivity and live data boundaries | Section 3 | Verified |
| - Animation and browser compatibility limits | Section 4 | Verified |
| - Media and security edge cases | Section 5 and 6 | Verified |
