import random
import time
    
    
class game_start:
    sleep_between_actions = 1
    list_of_snakes = {17:10,54:20,62:43,64:4,87:63,93:20,95:20,99:21}
    list_of_ladders = {4:10,9:22,20:18,28:56,40:19,51:16,63:18,71:20}
    fscore = 0
    sscore = 0
    def __init__(self,fname="user_1",sname="user_2"):
        self.fname = fname
        self.sname = sname
        self.fname_score = 0
        self.sname_score = 0
        self.count_1 = 0
        self.count_2 = 0
        self.c = 0
      #  print( '''~~~~~~~~>WELCOME TO SNAKE AND LADDER ###
       # @@==========================@@
                                         
       # Rules :
        #------   
        #    1. If The player will get 6 at starting then only he will enter the game.
        #    2. If the player get exact 100 points then only player wins.
        #    3. when you will get snake your score will decrease based on the snake.
        #    4. when you will get ladder your score will increase based on the ladder.
            
            
            
         #   ''')
            
        print("**** MATCH PLAYERS BETWEEN {} AND {} ***".format(self.fname,self.sname))

        print('-------------------------------------------------------')
                                            
        while(True):
            
            first_player_rolling_dice = random.randint(1,6)
            #print(first_player_rolling_dice)
            
            if first_player_rolling_dice == 6:
                self.count_1 = 1
            
        
            if self.count_1 == 1:
                #print(self.fname ,'entering the game===============')
                self.fscore = self.rolling_dice()
                self.fname_score += self.fscore
                print('fnamescore is',self.fname_score)
                
                if self.fname_score in self.list_of_snakes.keys():
                    self.fname_score -= self.hitting_snake(self.fname_score)
                    
                    print("{} oh!! no ~~~~>snake hitted {}".format(self.fname,self.fname_score))
                    
                if self.fname_score in self.list_of_ladders.keys():
                    self.fname_score += self.climb_ladder(self.fname_score)
                    
                    print(" woww {} is on ladder {}".format(self.fname,self.fname_score))
                    
                
                
            second_player_rolling_dice = random.randint(1,6)
            
            #print(second_player_rolling_dice)
            
            
            if second_player_rolling_dice == 6:
                self.count_2 = 1
                
            if self.count_2 == 1:
                #print(self.sname ,'entering the game===============')
                self.sscore = self.rolling_dice()
                self.sname_score += self.sscore
                print('sname score is',self.sname_score)
                
                if self.sname_score in self.list_of_snakes:
                    self.sname_score -= self.hitting_snake(self.sname_score)
                    
                    print("{} oh!! no ~~~~>snake hitted {}".format(self.sname,self.sname_score))
                    
                
                if self.sname_score in self.list_of_ladders:
                    self.sname_score += self.climb_ladder(self.sname_score)
                    
                    print(" woww {} is on ladder {}".format(self.sname,self.sname_score))
                    
                
                
            if 94 <= self.fname_score and self.fname_score <= 100:
                if self.fname_score == 100:
                    print("{} won the match".format(self.fname))
                    c = 1
                    break
                else:
                    self.fname_score = self.fname_score
            elif 100 < self.fname_score and self.fname_score <= 105:
                self.fname_score = self.fname_score - self.fscore
            
            if 94 <= self.sname_score and self.sname_score <= 100:
                if self.sname_score == 100:
                    print("{} won the match".format(self.sname))
                    c = 1
                    break 
                else:
                    self.sname_score = self.sname_score
            elif 100 < self.sname_score and 105 >= self.sname_score:
                self.sname_score = self.sname_score - self.sscore
            
        if c == 1:
            print(self.fname_score)
            print(self.sname_score)
            
            
            
            
    def rolling_dice(self):
        time.sleep(self.sleep_between_actions)
        return random.randint(1,6)
    
    def hitting_snake(self,snake_no):
        return self.list_of_snakes[snake_no]
        
    
    
    
    def climb_ladder(self,ladder_no):
        return self.list_of_ladders[ladder_no]
        
        
if __name__ == "__main__":
    game = game_start('rakesh','mahesh')
