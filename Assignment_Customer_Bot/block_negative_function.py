from agents import GuardrailFunctionOutput

async def block_negative_input(ctx, agent, user_input: str) -> GuardrailFunctionOutput:
    offensive_words = ["bad", "hate", "stupid", "angry", "terrible"]
    if any(word in user_input.lower() for word in offensive_words):
        return GuardrailFunctionOutput(
            output_info="⚠️ Please use polite language.",
            tripwire_triggered=True
        )
    # Agar normal input ho
    return GuardrailFunctionOutput(
        output_info=user_input,
        tripwire_triggered=False
    )
