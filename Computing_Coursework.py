from tkinter import *
from tkinter import ttk
import tkinter.font as font
root = Tk()

def shortest_route(start,end):
    textvar.set('')
    if start==end:
        verified['text'] = 'Please do not use the same stations.'
        return
    #station storage
    #storage convention --> [list of everything[line1list[station[<line number>,<station number>,<interchange line number(if exists)>,<interchange station number>]][line2list][line3list]...]
    lines=[[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8, 2, 9], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16, 3, 3], [1, 17], [1, 18], [1, 19], [1, 20], [1, 21, 2, 22], [1, 22], [1, 23], [1, 24], [1, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33]], [[2, 1, 3, 6], [2, 2], [2, 3], [2, 4, 4, 1], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9, 1, 8], [2, 10], [2, 11], [2, 12], [2, 13, 3, 12], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [2, 21], [2, 22, 1, 21], [2, 23], [2, 24], [2, 25], [2, 26], [2, 27], [2, 28], [2, 29, 3, 1]], [[3, 1, 2, 29], [3, 2], [3, 3, 1, 16], [3, 4], [3, 5], [3, 6, 2, 1], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12, 2, 13], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17]], [[4, 1, 2, 4], [4, 2], [4, 3]]]
    #all the lines stored starting with EW then CC then NE then CE
    
    #this block is to store all interchanges in a list, will be used later.
    linesCP=lines.copy()     #have to copy because lists like to reference to one another     
    interchanges=[] # this list will be populated with interchanges
    for i in linesCP:
        for j in i:
            if len(j) == 4:     #if it were a normal station it would only have a length of 2
                interchanges.append(j)
                line_no = j[2]
                station_no=j[3]
                linesCP[(line_no-1)][(station_no-1)] = [0,0]    #if i deleted the value it would mess up indexing in the next for loop. 
            else:
                pass

    #basically a brute force   
        
    from itertools import permutations
    time = [[0, 4, 2, 4, 3, 3, 2, 2, 3, 2, 3, 2, 2, 3, 2, 3, 2, 3, 2, 2, 3, 2, 3, 5, 2, 2, 3, 2, 3, 4, 2, 2, 3], [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 5, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3], [0, 4, 0, 1, 2, 3, 1, 1, 2, 3, 1, 2, 3, 2, 2, 2, 3], [0, 2, 2]]
    gates = [[18, 18, 18, 18, 18, 16, 19, 13, 18, 18, 17, 18, 19, 19, 19, 18, 17, 19, 19, 19, 14, 19, 19, 19, 19, 19, 20, 17, 18], [2, 6, 5, 8, 4, 4, 4, 5, 8, 9, 5, 8, 9, 5, 7, 7, 1, 4, 7, 7, 5, 9, 8, 5, 4, 4, 4, 8, 5, 6, 2], [9, 19, 6, 3, 8, 6, 8, 8, 6, 8, 2, 8, 9, 8, 18, 2], [3, 4, 6]]

    #basically a brute force

    length = len(interchanges)      
    total_time=0
    best_time=99999 #the best timing from permutating
    best_route=[] #the best route in the form of the index of the interchanges list
    gate_list=[]
    line_gates=[25,13,25,13] #to find the gates should someone be travelling the opposite way(e.g from dhouby ghaut to habourfront instead of habourfront to dhouby ghaut) the way to find the gate for "this" side from the "other" side is to take the total doors on a train, add 1 and minus the other side gate.
             # ^EW CC NE CE   (continuation) so if x is this side gate, the other side will be = (total doors+1)-x


    current_station = 0   #the current station
    current_line = 0    #the current station used when testing the permutation to see if the interchanges have connecting lines
    invalid = False #a check to escape trying a route permutation should it fail(interchanges don't meet at all)
    start_check = False  #check if the starting station has the same line as the 1st interchange
    end_check = False  #check if the starting station has the same line as the 1st interchange

    key=[] #this key will be permutated to create all possible routes -> [0,1] = [[0],[1],[0,1],[1,0]]
    temp_list=[] #this is a temporary holding list for possible routes
    master=[] #this will be the final list of routes subject to change in the next block

    for l in range(0,length): # this for loop adds numbers in accordance to the ammount of interchanges
        key.append(l)
    all_routes=list(permutations(key)) #creates all possible gate combinations(n!)

    for m in range(0,length):
        for n in all_routes:
            temp_list.clear()
            for o in range(0,(m+1)):    #this for loop is to create the key
                temp_list.append(n[o])
            if temp_list not in master: #check if this route is already stored
                master.append(list(temp_list)) #using list() is necessary so that the lists don't copy each other over and over ruining my precious code



    for p in master: #traversing list of permutations
        
        start_line = [] # have to check if starting station is an interchange
        start_station = []
        end_line = []
        end_station = []
        for ex1 in interchanges: #using ex1 because bug was found so cannot adherd to the alphabetical for loops. Basically this makes the start and end an interchange if the input was an interchange
            if start[0] == ex1[0] and start[1] == ex1[1]:
                start = ex1
            elif start[0] == ex1[2] and start[1] == ex1[3]:
                start = ex1
                
            if end[0] == ex1[0] and end[1] == ex1[1]:
                end = ex1
            elif end[0] == ex1[2] and end[1] == ex1[3]:
                end = ex1



                
        #this block is to validate that the start station and the first interchange is on the same line, if it isn't then skip this permutation
        if interchanges[p[0]][0] == start[0] or interchanges[p[0]][2] == start[0]:      #if the starting station and the first interchange have the same line
            start_line.append(start[0])
            start_station.append(start[1])
            start_check = True
        else:
            try: # if the start station is an interchange
                if interchanges[p[0]][0] == start[2] or interchanges[p[0]][2] == start[2]: # if the starting station is an interchange
                    start_line.append(start[2])
                    start_station.append(start[3])
                    start_check = True
            except:
                pass


        #this block is to validate that the end station and the last interchange is on the same line, if it isn't then skip this permutation
        if interchanges[p[-1]][0] == end[0] or interchanges[p[-1]][2] == end[0]:      #if the starting station and the 
            end_station.append(end[1])
            end_line.append(end[0])
            end_check = True
        else:
            try: # if the end station is an interchange
                if interchanges[p[-1]][0] == end[2] or interchanges[p[-1]][2] == end[2]: # if the starting station is an interchange
                    end_station.append(end[3])
                    end_line.append(end[2])
                    end_check = True
            except:
                pass

        if len(end) == 4:
            if interchanges[p[-1]][0] == end[0] and interchanges[p[-1]][1] == end[1]:
                del p[-1]
            elif interchanges[p[-1]][2] == end[0] and interchanges[p[-1]][3] == end[1]:
                del p[-1]
            else:
                pass


                
        if start_check == True and end_check == True: #continue checking the permutation if the start and end lines have a common line with the first and last interchange accordingly
            for ex in range(len(start_line)): # if the starting station is an interchange, we need to try both sides of the interchange. Using "ex" for the for loop instead of following alphabetical convention because i added this in bugtesting.
                current_line = start_line[ex]
                current_station = start_station[ex]
                

                for q in p: #traversing the combination of the permutation
                    if current_line == interchanges[q][0]:  #if the current line is the same as the 1st line the interchange is on
                        if current_station - interchanges[q][1] < 0:
                            gate_list.append(line_gates[interchanges[q][0]-1]-gates[interchanges[q][0]-1][interchanges[q][1]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
                        else:
                            gate_list.append(gates[interchanges[q][0]-1][interchanges[q][1]-1])
                        if current_station < interchanges[q][1]: # this is to prevent range(9,0) errors
                            for ac in range(current_station,(interchanges[q][1])):  #counting of how much time taken
                                    total_time += time[(current_line-1)][ac]
                        elif current_station > interchanges[q][1]:# this is to prevent range(9,0) errors
                            for ac in range((interchanges[q][1]),current_station):  #counting of how much time taken
                                total_time += time[(current_line-1)][ac]
                        elif current_station == interchanges[q][1]:
                            pass
                        current_line = interchanges[q][2]# change the current line to the one the not the same as the one we compared ~9 lines earlier
                        current_station = interchanges[q][3]# change the current station to the one the not the same as the one we compared ~9 lines earlier
                        
                    elif current_line == interchanges[q][2]:#if the current line is the same as the 2nd line the interchange is on
                        if current_station - interchanges[q][3] < 0:
                            gate_list.append(line_gates[interchanges[q][2]-1]-gates[interchanges[q][2]-1][interchanges[q][3]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
                        else:
                            gate_list.append(gates[interchanges[q][2]-1][interchanges[q][3]-1])
                            
                        if current_station < interchanges[q][3]:# this is to prevent range(9,0) errors
                            
                            for ac in range(current_station,(interchanges[q][3])):  #counting of how much time taken
                                total_time += time[(current_line-1)][ac]
                        elif current_station > interchanges[q][3]:# this is to prevent range(9,0) errors
                            
                            for ac in range((interchanges[q][3]),current_station):  #counting of how much time taken
                                total_time += time[(current_line-1)][ac]
                        elif current_station == interchanges[q][3]:
                            pass
                        current_line = interchanges[q][0]# change the current line to the one the not the same as the one we compared ~9 lines earlier
                        current_station = interchanges[q][1]# change the current station to the one the not the same as the one we compared ~9 lines earlier
                    else:
                        invalid = True # if interchanges do not have a common line, the train can't jump tracks so the permutation of interchanges is invalid
                        break



                for ex2 in range(len(end_line)):
                    if end_line[ex2] == current_line and invalid == False: # adding time to reach the end station. this if block is specially for calculating time from the last interchange to the end station
                        if current_station - end_station[ex2] < 0:
                            gate_list.append(line_gates[end_line[ex2]-1]-gates[end_line[ex2]-1][end_station[ex2]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
                        else:
                            gate_list.append(gates[end_line[ex2]-1][end_station[ex2]-1])
                            
                        if current_station < end_station[ex2]:
                            for ac in range(current_station,end_station[ex2]):  #counting of how much time taken
                                total_time += time[(current_line-1)][ac]
                        elif current_station > end_station[ex2]:
                            for ac in range(end_station[ex2],current_station):  #counting of how much time taken
                                total_time += time[(current_line-1)][ac]
                        elif current_station == end_station[ex2]:
                            pass
                    else: #if the last interchange doesn't have the same line as the ending station, it is invalid
                        invalid = True


                    
                if total_time <= best_time and invalid == False: # checking if there is a shorter route
                    best_time=total_time
                    best_route=p
                    best_gate=list(gate_list)
                    
                total_time = 0 # reset total time
        invalid = False # reset invalid flag
        start_check = False # reset checks
        end_check = False
        gate_list = []   



    #this block is purely to take the time if the start and end stations are on the same line
    if start[0] == end[0]:
        start_line.append(start[0])
        if start[1] - end[1] < 0:
            gate_list.append(line_gates[end[0]-1]-gates[end[0]-1][end[1]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
        else:
            gate_list.append(gates[end[0]-1][end[1]-1])
        if start[1] < end[1]: #because range(9,1) is not range(1,9)
            for ad in range(start[1], end[1]):
                total_time += time[(start[0]-1)][ad]
        else:
            for ad in range(end[1], start[1]):
                total_time += time[(start[0]-1)][ad]
    try :
        if start[2] == end[0]:
            start_line.append(start[2])
            if start[3] - end[1] < 0:
                gate_list.append(line_gates[end[0]-1]-gates[end[0]-1][end[1]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
            else:
                gate_list.append(gates[end[0]-1][end[1]-1])
            if start[3] < end[1]: #because range(9,1) is not range(1,9)
                for ad in range(start[3], end[1]):
                    total_time += time[(start[2]-1)][ad]
            else:
                for ad in range(end[1], start[3]):
                    total_time += time[(start[2]-1)][ad]
        

        elif start[0] == end[2]:
            if start[1] - end[3] < 0:
                gate_list.append(line_gates[end[2]-1]-gates[end[2]-1][end[3]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
            else:
                gate_list.append(gates[end[2]-1][end[3]-1])
            if start[1] < end[3]: #because range(9,1) is not range(1,9)
                for ad in range(start[1], end[3]):
                    total_time += time[(start[0]-1)][ad]
            else:
                for ad in range(end[3], start[1]):
                    total_time += time[(start[0]-1)][ad]
            

        elif start[2] == end[2]:
            start_line.append(start[2])
            if start[3] - end[3] < 0:
                gate_list.append(line_gates[end[2]-1]-gates[end[2]-1][end[3]-1])  #if x is side 1 gate, the other side will be = (total doors+1)-x
            else:
                gate_list.append(gates[end[2]-1][end[3]-1])
            if start[3] < end[3]: #because range(9,1) is not range(1,9)
                for ad in range(start[3], end[3]):
                    total_time += time[(start[2]-1)][ad]
            else:
                for ad in range(end[3], start[3]):
                    total_time += time[(start[2]-1)][ad]
    except:
        pass

    if total_time <= best_time and total_time != 0: # checking if there is a shorter route, the best_time = 0 is for the first case when best time is = 0 by default
        best_time=total_time
        best_route=[]
        best_gate=list(gate_list)
    total_time = 0


    # from here, we are translating the route to gates and interchange
    final_route=[] #is like best_route but we have converted interchange index to the interchange itself e.g [1,8,2,9] instead of interchanges[0]
    output=[]# the output
    names=[['EW1 Pasir Ris', 'EW2 Tampines', 'EW3 Simei', 'EW4 Tanah Merah', 'EW5 Bedok', 'EW6 Kembangan', 'EW7 Eunos', 'EW8 Paya Lebar', 'EW9 Aljunied', 'EW10 Kallang', 'EW11 Lavender', 'EW12 Bugis', 'EW13 City Hall', 'EW14 Raffles Place', 'EW15 Tanjong Pagar', 'EW16 Outram Park', 'EW17 Tiong Bahru', 'EW18 Redhill', 'EW19 Queenstown', 'EW20 Commonwealth', 'EW21 Buona Vista', 'EW22 Dover', 'EW23 Clementi', 'EW24 Jurong East', 'EW25 Chinese Garden', 'EW26 Lakeside', 'EW27 Boon Lay', 'EW28 Pioneer', 'EW29 Joo Koon', 'EW30 Gul Circle', 'EW31 Tuas Crescent', 'EW32 Tuas West Road', 'EW33 Tuas Link'], ['CC1 Dhouby Ghaut', 'CC2 Bras Basah', 'CC3 Esplanade', 'CC4 Promenade', 'CC5 Nicoll Highway', 'CC6 Stadium', 'CC7 Mountbatten', 'CC8 Dakota', 'CC9 Paya Lebar', 'CC10 MacPherson', 'CC11 Tai Seng', 'CC12 Bartley', 'CC13 Serangoon', 'CC14 Lorong Chuan', 'CC15 Bishan', 'CC16 Marymount', 'CC17 Caldecott', 'CC18 Bukit Brown(NOT BUILT)', 'CC19 Botanic Gardens', 'CC20 Farrer Road', 'CC21 Holland Village', 'CC22 Buona Vista', 'CC23 one-north', 'CC24 Kent Ridge', 'CC25 Haw Par Villa', 'CC26 Pasir Panjang', 'CC27 Labrador Park', 'CC28 Telok Blangah', 'CC29 HabourFront',], ['NE1 HabourFront', 'NE2 NOT BUILT', 'NE3 Outram Park', 'NE4 Chinatown', 'NE5 Clarke Quay', 'NE6 Dhouby Ghaut', 'NE7 Little India', 'NE8 Farrer Park', 'NE9 Boon Keng', 'NE10 Potong Pasir', 'NE11 Woodleigh', 'NE12 Serangoon', 'NE13 Kovan', 'NE14 Hougang', 'NE15 Buangkok', 'NE16 Sengkang', 'NE17 Punggol'],['CC4 Promanade', 'CE1 Bayfront', 'CE2 Marina Bay']]

    final_route.append(start) #we still need to enter the starting station because we need to compare lines
    for r in best_route: # add the interchanges
        final_route.append(interchanges[r])
    final_route.append(end)#we still need to ending the starting station because we need to compare lines


    for t in range(len(best_gate)): # to prevent the logic error where we print the wrong end of an interchange e.g 'Enter gate 5 at EW23 Clementi and exit at CC22 Buona Vista'
        if final_route[t][0] == final_route[t+1][0]:
            temporary_hold = "Enter gate {} at {} and exit at {}".format(best_gate[t],names[final_route[t][0]-1][final_route[t][1]-1], names[final_route[t+1][0]-1][final_route[t+1][1]-1])#don't we love complex nested lists
            output.append(temporary_hold)
        if len(final_route[t+1]) == 4:
            if final_route[t][0] == final_route[t+1][2]:
                temporary_hold = "Enter gate {} at {} and exit at {}".format(best_gate[t],names[final_route[t][0]-1][final_route[t][1]-1], names[final_route[t+1][2]-1][final_route[t+1][3]-1])
                output.append(temporary_hold)
        if len(final_route[t]) == 4:
            if final_route[t][2] == final_route[t+1][0]:
                temporary_hold = "Enter gate {} at {} and exit at {}".format(best_gate[t],names[final_route[t][2]-1][final_route[t][3]-1], names[final_route[t+1][0]-1][final_route[t+1][1]-1])
                output.append(temporary_hold)
        if len(final_route[t]) == 4 and len(final_route[t+1]) == 4:
            if final_route[t][2] == final_route[t+1][2]:
                temporary_hold = "Enter gate {} at {} and exit at {}".format(best_gate[t],names[final_route[t][2]-1][final_route[t][3]-1], names[final_route[t+1][2]-1][final_route[t+1][3]-1])
                output.append(temporary_hold)         
    minutes = "Your Journey has an ETA of {} minutes".format(best_time)
    print(minutes)
    for z in output:
        print(z,file=textvar)    

class WritableStringVar(StringVar):
    def write(self, added_text):
        new_text = self.get() + added_text
        self.set(new_text)

    def clear(self):
        self.set("")

def inteswap(e):
    i = e
    i[0],i[1],i[2],i[3] = i[2],i[3],i[0],i[1]
    print(e)
    return i

def getgates(e):
    stat = [[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8, 2, 9], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16, 3, 3], [1, 17], [1, 18], [1, 19], [1, 20], [1, 21, 2, 22], [1, 22], [1, 23], [1, 24], [1, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33]], [[2, 1, 3, 6], [2, 2], [2, 3], [2, 4, 4, 1], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9, 1, 8], [2, 10], [2, 11], [2, 12], [2, 13, 3, 12], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [2, 21], [2, 22, 1, 21], [2, 23], [2, 24], [2, 25], [2, 26], [2, 27], [2, 28], [2, 29, 3, 1],[2,30],[2,31]], [[3, 1, 2, 29], [3, 2], [3, 3, 1, 16], [3, 4], [3, 5], [3, 6, 2, 1], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12, 2, 13], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17]],[[4,1],[4,2]]]
    gates=[['7,18', '8,16', '5,13', '6,15', '6,15', '6,15', '6,15', '6,15', '11,14', '6,15', '6,15', '6,15', '8,14', '7,12', '6,18', '6,16', '6,17', '7,14', '8,14', '7,17', '7,17', '12', '6,17', '9,19', '7,17', '7,17', '7,18', '7,14', '7,16'], ['2', '6', '5', '8', '4', '4', '4', '5', '8', '9', '5', '8', '9', '5', '7', '7', '1', '4', '7', '7', '0', '5', '9', '8', '5', '4', '4', '4', '8', '5', '6', '2'], ['9,18', '0', '19,13', '6,15,24', '3,14,11', '8,12,16', '16,6', '8,16', '17,8', '6,7', '17,8', '8,2', '8,17', '17,9', '8,17', '17,9', '8,17', '21,20,18', '2,18,24']]
    index = stat[e[0]-1].index(e)
    list_pos = gates[e[0]-1][index]
    return list_pos
    

def statname(e):#Converting back into station names
    number=[['EW1 Pasir Ris', 'EW2 Tampines', 'EW3 Simei', 'EW4 Tanah Merah', 'EW5 Bedok', 'EW6 Kembangan', 'EW7 Eunos', 'EW8 Paya Lebar', 'EW9 Aljunied', 'EW10 Kallang', 'EW11 Lavender', 'EW12 Bugis', 'EW13 City Hall', 'EW14 Raffles Place', 'EW15 Tanjong Pagar', 'EW16 Outram Park', 'EW17 Tiong Bahru', 'EW18 Redhill', 'EW19 Queenstown', 'EW20 Commonwealth', 'EW21 Buona Vista', 'EW22 Dover', 'EW23 Clementi', 'EW24 Jurong East', 'EW25 Chinese Garden', 'EW26 Lakeside', 'EW27 Boon Lay', 'EW28 Pioneer', 'EW29 Joo Koon', 'EW30 Gul Circle', 'EW31 Tuas Crescent', 'EW32 Tuas West Road', 'EW33 Tuas Link'],['CC1 Dhouby Ghaut', 'CC2 Bras Basah', 'CC3 Esplanade', 'CC4 Promenade', 'CC5 Nicoll Highway', 'CC6 Stadium', 'CC7 Mountbatten', 'CC8 Dakota', 'CC9 Paya Lebar', 'CC10 MacPherson', 'CC11 Tai Seng', 'CC12 Bartley', 'CC13 Serangoon', 'CC14 Lorong Chuan', 'CC15 Bishan', 'CC16 Marymount', 'CC17 Caldecott', 'CC18 Bukit Brown(NOT BUILT)', 'CC19 Botanic Gardens', 'CC20 Farrer Road', 'CC21 Holland Village', 'CC22 Buona Vista', 'CC23 one-north', 'CC24 Kent Ridge', 'CC25 Haw Par Villa', 'CC26 Pasir Panjang', 'CC27 Labrador Park', 'CC28 Telok Blangah', 'CC29 HabourFront'],['NE1 HabourFront', 'NE2 NOT BUILT', 'NE3 Outram Park', 'NE4 Chinatown', 'NE5 Clarke Quay', 'NE6 Dhouby Ghaut', 'NE7 Little India', 'NE8 Farrer Park', 'NE9 Boon Keng', 'NE10 Potong Pasir', 'NE11 Woodleigh', 'NE12 Serangoon', 'NE13 Kovan', 'NE14 Hougang', 'NE15 Buangkok', 'NE16 Sengkang', 'NE17 Punggol'],['CE1 Bayfront', 'CE2 Marina Bay']]
    stat = [[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8, 2, 9], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16, 3, 3], [1, 17], [1, 18], [1, 19], [1, 20], [1, 21, 2, 22], [1, 22], [1, 23], [1, 24], [1, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33]], [[2, 1, 3, 6], [2, 2], [2, 3], [2, 4, 4, 1], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9, 1, 8], [2, 10], [2, 11], [2, 12], [2, 13, 3, 12], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [2, 21], [2, 22, 1, 21], [2, 23], [2, 24], [2, 25], [2, 26], [2, 27], [2, 28], [2, 29, 3, 1],[2,30],[2,31]], [[3, 1, 2, 29], [3, 2], [3, 3, 1, 16], [3, 4], [3, 5], [3, 6, 2, 1], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12, 2, 13], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17]],[[4,1],[4,2]]]
    index = stat[e[0]-1].index(e)
    list_pos = number[e[0]-1][index]
    return list_pos
        
textvar=WritableStringVar(root)
def interchanges(e): #interchange code
    textvar.set('')
    inte = []
    stat = [[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8, 2, 9], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16, 3, 3], [1, 17], [1, 18], [1, 19], [1, 20], [1, 21, 2, 22], [1, 22], [1, 23], [1, 24], [1, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33]], [[2, 1, 3, 6], [2, 2], [2, 3], [2, 4, 4, 1], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9, 1, 8], [2, 10], [2, 11], [2, 12], [2, 13, 3, 12], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [2, 21], [2, 22, 1, 21], [2, 23], [2, 24], [2, 25], [2, 26], [2, 27], [2, 28], [2, 29, 3, 1],[2,30],[2,31]], [[3, 1, 2, 29], [3, 2], [3, 3, 1, 16], [3, 4], [3, 5], [3, 6, 2, 1], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12, 2, 13], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17]],[[4,1],[4,2]]]
    list_pos = sindexs(w2)
    list_pos1 = eindexs(w)
    printer = []
    gates=[]
    if list_pos[0] == 4: #Converting the CE line extension into CC instead (starting station)
        list_pos[0] = 2
        list_pos[1] = list_pos[1] + 29
    if list_pos1[0] == 4: #Converting the ending station line from CE to CC
        list_pos1[0] = 2
        list_pos1[1] = list_pos1[1] +29
    if list_pos[0] == list_pos1[0]: #if the starting station line is the same as the ending station line
        if len(inte) == 0:
            verified['text'] = 'No need to change trains if both start and end is the same station'
    saved = list_pos[0]-1
    for i in range(len(stat[saved])): #Converting list_pos into the same one stored in stat
        if list_pos[0] == stat[saved][i][0] and list_pos[1] == stat[saved][i][1]:
            list_pos = stat[saved][i]
            break
    saved = list_pos1[0] - 1 #Line for the ending/list_pos1
    for i in range(len(stat[saved])):#Converting list_pos1 into the same one stored in stat
        if list_pos1[0] == stat[saved][i][0] and list_pos1[1] == stat[saved][i][1]:
            list_pos1 = stat[saved][i]
            break
    if len(list_pos) == 4 and len(list_pos1) == 4:
        if list_pos[0] == list_pos1[2]:# If starting station line is the same as the ending station( if its an interchange)
            if list_pos1[0] == list_pos[2]:#checking if both of them are interchanges and thus they are on the same line
                verified['text'] = inte
                
    
    for i in range(len(stat[list_pos[0]-1])):
        if len(stat[list_pos[0]-1][i]) == 4:
            if stat[list_pos[0]-1][i][2] == list_pos1[0]: #Checking if the first line interchanges has the second line
                inte.append(stat[list_pos[0]-1][i]) #Appending to list
                verified['text'] = inte
                if list_pos[0] == 2: #Converting the starting and ending station if changed into CC back into CE
                    if list_pos[1] > 29:
                        list_pos[1] = list_pos[1] -29 #Converting the CE'X' which had turned into CCx+29
                        list_pos[0] = 4
                elif list_pos1[0] == 2:
                    if list_pos1[1] > 29:
                        list_pos1[0] = 4
                        list_pos1[1] = list_pos1[1] - 29
                printer.append(list_pos)
                for i in range(len(inte)): #Appending the interchange into a list of what is needed to be outputted
                    printer.append(inte[i])
                if list_pos[0] == 2:
                    if list_pos[1] > 29:
                        list_pos[1] = list_pos[1] -29
                        list_pos[0] = 4
                elif list_pos1[0] == 2:
                    if list_pos1[1] > 29:
                        list_pos1[0] = 4
                        list_pos1[1] = list_pos1[1] - 29        
                            
                 
                            
                printer.append(list_pos1)
                for i in range(len(printer)-1):
                    gates.append(printer[i+1])
                for i in range(len(printer)-1): #Printing of the output in the verified label( bottom label)
                    try:
                        print('Enter {} at gate {} and exit at {}'.format(statname(printer[i]),getgates(gates[i]),statname(printer[i+1])),file=textvar)
                    except:
                        
                        
                        return inte
                    
                return inte
    
    if list_pos[0] == 2:
        if list_pos[1] > 29:
            list_pos[1] = list_pos[1] -29
            list_pos[0] = 4
    elif list_pos1[0] == 2:
        if list_pos1[1] > 29:
            list_pos1[0] = 4
            list_pos1[1] = list_pos1[1] - 29
        
    
                
        
line_check = ['EW','CC','NE','CE']
number=[['EW1 Pasir Ris', 'EW2 Tampines', 'EW3 Simei', 'EW4 Tanah Merah', 'EW5 Bedok', 'EW6 Kembangan', 'EW7 Eunos', 'EW8 Paya Lebar', 'EW9 Aljunied', 'EW10 Kallang', 'EW11 Lavender', 'EW12 Bugis', 'EW13 City Hall', 'EW14 Raffles Place', 'EW15 Tanjong Pagar', 'EW16 Outram Park', 'EW17 Tiong Bahru', 'EW18 Redhill', 'EW19 Queenstown', 'EW20 Commonwealth', 'EW21 Buona Vista', 'EW22 Dover', 'EW23 Clementi', 'EW24 Jurong East', 'EW25 Chinese Garden', 'EW26 Lakeside', 'EW27 Boon Lay', 'EW28 Pioneer', 'EW29 Joo Koon', 'EW30 Gul Circle', 'EW31 Tuas Crescent', 'EW32 Tuas West Road', 'EW33 Tuas Link'],['CC1 Dhouby Ghaut', 'CC2 Bras Basah', 'CC3 Esplanade', 'CC4 Promenade', 'CC5 Nicoll Highway', 'CC6 Stadium', 'CC7 Mountbatten', 'CC8 Dakota', 'CC9 Paya Lebar', 'CC10 MacPherson', 'CC11 Tai Seng', 'CC12 Bartley', 'CC13 Serangoon', 'CC14 Lorong Chuan', 'CC15 Bishan', 'CC16 Marymount', 'CC17 Caldecott', 'CC18 Bukit Brown(NOT BUILT)', 'CC19 Botanic Gardens', 'CC20 Farrer Road', 'CC21 Holland Village', 'CC22 Buona Vista', 'CC23 one-north', 'CC24 Kent Ridge', 'CC25 Haw Par Villa', 'CC26 Pasir Panjang', 'CC27 Labrador Park', 'CC28 Telok Blangah', 'CC29 HabourFront'],['NE1 HabourFront', 'NE2 NOT BUILT', 'NE3 Outram Park', 'NE4 Chinatown', 'NE5 Clarke Quay', 'NE6 Dhouby Ghaut', 'NE7 Little India', 'NE8 Farrer Park', 'NE9 Boon Keng', 'NE10 Potong Pasir', 'NE11 Woodleigh', 'NE12 Serangoon', 'NE13 Kovan', 'NE14 Hougang', 'NE15 Buangkok', 'NE16 Sengkang', 'NE17 Punggol'],['CE1 Bayfront', 'CE2 Marina Bay']]
gates=[['7,18', '8,16', '5,13', '6,15', '6,15', '6,15', '6,15', '6,15', '11,14', '6,15', '6,15', '6,15', '8,14', '7,12', '6,18', '6,16', '6,17', '7,14', '8,14', '7,17', '7,17', '12', '6,17', '9,19', '7,17', '7,17', '7,18', '7,14', '7,16'], ['2', '6', '5', '8', '4', '4', '4', '5', '8', '9', '5', '8', '9', '5', '7', '7', '1', '4', '7', '7', '0', '5', '9', '8', '5', '4', '4', '4', '8', '5', '6', '2'], ['9,18', '0', '19,13', '6,15,24', '3,14,11', '8,12,16', '16,6', '8,16', '17,8', '6,7', '17,8', '8,2', '8,17', '17,9', '8,17', '17,9', '8,17', '21,20,18', '2,18,24']]
list_pos,list_pos1 = [],[]
eindex=0

def sindexget(e): #Storing value of the starting station line 
    if w2.get() == 'EW':
        start.config(value = number[0])
        sindex = 1
    if w2.get() == 'CC':
        start.config(value=number[1])
        sindex = 2
    if w2.get() == 'NE':
        start.config(value=number[2])
        sindex = 3
    if w2.get() == 'CE':
        start.config(value=number[3])
        sindex = 4
    return sindex

def eindexget(e): #Storing value of the ending station line
    if w.get() == 'EW':
        end.config(value = number[0])
        eindex = 1
    if w.get() == 'CC':
        end.config(value=number[1])
        eindex = 2
    if w.get() == 'NE':
        end.config(value=number[2])
        eindex = 3
    if w.get() == 'CE':
        end.config(value=number[3])
        eindex = 4
    return eindex

def eindexs(e):
    list_pos1=[]
    list_pos1.append(eindexget(e))
    index = number[list_pos1[0]-1].index(end.get())+1
    list_pos1.append(index)
    if list_pos1 == [3,2]:
        verified['text'] = 'Station not built yet. Please pick another ending station.'
    return list_pos1 
    

def sindexs(e):
    list_pos = []
    list_pos.append(sindexget(e))
    index = number[list_pos[0]-1].index(start.get())+1
    list_pos.append(index)
    if list_pos == [3,2]:
        verified['text'] = 'Station are not built yet. Please pick another starting staion.'
    return list_pos



    
my_fonts = font.Font(size=20) #Font for the buttons 

#Background 
C = Canvas(root, bg="blue", height=528, width=950)


#Ending station
w = ttk.Combobox(root,state="readonly",value=line_check) #Dropdown for all the lines we covered, starting station
w.current(0)
w.place(rely=0.035,relx=0.7,relwidth=0.3)

w.bind("<<ComboboxSelected>>",eindexget)

least_button=Button(root,text='Least interchanges',fg='black',command=lambda: interchanges(1),activebackground='blue') #Button for calling function for shortest route
least_button['font'] = my_fonts
least_button.place(relx=0.5,relwidth=0.18,rely=0.2)

end = ttk.Combobox(root,state="readonly",value = number[0]) #Dropdown box for the stations in the line, for the starting station
end.place(rely=0.08,relx=0.7,relwidth=0.3)
end.current(0)

end.bind('<<ComboboxSelected>>',eindexs)

end_label = Label(root,text = 'Ending Station',bg='light blue') #Label to let people know which side is for what purpose
end_label.place(relx=0.7,relwidth=0.3)

#Starting station
w2 = ttk.Combobox(root,state="readonly",value=line_check) #Dropdown for all the lines we covered, starting station
w2.current(0)
w2.place(rely=0.035,relx=0,relwidth=0.3)

w2.bind("<<ComboboxSelected>>",sindexget)

start_button=Button(root,text='Shortest route',fg='black',command=lambda: shortest_route(sindexs(w2),eindexs(w)),activebackground='blue') #Button for calling function for shortest route
start_button['font'] = my_fonts
start_button.place(relx=0.31,relwidth=0.18,rely=0.2)

start = ttk.Combobox(root,state="readonly",value = number[0]) #Dropdown box for the stations in the line, for the starting station
start.place(rely=0.08,relx=0,relwidth=0.3)
start.current(0)

start.bind('<<ComboboxSelected>>',sindexs)

start_label = Label(root, text='Starting Station',bg='light blue') #Label for people to know what side is for what purpose
start_label.place(relx=0,relwidth=0.3)

#Framework
frame = Frame(root,bg='grey',bd=1)
frame.place(relx=1,rely=1,relwidth=0.75,relheight=1)

verified = Label(root,textvariable=textvar)
verified.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)



C.pack()

root.mainloop()




























































































