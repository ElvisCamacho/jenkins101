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
                python3 hello.py --name=Elvis
                '''
            }
        }
        stage('Snyk scanning') {
            steps {
                echo "scanning..."
                // snykSecurity(
                // snykInstallation: 'Snyk',
                // // snykTokenId: 'snykTokenId'
                // //snykTokenId: a78c804c-3175-491c-99de-28de9d5924e8
                // snyk test --all-projects --all-sub-projects --json snykTokenId=a78c804c-3175-491c-99de-28de9d5924e8 > snyk_report.json
                // // sh '''
                
               
            
                // // '''
                // // // apt install snyk -y
                // // snyk test --all-projects --all-sub-projects --json snykTokenId: 'a78c804c-3175-491c-99de-28de9d5924e8' > snyk_report.json
               
                // )
                script{
                def snykResult = snykSecurity projectName: 'my_first_buil_pipeline', snykInstallation: 'Snyk', snykTokenId: 'Snyk-Jenkins'
                if (snykResult == 0) {
                    echo "No low severity vulnerabilities found."
                } 
                else {
                error "Snyk scan detected low severity vulnerabilities. Please review and address them."
                }
            }
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
