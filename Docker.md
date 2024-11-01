# Common command
list all the images: `docker images`

pull a Docker image: `docker pull ghcr.io/pandapanda3/huggingface-ghcr:944e796b235b0ba903d17695b04e40d23fa8003a`

remove this image to free up space: `docker rmi ghcr.io/pandapanda3/huggingface-ghcr:944e796b235b0ba903d17695b04e40d23fa8003a`


run the Docker image: `docker run -d -p 8000:8000 ghcr.io/pandapanda3/huggingface-ghcr:944e796b235b0ba903d17695b04e40d23fa8003a`


`docker run -it --entrypoint /bin/bash ghcr.io/pandapanda3/huggingface-ghcr:944e796b235b0ba903d17695b04e40d23fa8003a`

check if the container is running: `docker ps`

Check the logs: `docker logs <container_id>`

stop the container: `docker stop <container_id>`

remove container: `docker rm <container_id>`

confirm that the credentials are valid and can successfully authenticate with Docker Hub: `echo <password> | docker login -u <username> --password-stdin`

