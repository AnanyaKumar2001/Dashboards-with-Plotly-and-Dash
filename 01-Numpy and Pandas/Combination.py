import numpy as np
import pandas as pd

np.random.seed(101)
mat = np.random.randint(1,101,(100,5))
print(mat)

df = pd.DataFrame(mat)
print(df)

df.columns = ['f1','f2','f3','f4','label']
random_numbers = np.random.randint(0,100,200)
random_mat = random_numbers.reshape(50,4)
col_names = 'A B C D'.split()
df = pd.DataFrame(data = random_mat,columns=col_names)
