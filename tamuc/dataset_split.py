import pandas as pd
from sklearn.model_selection import train_test_split

# Read csv with labeled image references downloaded from gcloud samples
df = pd.read_csv('labeled_images.csv')

# Split set into train and test with a 80/20 ratio
train, test = train_test_split(df, test_size=0.2)

# Output labeled data as 2 distinct csv files
train.drop('name', axis=1).to_csv('tamucc_train.csv', header=False, index=False)
test.drop('name', axis=1).to_csv('tamucc_test.csv', header=False, index=False)
