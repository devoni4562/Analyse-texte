def text_input():
    # Utilise la fonction input() pour obtenir le texte saisie
    user_text = input("Saisissez votre texte ici : ")

    # Retourne le texte saisie.
    return user_text


def display_results(word_frequency):
    print("Resultat de l'analyse de fréquence des mots :")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency} fois")