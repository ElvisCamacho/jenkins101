pipeline {
    // agent any
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
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Brad
                '''
            }
        }
        stage('Snyk scanning') {
            steps {
                echo "scanning..."
                // // snykSecurity(
                // // snykInstallation: 'Snyk'
                // // //snykTokenId: 'a78c804c-3175-491c-99de-28de9d5924e8',
                // // //sh "snyk test --all-projects --all-sub-projects --json --all-projects-api-token=a78c804c-3175-491c-99de-28de9d5924e8 > snyk_report.json"
                // // )
                // snykSecurity projectName: 'my_first_buil_pipeline', snykInstallation: 'Snyk', snykTokenId: 'Snyk-Jenkins'
                // echo "done installing snyk"
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
        stage('Kurbenetes') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
