##x=["key1","key2","key3"]
##thisdict=dict.fromkeys(x)
##print(thisdict)
##
##x={"key1","key2","key3"}
##y=1
##thisdict=dict.fromkeys(x,y)
##print(thisdict)

##x={
##    1:"one",
##    2:"two",
##    3:"three"
##    }
##print(x[1])
##
##var = {"name":{1:{"surname":["s","m","n"]}}}
##var["name"][1]["surname"][2] = "l"
##print(var)


##var = '{"country":"india"}'
##print(dict(var))
##
##import json
##var = '{"country":"india"}'
##print(type(var))
##output = json.loads(var)
##print(type(output))
##print(var)
##output1=json.dumps(output)
##print(output1)
##print(type(output1))
##
##print("lambda function")
##x = lambda a : a + 10
##print(x(5))


##def myfunc(n):
##  return lambda a : a * n
##
##mydoubler = myfunc(2)
##
##print(mydoubler(11))
