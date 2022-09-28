# kuralabs_deployment_2
Testing stage of the CI/CD pipeline deployment 2

Objective: The objective of Deployment 2 is to understand the various components of the stages in a basic CI/CD pipeline.
![Deployment 02](https://github.com/dacostaration/kuralabs_deployment_2/blob/main/Kura Deployment02 - RDC.svg)

*GitHub Repository*
- Repo edited by user directly or remotely 

*EC2 Instance - Jenkins*
- Fed Updated Repo Commits/Changes using GitHub WebHook
- Automatic Checkout, Build, Test and Deploy
- Note: Updated Tests introduced using pytest
  > test application functionality

*Elastic Beanstalk [EB CLI]*
- Elastic Beanstalk environment built [triggered using EC CLI on Jenkins EC2] 
- source artifact generated by Jenkins Build

*Web Application*
- cosmetic updates introduced to basic URL-shortener application

