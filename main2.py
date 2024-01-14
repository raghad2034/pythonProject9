from tkinter import *
from tkinter import messagebox

class PetInventory:
    def __init__(self):
        self.name = ""
        self.owner = ""
        self.pet_type = ""
        self.gender = ""
        self.service = ""
        self.days = 0
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

        Label(self.m, text='Name Of Your pet..').pack()
        self.e1 = Entry(self.m)
        self.e1.pack()

        Label(self.m, text='Owner').pack()
        self.e2 = Entry(self.m)
        self.e2.pack()

        Label(self.m, text='Choose pet type:').pack()
        self.pet_type_menu = OptionMenu(self.m, None, 'Cat', 'Dog')
        self.pet_type_menu.pack()

        Label(self.m, text='Gender').pack()
        self.gender_menu = OptionMenu(self.m, None, 'Male', 'Female')
        self.gender_menu.pack()

        Label(self.m, text='Choose service:').pack()
        self.service_menu = OptionMenu(self.m, None, 'Sleepover', 'Haircut', 'Shower')
        self.service_menu.pack()

        Label(self.m, text='Days if you want it to sleep..').pack()
        self.e3 = Entry(self.m)
        self.e3.pack()

        # Buttons
        Button(self.m, text="Calculate Price", command=self.calculate_price).pack()

    def calculate_price(self):
        pet = PetInventory()
        pet.name = self.e1.get()
        pet.owner = self.e2.get()
        pet.pet_type = self.pet_type_menu.cget("text")
        pet.gender = self.gender_menu.cget("text")
        pet.service = self.service_menu.cget("text")
        pet.days = int(self.e3.get())
        pet.calculate_price()
        messagebox.showinfo("Total Price", f"Total Price for {pet.service} ({pet.pet_type}): ${pet.price}")
        self.write_to_file(pet)

    def write_to_file(self, pet):
        with open("PetServicesInfo.txt", "a") as file:
            file.write(f"{pet.display()}\n")

    def run(self):
        self.m.mainloop()

# Create an instance of the GUI class
gui = GUI()
gui.run()