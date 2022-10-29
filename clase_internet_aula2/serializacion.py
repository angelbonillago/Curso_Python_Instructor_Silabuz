import json

variable_json="""
{ 
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": null,
		"correo": "janedoe@email.com"
	}
}

"""

print(type(variable_json))

#SERIALIZARLO
diccionario = json.loads(variable_json)
print(type(diccionario))
print((diccionario))

##DESERIALIZARLO
string_ = json.dumps(diccionario)
print(type(string_))
print((string_))