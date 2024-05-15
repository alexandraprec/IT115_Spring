#Class library
import json

#Python object
data = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf', 'Running', 'Football', 'Traveling'],
    'is_student': False
}


#Creating/writing file
with open('data.json','w') as json_file:
    #Converting data/python object to json file
    json.dump(data,json_file,indent=4)

#Confirmation receipt
print("Data has been written to data.json")



#Reading file
with open('data.json','r') as json_file:
    #
    loaded_data = json.load(json_file)

#Printing loaded data above and text
print("Succesfully able to read data.json")
print(loaded_data)

#Altering key value pairs
loaded_data['age'] = 34
loaded_data['interests'].append('History')

#For removing data:
#loaded_data['interest'].remove('Add String Here')

#Rewriting changes to json file
with open ('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

#Print following text
print("Data has been re-written to data.json")
