---
name: dom-interaction-explainer
description: Explains the JavaScript DOM manipulation layer of the coin flip challenge including event listeners, class toggling for animations, and statistics tracking.
---

## Purpose
Explain the JavaScript patterns used in the Flip The Coin challenge — specifically
how DOM events, class manipulation, and state tracking power the interactive coin flip.

## Capabilities
- Explain `getElementById` calls wiring up coin, result display, and stat elements
- Describe the flip animation trigger: adding a CSS class to invoke the rotateY transition
- Explain the random result logic: `Math.random() < 0.5` for heads vs tails determination
- Walk through stat tracking: incrementing headsCount and tailsCount on each flip
- Explain the event listener pattern: `flipBtn.addEventListener('click', flipCoin)`
- Describe the animation reset: removing and re-adding the flip class to allow re-triggering

## Key JavaScript Patterns
| Pattern | Purpose |
|---|---|
| `Math.random()` | Generates random 0-1 float for heads/tails outcome |
| `classList.add/remove` | Triggers and resets CSS flip transition |
| `getElementById` | Wires DOM elements to JS variables |
| `addEventListener` | Binds click event to flip function |
| Counter variables | Tracks headsCount, tailsCount, totalFlips |

## Execution Steps
1. Identify which JS interaction is being questioned
2. Locate the relevant code pattern in the inline script or external JS
3. Explain: pattern name -> what it does -> why it is used here
4. Describe the user-visible result of the interaction
