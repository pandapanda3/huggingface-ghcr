# 🤗 Hugging Face packaging using GitHub Container Registry

Learn how to create a container and package it with GitHub Actions. This repository gives you a good starting point for a Dockerfile, GitHub Actions workflow, and Python code.

The web application uses FastAPI with Hugging Face and exposes a single endpoint that you can interact with it. 

Fork this repository and run the GitHub Actions as-is so that you can register your own containerized application with no modifications needed.
# Run the service locally
## Generate the environment
`conda create --name huggingface python=3.8`

`conda activate huggingface`

`pip install --upgrade pip`

## Run locally
`pip install -r requirements.txt`
if it has the problem of "Could not build wheels for tokenizers, which is required to install pyproject.toml-based projects", install rust compiler in your environment, you can use the command:
`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
`

Allow warnings: `export RUSTFLAGS='-A warnings'`

Allow invalid reference casting: `export RUSTFLAGS='-A invalid_reference_casting'`

and then restart the Pycharm.
## Check uvicorn
`which uvicorn`
## Run the service
`cd webapp/`

`uvicorn --host 0.0.0.0 main:app
`
## Open the link of the service
`http://0.0.0.0:8000`

FastAPI: `http://0.0.0.0:8000/docs`

# Build the container
## Click to start the local Docker application.
## Build a Docker image
`docker build -t huggingface:local .`
## Run a container from an image
`docker run -i -p 8000:8000 huggingface:local
`

# Run workflow in github
