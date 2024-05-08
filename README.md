# BTCWeb
This is a webservice that displays historical timeseries data for Bitcoin. I've made this in order
to practice docker and k8 skills.
## Install
Run `pip install -r requirements.txt` to fetch the dependencies.
## Run
Run these commands within the project root (installing with docker):
```bash
docker image build -t python:0.0.1 ./
docker run -p [host port]:8888 python:0.0.1
```
alternatively, just run the python script.
