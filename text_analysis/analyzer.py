from service import letter_verification
def analyze_word_frequency(text):
    # Divise le texte en mots
    words = text.split()

    # Dictionnaire pour stocker la fréquence de chaque mot
    word_frequency = {}

    # analise des mots
    for word in words:
        # Suppression de la ponctuation
        word = word.strip('.,?!;:()\"\'')

        # Vérifier si le mot est valide
        if not letter_verification(word):
            continue  # Ignorer ce mot et passer au suivant

        # Conversion en minuscule pour une correspondance insensible à la casse
        word = word.lower()

        if word not in word_frequency:
            # Verifie que le mot n'est pas présent
            word_frequency[word] = 1
        else:
            # Incrémente le compteur.
            word_frequency[word] += 1

    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_frequency


