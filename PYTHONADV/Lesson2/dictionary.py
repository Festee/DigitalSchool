# Dictionary
# {}
#key
#value

contact_info = {"Alice":"555-1234",
                "Bob":"555-5678"
                }

alice_phone = contact_info["Alice"]
bob_phone = contact_info["Bob"]
print(alice_phone)
print(bob_phone)

contact_info["Alice"] = "555-6789" #set update
print(contact_info)

contact_info["Eve"] = "555-9999"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information ={
    "Alice":{
        "phone_number":"555-1234",
        "email":"alice@gmail.com",
        "home_address":"123 Main Street,CityVille",
        "birthday":"20/11/2000"
    },
    "Bob":{
        "phone_number":"555-6789",
        "email":"bob@gmail.com",
        "home_address":"123 Main Street,New York",
        "birthday":"01/01/1999"
    }
}
print(contact_information)
bob_information = contact_information["Bob"]
print(bob_information)

























