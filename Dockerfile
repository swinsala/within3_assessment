#Dockerfile to run either on Heroku or locally on Docker Desktop 

#Owner: Oluwaseun Winsala

#Start from the latest python image
FROM python:latest

#Owner of the file
LABEL Owner="Winsala"

#Copy requirements needed to complete the installation into the /app directory
COPY ./requirements.txt /app/requirements.txt

#Make/ app the working directoty
WORKDIR /app

#Install all the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

#Copy every file into /app directory
COPY . /app

#Expose port 5000 to be accessible 
EXPOSE 5000

#Entry point to run the puthon script
CMD [ "python3", "within3.py" ]