pipeline {
    agent any

    environment {

        RELEASE'1.0'
    }

    stages {
        stage('Build') {
        agent any
        environment {
            LOG_LEVEL="INFO"

        }
            steps {
                echo "Building Release ${Release} with log level ${LOG_LEVEL}"

            }
        }
        stage("Test") {
        steps {
          echo "Testing i can see Release ${Release} but not log level ${LOG_LEVEL}"
        }
        }
    }

