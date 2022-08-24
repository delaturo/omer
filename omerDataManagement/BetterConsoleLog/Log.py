
# REFERENCE: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

PROGRESS_MAX_VALUE = 0
PROGRESS_IN_PROGRESS = False
PROGRESS_BAR_SIZE = 20
PROGRESS_ANIMATION_STATE = 0

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def log(msg, logStyle = style.RESET):
    global PROGRESS_IN_PROGRESS
    if PROGRESS_IN_PROGRESS:
        print("")
        PROGRESS_IN_PROGRESS = False
    if len(msg)>0:
        print(logStyle + msg + style.RESET)

def logAsProgress(msg, progress = None, logStyle = style.RESET, animated = False):
    global PROGRESS_MAX_VALUE, PROGRESS_IN_PROGRESS, PROGRESS_BAR_SIZE, PROGRESS_ANIMATION_STATE
    PROGRESS_IN_PROGRESS = True
    toPrint = ""

    if progress is not None and progress>=0 and progress <= 1:
        completed = int(progress*PROGRESS_BAR_SIZE)
        completed = PROGRESS_BAR_SIZE if completed > PROGRESS_BAR_SIZE else completed
        toPrint = "|" + ("█" * completed) + ("░" * (PROGRESS_BAR_SIZE - completed)) + "| "

    if animated:
        PROGRESS_ANIMATION_STATE = PROGRESS_ANIMATION_STATE+1 if PROGRESS_ANIMATION_STATE<3 else 0
        if PROGRESS_ANIMATION_STATE == 0:
            toPrint += " - "
        elif PROGRESS_ANIMATION_STATE == 1:
            toPrint += " \ "
        elif PROGRESS_ANIMATION_STATE == 2:
            toPrint += " | "
        elif PROGRESS_ANIMATION_STATE == 3:
            toPrint += " / "

    toPrint += msg
    if len(toPrint) > PROGRESS_MAX_VALUE:
        PROGRESS_MAX_VALUE = len(msg) + 12
    missChars = PROGRESS_MAX_VALUE - len(toPrint)
    toPrint += (" " * missChars)
    print(logStyle + toPrint + style.RESET,  end="\r")



