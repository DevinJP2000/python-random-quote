import random
def primary():
  correct = False
  numquote = 1
  while(correct == False):
    print("How many quotes do you want?")
    try:
      numquote = int(input())
      correct = True
    except:
      print("Sorry, that's not a number.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  while(numquote != 0):
    last = 13
    rnd = random.randint(0, last)

    print(quotes[rnd])
    numquote = numquote - 1

if __name__== "__main__":
  primary()
