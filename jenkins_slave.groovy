pipeline {
    agent any

    parameters {
        string(name: 'NAME', value: 'Alice'),
        string(name: 'Ages', value: '21')
    }

    stages {
        stage('build') {
            steps {
              echo 'build in progress'
                sh ('python myscript.py' + params.NAME + params.Ages)
            }
        }
    }

}
