import csv

class Persona:
    def __init__(self, documento = 1, apellido = 'Torvalds', nombre = 'Linus'):
        self.documento = ""
        self.apellido = ""
        self.nombre = ""
        self.personas = []

    def __repr__(self):
        return f'Persona: {self.documento} - {self.apellido}, {self.nombre}'

    def addPersona(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')
        self.personas.append([self.documento,self.nombre,self.apellido])

    def write_file(self):
        with open('persona.csv','w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(self.personas)

    def load_file(self):
        with open('persona.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                self.personas.append(row)

    def show_all(self):
        for x in self.personas:
            print(x)

    def search_persona(self):
        busqueda=input('Ingrese DNI de la persona: ')
        for x in range(len(self.personas)):
            if self.personas[x][0] == busqueda:
                return self.personas[x]
            else: 
                return False
        


