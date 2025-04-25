from app.services.agent import alfred
import asyncio


async def test_alfred():
    # Test the agent with a simple query
    response = await alfred.run("What's the weather like in Paris?")
    print(f"🌤️ Alfred's Weather Response: {response}")


if __name__ == "__main__":
    asyncio.run(test_alfred())
