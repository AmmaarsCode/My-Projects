class Question:
  question_text=""
  answer=""

  def AskQuestion(self):
    print(self.question_text)
    
    uinput=input("Answer: ")

    if (self.answer==uinput):
      print("GOOD WORK")
      return True
    else:
      print("WRONG "+self.answer+".")
      return False
class Game:
  question_list=[]

  def CreateQuestion(self,question,answer):
    new_question=Question()
    new_question.question_text=question
    new_question.answer=answer
    self.question_list.append(new_question)

  def Run(self):

    for i in range(len(self.question_list)):
      print()
      print("QUESTION",i+1)
      result=self.question_list[i].AskQuestion()
      result

def GetChoice(min,max):
  choice=int(input("Enter a number from the list: "))
  while(choice<1 or choice>2):
    print("INVALID")
    choice=int(input("Enter a number from the list: "))
  return choice
  
def Menu():
  print("WELCOME TO THE GAME!")
  print("1. START THE GAME")
  print("2. LEAVE THE GAME")
  print("\n")

start=True
print("HOW TO TAKE CARE OF A PET!")

while(start):
  Menu()
  choice=GetChoice(1,2)
  if(choice==1):
    the_game=Game()
    the_game.CreateQuestion("Your pet is in need of water, do you get them water?  YES OR NO","YES")
  
    the_game.CreateQuestion("Your pet is stuck in a tree, do you help them? YES OR NO","YES")
  
    the_game.CreateQuestion("Yout pet is sad, do you cheer them up? YES OR NO", "YES")
    the_game.Run()
  
  elif (choice==2):
    start=False
print("\n")
print("GOODBYE")