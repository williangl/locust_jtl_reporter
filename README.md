# Locust with JTL Reporter

This project uses a reporter application to read and analyze locust load test.

[JTL Reporter](https://jtlreporter.site/)

## Requirements
JTL Reporter services running. See [on this page](https://jtlreporter.site/docs/)

Poetry installed. See [on this page](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)

## How to execute
First you need start de JTL Reporter services.

Just follow the instructions [on this page](https://jtlreporter.site/docs/)

**After you have the docker containers started you have to start Locust**

Install project dependencies
```shell
poetry install
```

Execute Locust
```shell
poetry run locust
```

## Visualize the Report
On your browser, access the URL `http://localhost:2020/`
Log into the JTL Reporter. See [on this page](https://jtlreporter.site/docs/#step-3-thats-it-)

When you start and stop a test the report will be automatically uploaded.

## JTL Reporter Configuration
On the URL `http://localhost:2020/`, I had to create a new project with name `locust_jtl_reporter_test`.
After that I had to create Tests Scenarios which will be uploaded as soon as the test finished.

**OBS:
The Project Name and the Scenarios are hard-coded configured, so when configuring the JTL Reporter you must have to create a project with the name `locust_jtl_reporter_test` and 2 Scenarios with the name `product_route` and `user_route`**
