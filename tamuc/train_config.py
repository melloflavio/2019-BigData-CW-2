from constants import *
import os
import datetime

# GCLOUD_DICT_FILE, GCLOUD_BUCKET, GCLOUD_GCS_PATH
#   --scale-tier= \
# basic
# basic-gpu
# basic-tpu
# --scale-tier=STANDARD_1 \
# --scale-tier=custom \
#   --master-machine-type=standard \
#   --worker-machine-type=standard \
#   --worker-server-count=3\

# Create Model
# create_model_cmd = 'gcloud ml-engine models create "{}" --regions us-central1'.format(GCLOUD_MODEL_NAME)
# os.system(create_model_cmd)

# Train multiple versions of the model with preset scale tiers
# scale_tiers = ['basic', 'basic-gpu', 'basic-tpu', 'standard-1']
# for tier in scale_tiers:
#     # Train
#     train_command = 'gcloud ml-engine jobs submit training "{job_id}" \
#         --stream-logs \
#         --module-name trainer.task \
#         --package-path trainer \
#         --staging-bucket "{bucket}" \
#         --region us-central1 \
#         --runtime-version=1.10 \
#         --scale-tier {tier}\
#         -- \
#         --output_path "{gcs_path}/training/{tier}" \
#         --eval_data_paths "{gcs_path}/preproc/eval*" \
#         --train_data_paths "{gcs_path}/preproc/train*"' \
#         .format(job_id=GCLOUD_JOB_ID, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH, tier=tier)
#     print(train_command)
#     # os.system(train_command)

#     # Delete previous version, if exists
#     # delete_version_cmd = 'gcloud ml-engine versions delete {version} --model={model} -q --verbosity none'.format(version=tier, model=GCLOUD_MODEL_NAME)
#     # os.system(delete_version_cmd)

#     create_version_cmd = 'gcloud ml-engine versions create "{version}" \
#         --model "{model}" \
#         --origin "{gcs_path}/training/{tier}/model" \
#         --runtime-version=1.10' \
#         .format(version=tier, model=GCLOUD_MODEL_NAME, gcs_path=GCLOUD_GCS_PATH)
#     os.system(create_version_cmd)


# gcloud ml-engine versions delete $VERSION_NAME --model=$MODEL_NAME -q --verbosity none
# gcloud ml-engine models delete $MODEL_NAME -q --verbosity none


train_command = 'gcloud ml-engine jobs submit training "{job_id}" \
    --stream-logs \
    --module-name trainer.task \
    --package-path trainer \
    --staging-bucket "{bucket}" \
    --region us-central1 \
    --runtime-version=1.10 \
    --scale-tier basic-gpu\
    -- \
    --output_path "{gcs_path}/training/first_try" \
    --eval_data_paths "{gcs_path}/preproc/eval*" \
    --train_data_paths "{gcs_path}/preproc/train*"' \
    .format(job_id=GCLOUD_JOB_ID, bucket=GCLOUD_BUCKET, gcs_path=GCLOUD_GCS_PATH)

os.system(train_command)

# # Models do not need a default version, but its a great way move your production
# # service from one version to another with a single gcloud command.
# gcloud ml-engine versions set-default "$VERSION_NAME" --model "$MODEL_NAME"
