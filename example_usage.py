import asyncio
from czechfabric_sdk.client import CzechFabricClient

async def main():
    client = CzechFabricClient(
        api_key="YOUR_API_KEY",
        base_url="https://8306d0192c98.ngrok-free.app/mcp/"
    )

    trip = await client.plan_trip("Prague", "Brno")
    print("Trip Plan:\n", trip)

    departures = await client.get_departures("Florenc")
    print("Departures:\n", departures)

    geocode = await client.geocode("Karlovo náměstí")
    print("Geocode:\n", geocode)

if __name__ == "__main__":
    asyncio.run(main())
