# ----------------- Liste de Pizzas avec des Tulpe-------------
"""pizzas = ("4 Fromages", "Végétarienne", "Hawai", "Calzone", "Orientale")
vide = ()


def display_pizza(collection):
    nb_pizza = len(collection)
    if nb_pizza == 0:
        print("Aucune pizzas n'est disponible !")
        return
    print(f"---------Menu des Pizzas ({nb_pizza}) ----------")

    for i in collection:
        print(i)
    print()
    print(f"Première pizza : {pizzas[0]}")
    print(f"Première pizza : {pizzas[-1]}")


# Ajouter une pizza
def add_pizza_user():
    add_pizza = input("Veuillez ajouter une pizza : ")
    pizzas.append(add_pizza)


print()
display_pizza(pizzas)
add_pizza_user()
display_pizza(pizzas)
"""


# --------------- Liste de Pizzas avec une Liste------------
# def tri_personnalise(e):
#   return len(e)


def display_pizza(collection, under_collection=-1):
    # collection.sort(reverse=True,  key=tri_personnalise)
    c = collection
    if under_collection != -1:
        c = collection[:under_collection]
    else:
        c = collection
    nb_pizza = len(c)
    if nb_pizza == 0:
        print("AUCUNE PIZZA !")
    else:
        print(f"  Liste des pizzas ({nb_pizza}) :")
        for pizza in c[:nb_pizza]:
            print("  -", pizza)
        print()
        print(f"Première pizza : {collection[0]}")
        print(f"Première pizza : {collection[-1]}")


def existe_pizza(new_pizza, collection):
    if new_pizza in collection:
        print(f"ERREUR : La pizza {new_pizza} existe déjà dans la liste")
        return False
    else:
        collection.append(new_pizza)
        return True


def add_pizza(pizzas_collection):
    new_pizza = input("Entrez le nom de la nouvelle pizza ou 'stop' pour arrêter : ")
    if new_pizza.lower() == 'stop':
        return False
    return existe_pizza(new_pizza, pizzas_collection)


pizzas = ["Margherita", "Pepperoni", "Quattro Stagioni"]

print(f"Liste initiale des pizzas : ")
display_pizza(pizzas, 2)

while add_pizza(pizzas):
    pass
# vide = ()
print("Liste finale des pizzas :")
display_pizza(pizzas)
