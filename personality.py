def analyze_personality(answers):
    traits = {
        "E": 0, "I": 0,
        "S": 0, "N": 0,
        "T": 0, "F": 0,
        "J": 0, "P": 0
    }

    for answer in answers:
        a = answer.lower()

        # E vs I
        if any(word in a for word in ["seul", "réfléchi", "indépendant", "calme", "introspection"]):
            traits["I"] += 1
        if any(word in a for word in ["parler", "groupe", "sociable", "énergique", "discuter", "extérieur"]):
            traits["E"] += 1

        # S vs N
        if any(word in a for word in ["réalité", "pratique", "concret", "observation", "détail"]):
            traits["S"] += 1
        if any(word in a for word in ["imaginatif", "idées", "intuition", "abstrait", "futur", "vision"]):
            traits["N"] += 1

        # T vs F
        if any(word in a for word in ["logique", "analyse", "objectivité", "raisonner", "cohérence"]):
            traits["T"] += 1
        if any(word in a for word in ["émotion", "sentiment", "valeurs", "empathie", "cœur", "relation humaine"]):
            traits["F"] += 1

        # J vs P
        if any(word in a for word in ["planifier", "organisé", "structure", "décision", "discipline", "agenda"]):
            traits["J"] += 1
        if any(word in a for word in ["spontané", "improviser", "flexible", "adaptable", "liberté", "changer"]):
            traits["P"] += 1

    # Construire le type final
    result = ""
    result += "E" if traits["E"] > traits["I"] else "I"
    result += "S" if traits["S"] > traits["N"] else "N"
    result += "T" if traits["T"] > traits["F"] else "F"
    result += "J" if traits["J"] > traits["P"] else "P"

    return result
