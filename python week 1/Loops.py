#Loops for while, for, break, continue
#list,tuple,string,range

#for loop will print one by one
#a = "Cow"
#for i in a:
    #print(i)
#using range start(where to start) stop(will stop over there) step(how many to skip)
#for i in range(0,20,3):
    #print(i)

#continue statement in the loop
#for i in 'Aeroplane':
    #if i == 'e' or i == 'a':
       #continue 
    #print(i)

#break with for loop
#for i in 'wordsworth':
    #if i == 'o' or i == 's':
       #break
       #print(i)

#Passestatement
#for i in 'trees':
    #if i == 'r':
        #pass
        #print(i)

#else statement with for loop
#for i in range(0,30):
    #print(i)
#else:
    #print("no break\n")

#Enumerate with for loop
#enumerate similar to the index
#li = ['rat','cat','dog']
#for i,j in enumerate(li):
    #print(i,j)

#nested for loop
#for i in range(2, 10):
        #print(i)
#f is used for the string formatting
a = ["Elephant", "Singapore", "Madras"]
b = []
for i in a:
    if i == "Singapore":
        continue
    else:
        print(f"sample program {i}")
b.append("India")
print(f"sample program {b}")
