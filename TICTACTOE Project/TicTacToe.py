import random
from time import*
while True:
 print("TIC-TAC-TOE GAME\n\n")
 print("1.PLAY SINGLE GAME")
 print("2.PLAY SERIES")
 print("3.VIEW HIGHSCORE")
 print("4.QUIT\n\n")
 fopen=open("mani.txt","r")
 readd=fopen.read()
 conv=int(readd)
 option=int(input("Enter options:"))
 print("")
 if(option==3):
    fopen=open("mani.txt",'r')
    readd=fopen.read()
    print("\n\n\n")
    print("-------------------------------------------\n\n")
    print("NOTE-->SCORE OF WINNING ONE MATCH IS '10'")
    print("")
    print("HIGHEST SCORE-->",readd)
    fopen.close()
    gopen=open("high.txt",'r')
    lic=gopen.read()
    print(lic)
    print("\n")
    print("-------------------------------------------\n\n\n\n")
    gopen.close()
 else: 
   if(option==4):
     break
   while True:
    win1=0;win2=0;mat=0;ext1='n';ext2='n'
    if(option==2):
      ply1=input("Enter Player 1 name:")
      print("")
      ply2=input("Enter Player 2 name:")
      print("")
      length=int(input("Enter How Many Matches to Play:"))
      print("")
      print("                                       -->[PRESS 10 TO QUIT GAME]")
      print("")
    elif(option==1):
      ply1=input("Enter Player 1 name:")
      print("")
      ply2=input("Enter Player 2 name:")
      print("")
      print("                                       -->[PRESS 10 TO QUIT GAME]")
      print("")
      length=1
    for leng in range(length):
      fopen=open("mani.txt","r")
      readd=fopen.read()
      conv=int(readd)
      r1=random.randint(1,2)
      print("----------------------TIC-TAC-TOE GAME--------------------------\n\n")
      print("COIN TOSSING",end="")
      for coin in range(4):
        print(".",end="")
        sleep(1)
      print("\n")
      if(r1==1):
        print("{}-->Player1 Won the Toss\n\n".format(ply1.upper()))
        sleep(1)
      elif(r1==2):
        print("{}-->Player2 Won the Toss\n\n".format(ply2.upper()))
        sleep(1)
      mat=mat+1
      b=[0,1,2,3,4,5,6,7,8,9]
      player2=0
      player1=0
      count=0
      k1=0;k=2
      c=[];t1=[];t2=[]
      print("")
      sleep(1)
      if(option==2):
        print("STATUS-->{}-{}\n".format(win1,win2))
        sleep(1)
        print("MATCH-{}".format(mat))
        print("")
        sleep(1)
      elif(option==1):
        print("")
      while True:
          def play(h,player1,player2):
              if(player2==10):
                  ext2=input("Do You Want Quit Game?\nPress 'y' for YES and 'n' for NO:")
                  if(ext2=='y'):
                      print("Player 2 quit the Match")
                      print("Player 1 wins")
                      return 'Fin1'
                  elif(ext2=='n'):
                          print("")
                          player2=int(input("Enter {} [P2] Position:".format(ply2.upper())))
              if(player1==10):
                  ext1=input("Do You Want Quit Game?\nPress 'y' for YES and 'n' for NO:")
                  if(ext1=='y'):
                      print("Player 1 quit the Match")
                      print("Player 2 wins")
                      return 'Fin2'
                  elif(ext1=='n'):
                      print("")
                      player1=int(input("Enter {} [P1] Position:".format(ply1.upper())))
              if(h==75):
                  if player1 in c:
                      while True:
                          print("Invalid Move")
                          print("Please Enter Other Position\n")
                          print("")
                          player1=int(input("Enter {} [P1] Position:".format(ply1.upper())))
                          print("")
                          if player1 not in c:
                              break
                      h=0
              if(h==85):        
                  if player2 in c:
                      while True:
                          print("Invalid Move")
                          print("Please Enter Other Position\n")
                          print("")
                          player2=int(input("Enter {} [P2] Position:".format(ply2.upper())))
                          print("")
                          if player2 not in c:
                              break
                      h=0
              for check in b:
                  if(check==player1):
                      b[check]='X'
                      if(check!=0):
                          c.append(check)
                          t1.append(check)
                  if(check==player2):
                      b[check]='O'
                      if(check!=0):
                          c.append(check)
                          t2.append(check)
              print("------------------------------------")
              print("")
              print("Match Status-->ONGOING\n")
              print("Players Positions-->",c,"\n")
              print("Player1 Positions-->",t1,"\n")
              print("Player2 Positions-->",t2,"\n")
              print("{} |{} |{}".format(b[1],b[2],b[3]))
              print("-------")
              print("{} |{} |{}".format(b[4],b[5],b[6]))
              print("-------")
              print("{} |{} |{}".format(b[7],b[8],b[9]))
              print("\n")
              if((b[1]==b[2]==b[3]=='X') or (b[4]==b[5]==b[6]=='X') or (b[7]==b[8]==b[9]=='X') or (b[1]==b[4]==b[7]=='X') or (b[2]==b[5]==b[8]=='X') or (b[3]==b[6]==b[9]=='X') or (b[1]==b[5]==b[9]=='X') or (b[3]==b[5]==b[7]=='X')):
                      print("MATCH STATUS-->PLAYER1--> {} WON THE GAME".format(ply1.upper()))
                      return 'Finish'
      
              elif((b[1]==b[2]==b[3]=='O') or (b[4]==b[5]==b[6]=='O') or (b[7]==b[8]==b[9]=='O') or (b[1]==b[4]==b[7]=='O') or (b[2]==b[5]==b[8]=='O') or (b[3]==b[6]==b[9]=='O') or (b[1]==b[5]==b[9]=='O') or (b[3]== b[5]==b[7]=='O')):
                      print("MATCH STATUS-->PLAYER2--> {} WON THE GAME".format(ply2.upper()))
                      return 'Finish'
              if(len(c)==9):
                  print("MATCH STATUS-->MATCH TIED")
                  return 'finish'
          h=85
          if(player1==10):
            player1=0
          k=play(h,player1,player2)
          if(k=='Fin1'):
                  win1=win1+1
                  ext2='y'
                  break
          if(k=='Finish'):
                  win2=win2+1
                  break
          if(k=='finish'):
              break
          if(r1==1 or r1==0):
              player1=int(input("Enter {} [P1] Position:".format(ply1.upper())))
              print("\n")
              r1=0
              h=75
              if(player2==10):
                player2=0
              l=play(h,player1,player2)
              if(l=='Fin2'):
                      win2=win2+1
                      ext1='y'
                      break
              if(l=='Finish'):
                      win1=win1+1
                      break
              if(l=='finish'):
                      break
          if(r1==2 or r1==0):
              player2=int(input("Enter {} [P2] Position:".format(ply2.upper())))
              print("\n")
              r1=0
      if(option==2):
        print("STATUS-->{}-{}".format(win1,win2))
        print("")
      if(ext1=='y' or ext2=='y'):
        break
      elif(ext1=='n' or ext2=='n'):
        pass
    if(option==2):
      if(option==2):
        if(win1>win2):
           print("{} Won the Series".format(ply1.upper()))
           print("")
           win1=win1*10
           print("YOUR SCORE IS-->",win1)
           if(win1>conv):
              fopen=open("mani.txt",'w')
              mic=str(win1)
              fopen.write(mic)
              fopen.close()
              gopen=open("high.txt",'w')
              gopen.write(ply1.upper())
              gopen.close()
              fopen=open("mani.txt",'r')
              readd=fopen.read()
              print("---------------------------\n")
              print("HIGHEST SCORE-->",readd)
              fopen.close()
              gopen=open("high.txt",'r')
              lic=gopen.read()
              print(lic)
              print("---------------------------\n")
              gopen.close()
             
        elif(win2>win1):
           print("{} Won the Series".format(ply2.upper()))
           print("")
           win2=win2*10
           print("YOUR SCORE IS-->",win2)
           if(win2>conv):
              fopen=open("mani.txt",'w')
              mic=str(win2)
              fopen.write(mic)
              fopen.close()
              gopen=open("high.txt",'w')
              gopen.write(ply2.upper())
              gopen.close()
              fopen=open("mani.txt",'r')
              readd=fopen.read()
              print("---------------------------\n")
              print("HIGHEST SCORE-->",readd)
              fopen.close()
              gopen=open("high.txt",'r')
              lic=gopen.read()
              print(lic)
              print("---------------------------\n")
              gopen.close()
           
        elif(win1==win2):
           print("MATCH TIED")
           print("")
        
    print("GAME OVER\n")
    again=input("Do You Want to Play again?\nPress 'y' for YES and 'n' for NO:")
    print("")
    print("---------------------------------")
    print("\n")
    if(again=='y'):
          pass
    elif(again=='n'):
          break
      
