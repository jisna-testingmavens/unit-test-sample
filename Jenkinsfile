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
                ${PYTHON_ENV}/bin/pip install fastapi uvicorn requests pytest httpx pytest-cov
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

           stage('Review') {
            steps {
                echo "Waiting for code review and PR approval on GitHub..."
            }
        }

        stage('Merge') {
            when {
                branch 'main'
            }
            steps {
                echo "Code merged into main branch..."
            }
        }

        stage('Deploy to Test') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to Test environment..."
                sh '''
                ${PYTHON_ENV}/bin/pip install gunicorn
                nohup ${PYTHON_ENV}/bin/gunicorn main:app --bind 0.0.0.0:8000 &
                '''
            }
        }

        stage('QA Gate') {
            steps {
                echo "Running QA gate checks (integration tests, smoke tests)..."
                sh '''
                ${PYTHON_ENV}/bin/pytest tests/integration -v
                '''
            }
        }

        stage('Deploy to Prod') {
            when {
                branch 'main'
            }
            input {
                message "Promote to Production?"
                ok "Deploy"
            }
            steps {
                echo "Deploying to Production environment..."
                sh '''
                # Example: SSH into prod server and deploy
                ssh user@prod-server "
                    cd /opt/fastapi_app &&
                    git pull origin main &&
                    source venv/bin/activate &&
                    pip install -r requirements.txt &&
                    systemctl restart fastapi_app
                "
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
