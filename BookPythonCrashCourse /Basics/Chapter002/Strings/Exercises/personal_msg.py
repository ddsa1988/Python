name = "diego alexander"

def greeting(person_name):
    if(type(person_name) is not str):
        return

    print(f"Hello, {person_name.title()}. Have a nice day!")

greeting(name)