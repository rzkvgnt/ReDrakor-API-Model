import joblib
import numpy as np
models = joblib.load('modelx.joblib')
distances, indices = models.kneighbors(np.array(features.reshape(1, -1)), n_neighbors=6)
print(indices)