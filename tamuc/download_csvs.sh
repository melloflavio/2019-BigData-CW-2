#!/bin/bash

# Download dictionary
gsutil cp gs://tamucc_coastline/dict.txt .

# Download dictionary explanation
gsutil cp gs://tamucc_coastline/dict_explanation.csv .

# Download all labeled images in csv
gsutil cp gs://tamucc_coastline/labeled_images.csv .
