#MAIN FUNCTION

###########################################



print("PLEASE ENTER YOUR DATA !!!")

     
name= input("ENTER YOUR NAME : ")
mail= input("ENTER YOUR MAIL ID: ")
start= input("PLEASE ENTER YOUR STARTING PLACE : ")
dest = input("PLEASE ENTER YOUR DESTINATION : ")
budget = input("PLEASE ENTER YOUR BUDGET : ")
print("NAME " + str(name))
print("MAIL ID " + str(mail))
print("STARTING PLACE : ",start)
print("DESTINATION : ", dest)
print("BUDGET : ", budget)
g1 = Graph()
g2 = Graph()

G = GraphVisualization()
start = []
goal = []
file = open("data.txt",'r')
for row in file:
    row = row.split(' ')
    start.append(row[0])
    goal.append(row[1])
  
    
for i in range(len(start)):
    G.addEdge(start[i],goal[i])
G.visualize()

start = []
goal = []
cost = []
distance = []

file = open("data.txt",'r')
for row in file:
    row = row.split(' ')
    start.append(row[0])
    goal.append(row[1])
    cost.append(int(row[2]))
    distance.append(float(row[3]))

for i in range(len(start)):
    g1.add_edge(start[i], goal[i], cost[i])    
    
for i in range(len(start)):
    g2.add_edge(start[i], goal[i], distance[i]) 

file.close()
data = g1.ucs('Abottabad','Gilgit')
print("*** Path ***")

# Print the path
print(data)
mylist = []
for i in range(len(data)):
    mylist.append(data[i][1])
cost = sum(mylist)

# Prints the total cost of path
print("Cost : ",cost)


print("*******")

data2 = g2.ucs('Abottabad','Gilgit')
print("\n *** Path ****")

# Print the path
print(data2)
mylist2 = []
for i in range(len(data2)):
    mylist2.append(data2[i][1])
distance = sum(mylist2)

#Print the total distance of path
print("Distance : ",distance)


#################33
