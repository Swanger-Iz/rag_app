# FROM nginxinc/nginx-unprivileged:stable-alpine3.23-slim

# COPY nginx.conf /etc/nginx/nginx.conf

# EXPOSE 8443

FROM nginxinc/nginx-unprivileged:stable-alpine3.23-slim

# Убираем дефолтный конфиг образа, чтобы не конфликтовал
RUN rm -f /etc/nginx/conf.d/default.conf

# Добавляем СВОЙ конфиг рядом, а не вместо родного nginx.conf
COPY conf.d/qdrant.conf /etc/nginx/conf.d/qdrant.conf

EXPOSE 8443 8080