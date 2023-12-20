# Q4Demo

## Run server/setup

### Create Project
- django-admin startproject projectname 

### Create app 
- python manage.py startapp file_storage


### virtual environment create
- python3 -m venv venv 

### activate virtual environment
- source venv/bin/activate

### Run the Application
- python manage.py runserver  


### Environment setup

- Add `.env` file from `env.example`


## LOCUST

### Install Package 
- pip3 install locust


### Validate the Installation
- locust -V


### Run locust
- locust

- Add number of users 
- Add spawn rate 
- Add host 
- Start Swarming


## File Storage with s3 Bucket

### Install Package 
- pip install boto3 django-storages


### Settings
configure the storage backend, AWS credentials, and other related settings:

#### Use Amazon S3 for storage for uploaded media files.
- DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#### Amazon S3 settings.
- AWS_ACCESS_KEY_ID = 'your_access_key_id'
- AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
- AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
- AWS_S3_REGION_NAME = 'your_region_name'  # e.g., 'us-east-1'

#### Optional: Set custom domain for serving static files directly from S3
- AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'




