pipeline {
    agent any
   
    stages {
        stage('Clone Repository') {
            steps {
                cleanWs()
                sh 'git clone https://github.com/gsindhuja1311/my_python_project.git $WORKSPACE/my_python_project'
                sh 'ls -la $WORKSPACE/my_python_project'
            }
        }

        stage('Setup Python Env & Build Wheel') {
            steps {
                dir('my_python_project') {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip build
                        python3 -m build --wheel
                    '''
                }
            }
        }
       
        stage('Build Docker Image') {
            steps {
                dir('my_python_project') {
                    sh 'docker build -t my-python-app:latest .'
                }
            }
        }
       
        stage('Deploy') {
            steps {
                sh '''
                    docker stop my-python-container 2>/dev/null || true
                    docker rm my-python-container 2>/dev/null || true
                    docker run -d --name my-python-container my-python-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Repository cloned, built, and deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
