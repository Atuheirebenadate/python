# def greet_multiple(**kwargs):
#      print(kwargs)
#      print(kwargs.keys())

# if "country" in keys:
#   print (f"Hello{kwargs['name']})

  #       you are from {kwargs['country']}")

  #    elif 'age' in keys:
  #        year = 2022-kwargs["age"]
  #       print(f"Hello{kwargs['name']}  you are born in {year}")

  #        elif not kwargs:
  # print(f"Hello Anomous")  
  
         
    
def sum_and_greet(*args ,**kwargs):
        sum=0
        for num in args:
            sum+=num
            keys=keys.keys()
        if "name" in keys:
          print(f"Hello{kwargs['name']}),the answer is{sum}") 

        elif "country" in keys:
          print(f"Hello{kwargs['name']},the answer is {sum}")

        elif "country" in keys:
          print(f"Hello from{kwargs['country']} the answer is {sum}")
          
        elif not kwargs:
            print("Hello anonymous the answer is {sum}")  

    