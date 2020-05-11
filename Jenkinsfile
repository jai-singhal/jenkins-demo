pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                cd
                sh "runCommit.sh"
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
