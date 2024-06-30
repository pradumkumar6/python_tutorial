import pandas as pd
data = {
  "Name":["Pradyum", "Laxman","Amex","Priyanshu","Hemant","Sanchit","Debasish"],
  "Age":[23,22,25,26,28,25,26],
  "City":["Jaunpur","Mumbai","Mumbai","Bengaluru","Dhanbad","Dhanbad","Kolkata"]
  
}
df = pd.DataFrame(data)
# print(df)

# dropData= df.drop([0,1],axis=0)
# print(dropData)


# dropData = df.drop(["Age"],axis=1)
# print("After deleting the one column is:\n", dropData)

# if we want to add a new column
df["Country"]=["India","India","Japan","USA","France","Australia","UK"]
print("The trained data is:\n",df)

# # if we want to update the specific data
# df.loc[1,"Age"]=25
# print(df)


# if we want to update all the values
# df["Age"]=[21,22,23,24,25,26,27]

def multiply(item):
  return item*2


updated_data= df["Age"].apply(multiply)
print(updated_data)