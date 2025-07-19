import asyncio
from czechfabric_sdk.client import CzechFabricClient

client = CzechFabricClient(
    api_key="key",
    base_url= "https://f4ce6369bda1.ngrok-free.app/mcp" #"https://mcp.czechfabric.cz"
)

async def main():
    print("=== Trip Plan ===")
    trip = await client.plan_trip("Florenc", "Karlovo náměstí", departure_time="in 15 minutes")
    print(trip)

    print("\n=== Departures ===")
    departures = await client.get_departures("Anděl", when="now", mode="tram")
    print(departures)

    print("\n=== Geocode ===")
    geo = await client.geocode("Florenc")
    print(geo)

    print("\n=== Departures by Coordinates ===")
    by_coords = await client.departures_by_coordinates(50.087, 14.420)
    print(by_coords)

    print("\n=== Reverse Geocode ===")
    nearest_stop = await client.reverse_geocode(50.087, 14.420)
    print(nearest_stop)

    print("\n=== Nearby Stops ===")
    nearby = await client.find_all_stops_near(50.087, 14.420, radius=300)
    print(nearby)

    print("\n=== Stop Metadata ===")
    metadata = await client.get_stop_metadata(stop_name="Dejvická")
    print(metadata)

    print("\n=== List All Stops ===")
    all_stops = await client.list_all_stops(name_contains="And", zone="P")
    print(all_stops)

if __name__ == "__main__":
    asyncio.run(main())
