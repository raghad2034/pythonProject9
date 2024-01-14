from tkinter import *
from tkinter import messagebox
class PetInventory:
    def __init__(self, name, owner, pet_type, gender, service):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        self.gender = gender
        self.service = service
        self.price = 0

    def calculate_price(self):
        if self.service.lower() == "sleepover":
            if self.pet_type.lower() == "cat":
                if self.days == 2:
                    self.price = 150
                elif self.days == 7:
                    self.price = 360
                elif self.days == 10:
                    self.price = 560
            elif self.pet_type.lower() == "dog":
                if self.days == 2:
                    self.price = 120
                elif self.days == 7:
                    self.price = 300
                elif self.days == 10:
                    self.price = 500
        elif self.service.lower() == "haircut":
            if self.pet_type.lower() == "cat":
                self.price = 30
            elif self.pet_type.lower() == "dog":
                self.price = 40
        elif self.service.lower() == "shower":
            if self.gender.lower() == "male":
                self.price = 30
            elif self.gender.lower() == "female":
                self.price = 45

    def display(self):
        return f"{self.owner},{self.gender},{self.name},{self.pet_type},{self.service},{self.price}"

class GUI:
    def __init__(self):
        self.m = Tk()
        self.m.title("Welcome to Pet Services")

        # Entry Widgets
        Label(self.m, text='Name Of Your pet..').pack()
        self.e1 = Entry(self.m)
        self.e1.pack()

        Label(self.m, text='Owner').pack()
        self.e2 = Entry(self.m)
        self.e2.pack()

        Label(self.m, text='Choose pet type:').pack()
        self.pet_type_var = StringVar()
        pet_type_options = ['Cat', 'Dog']
        self.pet_type_menu = OptionMenu(self.m, self.pet_type_var, *pet_type_options)
        self.pet_type_menu.pack()

        Label(self.m, text='Gender').pack()
        self.gender_var = StringVar()
        gender_options = ['Male', 'Female']
        self.gender_menu = OptionMenu(self.m, self.gender_var, *gender_options)
        self.gender_menu.pack()

        Label(self.m, text='Choose service:').pack()
        self.service_var = StringVar()
        service_options = ['Sleepover', 'Haircut', 'Shower']
        self.service_menu = OptionMenu(self.m, self.service_var, *service_options)
        self.service_menu.pack()

        # Buttons
        Button(self.m, text="Calculate Price", command=self.calculate_price).pack()


    def calculate_price(self):
        pet = PetInventory(self.e1.get(), self.e2.get(), self.pet_type_var.get(), self.gender_var.get(), self.service_var.get())
        pet.calculate_price()
        messagebox.showinfo("Total Price", f"Total Price for {pet.service} ({pet.pet_type}): ${pet.price}")
        self.pet_list.append(pet)

    def run(self):
        self.m.mainloop()

        # Write results to file
        with open("PetServicesInfo.txt", "w") as file:
            for pet in self.pet_list:
                file.write(f"{pet.display()}\n")

# Create an instance of the GUI class
gui = GUI()
gui.run()