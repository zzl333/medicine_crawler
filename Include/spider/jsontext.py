import json
fp = open("json.json","r",encoding = "utf-8")
js = json.load(fp)
wholesales = js["data"]["wholesales"]
# print(js["data"]["wholesales"])
import pandas as pd
exall=pd.DataFrame(wholesales)
import csv
# print(exall["chainPrice"])
# print(exall["promotionalPrice"])
# print(exall["provider_name"])
