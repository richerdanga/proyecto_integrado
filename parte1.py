from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]
arr = np.array([data['age']])
promedio_edad = np.mean(arr)
print(promedio_edad)