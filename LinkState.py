
f = open("test1.txt", "r")

line = f.readline()

nvertices = int(line.strip())


rowcount = -1
colcount = nvertices

for line in f:
    rowcount += 1

# print(rowcount)
# print(colcount)



router_arr = [[0 for i in range(colcount)]for j in range(rowcount)]

temp_arr = [0] * colcount

f.seek(0)
# print('temp: ', temp_arr)

# i want to use seek here but it's not working. need to fix that

f = open("test1.txt", "r")

f.readline()

line = f.readline()


for i in range(colcount):
    temp = line.split()
    # print(temp)

    for j in range(rowcount):
        # print(temp[j], end = ' ') 
        router_arr[i][j] = int(temp[j])
        print(router_arr[i][j], end = ' ')
    print()
    line = f.readline()



# line = f.readline()
temp = line.split()

gateway_arr = [0]*len(temp)
for k in range(len(temp)):
    gateway_arr[k] = int(temp[k])

print()
print(gateway_arr)
print()




def lcp(n, k, gateway_arr, router_arr):
    
    cost_arr = [[[0,0] for i in range(n)]for j in range(n)]
    path = ''

    cost_count = 0

    # for i in range(n):
    #     for j in range(n):
    #         print(cost_arr[i][j], end = ' ')

    #     print()

    for i in range(n):
        # print(i)


        minval_arr = [10 for i in range(n)]
        # print('minval:', minval_arr)
        if i + 1 not in gateway_arr:

            for j in range(n):

                print(router_arr[i][j], end = ' ')

                if router_arr[i][j] > 0:

                    cost_arr[i][j] = [i+1, router_arr[i][j]]
                    
                    if router_arr[i][j] < minval_arr[j]:

                        
                        minval_arr[j] = i
                        
                
            # print('MIN: ', minval_arr[i][0])

            path+=str(i+1)

                 
                    


        print()

    print('minval: ', minval_arr)

    print('path: ', path)
    for i in range(n):
        for j in range(n):
            print(cost_arr[i][j], end = '')
        print() 

    path_arr = list(map(int, path))
    print(path_arr)

    cost = 0
    nh = 0

    for a in range(len(path_arr)):

        print("Forwarding Table for ", path_arr[a])
        print("{:>10} {:>10} {:>10}".format("To", "Cost", "Next Hop"))

        for b in range(len(gateway_arr)):
            
            # print(router_arr[path_arr[a]][gateway_arr[b]])
            if router_arr[path_arr[a]-1][gateway_arr[b]] == -1:
                # print(router_arr[a][gateway_arr[b]])
                nh = path_arr[a-1]
            else: nh = 0
            # elif router_arr[a][gateway_arr[b]] == gateway_arr[b]:
            #     cost = router

            print("{:>10} {:>10} {:>10}".format(gateway_arr[b], cost, nh))
        
        print()

# def getMin(colcount, router_array):

#     current = 1

#     for i in range(colcount):
        
#         if router_arr[i]



lcp(colcount, len(gateway_arr), gateway_arr, router_arr)