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
<<<<<<< HEAD
        stage('Snyk scanning') {
            steps {
                echo "scanning..."
                snykInstallation: 'snyk',
                snykTokenId: 'a78c804c-3175-491c-99de-28de9d5924e8',
                sh "snyk test --all-projects --all-sub-projects --json --all-projects-api-token=a78c804c-3175-491c-99de-28de9d5924e8 > snyk_report.json"
            }
        }
=======
>>>>>>> 3a769937e97a48672b494fc41664d418dc90006d
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
