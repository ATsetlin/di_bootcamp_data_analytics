user_name = "Ari"
email = "ari@ari.com"
user_age = 35
is_online = True

user_info = [user_name, email, user_age, is_online]

print(user_info)



# Exercise 1

list1 = [5, 10, 15, 20, 25, 50, 20]

index_20 = list1.index(20)
print(index_20)

if 20 in list1:
    index_20 = list1.index(20)
    list1[index_20] = 200
print(list1)



