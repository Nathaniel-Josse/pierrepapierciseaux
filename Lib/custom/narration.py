from Lib.custom import player, opponent

# Variables definitions
choicesKeys = ["pi", "pa", "ci"]
choices = [("pi", "la Pierre"), ("pa", "le Papier"), ("ci", "les Ciseaux")]
choicesDict = dict(choices)
isGameRunning = True
playerScore = 0
opponentScore = 0

# Game
def intro() -> None:
    """Small text of introduction
    """
    print("Bienvenue dans le jeu exceptionnel de Pierre-Papier-Ciseaux !")
    print("Ce jeu fait rêver petits et grands. Alors vous aussi sans doute...hein ?")
    print("Rappel des règles : Pierre✊ bat Ciseaux✌ , Ciseaux✌ bat Papier✋ , Papier🤚 bat Pierre✊.")
    print("Vous allez jouer avec l'ordinateur. Que la chance soit avec vous !")
    
def game() -> None:
    """To run the game
    """
    global isGameRunning
    global playerScore
    global opponentScore

    while isGameRunning:
        playerChoice = player.choice(choicesKeys)
        if playerChoice == "q":
            showScores(isLastTime=True)
            isGameRunning = False
        else:
            opponentChoice = opponent.choice(choicesKeys)
            whoWins(playerChoice, opponentChoice)

def whoWins(playerChoice: str, opponentChoice: str) -> None:
    """To define who won the round

    Args:
        playerChoice (str): choice made by the player
        opponentChoice (str): choice made by the opponent
    """
    global playerScore
    global opponentScore
    global choicesDict
    global choicesKeys
        
    if playerChoice == opponentChoice:
        print(f"Vous avez tous les deux choisis {choicesDict[playerChoice]} ! C'est une égalité !")
    elif (playerChoice == choicesKeys[0] and opponentChoice == choicesKeys[2]) or (playerChoice == choicesKeys[1] and opponentChoice == choicesKeys[0]) or (playerChoice == choicesKeys[2] and opponentChoice == choicesKeys[1]):
        playerScore += 1
        print(f"✅ Vous avez gagné un point ! L'ordi avait choisi {choicesDict[opponentChoice]} et vous l'avez battu avec {choicesDict[playerChoice]} !")
    else:
        opponentScore += 1
        print(f"❌ Perdu ! Vous avez choisi {choicesDict[playerChoice]} et l'ordi vous a battu avec {choicesDict[opponentChoice]}...")
    showScores()
    return
    
def showScores(isLastTime: bool = False) -> None:
    """To show the current scores

    Args:
        isLastTime (bool, optional): if True, adds text. Defaults to False.
    """
    if isLastTime:
        print("Scores finaux :")
    print(f"Votre score : {playerScore} | Score de l'ordi : {opponentScore}")