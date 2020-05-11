pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "./runCommit.sh"
            }
        }
        stage('Test') {
            steps {
                echo "Test stage"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
