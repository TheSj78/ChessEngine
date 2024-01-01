from stockfish import Stockfish
import bs4
import requests
from colorama import Fore

sf = Stockfish('C:\D$\Junior Year\Random\ChessEngine\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe')
sf.set_elo_rating(3500)
sf.set_depth(5)
    
res = input("Enter the URL: ")
char = input("Enter color: b or w: ")

def getFen():
    req = requests.get(res)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    soup = soup.find_all('script')[3]
    soupStr = str(soup)

    fen = soupStr[soupStr.rindex('fen'): len(soupStr)]
    fen = fen[fen.index(':"')+2: fen.index('}')-1]
    return fen

while True:
    try:
        fen = getFen()
        temp = fen
        #print(Fore.LIGHTBLACK_EX + fen)

        if (fen.split(" ")[1] == char):
            sf.set_fen_position(fen) # setting the position
            bestMove = sf.get_best_move()
            print(Fore.GREEN + 'Your best move: ' + str(bestMove) + Fore.RESET)

        while fen == temp: #keep checking while the fen doesn't change
            temp = getFen()

    except:
        print(Fore.YELLOW + '\n\nDoesn\'t work right now!\n\n' + Fore.RESET)
        break
    