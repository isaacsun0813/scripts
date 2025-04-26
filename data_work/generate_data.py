# initial data points (1, 2), (2, 1), (2, 3), (4, 3), (10, 3)

import numpy as np
import os
data = np.array([[1, 2], [2, 1], [2, 3], [4, 3], [10, 3]])
mean = np.mean(data, axis=0)
cov = np.cov(data, rowvar=False)
np.random.seed(42)
new_data = np.random.multivariate_normal(mean, cov, size=100)
print(new_data)
if not os.path.exists('data_work'):
    with open ('data_work.csv', 'w') as f:
        pass
np.savetxt('data.csv', new_data, delimiter=',', header='x,y', comments='')