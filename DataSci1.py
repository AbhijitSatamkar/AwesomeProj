import numpy as np

list=np.array([1,2,4])
list2=list + list
list3=list * list
print(list2,list3)
print(type(list))

import requests
url="https://www.google.com"
r=requests.get(url)
text=r.text
print(r.text)