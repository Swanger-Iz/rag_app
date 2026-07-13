import asyncio

from config import qdrant_client
from qdrant_client import models


async def create_collection(c_name):
    try:
        response = await qdrant_client.create_collection(
            collection_name=c_name, vectors_config=models.VectorParams(size=12, distance=models.Distance.COSINE)
        )
        if await qdrant_client.get_collection(collection_name=c_name):
            print(f"collection {c_name} created successfully!")
            return True
        else:
            print(f"⚠️ Коллекция '{c_name}' не создана: {response}")
            return False

    except Exception as e:
        print(f"Error: {e}")


async def get_collection_info():
    return await qdrant_client.get_collections()


asyncio.run(create_collection("test"))
# asyncio.run(get_collection_info())
