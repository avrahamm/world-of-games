pipeline {
    agent any

    stages {
        stage('Load Environment Variables') {
            steps {
                script {
                    // Access the global environment variable
                    def envFilePath = env.JENKINS_ENV_FILE_PATH
                    // Load the environment variables from the file
                    def props = readFile(envFilePath)
                    def lines = props.split('\n')
                    for (line in lines) {
                        if (line.trim()) {
                            def (key, value) = line.split('=').collect { it.trim() }
                            env."${key}" = value
                        }
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                git branch: 'main', url: 'https://github.com/avrahamm/world-of-games.git'
            }
        }

        stage('Copy to env file') {
            steps {
                sh 'whoami'
                sh 'pwd'
                sh 'echo $DOCKER_ENV_FILE_PATH; cp $DOCKER_ENV_FILE_PATH .env; chmod 644 .env '
                sh 'cat .env'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'echo $INITIAL_SCORE_FOR_TESTING > scores.txt;'
                sh 'docker compose up -d --build'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: env.DOCKER_HUB_CREDENTIALS_ID,
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                  )]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker images | grep wo'
                sh 'docker compose push'
//                 sh 'echo "docker compose push"'
            }
        }

        stage('Cleaning') {
            steps {
                echo 'Cleaning....'
                sh 'docker compose down; pwd'
            }
        }
    }
}
