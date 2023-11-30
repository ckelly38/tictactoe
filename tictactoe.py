#save the game
#read the game in
#want to be able to edit a position
#need to be able to display the board to the user
#-------
#|-|-|-|
#|-+-+-|
#|-|-|-|
#|-+-+-|
#|-|-|-|
#-------
import os;
class TicTacToe:
    def __init__(self):
        self.game = self.initGame();
        if (self.isValidGame()): self.playGame(self.startWithX());
        else:
            print("game.txt contains invalid characters and is corrupted, so removing it now!");
            os.remove("game.txt");
            self.game = [["-" for c in range(3)] for r in range(3)];
            self.playGame(True);
        

    def printGame(self):
        print("-------");
        for r in range(len(self.game)):
            for c in range(len(self.game[0])): 
                print("|" + self.game[r][c], end="");
            print("|");
            if (r + 1 < len(self.game)): print("|-+-+-|");
        print("-------");

    def getNumXsOrOs(self, usexs):
        typestr = "";
        if (usexs): typestr = "x";
        else: typestr = "o";
        cnt = 0;
        for r in range(3):
            for c in range(3):
                if (self.game[r][c] == typestr): cnt += 1;
        return cnt;

    def getNumXs(self): return self.getNumXsOrOs(True);

    def getNumOs(self): return self.getNumXsOrOs(False);

    def isValidGame(self):
        numxs = self.getNumXs();
        numos = self.getNumOs();
        print(f"numxs = {numxs}");
        print(f"numos = {numos}");
        #they can both be 0
        if (numxs < 0 or numos < 0 or numxs > 5 or numos > 5 or 9 < numxs + numos): return False;
        if (numxs == numos or numxs == numos + 1): pass;
        else: return False;
        if (self.isGameOver()): return False;
        else: return True;

    def startWithX(self):
        numxs = self.getNumXs();
        numos = self.getNumOs();
        print(f"numxs = {numxs}");
        print(f"numos = {numos}");
        return (numxs == numos);

    def initGame(self):
        mgame = [["-" for c in range(3)] for r in range(3)];
        ival = -1;
        while(True):
            ival = self.getIntegerInput("Do you want to load in a file (1) or play a new game (0): ");
            if (ival == 0 or ival == 1): break;
            else: print("invalid answer you must enter 1 or 0!");
        if (ival == 1): pass;
        elif (ival == 0): return mgame;
        else: raise Exception("invalid value found and used here for ival!");
        lines = [];
        try:
            with open("game.txt", "r") as mfile:
                lines = mfile.readlines();
                mfile.close();
        except:
            print("there was a problem opening or reading game.txt! Playing a new game it is!");
            return mgame;
        print(f"lines = {lines}");
        issafe = True;
        for n in range(len(lines)):
            for i in range(len(lines[n])):
                if (i < 3):
                    if (lines[n][i] in ["x", "o", "-"]): mgame[n][i] = lines[n][i];
                    else:
                        issafe = False;
                        break;
            if (issafe): pass;
            else: break;
        if (issafe): pass;
        else:
            print("game.txt contains invalid characters and is corrupted, so removing it now!");
            mgame = [["-" for c in range(3)] for r in range(3)];
            os.remove("game.txt");
        return mgame;

    def getIntegerInput(self, msg):
        r = -1;
        while(True):
            try:
                r = int(input(msg));
                return r;
            except:
                print("Error: it must be a number!");
        return r;

    def getRowOrColFromUser(self, userow):
        r = -1;
        typestr = "";
        if (userow): typestr = "row";
        else: typestr = "col";
        while(True):
            r = self.getIntegerInput("Enter " + typestr + ": ");
            if (r < 0 or 2 < r):
                print("Error: " + typestr + " must be less than 3 and greater than or equal to 0!");
                ival = self.getIntegerInput("Do you want to exit (0), or continue (1): ");
                if (ival == 0): exit();
            else: return r;
        return r;

    def getRowFromUser(self): return self.getRowOrColFromUser(True);

    def getColFromUser(self): return self.getRowOrColFromUser(False);

    def turn(self, isxturn):
        self.printGame();
        r = self.getRowFromUser();
        c = self.getColFromUser();
        print("r = " + str(r));
        print("c = " + str(c));
        print("isxturn = " + str(isxturn));
        if (self.game[r][c] == "-"):
            if (isxturn): self.game[r][c] = "x";
            else: self.game[r][c] = "o";
            ival = -1;
            if (self.isGameOver()): ival = 1;
            else:
                ival = self.getIntegerInput("Do you want to exit and save for later (0), or " +
                                            "continue (1): ");
            if (ival == 0): self.saveAndExit();
        else:
            print("Already used! Please pick a different spot!");
            ival = -1;
            if (self.isGameOver()): ival = 1;
            else:
                ival = self.getIntegerInput("Do you want to exit and save for later (0), or resume (1): ");
            if (ival == 0): self.saveAndExit();
            else: self.turn(isxturn);
        print("end of turn!");

    def areAllSpotsFilled(self):
        for r in range(3):
            for c in range(3):
                if (self.game[r][c] == "x" or self.game[r][c] == "o"): pass;
                else: return False;
        return True;

    def isThereAColWinner(self):
        for c in range(3):
            for n in range(2):
                turnstr = "";
                if (n == 0): turnstr = "x";
                else: turnstr = "o";
                allsame = True;
                for r in range(3):
                    if (self.game[r][c] == turnstr): pass;
                    else:
                        allsame = False;
                        break;
                if (allsame): return True;
        return False;

    def isThereARowWinner(self):
        for r in range(3):
            for n in range(2):
                turnstr = "";
                if (n == 0): turnstr = "x";
                else: turnstr = "o";
                allsame = True;
                for c in range(3):
                    if (self.game[r][c] == turnstr): pass;
                    else:
                        allsame = False;
                        break;
                if (allsame): return True;
        return False;

    def isThereADiagnalWinner(self):
        for k in range(2):
            for n in range(2):
                turnstr = "";
                if (n == 0): turnstr = "x";
                else: turnstr = "o";
                allsame = True;
                for r in range(3):
                    rval = -1;
                    if (k == 0): rval = r;
                    else: rval = 2 - r;
                    if (self.game[rval][r] == turnstr): pass;
                    else:
                        allsame = False;
                        break;
                if (allsame): return True;
        return False;

    def isThereAWinner(self):
        return (self.isThereAColWinner() or self.isThereARowWinner() or self.isThereADiagnalWinner());

    def isGameOver(self):
        #if all spots are filled with xs or os -> yes
        #if x wins or o wins -> yes
        #otherwise -> no
        return (self.isThereAWinner() or self.areAllSpotsFilled());


    def playGame(self, initisxturn = True):
        isxturn = initisxturn;
        if (isxturn): print("x starts!");
        else: print("o starts!");
        while (not self.isGameOver()):
            self.turn(isxturn);
            isxturn = not isxturn;
        self.printGame();
        if (self.isThereAWinner()):
            if (isxturn): print("o wins!");
            else: print("x wins!");
        else: print("cat wins!");
        try:
            os.remove("game.txt");
        except:
            pass;
    
    def saveAndExit(self):
        with open("game.txt", "w") as mfile:
            for r in range(3):
                for c in range(3):
                    mfile.write(self.game[r][c]);
                mfile.write("\n");
            mfile.close();
        exit();

myg = TicTacToe();
#myg.playGame();
