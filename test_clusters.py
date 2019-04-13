from constants import *
import os
import datetime

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')
test_name='dropout_09'
job_id='{}_{}'.format(test_name, timestamp)
train_command = 'gcloud ml-engine jobs submit training "{job_id}" \
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
    --label_count=18' \
    .format(job_id=job_id, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH)
os.system(train_command)


# # Models do not need a default version, but its a great way move your production
# # service from one version to another with a single gcloud command.
# gcloud ml-engine versions set-default "$VERSION_NAME" --model "$MODEL_NAME"
