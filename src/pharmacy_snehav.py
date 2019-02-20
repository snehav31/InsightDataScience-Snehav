id=[]


file = open("itcont.txt", "r")
for line in file:
    id.append(line.split(','))


del id[0]
for i in range(0,len(id)):
    subid = id[i]
    subid[0] = int(subid[0])
    subid[4] = float(subid[4])
    del subid[1]
    del subid[1]
    subid.append(1)
    subid.append(subid[2])
    


mydict = {}
otherdict = {}
for i in range(0,len(id)):
    subid = id[i]
    if subid[1] in mydict:
        p = mydict[subid[1]]
        p[2] = p[2] + 1
        p[3] = p[3] + subid[2]
    else:
        newkey = subid[1]
        mydict[newkey] = id[i][1:5]
        
    if subid[1] in otherdict:
        q = otherdict[subid[1]]
        j = 0
        for j in range(0,len(q)):
            if q[j] == subid[0]:
                break
        if j != len(q):
            q.append(id[i][0])
    else:
        otherdict[subid[1]] = []
        otherdict[subid[1]].append(id[i][0])
    
output = []     
for key in mydict:
    p = mydict[key]
    r = otherdict[key]
    q = []
    q.append(p[0])
    q.append(len(r))
    q.append(p[3])
    output.append(q)


output.sort(key=lambda x:x[0])
output.sort(key=lambda x: x[2], reverse=True)


print("drug_name,num_prescriber,total_cost")
for i in range (len(output)):
    
    print(output[i][0]+","+str(output[i][1])+","+str(output[i][2]))

f = open('top_cost_drug.txt','w')
f.write("drug_name,num_prescriber,total_cost"+"\n")
for i in range (len(output)):
    
    f.write(output[i][0]+","+str(output[i][1])+","+str(output[i][2])+"\n")
f.close()

