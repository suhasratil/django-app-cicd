[![Build and Push Piston docker image to GHCR](https://github.com/suhasratil/django-app-cicd/actions/workflows/pipeline.yml/badge.svg)](https://github.com/suhasratil/django-app-cicd/actions/workflows/pipeline.yml)

## Django, Python, CICD

<!-- # Mojang Java Build Engineer Assignment

## Overview
You are provided with a minimal Django project `piston` as the starting point for the assignment.

### Part 1
Your task is to add a `/health` endpoint for the Django application. You can either use the `django-health-check` plugin with custom health checks or write your own endpoint implementation from scratch.

In the endpoint, you need to check the health of:
- Database.
- Jira integration.

For database check, you can use the embedded sqlite database `db.sqlite3`.

Jira integration is non-critical, meaning the endpoint will still return 200 when the check fails.

For Jira integration check, you can use [Python Jira library](https://pypi.org/project/jira/). We have a [public jira site](https://bugs-legacy.mojang.com/) you can use without authentication.

Tips, you can choose to test if the Django application can get jira issues back from jira filter: [MC Most Popular Issues](https://bugs-legacy.mojang.com/issues/?filter=14500).

You also need to write tests for the health checks you have written.

All necessary dependencies need to be added to `requirements.txt`

### Part 2
Write a Dockerfile to dockerize the Django application.

You must also provide a build pipeline definition in yaml that does continuous integration (CI) and continuous deployment (CD) for every commit on the `main` branch.

You can choose between Azure DevOps pipeline and GitHub Actions.

For continuous integration part, it needs to:
- Lint the python code
- Run tests
- Build a docker image using the Dockerfile to dockerize the django application.

For continuous deployment part, it needs to:
- Upload the docker image to a container registry of your choice.

### Part 3
Assume GitHub is used for version control. You need to add a pull request automation with GitHub Actions. When a pull request is opened towards main, it should do the following:
- Lint the python code
- Run tests
- Run semantic code analysis with CodeQL

### Bonus points:
In Part 1, besides checking database and jira integration health, implement following integration health checks:
- Azure Front Door CDN integration.
- Azure Blob Storage integration.

You can make the following assumptions if you don't already have an azure subscription.

For Azure Front Door CDN integration check, assume you can create a [CdnManagementClient](https://learn.microsoft.com/en-us/python/api/azure-mgmt-cdn/azure.mgmt.cdn.cdnmanagementclient?view=azure-python) with a valid credential.

For Azure Blob Storage integration check, assume you can construct a [BlobServiceClient](https://learn.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python) with a connection string that contains the AccountName and AccountKey.

Both of the checks are none-critical, same as the Jira integration check.

### Notes:
It is fine if you can't set up the dependencies (GitHub Actions, Azure DevOps pipeline, Azure subscriptions). Don't spend too much time on that.

We also don't expect a fully working solution, as long as you can explain your reasoning and demonstrate you are proficient in using relevant SDKs, tools and services.

Please add your reasoning and anything you want us to know to help understand your solution in `solution.txt`.

Feel free to reach out to the recruiter if you have any questions for this assignment.

Good luck!
-->
TEST Ignre ci
