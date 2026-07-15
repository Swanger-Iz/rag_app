from qdrant_client import models
from vector_db.config import qdrant_client

qdrant_client.create_collection(
    collection_name="lohito_reglaments",
    vectors_config=...,
    sparse_vectors_config=...,
    payload=...,
)
