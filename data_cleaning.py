import pandas as pd
# data = {
#   "item":["milk","sugar","chips","coffee"],
#   "quantity":[2,1,5,4],
#   "price":[67,pd.NA,45,73]
# }
# df = pd.DataFrame(data)
# print(df)

# # to fill the na column
# df["price"]=df["price"].fillna(df["price"].mean())
# print(df)

# if data is in wrong format

data = {
  "Duration": [60,60,60,45,45,60,60,450,30,60,60],
                   "Pulse": [110,117,103,109,117,102,104,109,98,100,100],
                   "Calories": [409.1,479.0,340.0,282.4,406.0,300.0,374.0,253.3,195.1,269.0,269.0],
                   "Date": ['2020/12/01','2020/12/02','20201203','2020/12/04','2020/12/05',pd.NA,'2020/12/07','2020/12/08','2020/12/09','2020/12/10','2020/12/10']
}
df = pd.DataFrame(data)
print(df)

for i in df.index:
  if df.loc[i,"Duration"]>120:
    df.loc[i,"Duration"]=120
    
print("Data after cleaning is:\n",df)   


# to remove the duplicate data
duplicate = df.duplicated(data)
print(duplicate) 
df.drop_duplicates(inplace=True)
print(df)