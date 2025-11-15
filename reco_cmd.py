import pandas as pd
import numpy as np
np.set_printoptions(linewidth=1000)

df = pd.read_csv('movie_reviews.csv', index_col=0)
data = df.to_numpy()

def to_uv(v, axis):
    vnorm = np.linalg.norm(v, axis=axis)
    vnorm = vnorm.reshape(-1, 1)
    return v / vnorm

udata = to_uv(data, axis = 1)

sim_mat = udata @ udata.T
# For every person find most similar buddy
bud_idx = sim_mat.argmax(axis=1)
buddy = df.index[[9, 6, 8, 9, 9, 8, 1, 9, 2, 0]]
p = df.index
print(list(zip(p, buddy)))
