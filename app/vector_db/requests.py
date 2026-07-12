import asyncio

from config import qdrant_client
from qdrant_client import models


async def create_collection(c_name):
    try:
        response = await qdrant_client.create_collection(
            collection_name=c_name, vectors_config=models.VectorParams(size=12, distance=models.Distance.COSINE)
        )
        if response and hasattr(response, "result"):
            print(f"collection {c_name} created successfully!")
            return True
        else:
            print(f"⚠️ Коллекция '{c_name}' не создана: {response}")
            return False

    except Exception as e:
        print(f"Error: {e}")


async def main():
    success = await create_collection("test_collection")
    if success:
        print(await qdrant_client.get_collections())
    else:
        print("ERROR, Не удалось создать коллекцию")


asyncio.run(main())
