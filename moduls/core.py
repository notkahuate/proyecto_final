import os
import json

MY_DATA_BASE = 'data/datos.son'

def NewFile(data):
    with open(MY_DATA_BASE,"w") as wf:
      json.dump(data, wf, indent=4) 

def Readfile():
   if os.path.isfile(MY_DATA_BASE):
        with open(MY_DATA_BASE,"r") as rf:
          return json.load(rf)
   else:
      return {}

def Checkfile(initial_Data):
    if  not os.path.isfile(MY_DATA_BASE):
        NewFile(initial_Data)

