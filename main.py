from datetime import datetime


def buildVersete():
    now = datetime.now()

    chapter = now.year - 2000 + now.month + now.day
    versete = now.month + now.day + now.hour + now.minute + now.second

    return f"🤣UPAKO {chapter}:{versete} 🤣"


def main():
    versete = buildVersete()

    print(versete)

if __name__ == "__main__":
    main()