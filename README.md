# 🇨🇿 CzechFabric SDK

The official Python SDK for accessing the **Czech Intelligence Fabric (MCP)** - a unified API for public services like public transport, geolocation, and stop metadata across the Czech Republic.

---

## 🚀 Features

- Plan public transport trips using OTP
- Get real-time departures from any stop or coordinates
- Geocode and reverse-geocode locations
- Search nearby transport stops
- Fetch detailed stop metadata
- Built-in retry and caching support

---

## 📦 Installation

```bash
pip install czechfabric-sdk
````

---

## 🧪 Quick Start

```python
from czechfabric_sdk.client import CzechFabricClient

client = CzechFabricClient(
    api_key="your-api-key",
    base_url="https://mcp.czechfabric.cz"
)

# Plan a trip
trip = await client.plan_trip("Florenc", "Karlovo náměstí", departure_time="in 15 minutes")
print(trip)
```

---

## 📚 Usage Examples

All usage examples are available in [`examples.md`](./examples.md):

* [Trip planning](./examples.md#plan-a-trip)
* [Get departures](./examples.md#get-departures)
* [Geocode](./examples.md#geocode-location)
* [Reverse geocode](./examples.md#reverse-geocode)
* [Nearby stops](./examples.md#find-all-stops-near-coordinates)
* [Stop metadata](./examples.md#get-stop-metadata)
* [List stops](./examples.md#list-all-stops)

---

## 🧪 Running Tests

This SDK includes `pytest`-based tests for all endpoints.

```bash
pip install -r requirements-dev.txt
pytest tests/
```

---

## 📜 License

MIT © 2025 [Aliyu Abdulbasit Ayinde](mailto:ayindealiyu1@gmail.com)

---

## 🌐 Project Links

* Czech Intelligence Fabric: [https://mcp.czechfabric.cz](https://mcp.czechfabric.cz)
* Issues / Feedback: [GitHub Issues](https://github.com/czechfabric/czechfabric-sdk/issues)

```

