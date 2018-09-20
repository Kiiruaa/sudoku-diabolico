import copy
import os
from operator import itemgetter
#pos1 = copy.deepcopy(pos) # copier une liste d'objets

def creer_sudoku() :
    sudoku = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
    for x in range(0,8+1) :
        for y in range(0,8+1) :
            sudoku[x][y] = [1,2,3,4,5,6,7,8,9]
    return sudoku

def print_sudoku(sudoku) :
    for y in range(0,8+1) :
        print(" ",format_case(sudoku[0][y]),format_case(sudoku[1][y]),format_case(sudoku[2][y])," ",format_case(sudoku[3][y]),format_case(sudoku[4][y]),format_case(sudoku[5][y])," ",format_case(sudoku[6][y]),format_case(sudoku[7][y]),format_case(sudoku[8][y]))
        if y == 2 or y == 5 or y == 8 :
            print(" ")
    print("===========================================")
    print(" ")

def format_case(table) :
    if len(table) > 1 :
        return "[ ]"
    elif len(table) == 1 :
        return table

def sudoku_valide(sudoku) :
    for x1 in range(0,8+1) :
         for y1 in range(0,8+1) :
             if sudoku[x1][y1] == [] :
                 return False
    return True

def ligne(sudoku) :
    for x1 in range(0,8+1) :
         for y1 in range(0,8+1) :
             
            for x in range(0,8+1) :
                 if x != x1 and len(sudoku[x][y1]) == 1 and sudoku[x1][y1].count(sudoku[x][y1][0]) == 1 :
                     sudoku[x1][y1].remove(sudoku[x][y1][0])

            for y in range(0,8+1) :
                 if y != y1 and len(sudoku[x1][y]) == 1 and sudoku[x1][y1].count(sudoku[x1][y][0]) == 1 :
                     sudoku[x1][y1].remove(sudoku[x1][y][0])
                     
def range_region(a) :
    if a >= 0 and a <= 2 :
        return range(0,2+1)
    elif a >= 3 and a <= 5 :
        return range(3,5+1)
    elif a >= 6 and a <= 8 :
        return range(6,8+1)

def region(sudoku) :
    for x1 in range(0,8+1) :
         for y1 in range(0,8+1) :

            for x in range_region(x1) :
                for y in range_region(y1) :
                    if ( x != x1 or y != y1 ) and len(sudoku[x][y]) == 1 and sudoku[x1][y1].count(sudoku[x][y][0]) == 1 :
                        sudoku[x1][y1].remove(sudoku[x][y][0])

def ligne_exclusif(sudoku) :
    for x1 in range(0,8+1) :
        for y1 in range(0,8+1) :
            
            if len(sudoku[x1][y1]) > 1 :
                table = []
                for k in range(0,len(sudoku[x1][y1])) :
                    a = 0
                    for x in range(0,8+1) :
                        if x != x1 and sudoku[x][y1].count(sudoku[x1][y1][k]) == 1 :
                            a = 1
                            break
                    if a == 0 :
                        table.insert( len(table), sudoku[x1][y1][k])
                if len(table) == 1 :
                    sudoku[x1][y1] = [ table[0] ]

                table = []
                for k in range(0,len(sudoku[x1][y1])) :
                    a = 0
                    for y in range(0,8+1) :
                        if y != y1 and sudoku[x1][y].count(sudoku[x1][y1][k]) == 1 :
                            a = 1
                            break
                    if a == 0 :
                        table.insert( len(table), sudoku[x1][y1][k])
                if len(table) == 1 :
                    sudoku[x1][y1] = [ table[0] ]

def region_exclusif(sudoku) :
    for x1 in range(0,8+1) :
        for y1 in range(0,8+1) :
            
            table = []
            if len(sudoku[x1][y1]) > 1 :
                for k in range(0,len(sudoku[x1][y1])) :
                    a = 0
                    for x in range_region(x1) :
                        for y in range_region(y1) :
                            if ( x != x1 or y != y1 ) and sudoku[x][y].count(sudoku[x1][y1][k]) == 1 :
                                a = 1
                                break
                    if a == 0 :
                        table.insert(len(table), sudoku[x1][y1][k])
                if len(table) == 1 :
                    sudoku[x1][y1] = [ table[0] ]

def ligne_paire_exclusif(sudoku) :
    for x1 in range(0,8+1) :
        for y1 in range(0,8+1) :
            if len(sudoku[x1][y1]) == 2 :
                    pair = False
                    for x in range(0,8+1) :
                        if x != x1 and len(sudoku[x][y1]) == 2 and sudoku[x][y1].count(sudoku[x1][y1][0]) == 1 and sudoku[x][y1].count(sudoku[x1][y1][1]) == 1 :
                            pair = True
                            pair2x = x
                            break
                    if pair == True :
                        for x in range(0,8+1) :
                            if x != x1 and x != pair2x and len(sudoku[x][y1]) > 1 :
                                if sudoku[x][y1].count(sudoku[x1][y1][0]) == 1 and len(sudoku[x][y1]) > 1 :
                                    sudoku[x][y1].remove(sudoku[x1][y1][0])
                                if sudoku[x][y1].count(sudoku[x1][y1][1]) == 1 and len(sudoku[x][y1]) > 1 :
                                    sudoku[x][y1].remove(sudoku[x1][y1][1])

                    pair = False
                    for y in range(0,8+1) :
                        if y != y1 and len(sudoku[x1][y]) == 2 and sudoku[x1][y].count(sudoku[x1][y1][0]) == 1 and sudoku[x1][y].count(sudoku[x1][y1][1]) == 1 :
                            pair = True
                            pair2y = y
                            break
                    if pair == True :
                        for y in range(0,8+1) :
                            if y != y1 and y != pair2y and len(sudoku[x1][y]) > 1 :
                                if sudoku[x1][y].count(sudoku[x1][y1][0]) == 1 and len(sudoku[x1][y]) > 1 :
                                    sudoku[x1][y].remove(sudoku[x1][y1][0])
                                if sudoku[x1][y].count(sudoku[x1][y1][1]) == 1 and len(sudoku[x1][y]) > 1 :
                                    sudoku[x1][y].remove(sudoku[x1][y1][1])

def region_paire_exclusif(sudoku) :
    for x1 in range(0,8+1) :
        for y1 in range(0,8+1) :
            #table = []
            #pair = False
            if len(sudoku[x1][y1]) == 2 :
                    pair = False
                    for x in range_region(x1) :
                        for y in range_region(y1) :
                            if ( x != x1 or y != y1 ) and len(sudoku[x][y]) == 2 and sudoku[x][y].count(sudoku[x1][y1][0]) == 1 and sudoku[x][y].count(sudoku[x1][y1][1]) == 1 :
                                pair = True
                                pair2x = x
                                pair2y = y
                                break
                            
                    if pair == True :
                        for x in range_region(x1) :
                            for y in range_region(y1) :
                                if ( x != x1 or y != y1 ) and ( x != pair2x or y != pair2y ) and len(sudoku[x][y]) > 1 :
                                    if sudoku[x][y].count(sudoku[x1][y1][0]) == 1 and len(sudoku[x][y]) > 1 :
                                        sudoku[x][y].remove(sudoku[x1][y1][0])
                                    if sudoku[x][y].count(sudoku[x1][y1][1]) == 1 and len(sudoku[x][y]) > 1 :
                                        sudoku[x][y].remove(sudoku[x1][y1][1])
                                        
#table_choix = [ [ x1,y1,len(table1),table1=[] ] , [ x2,y2,len(table2),table2=[] ] , [ x3,y3,len(table3),table3=[] ] ]
#table_choix[0]         ->  [ x1,y1,table1=[] ]
#table_choix[0][0]      ->  x1
#table_choix[0][1]      ->  y1
#table_choix[0][2]      ->  len(table1) taille table1                                     
#table_choix[0][3]      ->  table1 = [a1,a2,a3,a4]
#table_choix[0][3][0]   ->  a1
#list.append(obj)       -> ajoute l'object obj to list

def creer_table_choix(sudoku):
    table_choix = []
    for x1 in range(0,8+1) :
        for y1 in range(0,8+1) :
            if len(sudoku[x1][y1]) > 1 :
                table_choix.append([x1,y1,len(sudoku[x1][y1]),sudoku[x1][y1]])
    table_choix = sorted(table_choix, key=itemgetter(2))
    return table_choix

def choix_multiples(sudoku) :
    #print("diabolico")
    #diabolico_sudoku = copy.deepcopy(sudoku)
    table_choix = creer_table_choix(sudoku)
    fin = False
    n = 0
    while fin == False and n < len(table_choix) :
        xdiabolico = table_choix[n][0]
        ydiabolico = table_choix[n][1]
        v = 0
        while fin == False and v < len(table_choix[n][3]) :
            diabolico_sudoku = copy.deepcopy(sudoku)
            value_diabolico = table_choix[n][3][v]
            diabolico_sudoku[xdiabolico][ydiabolico] = [ value_diabolico ]
            fin = resoudre(diabolico_sudoku)
            v = v+1
        n = n+1
    return fin 

def sudoku_finis(sudoku) :
    for x1 in range(0,8+1) :
         for y1 in range(0,8+1) :
             if len(sudoku[x1][y1]) != 1 :
                 return False
    return True

def resoudre(sudo) :
    sudoku = copy.deepcopy(sudo) # Pour ne pas modifier le sudoku non rempli
##    os.system('cls')
##    print_sudoku(sudoku)
##    os.system('pause')
    
    old_sudoku = []
    while sudoku_finis(sudoku) == False and sudoku_valide(sudoku) and old_sudoku != sudoku :
        old_sudoku = copy.deepcopy(sudoku)
        ligne(sudoku)
        region(sudoku)
        ligne_exclusif(sudoku)
        region_exclusif(sudoku)
        ligne_paire_exclusif(sudoku)
        region_paire_exclusif(sudoku)
        
        #os.system('cls')
        #print_sudoku(sudoku)
        #os.system('pause')
    
    if sudoku_finis(sudoku) :
        fin = sudoku
    elif sudoku_valide(sudoku) == False :
        fin = False
    elif old_sudoku == sudoku :
        fin = choix_multiples(sudoku)
    return fin

def string_remplir(sudoku,string,y) :
    for x in range(0,len(string)) :
        if string[x] != "0" : 
            sudoku[x][y] = [ int(string[x]) ]

pos = creer_sudoku()

##string_remplir(pos,"070000000",0)
##string_remplir(pos,"900400000",1)
##string_remplir(pos,"000000506",2)
##string_remplir(pos,"800904000",3)
##string_remplir(pos,"060030280",4)
##string_remplir(pos,"510000430",5)
##string_remplir(pos,"100080000",6)
##string_remplir(pos,"002003910",7)
##string_remplir(pos,"040060800",8)

##string_remplir(pos,"021080350",0)
##string_remplir(pos,"060910000",1)
##string_remplir(pos,"000020610",2)
##string_remplir(pos,"008279160",3)
##string_remplir(pos,"600531002",4)
##string_remplir(pos,"210468905",5)
##string_remplir(pos,"006040500",6)
##string_remplir(pos,"745090000",7)
##string_remplir(pos,"182050496",8)

##string_remplir(pos,"050400108",0)
##string_remplir(pos,"000035000",1)
##string_remplir(pos,"009080500",2)
##string_remplir(pos,"296310005",3)
##string_remplir(pos,"003650010",4)
##string_remplir(pos,"175800300",5)
##string_remplir(pos,"900203051",6)
##string_remplir(pos,"000501903",7)
##string_remplir(pos,"531978200",8)

##string_remplir(pos,"000020000",0) ## difficile
##string_remplir(pos,"750000000",1)
##string_remplir(pos,"038605000",2)
##string_remplir(pos,"003956017",3)
##string_remplir(pos,"000004020",4)
##string_remplir(pos,"090001400",5)
##string_remplir(pos,"000500260",6)
##string_remplir(pos,"300100054",7)
##string_remplir(pos,"800070100",8)

##string_remplir(pos,"048090370",0) ## diabolique facile
##string_remplir(pos,"009000500",1)
##string_remplir(pos,"000863000",2)
##string_remplir(pos,"084000210",3)
##string_remplir(pos,"030271040",4)
##string_remplir(pos,"000000000",5)
##string_remplir(pos,"800406005",6)
##string_remplir(pos,"001000900",7)
##string_remplir(pos,"007000400",8)

string_remplir(pos,"100007090",0) ## diabolique "AI Escargot"
string_remplir(pos,"030020008",1) ## le plus difficile des sudoku
string_remplir(pos,"009600500",2)
string_remplir(pos,"005300900",3)
string_remplir(pos,"010080002",4)
string_remplir(pos,"600004000",5)
string_remplir(pos,"300000010",6)
string_remplir(pos,"040000007",7)
string_remplir(pos,"007000300",8)

sudoku_resolu = resoudre(pos)

print_sudoku(pos) ## sudoku de départ
print_sudoku(sudoku_resolu)

#os.system('pause')

