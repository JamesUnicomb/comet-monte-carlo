# Simple Comet Monte-Carlo Simulation using GMAT

## Build the Docker Image
```
docker build --progress=plain --no-cache . -t  myubuntu
```

## Running Example Files
```
docker run -it myubuntu /bin/bash -c 'cd /GMAT/R2022a/api/ && python3 Ex_R2020a_FindTheMoon.py'
```