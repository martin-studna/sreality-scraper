FROM postgres:latest
ENV POSTGRES_PASSWORD=password123
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=sreality
COPY create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql