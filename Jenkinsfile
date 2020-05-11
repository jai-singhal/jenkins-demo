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
                python add.py 4 1
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
