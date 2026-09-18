---
name: css-animation-guide
description: Explains the 3D CSS coin flip animation pipeline including perspective, transform-style, rotateY, transition timing, and backface-visibility mechanics.
---

## Purpose
Provide precise, code-grounded explanations of the CSS 3D animation system used in
the Flip The Coin challenge, enabling developers to understand and replicate the technique.

## Capabilities
- Explain `perspective` and how it creates the 3D depth illusion on the coin container
- Describe `transform-style: preserve-3d` and why it is required for nested 3D elements
- Walk through `rotateY(180deg)` as the flip mechanism between heads and tails
- Explain `transition` property timing and easing for the flip animation
- Clarify `backface-visibility: hidden` and how it hides the reverse face during rotation
- Describe the gold/silver color theme applied to each coin face

## Execution Steps
1. Identify which CSS animation property or concept is being queried
2. Locate the relevant rule in styles.css
3. Explain: property name -> value -> visual effect -> browser rendering behavior
4. Provide the exact CSS snippet from the source
5. Note any browser compatibility considerations
