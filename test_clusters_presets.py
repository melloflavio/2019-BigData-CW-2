from constants import *
import os
import datetime

# Get timestamp to prevent duplicate job ids & resulting folders
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')


# Preset scale tiers
tiers_to_train = [
    "basic",
    "basic_gpu",
    "standard_1",
    "premium_1",
    # "basic_tpu", # Disabled, training job not configured to use TPUs
]

# Send a different training job for each preset
for scale_tier in tiers_to_train:

    job_id='{}_{}'.format(scale_tier, timestamp)
    train_command = 'gcloud beta ml-engine jobs submit training "{job_id}" \
        --stream-logs \
        --module-name trainer.task \
        --package-path trainer \
        --staging-bucket "{bucket}" \
        --region us-central1 \
        --runtime-version=1.10 \
        --scale-tier={scale_tier} \
        -- \
        --output_path "{gcs_path}/{job_id}" \
        --eval_data_paths "{gcs_path}/preproc/test*" \
        --train_data_paths "{gcs_path}/preproc/train*" \
        --label_count=18' \
        .format(job_id=job_id, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH, scale_tier=scale_tier)
    os.system(train_command)
