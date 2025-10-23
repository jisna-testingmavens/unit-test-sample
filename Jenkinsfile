pipeline {
    agent any

    environment {
        PYTHON_ENV = "fastapi_env"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jisna-testingmavens/unit-test-sample.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo "Setting up environment"
                sh '''
                python3 -m venv ${PYTHON_ENV}
                ${PYTHON_ENV}/bin/pip install --upgrade pip
                ${PYTHON_ENV}/bin/pip install fastapi uvicorn requests pytest pytest-cov
                '''
            }
        }

        stage('Build') {
            steps {
                echo "Checking syntax"
                sh '''
                ${PYTHON_ENV}/bin/python -m py_compile main.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo "Running pytest with coverage"
                sh '''
                PYTHONPATH=. ${PYTHON_ENV}/bin/pytest --cov=. --cov-report=xml --cov-report=term -v
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
            publishCoverage adapters: [coberturaAdapter('coverage.xml')]
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
