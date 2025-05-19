pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('flask-app')
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop flask-app || true && docker rm flask-app || true'
                sh 'docker run -d -p 5000:5000 --name flask-app flask-app'
            }
        }
    }
}
