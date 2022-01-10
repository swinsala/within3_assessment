# SWINSALA WEATHER API

This project is about retreiving API from a weather website (openweathermap.org) and manipulating it to get the needed weather information using a zip code. 

This is deployed either in the cloud using Heroku or locally using Docker desktop app. The results can be used to create a weather web app.

# REQUIREMENTS

- A code editor of your choice
- Python
- Flask
- Virtual environment (optional)
- Github
- Docker
- Heroku CLI

# ACCOUNT REGISTRATION

To be able to use the codes, you need to create accounts on the following:

- Weather website
- Docker
- Heroku

# DEPLOYING LOCALLY

- Start up Docker Desktop.
  - Download at https://www.docker.com/products/docker-desktop and follow the installation instructions provided there.
  - Run `docker info` to ensure you have it installed right.
- Run `./docker_bash.sh`
- The script will build a Docker image, check if a Docker container is running and spin up a new one if none is running under that name.
- The Dockerfile has an entry point to run `within3.py` python script.
- Go to http://localhost:5000?zip_code=07018 to view the API result on your browser. Other zip codes can used to query the app too by replacing the zip code in the URL.
- To stop the container running and delete the image, run the following commands:
  - `docker container stop weather`
  - `docker container rm weather`
  - `docker image rm app`
- Confirm container and image are deleted using the following commands:
  - `docker container ls -a`
  - `docker images`

# DEPLOYING IN HEROKU

This can be done using two entry points. The one Heroku picks up if it is available in the working directory is `heroku.yml`. But if it is not there, it uses `Procfile`. This is where Git comes into play. The following are the simple process of using Git to push all the files to Heroku then deploy the app to be accessed through an endpoint provided by Heroku.

- Run the following commands on your terminal to add the files to your Git:
 ```
 git add . 
 git add .
 git commit -m "Initial commit"
 git push -u origin main
```
- Run the following commands to communicate with Heroku to set environment keys needed and then spin up the app:
```
heroku stack:set container --app swinsala-weather-api
heroku config:set API_KEY={your API key} --app swinsala-weather-api
git push heroku main
```
The first line above allows Heroku set its enverionment to be able to run Docker if it is going through `heroku.yml`. If not, do not run it so it can use `Procfile`. The next line sets the `API_KEY` variable to be used in the URL python code to get the API from the weather website. The last line bundles everything and pushes them to Heroku where `within.py` python script is ran. Use https://swinsala-weather-api.herokuapp.com?zip_code=07018 to view the result. As said earlier, the zip code can be replaced with another zip code.
