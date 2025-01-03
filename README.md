# ML-Pipeline-using-DVC


# Way to Build & Track ML Pipelines with DVC
 
conda create -n twitter python=3.11 -y

conda activate twitter

pip install -r requirements.txt



# DVC Commands

git init   #initalising git

dvc init  #initalising dvc

dvc repro   #main end point to run the entire pipeline/project

dvc dag   #to see the pipeline diagram

dvc metrics show  #shows the metrics

