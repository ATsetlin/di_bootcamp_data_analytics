#Dictionaries 
#Syntax
# {'Key' : Value, 'Key': Value}

dict_constructor = {'name':'Ari', 
                    'age': 35, 
                    'pets': ['Dog', 'Cat']}

student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age' : 14,
    'address': '4 Privet Dr',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main':'Griffendor', 'second':'Slytherin'},
    'best_freinds' : ('Ron Weasly', 'Hermione Granger')

}

print(student_info['pets'])
print(student_info['pets'][1])
student_info['pets'].append('Pheonix')
print(student_info['pets'])


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history_score = sample_dict["class"]["student"]["marks"]["history"]
print(history_score)


# Loops and built-in methods for dictionaries 

#keys()
