// jenking file
pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
    stage('Snyk Scan') {
    steps {
        script {
            def snykResult = sh script: 'snyk test --all-projects --severity-threshold=low', returnStatus: true
            if (snykResult == 0) {
                echo "No low severity vulnerabilities found."
            } else {
                error "Snyk scan detected low severity vulnerabilities. Please review and address them."
            }
        }
    }
}

        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=bachalor
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
