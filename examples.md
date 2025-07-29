### 📘 `examples.md`

````markdown
# CzechFabric SDK Usage Examples

## 🔐 Initialization

```python
from czechfabric_sdk.client import CzechFabricClient

client = CzechFabricClient(
    api_key="your-api-key",
    base_url="https://mcp.czechfabric.cz"
)
````

---

## 🚌 Core Transport Tools

### 🚉 Plan a Trip

```python
await client.plan_trip("Florenc", "Karlovo náměstí", departure_time="in 15 minutes")
```

### 📆 Get Departures

```python
await client.get_departures("Anděl", when="in 5 minutes", mode="tram")
```

### 📍 Geocode a Location

```python
await client.geocode("Florenc")
```

### 📍 Reverse Geocode Coordinates

```python
await client.reverse_geocode(50.087, 14.420)
```

### 📌 Departures by Coordinates

```python
await client.departures_by_coordinates(50.087, 14.420)
```

### 🧭 Find All Stops Near Coordinates

```python
await client.find_all_stops_near(50.087, 14.420, radius=300)
```

### 🧾 Get Stop Metadata

```python
await client.get_stop_metadata(stop_name="Dejvická")
```

### 📋 List All Stops

```python
await client.list_all_stops(name_contains="And", zone="P")
```

---

## 🛠️ Tool Operations

### 📜 List Available Tools

```python
tools = await client.list_tools()
for tool in tools:
    print(f"{tool.name}: {tool.description}")
```

### 🧠 Pretty Tool Summary (Prompt / LLM Style)

```python
summary = await client.get_tool_prompt_summary()
print(summary)
```

### 🏷️ Filter Tools by Tag

```python
analysis_tools = await client.filter_tools_by_tag("analysis")
for tool in analysis_tools:
    print(tool.name)
```

### 🧪 Execute Tool with Structured Output

```python
result = await client.execute_tool_raw("get_departures", {"stop_name": "Anděl"})
print("Structured result:", result.data)
```

### 🧾 Fallback to Content Text

```python
result = await client.execute_tool_raw("legacy_tool", {"param": "value"})
if result.data is not None:
    print(result.data)
else:
    for content in result.content:
        if hasattr(content, "text"):
            print(content.text)
```

---

## ⚠️ Error Handling

```python
from czechfabric_sdk.exceptions import ToolExecutionError

try:
    result = await client.execute_tool_raw("failing_tool", {"x": 1})
    print("Result:", result.data)
except ToolExecutionError:
    print("Tool failed gracefully.")
```

---

## 🐞 Debug Tool Result Internals

```python
await client.debug_tool_response("get_departures", {"stop_name": "Florenc"})
```
