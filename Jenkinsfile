pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh runCommit.sh
            }
        }
        stage('Test') {
            steps {
                python runAllfiles.py
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}