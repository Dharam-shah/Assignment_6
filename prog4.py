List = [ 4,'a', 'b', 'c', 1, 'd', 3, 3.4, 4.5]
IntList = [x for x in List if isinstance(x, int)]
StrList = [x for x in List if isinstance(x, str)]
FltList = [x for x in List if isinstance(x, float)]
print(List)
print(IntList)
print(StrList)
print(FltList)