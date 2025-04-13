pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = 'github-creds'
        SSH_CREDENTIALS_ID = 'jenkins-ssh-key'
        PROJECT_SERVER_IP = '46.101.147.132'
        PROJECT_SERVER_USER = 'root'
        PROJECT_PATH = '/root/Projects'
    }

    stages {
        stage('Clone Repository on Jenkins') {
            steps {
                git credentialsId: "${GIT_CREDENTIALS_ID}", url: 'https://github.com/jalalsadeghi/TrackTrace.git', branch: "${env.BRANCH_NAME}"
            }
        }

        stage('Deploy via SSH on Server') {
            steps {
                script {
                    sshagent(credentials: ["${SSH_CREDENTIALS_ID}"]) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ${PROJECT_SERVER_USER}@${PROJECT_SERVER_IP} '
                            cd ${PROJECT_PATH}/${BRANCH_NAME}/TrackTrace &&
                            git checkout ${BRANCH_NAME} &&
                            git pull origin ${BRANCH_NAME} &&
                            chmod +x docker/*.sh &&
                            docker-compose -f docker-compose.${BRANCH_NAME}.yaml down &&
                            docker-compose -f docker-compose.${BRANCH_NAME}.yaml build &&
                            docker-compose -f docker-compose.${BRANCH_NAME}.yaml up -d
                        '
                        """
                    }
                }
            }
        }
    }
}
