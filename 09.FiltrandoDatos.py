DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Nombre de los python developers
    # List comprehension 
    all_python_devs_comprehension=[worker["name"] for worker in DATA if worker["language"]=="python"]
    print(all_python_devs_comprehension)

    # Nombre de los trabajadores de Platzi
    # List comprehension
    all_platzi_workers_comprehension=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    print(all_platzi_workers_comprehension)

    # Nombre personas mayores de edad
    # Filter, Map & Lambda
    adults_filter=list(filter(lambda worker: worker["age"]>18 ,DATA))
    adults_filter=list(map(lambda worker: worker["name"], adults_filter))
    print(adults_filter)

    # Nueva lista de diccionarios con una llave mas (old) mayor a 70 años o no
    # Map & Lambda (Simbolo | para combinar un diccionario con uno nuevo)
    old_people=list(map(lambda worker: worker | {"old": worker["age"]>70}, DATA))
    print(old_people)


# Punto de entrada del programa Python
if __name__=='__main__':
    run()