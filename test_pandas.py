import pandas as pd
a = pd.Series([10,12,15,16,18])
print(a)

#  If we want to give index according to ourself
b = pd.Series([10,18,12,20,25],index=["a","b",'c',"d","e"])
print(b)

person={
  "name":"pradum",
  "age":21,
  "location":"mumbai"
}
res = pd.Series(person)
print(res)

data = [["Alice","10","80"],["Bob","30","40"],["Tony","50","60"]]
df = pd.DataFrame(data,columns=["Name","Age","Marks"])
print(df)

student = {
  "Name":["Pradyum","Manish","Mukesh","Neeraj"],
  "Marks":[90,80,85,100]
}
res = pd.DataFrame(student)
print(res)



d={
  "one":pd.Series([1,2,3]),
  "two":pd.Series([1,2,3,4])
}
ans = pd.DataFrame(d)
print(ans)

data = pd.read_json("sample1.json")
print(data)
length = len(data)
print(length)
shape = data.shape
print(shape)

tail = data.tail(3)
print(tail)