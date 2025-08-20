from agents import GuardrailFunctionOutput, output_guardrail

@output_guardrail
async def block_political_output(ctx, agent, output_text: str):
    banned_keywords = [
        "politics", "political", "election", "government",
        "Trump", "Biden", "Imran Khan", "Nawaz Sharif",
        "Modi", "Putin"
    ]
    if any(word.lower() in output_text.lower() for word in banned_keywords):
        return GuardrailFunctionOutput(
            output_info="⚠ Sorry, I cannot discuss political topics.",
            tripwire_triggered=True
        )
    return GuardrailFunctionOutput(
        output_info=output_text,
        tripwire_triggered=False
    )
