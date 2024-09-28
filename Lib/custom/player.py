def choice(choicesKeys: list) -> str:
    print("Choisissez entre pierre, papier et ciseaux ! (Ou appuyez sur 'q' pour quitter)")
    while True:
        player = input("pi✊/pa✋/ci✌ : ")
        if player in choicesKeys:
            return player
        if player == "q":
            print("Merci d'avoir joué !👋")
            return "q"
        else:
            print("Veuillez sélectionner votre choix parmi les choix possibles. Seules les abréviations données sont acceptées.")