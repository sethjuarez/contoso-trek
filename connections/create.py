import os
from promptflow import PFClient
from promptflow.entities import (
    AzureOpenAIConnection,
    CustomConnection,
    CognitiveSearchConnection,
)
from dotenv import load_dotenv

load_dotenv()


pf = PFClient()


# isis-aoai is the name of the connection
connection = AzureOpenAIConnection(
    name="isis-aoai",
    api_key=os.getenv("ISIS_KEY"),
    api_base=os.getenv("ISIS_ENDPOINT"),
    api_type="azure",
    api_version="2023-07-01-preview",
)

print(f"Creating connection {connection.name}...")
result = pf.connections.create_or_update(connection)
print(result)


# contoso-aoai is the name of the connection
connection = AzureOpenAIConnection(
    name="contoso-aoai",
    api_key=os.getenv("CONTOSO_KEY"),
    api_base=os.getenv("CONTOSO_ENDPOINT"),
    api_type="azure",
    api_version="2023-07-01-preview",
)

print(f"Creating connection {connection.name}...")
result = pf.connections.create_or_update(connection)
print(result)


# contoso-cosmos is the name of the connection
connection = CustomConnection(
    name="contoso-cosmos",
    configs={
        "endpoint": os.getenv("COSMOS_ENDPOINT"),
        "databaseId": "contoso-outdoor",
        "containerId": "customers",
    },
    secrets={"key": os.getenv("COSMOS_KEY")},
)

print(f"Creating connection {connection.name}...")
result = pf.connections.create_or_update(connection)
print(result)


connection = CognitiveSearchConnection(
    name="contoso-search",
    api_key=os.getenv("SEARCH_KEY"),
    api_base=os.getenv("SEARCH_ENDPOINT"),
    api_version="2023-07-01-preview",
)

print(f"Creating connection {connection.name}...")
result = pf.connections.create_or_update(connection)
print(result)
