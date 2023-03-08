pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '2337591e-8f17-430a-9887-0dc1ba19a895', url: 'https://github.com/mahmoudodoo/glassdoor-website-check.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'githubinfo', url: 'https://github.com/mahmoudodoo/glassdoor-website-check.git'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r req.txt'
                sh 'python main_send_email.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r req.txt'
                sh 'python send_email.py'
                echo 'the Job is tested'
            }
        }
    }
}
