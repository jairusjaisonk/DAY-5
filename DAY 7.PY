# SET {}
# is a collection of data 
# is unordered,unindexed
# # does not contain duplicate data 
# #set is mutable
# a={'jacob','martin','arron','jairus','jenny','sam'}
# for i in a :
#     print(i)
# # as set is unordred 
# set is mainly used in non specified 
#intersection is used to print common elements in 2 sets 

# a={1,2,4,5,6,9,10,1}
# b={2,3,4,5,9,10,11,12,13,14,11}
# print(a&b)* same
# print(a|b)
# print(b-a)
# print(a.union(b))
# print(a.intersection(b))* same

# DICTIONARY 

#no index
# data can always be added to dictionary 
# represented by (userdata) 
# data={"name":"jairus","age":"18","email":"jairusjaison@gmail.com"}

# data["name"] = "das"
# data["age"] = 19 
# data["email"]="dasetten@gmail.com"
# print(data)
# dictionary is only updatable 
# restrictions of a dictionary
# keys are unique 
# keys should be immutable 
# a={"name":"jacob","age":30,"location":"kochi"}
# print(a.get("name"))
# print(a['location'])
# print(a.keys())#used for collection of keys 
# print(a.values())
# print(a.items())
# a.update({'phone':7654345867})
# # a.pop("name")
# # a.popitem()
# # a.clear # used to clear the whole dictionary 
# print(a)
# for i in data:
#     print(i,data[i])

# for i,j in data.items ():
#     print(i,j)

a=" my name is jairus "
# word=""
# b=[]
# for i in (a):
#     if i!=b:
#         word=word+i
#     else:
#         b.append(word)
#         word=""
# b.append(word)
# print(b)

#       or
# b= a.split('a')
b= a.split(' ')
print(b)