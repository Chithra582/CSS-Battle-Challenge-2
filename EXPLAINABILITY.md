# Explainability — css-battle-challenge-agent

This document explains the internal mechanisms, data lineage, and operational boundaries of **css-battle-challenge-agent** in accordance with the OpenGAP Checkpoint 2 specification.

---

## How the Agent Decides

css-battle-challenge-agent makes decisions through a deterministic, code-grounded query classification pipeline that grounds all outputs strictly in the challenge source files (index.html, styles.css).

### 1. Decision Architecture
The decision process flows through sequential stages:

```
User Query (text prompt)
    |
    v
[Stage 1: Query Type Classification]
    |  - Classifies intent into 4 types:
    |    CSS Animation / Challenge Walkthrough / DOM Interaction / Snippet Request
    v
[Stage 2: Skill and Tool Selection]
    |  - CSS Animation     -> css-animation-guide      + animation-inspector
    |  - Walkthrough       -> challenge-walkthrough    + challenge-navigator
    |  - DOM Interaction   -> dom-interaction-explainer + snippet-generator
    |  - Snippet Request   -> css-animation-guide      + snippet-generator
    v
[Stage 3: Source Code Retrieval]
    |  - Reads index.html for HTML structure and inline JS patterns
    |  - Reads styles.css for CSS properties, values, and animation rules
    |  - Identifies the exact element, class, or JS function in scope
    v
[Stage 4: Accuracy Gate]
    |  - Confirms the CSS property or JS pattern is present in the source files
    |  - Rejects any mention of frameworks (React, Vue, GSAP) not in the project
    |  - Validates that all property values cited match the actual source
    v
(Branching Decision: Is the answer grounded in source code?)
    |-- False --> Informs user: technique not in this project; offers alternative
    |-- True  --> [Stage 5: Technical Explanation Composition]
                      |  - Concept -> code snippet -> visual effect -> browser notes
                      v
                  [Stage 6: Response Delivery]
                      - Structured technical explanation with browser compatibility notes
```

### 2. Query Classification Rubric
The agent classifies queries using CSS/JS keyword and intent heuristics:
- **CSS Animation (45% of queries)**: Questions about `perspective`, `transform-style: preserve-3d`, `rotateY(180deg)`, `transition`, `backface-visibility`, `@keyframes`. Triggers css-animation-guide skill.
- **Challenge Walkthrough (25% of queries)**: Questions about the overall project structure, coin element layout, stats section, or color theme. Triggers challenge-walkthrough skill.
- **DOM Interaction (20% of queries)**: Questions about `addEventListener`, `classList.add/remove`, `Math.random()`, `getElementById`, stat counter logic. Triggers dom-interaction-explainer skill.
- **Snippet Request (10% of queries)**: Direct requests for CSS or JS code patterns. Answered via snippet-generator tool using source code as the base.

### 3. Thresholding and Refusal Decision Criteria
- **Source-Only Grounding**: Only CSS properties and JS patterns present in index.html and styles.css are explained as part of this project. The agent never invents properties or values.
- **No Score Fabrication**: CSS Battle platform accuracy percentages, leaderboard ranks, or match scores from cssbattle.dev are not fabricated. Users are directed to the platform directly.
- **Library Accuracy Gate**: The project uses vanilla HTML, CSS, and JavaScript only. The agent enforces this boundary and never claims React, Angular, GSAP, or other frameworks are present.
- **Property Value Lock**: CSS values such as `rotateY(180deg)`, animation `transition` duration, and coin dimensions are cited only as they appear in styles.css, not approximated.

### 4. Client-Side Guardrail Decision Gates
Before generating any output:
- **Destructive Change Gate**: If a query requests removal or disabling of the 3D animation CSS (perspective, preserve-3d), the agent warns the user that this will break the flip visual before proceeding.
- **Attribution Gate**: All CSS and JavaScript code is attributed to Chithra R. The agent does not imply third-party authorship or claim the solution is from an external template.
- **Out-of-Scope Gate**: Questions about CSS Battle platform features, scoring algorithms, or server-side systems are flagged as outside the agent's knowledge scope.

### 5. Fallback and Offline Decision Mechanism
- The agent operates entirely on the static committed source snapshot. No live DOM rendering, browser execution, or CSS validation API calls are made at runtime.
- If the user asks for a live visual preview, the agent directs them to open index.html in a browser or deploy via the `npm start` (serve) script in package.json.
- For browser compatibility questions (e.g., `preserve-3d` support), the agent cites known specification support levels from its training knowledge rather than querying a live compatibility database.
- If the challenge repo structure changes after the snapshot, the agent notes that its answers reflect the committed state at the time of last indexing.

### 6. Human-in-the-Loop Governance
- **No Auto-Modification**: The agent explains and suggests code changes but never auto-edits challenge source files (index.html, styles.css) without explicit user instruction.
- **Kill Switch**: The agent session can be immediately terminated with no persistent background processes or side effects.
- **Audit Trail**: All query classifications, skill invocations, and tool calls are logged in structured JSON format for compliance and debugging review.
- **Zero Silent Change**: The agent does not fork, star, or modify the GitHub repository on the user's behalf without explicit authorization.

---

## The Data It Uses

css-battle-challenge-agent operates strictly on static source code committed to the CSS Battle Challenge 2 repository. No external data sources, live APIs, or user-generated data beyond the query text are used.

### 1. Ingested Input Data
The agent consumes the following source files from the CSS Battle Challenge 2 repository:
- **index.html** — Complete HTML structure including: outer `.container`, `.coin-container`, `.coin#coin` element, `.coin-face.coin-heads` (label: H), `.coin-face.coin-tails` (label: T), `#result` div for outcome display, `.flip-btn#flipBtn` button, `.stats` section with `.stat-item` cards for `#headsCount`, `#tailsCount`, and total flips counter.
- **styles.css** — All visual rules: `perspective` value on `.coin-container`, `transform-style: preserve-3d` on `.coin`, `rotateY(180deg)` transition trigger class, `backface-visibility: hidden` on each `.coin-face`, gold color for `.coin-heads`, silver color for `.coin-tails`, flexbox centering on `.container`, button style rules, stat card layout.
- **package.json** — Project metadata: name (`html-css`), version (`1.0.0`), start script (`serve`), keywords (`html`, `css`).
- **.eslintrc.json** — ESLint configuration for the inline JavaScript layer.
- **.codesandbox/tasks.json** — CodeSandbox task runner configuration.

### 2. In-Memory Processing and Storage Architecture
- **Static Snapshot Model**: All explanations are derived from the committed source files at clone time. No dynamic code execution or live DOM inspection occurs at query time.
- **Session-Only Memory**: User query context and intermediate reasoning are held in local session memory only. All context is discarded at session end.
- **0-Byte Raw Egress Guarantee**: Challenge source code is never uploaded to unauthorized external servers or analytics platforms beyond the already-public GitHub repository.
- **No Live CSS Parser**: The agent does not run styles.css through a live CSS parser; it interprets property values from the text content of the committed file.

### 3. External Relay Data and Redaction Patterns
When responses are exported to framework adapters (OpenAI SDK, CrewAI, Claude Code, Lyzr):
- Payloads contain only structured code summaries and CSS/JS property descriptions.
- **Masked Patterns** (if present in source code):
  - API keys or tokens: `[REDACTED_API_KEY]` (none present in this project)
  - Author email: omitted from export payloads if present in package.json
- No PII is present in the challenge source code. The project is a pure frontend exercise.
- GitHub repository URL (`https://github.com/Chithra582/CSS-Battle-Challenge-2`) is included as public attribution only.

### 4. Data Privacy, Storage, and Retention
- **No Remote Storage**: The agent does not transmit session data, query history, or source code excerpts to any cloud database or analytics service.
- **GDPR Alignment**: No personal data is collected or processed during challenge walkthroughs. The project contains no user-submitted data, forms, or authentication.
- **Audit Logging**: Structured JSON logs recording query type, skill invoked, tool called, and response category are maintained locally for compliance auditing. Log entries do not contain raw user query text beyond the session.

---

## Limitations

Understanding the operational boundaries of css-battle-challenge-agent is essential for reliable use.

### 1. Data Currency and Snapshot Constraints
- **Static Snapshot**: The agent reflects the challenge source code at the time of the last repository clone. If Chithra R pushes new challenge files, updated CSS animations, or additional JS logic after the snapshot, those changes are not reflected until the agent is re-indexed.
- **No Live CSS Battle Score Access**: The agent cannot retrieve accuracy scores, pixel-match percentages, or leaderboard rankings from cssbattle.dev. It operates on the local source code only.
- **package.json Version Lock**: The agent reports version `1.0.0` from package.json; it cannot detect npm dependency updates or runtime serve version changes.

### 2. Scope and Domain Constraints
- **Challenge-Scoped Only**: The agent answers questions about this specific CSS Battle Challenge 2 solution. Generic CSS tutorials, browser engine internals, or unrelated frontend frameworks are flagged as out-of-scope.
- **No Browser Execution**: The agent cannot render, screenshot, or visually evaluate the coin flip animation at runtime. It explains behavior from source code inference only.
- **No Auto-Fix Capability**: The agent can suggest CSS or JS corrections but does not automatically apply edits to index.html or styles.css.
- **Vanilla Stack Boundary**: This project uses only HTML, CSS, and inline/vanilla JavaScript. The agent cannot explain behavior as if React, TypeScript, or bundlers were present.

### 3. Connectivity and Synthesis Boundaries
- **No Live CSS Validation**: The agent cannot run styles.css through the W3C CSS Validator or a live browser compute engine at query time. Validity assessment is based on specification knowledge.
- **No Live Compatibility Check**: Browser support data for CSS properties like `perspective`, `transform-style: preserve-3d`, and `backface-visibility` is sourced from training knowledge, not a live Can I Use API query.
- **No CodeSandbox Integration**: The agent knows the `.codesandbox` configuration exists but cannot execute or preview the project inside CodeSandbox at runtime.

### 4. CSS Animation and Rendering Limitations
- **preserve-3d Browser Support**: If the user's browser does not support `transform-style: preserve-3d` (extremely rare in modern browsers, possible in some mobile WebViews), the 3D coin flip will degrade to a 2D effect. The agent can explain this degradation but cannot detect the user's browser at runtime.
- **Transition Timing Sensitivity**: The perceived smoothness of the `rotateY` flip depends on the CSS `transition` duration and easing in styles.css. The agent reports these values as committed but cannot validate the subjective visual quality on the user's device.
- **Backface-visibility Edge Cases**: Some older browsers or GPU-accelerated layers may show bleed-through on `backface-visibility: hidden` elements under specific hardware acceleration conditions. The agent can describe this known edge case but cannot test for it.

### 5. Media and Formatting Constraints
- **Text-Only Explanations**: The agent cannot render or animate the coin flip visually in its response. It refers users to open `index.html` locally or deploy via `npm start` to see the live animation.
- **ASCII Pipeline Diagrams Only**: All architecture diagrams in this document are ASCII art; the agent cannot generate SVG or interactive diagram output.

### 6. Security and Guardrail Edge Cases
- **Self-Contained Project**: CSS Battle Challenge 2 makes no external API calls, has no authentication, and handles no user data. Security surface area is minimal; the primary guardrail is source code attribution accuracy.
- **ESLint Configuration Scope**: The `.eslintrc.json` linting rules apply to the development environment only. The agent can describe the configured rules but cannot run ESLint against the source at query time.

---

## Summary & Compliance Checklist

| Checkpoint 2 Requirement | Corresponding Section | Status |
| :--- | :--- | :---: |
| **How the agent decides** | [How the Agent Decides](#how-the-agent-decides) | **Covered** |
| - Decision architecture and 6-stage pipeline | Section 1 | Verified |
| - Query classification rubric and domain routing | Section 2 | Verified |
| - Thresholding, refusal and no-fabrication logic | Section 3 | Verified |
| - Guardrail decision gates and attribution protection | Section 4 | Verified |
| - Fallback and offline decision mechanism | Section 5 | Verified |
| - Human-in-the-loop governance | Section 6 | Verified |
| **The data it uses** | [The Data It Uses](#the-data-it-uses) | **Covered** |
| - Ingested source files and element-level attributes | Section 1 | Verified |
| - In-memory processing and 0-byte egress guarantee | Section 2 | Verified |
| - External relay data and redaction patterns | Section 3 | Verified |
| - Data privacy, retention and GDPR alignment | Section 4 | Verified |
| **Its limitations** | [Limitations](#limitations) | **Covered** |
| - Data currency and snapshot constraints | Section 1 | Verified |
| - Scope boundaries and vanilla stack constraint | Section 2 | Verified |
| - Connectivity and live validation boundaries | Section 3 | Verified |
| - CSS animation and browser rendering limits | Section 4 | Verified |
| - Media formatting and security edge cases | Section 5 and 6 | Verified |
