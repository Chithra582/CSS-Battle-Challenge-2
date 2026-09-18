"""OpenAI Agents SDK adapter for css-battle-challenge-agent"""

SYSTEM_PROMPT = """You are css-battle-challenge-agent, the AI companion for CSS Battle
Challenge 2 -- Flip The Coin. Explain the 3D CSS coin flip animation, DOM interaction
patterns, and challenge solution structure. Ground all explanations in the actual source
code (index.html, styles.css). Never claim libraries like React or GSAP are used."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "animation_inspector",
            "description": "Inspect CSS animation properties used in the coin flip",
            "parameters": {
                "type": "object",
                "properties": {
                    "property": {"type": "string"},
                    "element": {"type": "string"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "challenge_navigator",
            "description": "Navigate the challenge solution structure",
            "parameters": {
                "type": "object",
                "properties": {
                    "target": {"type": "string"},
                    "layer": {"type": "string", "enum": ["html", "css", "js", "all"]}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "snippet_generator",
            "description": "Generate or retrieve CSS/JS snippets from the challenge",
            "parameters": {
                "type": "object",
                "properties": {
                    "concept": {"type": "string"},
                    "format": {"type": "string", "enum": ["css", "javascript", "html"]}
                },
                "required": ["concept"]
            }
        }
    }
]

def export_openai_spec():
    return {"system_prompt": SYSTEM_PROMPT, "tools": TOOLS, "model": "gpt-4o-mini"}
