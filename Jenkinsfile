pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            	script {
		            try {
		            	sh '''
		            		cd
		            		ls
		            	'''
		            	sh "runCommit.sh"
		            }
		            except (err) {
		            	echo err.getMessage()
		            	echo "Issue in running runcommit.sh"
		            	
		            }
		            finally {
		            	echo "Hello Build"
		            }            	
            	}
            }
        }
        stage('Test') {
            steps {
            	script {
		            try {
		            	python "runAllfiles.py"
		            }
		            finally {
		            	echo "Hello Test"               
		            }            	
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
