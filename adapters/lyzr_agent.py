"""Lyzr Agent adapter for css-battle-challenge-agent"""

def export_lyzr_agent():
    return {
        "agent_name": "css-battle-challenge-agent",
        "agent_description": (
            "AI companion for CSS Battle Challenge 2 -- Flip The Coin by Chithra R. "
            "Explains the 3D CSS coin flip animation pipeline, JavaScript DOM event "
            "handling, and the full HTML/CSS/JS challenge solution structure."
        ),
        "system_prompt": (
            "You are css-battle-challenge-agent. Explain the Flip The Coin CSS Battle "
            "challenge. Use css-animation-guide for 3D transform questions, "
            "challenge-walkthrough for full solution overviews, and "
            "dom-interaction-explainer for JavaScript event handling questions. "
            "Always ground answers in the actual source files."
        ),
        "tools": [
            {"name": "animation-inspector", "type": "code-analysis"},
            {"name": "challenge-navigator", "type": "code-analysis"},
            {"name": "snippet-generator", "type": "code-generation"}
        ],
        "model_config": {"model": "gemini-2.0-flash", "temperature": 0.2}
    }
