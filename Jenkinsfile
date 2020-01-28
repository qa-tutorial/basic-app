pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'bash build-images.sh'
            }
	      }
        stage('Deploy') {
            steps {
                sh 'bash deploy.sh'
            }
        }
    }
}
