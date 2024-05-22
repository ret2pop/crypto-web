# cryptoweb
This is a webservice that displays historical timeseries data for cryptocurrencies. I've made this in order
to practice docker and k8 skills.
## Install
Run `pip install -r requirements.txt` to fetch the dependencies. The recommended way to install this is by using docker, however.
See the `run` section for more details.
### API Key
Place the api key in ./apikey.txt before running the dockerfile, or alternatively
place it in ./secret/apikey.txt if you're running without docker.
## Run
Run these commands within the project root (installing with docker):
```bash
# if running MiniKube
minikube start
env $(minikube docker-env)
minikube image build -t cryptoweb:latest ./
minikube apply -f k8s/configmap.yaml
minikube apply -f k8s/service.yaml
minikube apply -f k8s/cryptoweb.yaml

# if running with docker
docker image build -t cryptoweb:0.0.1 ./
docker run -p [host port]:8888 cryptoweb:0.0.1
```
alternatively, just run the python script. Make sure to make an `apikey.txt` file in the project root containing an
https://www.alphavantage.co/ api key, or provide an APIKEY environment variable to the docker image while altering the configmap.yaml
file.
## For the Record
I have no idea how k8s works; I read the documentation and then hacked together everything in the k8s/ folder. I don't
have a real way to test it as I don't have my own k8s node cluster, and so if I messed this up somehow at least you
understand the logic.
