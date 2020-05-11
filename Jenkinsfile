pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
            	script {
		            try {
		            	sh '''
		            		ls
		            	'''
		            	sh "runCommit.sh"
		            }
		            catch (err) {
		            	echo err.getMessage()
		            	echo "Issue in running runcommit.sh"
		            	
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
		            catch (err) {
		            	echo err.getMessage()
		            	echo "Issue in running runAllfiles.py"
		            	
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
