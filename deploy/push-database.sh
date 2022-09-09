docker-compose build
docker tag backend_db "${DOCKER_URL}"/db
docker push "${DOCKER_URL}"/db
