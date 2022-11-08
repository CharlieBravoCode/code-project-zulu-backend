#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        ECR_REPO_URL = '398514128704.dkr.ecr.eu-central-1.amazonaws.com/'
        IMAGE_REPO = "${ECR_REPO_URL}/zulu-backend-app"
    }
    stages {
        stage('Build Docker Image and pusing to AWS ECR') {
            steps {
                script {
                    echo "building the docker image..."
                    withCredentials([usernamePassword(credentialsId: 'ecr-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        sh "docker build -t ${IMAGE_REPO}:${IMAGE_NAME} ."
                        sh "echo $PASS | docker login -u $USER --password-stdin ${ECR_REPO_URL}"
                        sh "docker push ${IMAGE_REPO}:${IMAGE_NAME}"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}