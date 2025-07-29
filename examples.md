### 📘 `examples.md`


# CzechFabric SDK Usage Examples

## Initialization

```python
from czechfabric_sdk.client import CzechFabricClient

client = CzechFabricClient(
    api_key="your-api-key",
    base_url="https://mcp.czechfabric.cz"
)
````

---

## Plan a Trip

```python
await client.plan_trip("Florenc", "Karlovo náměstí", departure_time="in 15 minutes")
```

## Get Departures

```python
await client.get_departures("Anděl", when="in 5 minutes", mode="tram")
```

## Geocode Location

```python
await client.geocode("Florenc")
```

## Get Departures by Coordinates

```python
await client.departures_by_coordinates(50.087, 14.420)
```

## Reverse Geocode

```python
await client.reverse_geocode(50.087, 14.420)
```

## Find All Stops Near Coordinates

```python
await client.find_all_stops_near(50.087, 14.420, radius=300)
```

## Get Stop Metadata

```python
await client.get_stop_metadata(stop_name="Dejvická")
```

## List All Stops

```python
await client.list_all_stops(name_contains="And", zone="P")
```

---

## List Available Tools

```python
tools = await client.get_tool_names()
print(tools)
```

## Pretty Tool Summary Prompt (LLM Style)

```python
prompt = await client.get_tool_prompt_summary()
print(prompt)
```