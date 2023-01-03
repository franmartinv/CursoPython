#print 
#print

def function1():
  name = input("Whats your name?: ")
  surname = input("Whats your surname?: ")
  
  long_name = f"{name} {surname}"
  
  creator = francisco martin villegas
  
  print(f"Hi {name.title()} {surname.title()}! The creator of this Python script was {creator.title()} :-)")
  
def main():
  function1()

main()
