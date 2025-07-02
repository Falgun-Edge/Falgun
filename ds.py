car = {"brand":"BMW", "model":"Z4","manuf_year":1999}
car2= car.copy()#coping the dictionary
car3 = dict(engine="V8",e_model= "M3")

car4 = car | car3 
print(car4)


car2["manuf_year"] = 2005
print(car2)
print(car.items())#dict_items([('brand', 'BMW'), ('model', 'Z4'), ('manuf_year', 1999)])
print(car.keys())#dict_keys(['brand', 'model', 'manuf_year'])
print(car.values())#dict_values(['BMW', 'Z4', 1999])

#accessing the value of a key
a = car.keys()
print(a)


x= car.get("model")
print(x)

print(car2.keys())
print(car2.values())
print(car.values())