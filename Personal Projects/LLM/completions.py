from groq import Groq

client = Groq()

prompt = "how to ask my boss for a raise?"
behavior = "you are a helpul assistant that provides concise and actionable advice on professional development topics."
stream = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": behavior
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": prompt,
        }
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile",

    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.5,

    # The maximum number of tokens to generate. Requests can use up to
    # 2048 tokens shared between prompt and completion.
    max_completion_tokens=1024,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    stop=None,

    # If set, partial message deltas will be sent.
    stream=True,
)

# Print the incremental deltas returned by the LLM.
def promptinput(prompt, stream):
    if len(prompt) == 0:
        prompt = input("Press Enter to get a tip: ")
    """Prints the prompt and waits for user input."""
    for chunk in stream:
        print(chunk.choices[0].delta.content, end="", flush=True)
