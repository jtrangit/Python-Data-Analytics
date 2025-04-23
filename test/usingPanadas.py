import pandas as pd
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")

dataset['train'].to_pandas()