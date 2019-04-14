# INM432 - Coursework 2 - Machine Learning in the Cloud

## File Description
Brief description of all the files used.

### data
Folder containing original and processed coastline dataset along with the scripts used for dataset preparation.
**dict.txt/labeled_images.csv/dict_explanation.csv:** Original files downloaded from google cloud sample public bucket gs://tamucc_coastline/
**download_csvs.sh:** Bash script that issues gcloud commands to download the original coastline files
**dataset_split.py:** Python script used for splitting the original dataset into train/test sets
**tamucc_train.csv/tamucc_test.csv:** Train/Test sets used in the study. Obtained by running *dataset_split.py* with *labeled_images.csv*

### flowers-sample
Folder containing original scripts from Google Cloud flowers sample. Obtained from [Google Cloud's ML-Samples Github repository](https://github.com/GoogleCloudPlatform/cloudml-samples).

### Root folder
Scripts used for running the pipeline with the coastline dataset. In general, they represent excerpts from the *sample.sh* bash script provided in *flowers-sample*, with some changes to account for the different dataset and multiple tests ran. Bash scripts were also wrapped in python scripts for easier manipulation.

**declare_constants.sh:** Exports to shell environment constants containing configuration data for the experiment. Examples are gcloud project name, dataset bucket URI, etc.
**constants.py:** Used to expose as python constants the environment constants set by *declare_constants.sh*
**preprocess.py:** Submits preprocessing tasks to Google Cloud for preprocessing both train and eval(test) sets.
**test_clusters_preset.py:** Submits training tasks to Google Cloud with multiple preset cluster configurations to evaluate its effects in terms of training speed and accuracy.
**test_clusters_custom.py:** Submits training tasks to Google Cloud with multiple 16 vCPU machine configurations to assess the effects of cpu to memory ratio in single machine training speed and accuracy.
**test_dropout.py:** Submits training tasks to Google Cloud with different values for dropout ratio to assess the effects of dropout in accuracy.
