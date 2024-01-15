from user_interface import text_input, display_results
from analyzer import analyze_word_frequency


def main():
    # Message de bienvenue
    print("Bonjour et bienvenue dans le programme d'analyse de fréquence de mots.")
    print("Veuillez entrer un texte afin que nous puissions l'analyser.")

    # Appel de la fonction de saisie de texte
    user_text = text_input()

    # Analyse la fréquence des mots
    result = analyze_word_frequency(user_text)

    # Affiche le résultat
    display_results(result)


if __name__ == "__main__":
    main()
