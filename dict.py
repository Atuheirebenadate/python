# list = [{'age':34,'name':'joana'},{'age':12,'name':'sarah'}]
# dicx = list[0]['age'] 
# def greet():
#    list = [{'age':34,'name':'joana'},{'age':12,'name':'sarah'}]
#    current = 2022-{list[0]['age']}

#    print(current)
# # print(f"hello {list[0]['name']} your are {list[0]['age']}")

# greet()

list = [{'age':34,'name':'joana'},{'age':12,'name':'sarah'}]
for i in range(len(list)):
    for key in list[i]:
    #   break
        print(f" Hello{list[0]['name']}")