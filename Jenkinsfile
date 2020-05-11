pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                try {
                  sh "runCommit.sh"
                }
                finally {
                  echo "Hello Build"
                }
            }
        }
        stage('Test') {
            steps {
                try {
                  python "runAllfiles.py"
                }
                finally {
                  echo "Hello Test"               
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
