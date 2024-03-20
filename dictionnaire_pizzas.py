def display_pizza(collection, under_collection=-1):
    if under_collection != -1:
        c = collection[:under_collection]
    else:
        c = collection

    nb_pizza = len(c)

    if nb_pizza == 0:
        print("AUCUNE PIZZA !")
    else:
        print(f"Liste des pizzas ({nb_pizza}) :")
        for i, pizza in enumerate(c, 1):
            print(f"  Pizza {i}: {pizza['nom']} - Prix: {pizza['prix']} € - Description: {pizza['description']}")
        print()
        print(f"Première pizza : {collection[0]['nom']}")
        print(f"Dernière pizza : {collection[-1]['nom']}")


def existe_pizza(new_pizza, collection):
    for pizza in collection:
        if new_pizza.lower() == pizza['nom'].lower():
            print(f"ERREUR : La pizza {new_pizza} existe déjà dans la liste")
            return False
    return True


def add_pizza(pizzas_collection):
    new_pizza = input("Entrez le nom de la nouvelle pizza ou 'stop' pour arrêter : ")
    if new_pizza.lower() == 'stop':
        return False
    prix = float(input("Entrez le prix de la pizza : "))
    description = input("Entrez une description de la pizza : ")
    if existe_pizza(new_pizza, pizzas_collection):
        pizzas_collection.append({'nom': new_pizza, 'prix': prix, 'description': description})
    return True


pizzas = [
    {'nom': "Margherita", 'prix': 8.50, 'description': "Tomate, mozzarella, basilic"},
    {'nom': "Pepperoni", 'prix': 9.00, 'description': "Tomate, mozzarella, pepperoni"},
    {'nom': "Quattro Stagioni", 'prix': 10.00, 'description': "Tomate, mozzarella, jambon, champignons, artichauts"}
]

print(f"Liste initiale des pizzas : ")
display_pizza(pizzas)

while add_pizza(pizzas):
    pass

print("Liste finale des pizzas :")
display_pizza(pizzas)
