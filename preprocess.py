from constants import *
import os
import datetime

timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
# Setup both commands for preprocessing
preprocess_command_train = 'python trainer/preprocess.py \
  --input_dict "{}" \
  --input_path "{}/data/tamucc_train.csv" \
  --output_path "{}/preproc/train" \
  --job_name "tamucc-train-{}" \
  --cloud'.format(GCLOUD_DICT_FILE, GCLOUD_BUCKET, GCLOUD_GCS_PATH, timestamp)

preprocess_command_test = 'python trainer/preprocess.py \
  --input_dict "{}" \
  --input_path "{}/data/tamucc_test.csv" \
  --output_path "{}/preproc/test" \
  --job_name "tamucc-test-{}" \
  --cloud'.format(GCLOUD_DICT_FILE, GCLOUD_BUCKET, GCLOUD_GCS_PATH, timestamp)

# Run both commands sequentially
os.system(preprocess_command_train)
os.system(preprocess_command_test)
