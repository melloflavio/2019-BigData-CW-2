from constants import *
import os
import datetime

# Get timestamp to prevent duplicate job ids & resulting folders
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')


# Custom scale tier
architectures_to_train = [
    {'description':"standard_16", 'machine':"n1-standard-16"},
    {'description':"highmem_16", 'machine':"n1-highmem-16"},
    {'description':"highcpu_16", 'machine':"n1-highcpu-16"},
]

for arch in architectures_to_train:

    test_name=arch['description']
    machine=arch['machine']
    job_id='{}_{}'.format(test_name, timestamp)
    train_command = 'gcloud beta ml-engine jobs submit training "{job_id}" \
        --stream-logs \
        --module-name trainer.task \
        --package-path trainer \
        --staging-bucket "{bucket}" \
        --region us-central1 \
        --runtime-version=1.10 \
        --scale-tier=custom \
        --master-machine-type={machine} \
        --scale-tier=basic \
        -- \
        --output_path "{gcs_path}/{job_id}" \
        --eval_data_paths "{gcs_path}/preproc/test*" \
        --train_data_paths "{gcs_path}/preproc/train*" \
        --label_count=18' \
        .format(job_id=job_id, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH, machine=machine)
    os.system(train_command)
