class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"{self.name} is {self.age} years old.")



input_name = input("Enter your name: ")
input_age = input("Enter your age: ")
human_info = human(input_name, input_age)
human_info.display_info()