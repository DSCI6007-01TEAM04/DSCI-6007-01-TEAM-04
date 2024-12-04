import time
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def run_reddit_etl():
    api = KaggleApi()
    api.authenticate()

    
    for _ in range(3):
        try:
            # Download the dataset from Kaggle using the Kaggle API
            api.dataset_download_file('UMAIR_TAJ/reddit-hateful-comment-detetction', file_name='reddit.csv')
            break  # If successful, exit the loop
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            time.sleep(5)  

    data = pd.read_csv('reddit.csv')

    
    
    print(data)

    df= pd.DataFrame(data)
    df.to_csv("s3://team04/reddit_data.csv")


