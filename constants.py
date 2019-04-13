import os

# Read environment variables set for gcloud shell commands
GCLOUD_PROJ_NAME = os.environ['PROJECT']
GCLOUD_JOB_ID = os.environ['JOB_ID']
GCLOUD_BUCKET = os.environ['BUCKET']
GCLOUD_GCS_PATH = os.environ['GCS_PATH']
GCLOUD_DICT_FILE = os.environ['DICT_FILE']
GCLOUD_MODEL_NAME = os.environ['MODEL_NAME']
GCLOUD_VERSION_NAME = os.environ['VERSION_NAME']
