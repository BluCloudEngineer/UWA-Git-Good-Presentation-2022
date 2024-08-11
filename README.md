# UWA Git Good Presentation

![GitHub Contributors](https://img.shields.io/github/contributors-anon/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Downloads](https://img.shields.io/github/downloads/BluCloudEngineer/UWA-Git-Good-Presentation-2022/total)
![GitHub Forks](https://img.shields.io/github/forks/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Issues](https://img.shields.io/github/issues/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub License](https://img.shields.io/github/license/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Open Issues](https://img.shields.io/github/issues-raw/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Open Pull Requests](https://img.shields.io/github/issues-pr-raw/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Python Version](https://img.shields.io/badge/python%20version-3.10.4-blue)
![GitHub Repository Size](https://img.shields.io/github/repo-size/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Stars](https://img.shields.io/github/stars/BluCloudEngineer/UWA-Git-Good-Presentation-2022)
![GitHub Weekly Commit Activity](https://img.shields.io/github/commit-activity/w/BluCloudEngineer/UWA-Git-Good-Presentation-2022)

Demonstration files to build and deploy a sample Python Flask web application to Docker Hub and Amazon Web Services (AWS).

## Assumptions

*   You will need a [Docker Hub](https://hub.docker.com/) account.
*   You will need to create a Docker Access Token and add it as a secret to your GitHub repository. Please see the reference `Build and push Docker images` in the `REFERENCES.md` file.
*   You will need an [Amazon Web Services](https://aws.amazon.com/) Account.
*   All AWS resources are used in this repository fall under the [AWS Free Tier](https://aws.amazon.com/free/), however if you do deploy this to your AWS account, you are responsible for any costs incurred.
*   You already have the default Amazon S3 Bucket used by AWS CodePipeline.
*   The Amazon EC2 web server will be deployed in the default VPC of your AWS account. If you are deploying this for a production environment, it is recommended to create a new VPC.
*   All AWS resources are deployed in the Asia Pacific (Sydney) ap-southeast-2 Region.
*   You will need to have setup the connector between GitHub and AWS. More information can be found [here](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html).

## Automated GitHub Actions

Please see the table below for an overview of the implemented GitHub actions, these files can be found the following directory: `.github/workflows/`

| GitHub Action File Name | Description                                                                                                                          | Affected Branches | Event Type                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | ------------------------- |
| push_to_docker_hub.yml  | Runs unit tests, build and pushes the Docker container to Docker Hub                                                                 | main              | Push to single branch     |
| python_linting.yml      | Run Python PEP 8 formatting over the codebase and creates an new pull request if the linting fails. An example can be seen here: #17 | main and develop  | Push to multiple branches |
| python_unit_tests.yml   | Runs pytest unit tests against the codebase                                                                                          | main and develop  | New Pull Requests         |

## AWS CodePipeline Pipeline

### Overview

A pipeline has been created that runs unit tests of the codebase and deploys the Python Flask web application to an Amazon EC2 instance. The pipeline is executed when changes are made to the `main` branch.

### Deploying the Pipeline

1.  Login to the AWS Management Console.

2.  Change your Region to `ap-southeast-2 (Sydney)` (if you haven't already).

3.  Once logged in, navigate to the `AWS CloudFormation Console`.

4.  Create a new Stack with new resources.

5.  Choose the `Upload a template file` option and upload the following file `pipeline/pipeline.yml`, then press `Next`.

6.  Enter the following for the `Stack name`: UWA-Git-Good-Presentation-Pipeline

7.  Enter the GitHub connector ARN for the `GitHubConnectionArn` parameter.

8.  Enter the name of the Amazon S3 bucket used by AWS CodePipeline for the `PipelineAmazonS3Bucket` parameter.

9.  Press `Next`.

10. Press `Next` again.

11. Scroll down to the bottom of the page and select the `I acknowledge that AWS CloudFormation might create IAM resources` checkbox, then press `Create stack`.

12. Once the pipeline stack has been deployed, it will automatically deploy the Python Flask web application to AWS.

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
python3 -m pytest tests/
# OR
python3 -m pytest tests/ --junitxml=tests/report.xml
```

If you want to print the tests standard output to the screen, run the following command:

```bash
python3 -m pytest -s tests/
# OR
python3 -m pytest -s tests/ --junitxml=tests/report.xml
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
docker build -t uwagitgoodwebapp .
```

### Run Docker Container

To run the Python web application Docker Container, run the following command:

```bash
docker run -it --rm -p 80:5000 uwagitgoodwebapp:latest
```

## Web Application Usage

The usage commands are slightly different when running the code locally or using a Docker container. Follow the instructions based on how you plan to run the code.

### Local Usage

Follow this section if you are going to run the Python code on your local machine and not use a Docker container:

#### Main Webpage

Open a web browser and navigate [to](http://127.0.0.1:5000/):

```
http://127.0.0.1:5000/
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/
```

#### Greeter API - Default Response

Open a web browser and navigate [to](http://127.0.0.1:5000/greeter):

```
http://127.0.0.1:5000/greeter
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/greeter
```

#### Greeter API - Custom Response

Open a web browser and navigate [to](http://127.0.0.1:5000/greeter?name=test):

```
http://127.0.0.1:5000/greeter?name=test
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1:5000/greeter?name=test
```

You can change the value of `name` to any string value of your choosing.

### Docker Container Usage

Follow this section if you are going to run the Python code as a Docker container:

#### Main Webpage

Open a web browser and navigate [to](http://127.0.0.1/):

```
http://127.0.0.1/
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1/
```

### Greeter API - Default Response

Open a web browser and navigate [to](http://127.0.0.1/greeter):

```
http://127.0.0.1/greeter
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1/greeter
```

### Greeter API - Custom Response

Open a web browser and navigate [to](http://127.0.0.1/greeter?name=test):

```
http://127.0.0.1/greeter?name=test
```

or open a Terminal and run the following command:

```bash
curl -X GET http://127.0.0.1/greeter?name=test
```

You can change the value of `name` to any string value of your choosing.

## AWS Lab Cleanup

If you have deployed the AWS CodePipeline pipeline in your AWS account, follow the instructions to delete and cleanup your AWS account:

1.  Login to the AWS Management Console.

2.  Change your Region to `ap-southeast-2 (Sydney)` (if you haven't already).

3.  Once logged in, navigate to the `AWS CloudFormation Console`.

4.  Select the `UWA-Git-Good-Presentation-Webserver` stack, press `Delete` then `Delete stack`.

5.  Once the `UWA-Git-Good-Presentation-Webserver` stack has been deleted, select the `UWA-Git-Good-Presentation-Pipeline` stack, press `Delete` then `Delete stack`.

6.  Navigate to the `Amazon S3 Console`.

7.  Empty the default Amazon S3 Buckets used by `AWS CloudFormation` and `AWS CodePipeline`.
