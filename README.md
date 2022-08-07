# UWA-Git-Good-Presentation

![GitHub Contributors](https://img.shields.io/github/contributors-anon/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Downloads](https://img.shields.io/github/downloads/BluCloudEngineer/UWA-Git-Good-Presentation/total)
![GitHub Forks](https://img.shields.io/github/forks/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Issues](https://img.shields.io/github/issues/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub License](https://img.shields.io/github/license/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Open Issues](https://img.shields.io/github/issues-raw/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Open Pull Requests](https://img.shields.io/github/issues-pr-raw/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Python Version](https://img.shields.io/badge/python%20version-3.10.4-blue)
![GitHub Repository Size](https://img.shields.io/github/repo-size/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Stars](https://img.shields.io/github/stars/BluCloudEngineer/UWA-Git-Good-Presentation)
![GitHub Weekly Commit Activity](https://img.shields.io/github/commit-activity/w/BluCloudEngineer/UWA-Git-Good-Presentation)

Demonstration files to build and deploy a sample Python Flask web application to Docker Hub and Amazon Web Services (AWS).

## Installation

Run the following commands to download and install the required Python Dependencies:

```bash
sudo apt install python3-flask -y
sudo pip3 install -r requirements.txt
```

## Code Linting

To run linting over the code, run the following commands in Visual Studio Code:

1.  Press `F1`.

2.  Search for `Python: Run Linting`.

3.  Press `CTRL + ~` to open the inbuilt Terminal.

4.  Select `PROBLEMS` and address the identified linting issue(s).

## Running Unit Tests

To run all unit tests, run the following command:

```bash
python3.10 -m pytest tests/
```

If you want to print the tests standard output to the screen, run the following command:

```bash
python3.10 -m pytest -s tests/
```

## Local Development

Complete this section if you want to develop and run the code locally.

### Running the Web Application

Run the following command to start the web application:

```bash
flask run
```

## Docker Container Development

Complete this section if you want to build and run a Docker container

### Build Docker Container

To build the Python web application Docker Container, run the following command:

```bash
docker build -t uwapythonwebapp .
```

### Run Docker Container

To run the Python web application Docker Container, run the following command:

```bash
docker run -it --rm -p 5000:5000 uwapythonwebapp:latest
```

## Web Application Usage

The steps in this section are the same whether you run the code locally or using a Docker container.

### Main Webpage

Open a web browser and navigate [to](http://127.0.0.1:5000/):

```
http://127.0.0.1:5000/
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/
```

### Greeter API - Default Response

Open a web browser and navigate [to](http://127.0.0.1:5000/greeter):

```
http://127.0.0.1:5000/greeter
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/greeter
```

### Greeter API - Custom Response

Open a web browser and navigate [to](http://127.0.0.1:5000/greeter?name=test):

```
http://127.0.0.1:5000/greeter?name=test
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/greeter?name=test
```

You can change the value of `name` to any string value of your choosing.
