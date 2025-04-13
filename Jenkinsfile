pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = 'github-creds'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: "${GIT_CREDENTIALS_ID}", url: 'https://github.com/jalalsadeghi/TrackTrace.git', branch: "${env.BRANCH_NAME}"
            }
        }

        stage('Deploy Product (develop)') {
            when { branch 'develop' }
            steps {
                script {
                    echo "🔵 Deploying Product environment (product.min-wave.com)"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.product.yaml down
                    docker-compose -f docker-compose.product.yaml build
                    docker-compose -f docker-compose.product.yaml up -d
                    '''
                }
            }
        }

        stage('Deploy Testing (staging)') {
            when { branch 'staging' }
            steps {
                script {
                    echo "🟡 Deploying Testing environment (testing.min-wave.com)"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.testing.yaml down
                    docker-compose -f docker-compose.testing.yaml build
                    docker-compose -f docker-compose.testing.yaml up -d
                    '''
                }
            }
        }

        stage('Deploy Production (main)') {
            when { branch 'main' }
            steps {
                script {
                    echo "🟢 Deploying Production environment (production.min-wave.com)"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.production.yaml down
                    docker-compose -f docker-compose.production.yaml build
                    docker-compose -f docker-compose.production.yaml up -d
                    '''
                }
            }
        }
    }
}
