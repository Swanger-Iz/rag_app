FROM qdrant/qdrant:v1.18.2@sha256:75eab8c4ba42096724fdcfde8b4de0b5713d529dde32f285a1f86fdcb2c9e50c

# USER SETTINGS
RUN groupadd -r -g 1000 qdrant && \
    useradd -r -u 1000 -g qdrant -m -s /bin/bash qdrant && \
    chown -R qdrant:qdrant /qdrant

EXPOSE 6333 6334

