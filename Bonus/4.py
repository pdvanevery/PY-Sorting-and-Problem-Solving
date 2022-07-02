def Sorting(list):
    result = list.split()
    result.sort(key=str.lower)
    return result
    
list = "i love software engineering"
print(Sorting(list))

