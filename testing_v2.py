# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# setting the seed to re-create the dataframe
np.random.seed(25)

# Creating a 5 * 4 dataframe
df = pd.DataFrame(np.random.random([5, 4]), columns =["A", "B", "C", "D"])

df = df.round(3)

# Print the dataframe
print(df)
