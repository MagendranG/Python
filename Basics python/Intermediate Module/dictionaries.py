#unordered,changeable and Does Not allows duplicates
'''
dictt={ 
    "name":"Magendran",
    "age":"20",
    "DOB":"12.12.12",
    "vehicle":"Car"
}
'''
'''
dictt={ 
    "name":"Magendran",
    "age":"20",
    "DOB":"12.12.12",
    "vehicle":"Car",
    "vehicle":"bike" #gets printed replacing old
}'''
#print(len(dictt))

dictt={ 
    "name":"Mahe",
    "age":"20",
    "DOB":"12.12.12",
    "vehicle":"Car",
    "food":["apple","orange","donut"]
    }

#x=dictt["vehicle"]
x=dictt.get("vehicle")
#dictt.pop
#print(x)

'''
dictt["vehicle"]="Bike"
dictt.update({"name":"Mahendran"})
dictt.pop("age")
dictt["Dress"]="Shirt"
print(dictt)
'''
