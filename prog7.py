dictionary = {'jitu' : 16, 'amber' : 18, 'dipu' : 19}
search_age = int(input("Enter age"))
for name, age in dictionary.items():
            if age == search_age:
                print(name)