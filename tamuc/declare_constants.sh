# Now that we are set up, we can start processing some flowers images.
export PROJECT=$(gcloud config list project --format "value(core.project)")
export JOB_ID="tamucc_${USER}_$(date +%Y%m%d_%H%M%S)"
export BUCKET="gs://${PROJECT}-ml"
export GCS_PATH="${BUCKET}/${USER}/${JOB_ID}"
export DICT_FILE=gs://cloud-samples-data/ml-engine/flowers/dict.txt

export MODEL_NAME=flowers
export VERSION_NAME=v1

echo
echo "Using job id: " $JOB_ID
