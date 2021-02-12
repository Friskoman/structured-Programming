checkt hij die code, en als dat 4 zwarte pionnen geeft is het klaarimport random
global solution
solution = []
global turns
turns = 0
SpellerKeuze = 0

def MainMenu():
    """
MainMenu is waar de keuzen maakt voor hoe je het spel wilt spelen
    :rtype: object
    """
    print(f'welkom bij MasterMind \n' 
          f'Kies een GameMode \n' 
          f'\n' 
          f'1. PvP (working progress)\n' 
          f'2. PvC \n'
          f'3. CvC \n')
    GameMode1 = int(input())#selecten the playing style
    if GameMode1 == 1:
        PvP()
    if GameMode1 == 2:
        PvC()
    if GameMode1 == 3:
        CvC()


def PvP():
    """
PvP player tegen player alle volgende menu's wordewn ingesteld op dat alle shandmatig wordt ingevoerd
    :rtype: object
    """
    Player = True
    generateCode(Player)

def PvC():
    """
 PvC Player tegen computer je moet zelf een rol kiezen waarna je wordt geleid naar het menu waar jij op speelt
    :rtype: object
    """
    global SpellerKeuze
    print(f'Welke Rol wil je nemen? \n'
          f'1. CodeCracker \n'
          f'2. CodeMaster \n')
    SpellerKeuze = int(input())#selecting what rol you want as player
    if SpellerKeuze == 1:
        Player = False
    elif SpellerKeuze == 2:
        Player = True
    else:
        print('Pleas pick between the given options')
        PvC()
    generateCode(Player)



def CvC():
    """
    CvC is Computer tegen Computer dus zowel de Solution als de Attempt worden gedaan door de computer
    :rtype: object
    """
    Player = False
    generateCode(Player)

def generateCode(Player):
    """
generateCode is de functie waar de solution aangemaakt wordt
dit wordt gedaan door de computer die een lijst van 4 lang maakt en voor elke plek een random getal generert tussen 0 en 5
of je mag zelf de code bepalen dit moet je dan zelf in vullen (1 voor 1) of je dit zelf moet doen ligt aan de keuzen die je in menu 2 hebt gemaakt
    :rtype: object
    """
    if Player == False:#computer random generated code
        for i in range(0,4):
            code = random.randint(0,5)
            solution.append(code)
        print('The secret Code is:', solution)
        GetAttempt()
    elif Player == True:#player self made code
        while len(solution) != 4:
            CodeInput = int(input('Maak een code van 4 lang tussen 0 en 5'))
            if CodeInput >= 6 or CodeInput <= -1:
                print('Tussen 0 en 5!')
            else:
                solution.append(CodeInput)
        print('The secret Code is:', solution)
        GetAttempt()

def game():
    """
game vindt plaats in een loop van 10 beurten, in die loop genereert hij een code
checkt hij die code, en als dat 4 zwarte pionnen geeft is het klaar
    :rtype: object
    """
    global solution
    turn = 0
    while turn < 10:
        attempt = GetAttempt()
        black, white = check(attempt, solution)
        if black == 4:
            print('won with attempt', attempt, 'for solution', solution )
            break
        turn += 1

def check(solution, attempt):
    """
er wordt gekeken naar de 2 lijsten solution en attempt
als de positie en de getal op de positie het zelfde zijn wordt er bij black + 1 gedaan
als het getal wel in de lijst voorkomt maar niet op de juiste plaats staat wordt het volgende de gedaan
    als het getal vaker in de ene lijst dan de andere lijst voor komt wordt alleen wit + zo vaak gedaan als hij het minst voorkomt in een van de lijsten
    mocht dat toch evenveel zijn wordt het gewoon + de hoeveelheid hij voor komt gedaan
    :rtype: object
    """
    black = 0
    white = 0
    if solution != attempt:
        for i in range(len(solution)):
            if attempt[i] == solution[i]:
                black += 1
                attempt[i] = None
                solution[i] = None
        for i in range(5):
            if i in (attempt and solution):
                if solution.count(i) > attempt.count(i):
                    white += attempt.count(i)
                elif attempt.count(i) > solution.count(i):
                    white += solution.count(i)
                elif attempt.count(i) == solution.count(i):
                    white += attempt.count(i)
        print(black, 'black pigs', white, 'white pigs')
        game()
    else:
        print('gefeliciteerd je hebt de code gekraakt')


def GetAttempt():
    """
    hier wordt de attempt aan gemaakt door de speller of door de computer
    dit hangt af van de keuze die je in menu 2 hebt gemaakt
    bij de computer wordt er een random lijst gegenereert tussen 0 en 5 van 4 lang
    bij je zelf wordt wer een code gevraagt van 4 lang tussen 0 en 5 1 voor 1 moet je hem invullen
    :rtype: object
    """
    attempt = []
    if SpellerKeuze == 2:
        for i in range(0, 4):
            code = random.randint(0, 5)
            attempt.append(code)
        check(solution, attempt)
        print(attempt)
    elif SpellerKeuze == 1:
        for i in range(len(solution)):
            userCode = int(input('wat denk jij dat de code is?(1 voor 1)'))
            attempt.append(userCode)
        check(solution, attempt)


MainMenu()
