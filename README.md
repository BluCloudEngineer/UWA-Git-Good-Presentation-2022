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

## Running Unit Tests

To run all unit tests, run the following command:

```bash
python3.10 -m pytest tests/
```

If you want to print the tests standard output to the screen, run the following command:

```bash
python3.10 -m pytest -s tests/
```

## Running the Web Application

Run the following command to start the web application:

```bash
flask run
```

Then open a web browser and navigate [to](http://127.0.0.1:5000/):

```
http://127.0.0.1:5000/
```
