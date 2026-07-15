FROM nginxinc/nginx-unprivileged:stable-alpine3.23-slim@sha256:d5b51cfc7d55fc7a7bcf4d1d577b9c3738331df56d68f0b1d8ac9795b9470a5a

# Убираем дефолтный конфиг образа, чтобы не конфликтовал
RUN rm -f /etc/nginx/conf.d/default.conf

# Добавляем СВОЙ конфиг рядом, а не вместо родного nginx.conf
COPY conf.d/qdrant.conf /etc/nginx/conf.d/qdrant.conf

EXPOSE 8443 8080