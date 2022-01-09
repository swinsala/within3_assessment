#!/bin/bash
#Script to run the API on docker locally

#sudo docker build -t weather:v1 .
 
#sudo docker run -it --rm -p 5000:5000 --name weather weather:v1

#running docker on heroku
heroku plugins:install heroku-docker
heroku docker:start
heroku docker:release

#declare image and container variables
imageName=weather:v1
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




