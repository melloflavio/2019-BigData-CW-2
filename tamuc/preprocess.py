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
# os.system(preprocess_command_train)
os.system(preprocess_command_test)

# # Takes about 30 mins to preprocess everything.  We serialize the two
# # preprocess.py synchronous calls just for shell scripting ease; you could use
# # --runner DataflowRunner to run them asynchronously.  Typically,
# # the total worker time is higher when running on Cloud instead of your local
# # machine due to increased network traffic and the use of more cost efficient
# # CPU's.  Check progress here: https://console.cloud.google.com/dataflow
# python trainer/preprocess.py \
#   --input_dict "$DICT_FILE" \
#   --input_path "gs://cloud-samples-data/ml-engine/flowers/eval_set.csv" \
#   --output_path "${GCS_PATH}/preproc/eval" \
#   --cloud

# python trainer/preprocess.py \
#   --input_dict "$DICT_FILE" \
#   --input_path "gs://cloud-samples-data/ml-engine/flowers/train_set.csv" \
#   --output_path "${GCS_PATH}/preproc/train" \
#   --cloud
