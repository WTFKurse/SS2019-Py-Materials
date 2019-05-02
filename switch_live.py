def main():
  name = input("Bitte gib deinen Vornamen ein.\nEingabe: ")

  switch = {
    "Jannusch" : bigge,
    "Patrik": phan,
    "Kevin": schmid
  }

  switch[name]()

def bigge():
  print("Hallo Herr Bigge.")


def phan():
  print("Hallo Herr Phan")


def schmid():
  print("Hallo Herr Schmid")


if __name__ == "__main__":
  main()
