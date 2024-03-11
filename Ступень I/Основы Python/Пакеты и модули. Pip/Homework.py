import numpy as np
import pandas as pd
import requests

# Применение numpy
array = np.array([0, 1, 2, 3, 4])
print(array)

# Применение pandas
df = pd.DataFrame(['Python', 'Java', 'Javascript', 'C#', 'PHP'], array, columns=['Languages'])
print(df)

# Использование requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print(response_dict.keys())
