#!/bin/bash
#Script to run the API on docker locally
#Owner: Oluwaseun Winsala

#declare image and container variables
imageName=app:v1
containerName=weather

#build image
docker build -t $imageName -f Dockerfile .

#remove loose images
docker rmi $(docker images | grep "<none>" | awk '{print $3}')

#check if container is already running
containerRunning=$(docker inspect --format="{{ .State.Running }}" $containerName 2> /dev/null)

#use condition to remove old container then create a new or create a new one from the scratch
if [ "$containerRunning" == "true" ]; then
    echo Removing old container...
    docker rm -f $containerName
    echo Spinning up new container...                       
    docker run -d -p 5000:5000 --env-file .env --name $containerName $imageName
else
    echo Spinning up new container...                       
    docker run -d -p 5000:5000 --env-file .env --name $containerName $imageName
fi




