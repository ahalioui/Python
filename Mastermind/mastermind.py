from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
code = []
size = 4

# génération du code à deviner

for n in range(size):
    index = randint(0, len(letters) - 1)
    letter = letters[index]
    code.append(letter)

print(code)

user_code = None

# on boucle tant que l'utilisateur ne donne pas la bonne réponse.
while user_code != code:
    
    # demande à l'utilisateur d'un code 
    user_code = input("Entre un code de " + str(size) + " lettres: ")

    # on lui redemande tant que la longueur n'est pas égale à 'size'
    while len(user_code) != size:
        print("Longueur de code incorrect.")
        user_code = input("Entre un code de " + str(size) + " lettres: ")

    # convertion du code de l'utilisateur en chaine de caractère (plus facile à traiter pour la suite).
    user_code = list(user_code)

    right_places = []

    # check les lettres à la bonne place. 
    for index in range(size):
        if user_code[index] == code[index]:
            right_places.append(index)

    print("Il y a " + str(len(right_places)) + " lettre(s) à la bonne place.")

    wrong_places = []
    
    # check les lettres présentes dans le code mais mal placées


