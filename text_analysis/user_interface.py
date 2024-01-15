from service import letter_verification


def text_input():
    while True:
        try:
            # Utilise la fonction input() pour obtenir le texte saisie
            user_text = input("Saisissez votre texte ici : ")

            # Verification de la validiter du texte
            if not letter_verification(user_text):
                raise ValueError("Le texte ne contient pas de lettres.")

            # Retourne le texte saisie.
            return user_text

        except ValueError as ve:
            print(f"Erreur : {ve}")

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None


def display_results(word_frequency):
    print("Resultat de l'analyse de fréquence des mots :")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency} fois")