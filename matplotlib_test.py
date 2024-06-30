import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,1])
# plt.ylabel("Y axis")
# plt.xlabel("X axis")
# plt.show()

# categories = ["Cat A","Cat B","Cat C","Cat D"]
# values = [20,35,25,45]
# plt.bar(categories,values,color="g")
# plt.ylabel("Y axis")
# plt.xlabel("X axis")
# plt.title("Information")
# plt.show()


# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
# label="BMW",width=.5)
# plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
# label="Audi", color='r',width=.5)
# plt.legend()
# plt.xlabel('Days')
# plt.ylabel('Distance (kms)')
# plt.title('Information')
# plt.show()



# X=[1,2,3,4,5]
# Y=[3,5,4,6,8]
# plt.scatter(X,Y)
# plt.show()


fruits=["Apples","Bananas","Mangoes","Grapes"]
sizes=[30,40,25,35]
plt.pie(sizes,labels=fruits,autopct="%1.1f%%")
plt.title("Fruits Data")
plt.legend()
plt.show()