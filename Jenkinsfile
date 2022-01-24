pipeline {
    agent any

    environment {

        RELEASE='1.0'
    }

    stages {
        stage('Build') {

        environment {
        LOG_LEVEL='INFO'
        }
            steps {
                echo "Building Release ${RELEASE} With log level ${LOG_LEVEL}"
            }
        }
        stage("Test"){
        steps {
           echo "Testing i can see  Release ${RELEASE}"
            }
        }
    }
}