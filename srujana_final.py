#srujana's final
f = open("travels.txt", "w")
f.write("New York,Los Angeles\nSan Francisco,New York\nSeatle,Bethesda\nLas Vegas,Dallas\nBoston,Las Vegas\nLos Angeles,Seatle\nDallas,San Francisco\nBethesda,Boston")
f.close()

f = open("travels.txt", "r")
lst = []
for x in f:
  #print(x)
  lst.append(x)



trips = {}
for x in lst:
  print(x)
  i = 0 #counter
  for y in x:
    if y == ",":
      print("city 1:", x[:i], "city 2:", x[i+1:])
      #city1 = x[:i]
      #city2 = x[i+1:]
      trips[x[:i]] = x[i+1:]
    i += 1

for x in trips:
  print(x, trips[x])
    

