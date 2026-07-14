FROM qdrant/qdrant:1.18.2-gpu-nvidia@sha256:3941c9db1b1b9144748298ed799afa69fe00baf87687eaa7ffd21d8a30570ee3

# USER SETTINGS
RUN groupadd -r -g 1000 qdrant && \
    useradd -r -u 1000 -g qdrant -m -s /bin/bash qdrant && \
    chown -R qdrant:qdrant /qdrant

RUN rm -f /qdrant/config/config.yaml

COPY config.yaml /qdrant/config/config.yaml

EXPOSE 6333 6334

