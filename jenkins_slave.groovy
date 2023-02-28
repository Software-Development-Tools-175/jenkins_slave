pipeline {
    agent any

    parameters {
        string(name: 'NAME', value: 'Alice'),
        string(name: 'Ages', value: '21')
    }

    stages {
        stage('build') {
            steps {
                sh ('python myscript.py' + params.NAME + params.Ages)
            }
        }
    }

}
