# Simple Comet Monte-Carlo Simulation using GMAT

## Build the Docker Image
```
docker build --progress=plain --no-cache . -t  myubuntu
```

## Running Example Files
```
docker run -it myubuntu /bin/python3 propagation_loop.py
```