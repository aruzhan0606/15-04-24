a={
    "car":"Toyota",
    "model":"camry",
    "image":["https://toyota-almaty.kz/","https://www.toyotakz.com/"]
}



b={
    "car":"Toyota",
    "model":"camry",
    "images":["https://toyota-almaty.kz/","https://www.toyotakz.com/"],
    "price":25000000,
    "is_published":True
}


a={'name':"Erbol","surname":"Askarov"}
b=a["name"]
b=a.get("name")
b=None
a["middle_name"]="Erzhanuly"
print(a)

a={"name":"Askar","last_name":"Erlanov"}
for k,v in a.items():
    print("key:",k)
    print("value",v)

list_1=[ {
            "name":"Kanat",
            "last_name":"Erbolov",
            "age":20
        },
        {
            "name":"Askar",
            "last_name":"Erzhanov",
            "age":15
        },
        {
            "name":"Kairat",
            "last_name":"Zhandosov",
            "age":45
        }
       ]

total=0
for n in list_1:
    total += n["age"]

count=len(list_1)

age=total/count
print(age)