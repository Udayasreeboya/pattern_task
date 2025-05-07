# *       *
# * *     *
# *   *   *
# *     * *
# *       *

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

# * * * * *
#       *
#     *
#   *
# * * * * *

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
 

# * * * * *
# *       *
# * * * * *      
# *     *
# *       *

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or j==1 or i==mid:
            res+="*"+" "
        elif j==rows and i<mid or i==j and i>mid-1 :
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

# * * * * *
#     *
#     * 
# *   *
# * * *

rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or j==mid:
            res+="*"+" "
        elif i==rows and j<=mid or j==1 and i>mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)