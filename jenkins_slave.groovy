pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              echo 'build in progress'
              echo 'running script ...'
              sh "python myscript.py ${params.file}"
            }
        }
    }

}
