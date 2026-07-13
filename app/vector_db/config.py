import os

from dotenv import load_dotenv
from qdrant_client import AsyncQdrantClient

load_dotenv()

print(f"QDRANT_MY_URL: {os.getenv("QDRANT_MY_URL")}")

qdrant_client = AsyncQdrantClient(
    url=os.getenv("QDRANT_MY_URL"), api_key=os.getenv("QDRANT__SERVICE__API_KEY"), verify=False, check_compatibility=False
)
