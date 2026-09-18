# CSS Battle Challenge 2 — Flip The Coin

![HiDevs GitAgent Passport](https://img.shields.io/badge/HiDevs-GitAgent%20Passport-blueviolet?style=flat-square)
![OpenGAP](https://img.shields.io/badge/OpenGAP-v0.1.0-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Agent](https://img.shields.io/badge/agent-css--battle--challenge--agent-orange?style=flat-square)

An interactive **coin flip simulator** built with pure HTML, CSS, and JavaScript for
CSS Battle Challenge 2. Features a 3D CSS flip animation with heads/tails tracking
and flip statistics.

## Features
| Feature | Implementation |
|---|---|
| 3D Coin Flip Animation | CSS `perspective` + `rotateY(180deg)` + `transition` |
| Heads/Tails Faces | `backface-visibility: hidden` on each `.coin-face` |
| Flip Result Display | JavaScript `Math.random()` + DOM update |
| Stats Tracking | `headsCount`, `tailsCount`, `totalFlips` counters |
| Responsive Layout | CSS Flexbox centering |

## Tech Stack
HTML5 · CSS3 (3D Transforms, Transitions, Flexbox) · Vanilla JavaScript · ESLint

## Repository Structure
```
CSS-Battle-Challenge-2/
├── agent.yaml
├── SOUL.md
├── RULES.md
├── DUTIES.md
├── AGENTS.md
├── EXPLAINABILITY.md
├── README.md
├── LICENSE
├── index.html
├── styles.css
├── package.json
├── .eslintrc.json
├── agent.py
├── skills/
│   ├── css-animation-guide/SKILL.md
│   ├── challenge-walkthrough/SKILL.md
│   └── dom-interaction-explainer/SKILL.md
├── tools/
│   ├── animation-inspector.yaml
│   ├── challenge-navigator.yaml
│   └── snippet-generator.yaml
└── adapters/
    ├── openai_agent.py
    ├── crewai_agent.py
    ├── claude_code.json
    └── lyzr_agent.py
```

## HiDevs GitAgent Passport
Submit at: https://app.hidevs.xyz/passport/submit
Category: **Developer tools**

## Author
Chithra R — https://github.com/Chithra582
