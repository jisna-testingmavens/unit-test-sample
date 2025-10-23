pipeline {
    agent any

    environment {
        PYTHON_ENV = "fastapi_env"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your repo
                git branch: 'main', url: 'https://your-repo-url.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo "Creating virtual environment and installing dependencies"
                sh '''
                python3 -m venv ${PYTHON_ENV}
                source ${PYTHON_ENV}/bin/activate
                pip install --upgrade pip
                pip install fastapi uvicorn requests pytest
                '''
            }
        }

        stage('Build') {
            steps {
                echo "No build required for FastAPI, just check syntax"
                sh '''
                source ${PYTHON_ENV}/bin/activate
                python -m py_compile main.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo "Running pytest unit tests"
                sh '''
                source ${PYTHON_ENV}/bin/activate
                PYTHONPATH=. pytest -v
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up virtual environment"
            sh 'rm -rf ${PYTHON_ENV}'
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
