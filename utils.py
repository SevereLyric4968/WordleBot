from rich.live import Live
from rich.panel import Panel
from rich.console import Group
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TimeElapsedColumn
import time

def displayBoard(board,guesses):
    emoji_map = {3:"⬜", 2:"🟩", 1:"🟨", 0:"⬛"}
    lines=[]

    for i,row in enumerate(board):
        colours="".join(emoji_map[i] for i in row)
        word=guesses[i] if i<len(guesses) else ""
        lines.append(f"{colours}  {word}")

    return("\n".join(lines))

def buildGamePanels():
    pass
    panels=[]
    for i, state in enumerate(gameStates):
        board=state["board"]
        guesses=state["guesses"]
        content=displayBoard(board,guesses)
        panels.append(Panel(content,title=f"Game {i+1}"))
    return Group(*panels)

def updatePanel(guess,board):
    pass
    state["board"]=board
    state["guesses"]=guess

