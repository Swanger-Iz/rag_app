from qdrant_client import models
from vector_db.config import qdrant_client

regs_name = "lohito_reglaments_v1"
regs_name_alias = "lohito_reglaments"

qdrant_client.create_collection(
    collection_name=regs_name,
    vectors_config={
        "dense": models.VectorParams(
            size=...,
            distance=models.Distance.COSINE,
            datatype=models.VectorStorageDatatype("float32"),
            on_disk=True,
        )
    },  # size будет равно bge-m3
    sparse_vectors_config={
        "sparse": models.SparseVectorParams(
            index=models.SparseIndexParams(
                full_scan_threshold=0,
                on_disk=False,
                datatype=models.Datatype.FLOAT32,
            ),
        )
    },
    hnsw_config=models.HnswConfigDiff(
        m=16,
        ef_construct=150,
        on_disk=True,
        full_scan_threshold=5000,  # Нужно чтобы он начал строить Hierarchical Navigable Small World
        max_indexing_threads=0,
    ),  # Буду экспериментировать
    optimizers_config=models.OptimizersConfigDiff(
        indexing_threshold=5000,
    ),
    on_disk_payload=True,
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.99,
            always_ram=False,
        )
    ),  # Буду использовать Oversampling + Rescoring
)

qdrant_client.update_collection_aliases(
    change_aliases_operations=[
        models.CreateAliasOperation(
            create_alias=models.CreateAlias(
                collection_name=regs_name, alias_name=regs_name_alias  # Далее в приложении весь код должен обращаться к алиасу
            ),
        )
    ]
)
