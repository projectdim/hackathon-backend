#TAG=`date -u +"%Y%m%d%H%M%S"`
#TAG="build_$TAG"

docker build -t dim/backend:latest -f docker/backend.dockerfile .
