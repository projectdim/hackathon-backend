docker-compose build
docker tag backend_backend_app "${DOCKER_URL}"/backend
docker push "${DOCKER_URL}"/backend
