FROM postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB dim_db
COPY ./docker/dim_db_seed.sql /docker-entrypoint-initdb.d/

EXPOSE 5436