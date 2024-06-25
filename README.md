Devops Experts "Devops course" project - World of games.
Currently it is level 4 of 5.

There is a console application with CI/CD process managed by Jenkins.
There is a Declarative Jenkinsfile manages a deployment.
In order to not expose sensitive info in version control repo,
App code uses environment variables defined directly on Jenkins server,
taken by Jenkinsfile. 
Take a look of example files to configure Jenkins server environment variables correctly.
Jenkins pipeline configurations is in charge of deploying correctly.
