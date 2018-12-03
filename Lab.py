import numpy as np
import pandas as pd
from hmmlearn import hmm

filename = open("1990-201310日线.csv","rb")
# a = np.loadtxt(filename)
data  = pd.read_csv(filename)
filename.close()

data["Date"] = data["Date"].astype('<M8[ns]')
temp= data[data.Date>"2007-12-31"]
a = data["Date"].astype("<M8[ns]")


def get_price(filename,name,start_date,end_date):
    filename = open("1990-201310日线.csv", "rb")
    data = pd.read_csv(filename)
    data["Date"] = data["Date"].astype('<M8[ns]')
    data = data[name]

    tmp = data[data.Date > start_date]
    data2 = tmp[tmp.Date < end_date]
    return data2

a = get_price(filename,"Open","2007-12-31","2013-04-24")


