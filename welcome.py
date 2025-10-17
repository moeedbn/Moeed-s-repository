my_list = [1,2,3,4]
my_list += [6,7]
print(my_list)




extend چند عنصر
my_list.extend([90])
print(my_list)




unpacking
my_list= [*my_list,6]
print(my_list)

my_list = [1,2,3,4]
my_list.insert(len(my_list),5)

"""my_list = [*my_list,7]
print(my_list)"""


#internal method  روش متود داخلی

"""my_list = [1,2,3,4]
my_list = my_list.add([111])
print(my_list)"""



my_list = [1,2,3,4]

my_list[len(my_list):]
        
        
import _operator
my_list = [1,2,3,4,5]

_operator.iadd(my_list,[6,7,8])
 
print(my_list)


chain
my_list = [1,2,3,4]



my_list = [1,11,111]

my_list.append(22)

print(my_list)



my_list = [1,1,2,3,6,1,4,5]

print(*my_list, sep=' , ')

print("ssorted by list : ",sorted(my_list))

print(f"maximum {max(my_list)} , minimum {min(my_list)}")

join
 sttring str python

my_list = [1,1,2,3,6,1,4,5]

print(" , ".join(map(str,my_list)))

fruit = ["aplle","cherry","banana"]
print("  ".join(fruit))

 
json
print(json.dumps(my_list,indent=15))



print(my_list)

for i, num in enumerate(my_list):
    print(f"index {i} value  {num}")


for num in my_list:
    print(my_list)