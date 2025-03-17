from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

model=OpenAIChatCompletionsModel(
    model="llama3.2",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="secret",
    )
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

result=Runner.run_sync(agent,"Create a meal plan for a week. I'm a vegetarian. This should be for someone who wants to build muscle.")
print(result.final_output)