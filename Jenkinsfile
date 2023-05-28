// jenking file
pipeline {

    agent any
    environment {
        SNYK_API_TOKEN = credentials('a78c804c-3175-491c-99de-28de9d5924e8')
    }
      
// =======
//     agent { 
//         node {
//             label 'docker-agent-snyk'
//             }
//       }
// >>>>>>> c12959366c0039595ed50cb339bb8bf3efdbab0b
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
        stage('Snyk Security Scan') {
            steps {
                // Run Snyk security scan
                sh "snyk test --all-projects --all-sub-projects --json --all-projects-api-token=${SNYK_API_TOKEN} > snyk_report.json"
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
