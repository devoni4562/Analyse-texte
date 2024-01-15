def analyze_word_frequency(text):
    # Divise le texte en mots
    words = text.split()

    # Dictionnaire pour stocker la fréquence de chaque mot
    word_frequency = {}

    # analise des mots
    for word in words:
        # Suppression de la ponctuation
        word = word.strip('.,?!;:()\"\'')

        # Vérifier si le mot est composé uniquement de ponctuation
        if not word or all(char in '.,?!";:()' for char in word):
            continue  # Ignorer ce mot et passer au suivant

        # Conversion en minuscule pour une correspondance insensible à la casse
        word = word.lower()

        if word not in word_frequency:
            # Verifie que le mot n'est pas présent
            word_frequency[word] = 1
        else:
            # Incrémente le compteur.
            word_frequency[word] += 1

    return word_frequency
