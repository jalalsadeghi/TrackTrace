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

        stage('Deploy to Product (develop)') {
            when { branch 'develop' }
            steps {
                script {
                    echo "🔵 Deploying to Product environment"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.product.yml down
                    docker-compose -f docker-compose.product.yml build
                    docker-compose -f docker-compose.product.yml up -d
                    '''
                }
            }
        }

        stage('Deploy to Testing (staging)') {
            when { branch 'staging' }
            steps {
                script {
                    echo "🟡 Deploying to Testing environment"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.testing.yml down
                    docker-compose -f docker-compose.testing.yml build
                    docker-compose -f docker-compose.testing.yml up -d
                    '''
                }
            }
        }

        stage('Deploy to Production (main)') {
            when { branch 'main' }
            steps {
                script {
                    echo "🟢 Deploying to Production environment"
                    sh '''
                    chmod +x docker/*.sh
                    docker-compose -f docker-compose.production.yml down
                    docker-compose -f docker-compose.production.yml build
                    docker-compose -f docker-compose.production.yml up -d
                    '''
                }
            }
        }
    }
}
