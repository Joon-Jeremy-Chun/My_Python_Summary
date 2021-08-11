#ex) any 10 number list
data1 = [1,9,4,5,7,2,3,6,8,0]
data2 = []



# test calls all  
#for i in data1:
#    print(i)

   
# test mark index i
#for i in range(len(data1)):
#   print(data1[i])

   
# test mark index j = i +1
#i=0
#for j in range(i+1,len(data1)):
#   print(data1[j])


# test for i,j result in 1~9,2~9,3~9...
#for i in range(len(data1)):
#    for j in range(i+1,len(data1)):
#       print(j)


# sort 
for i in range(len(data1)):
    min_index = i
    for j in range(i+1,len(data1)):
        if data1[min_index] > data1[j]:
            min_index = j
            print(j)
    data1[i],data1[min_index] = data1[min_index],data1[i]
         
print(data1)
 
