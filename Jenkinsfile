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
        stage('Unit Test') {
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
                echo "security scanning in the background..."
                snykSecurity(
                    snykInstallation: 'Snyk',
                    token:
                        Authorization: "2bad0831-f687-4cf8-b184-5055f21fc6a2",
                    //snykTokenId: 'b4cfac1a-a91d-4b32-90fb-4444f7db9480',
                )
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
            //     script{
            //     def snykResult = snykSecurity projectName: 'my_first_buil_pipeline', snykInstallation: 'Snyk', snykTokenId: 'Snyk-Jenkins'
            //     if (snykResult == 0) {
            //         echo "No low severity vulnerabilities found."
            //     } 
            //     else {
            //     error "Snyk scan detected low severity vulnerabilities. Please review and address them."
            //     }
            // }
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
                echo "her goes kurbenetes shell script to make deployment"
                '''
            }
        }
    }
}
