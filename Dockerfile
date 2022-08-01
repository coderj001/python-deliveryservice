# Base image of the docker container
FROM python:3


# Copy the contents of the repo into the /app folder inside the container
COPY . /app
# Update the current working directory to the /app folder
WORKDIR /app

# Add your CLI's installation setups here using the RUN command
# If you have any pip requirements you can do that here
 RUN pip install --user -e .

# Provdide a path to your cli apps executable
ENTRYPOINT [ "python", "cli.py" ]
