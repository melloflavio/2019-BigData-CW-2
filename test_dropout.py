from constants import *
import os
import datetime

# Get timestamp to prevent duplicate job ids & resulting folders
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')


dropouts_archs_to_train = [
    {'description':"dropout_0_2", 'dropout':0.2},
    {'description':"dropout_0_4", 'dropout':0.4},
    {'description':"dropout_0_6", 'dropout':0.6},
    {'description':"dropout_0_8", 'dropout':0.8},
]

# Send a different training job for each dropout to be tested
for dropout_arch in dropouts_archs_to_train:
    test_name=dropout_arch['description']
    dropout=dropout_arch['dropout']
    job_id='{}_{}'.format(test_name, timestamp)
    train_command = 'gcloud beta ml-engine jobs submit training "{job_id}" \
        --stream-logs \
        --module-name trainer.task \
        --package-path trainer \
        --staging-bucket "{bucket}" \
        --region us-central1 \
        --runtime-version=1.10 \
        --scale-tier=basic \
        -- \
        --output_path "{gcs_path}/{job_id}" \
        --eval_data_paths "{gcs_path}/preproc/test*" \
        --train_data_paths "{gcs_path}/preproc/train*" \
        --label_count=18 \
        --dropout={dropout}' \
        .format(job_id=job_id, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH, dropout=dropout)
    os.system(train_command)
