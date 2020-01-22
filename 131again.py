import turtle as trtl 

board = "tic.png" # import picture

# set background as picture
wn= trtl.Screen()
wn.bgpic(board)
wn.setup(width = 1.0, height = 1.0)

# drawing turtle
toe = trtl.Turtle()
toe.hideturtle()
toe.penup()
toe.speed(0)


# set x and o color variables

x_color = "red"
o_color = "blue"


# winner print stement writer
tic = trtl.Turtle()
tic.hideturtle()
tic.penup()

# quadrent variables
square_1 = (-280, 100) # done
square_2 = (-50, 100) #done
square_3 = (170, 100) # done
square_4 = (-280, -120) #done
square_5 = (-50, -120) # done
square_6 = (170, -120) #done
square_7 = (-280, -340) #done 
square_8 = (-50, -340) #done
square_9 = (170, -340) #done

# set whose turn
count = 1

# winner variables
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""
s6 = ""
s7 = ""
s8 = ""
s9 = ""

# used squares
used_squares = []

def quadrent_1():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_1)
    if (square_1 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s1 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s1 = "o"
    winner()
    used_squares.append(square_1)
        

def quadrent_2():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_2)
    if (square_2 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s2 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s2 = "o"
    winner()
    used_squares.append(square_2)
   

def quadrent_3():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_3)
    if (square_3 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s3 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s3 = "o"
    winner()
    used_squares.append(square_3)
    

def quadrent_4():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_4)
    if (square_4 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s4 = "x"
        else: 
            toe.color(o_color)           
            toe.write ("o", font = ("Arial", 150, "bold"))
            s4 = "o"
    winner()
    used_squares.append(square_4)
    

def quadrent_5():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_5)
    if (square_5 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s5 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s5 = "o"
    winner()
    used_squares.append(square_5)
    

def quadrent_6():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_6)
    if (square_6 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s6 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s6 = "o"
    winner()
    used_squares.append(square_6)
    

def quadrent_7():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_7)
    if (square_7 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s7 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s7 = "o" 
    winner()
    used_squares.append(square_7)
    

def quadrent_8():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_8)
    if (square_8 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s8 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s8 = "o"
    winner()
    used_squares.append(square_8)
    

def quadrent_9():
    global count
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    toe.goto(square_9)
    if (square_9 not in used_squares):
        count += 1
        if (count % 2 == 0):
            toe.color(x_color)
            toe.write("x", font = ("Arial", 150, "bold"))
            s9 = "x"
        else: 
            toe.color(o_color)
            toe.write ("o", font = ("Arial", 150, "bold"))
            s9 = "o" 
    winner()
    used_squares.append(square_9)
    

def winner():
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9

    # check if x wins
    if (s1 == "x" and s2 == "x" and s3 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s4 == "x" and s5 == "x" and s6 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s7 == "x" and s8 == "x" and s9 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s3 == "x" and s5 == "x" and s7 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s9 == "x" and s5 == "x" and s1 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s7 == "x" and s4 == "x" and s1 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s8 == "x" and s5 == "x" and s2 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    elif (s9 == "x" and s6 == "x" and s3 == "x"):
        tic.write ("x wins!", font = ("Arial", 150, "bold"))
    
    # check if o wins
    elif (s1 == "o" and s2 == "o" and s3 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s4 == "o" and s5 == "o" and s6 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s7 == "o" and s8 == "o" and s9 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s3 == "o" and s5 == "o" and s7 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s9 == "o" and s5 == "o" and s1 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s7 == "o" and s4 == "o" and s1 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s8 == "o" and s5 == "o" and s2 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    elif (s9 == "o" and s6 == "o" and s3 == "o"):
        tic.write ("o wins!", font = ("Arial", 150, "bold"))
    
def end_game():
    wn.clear() # clear screen
    # re-create board
    wn.bgpic(board)
    wn.setup(width = 1.0, height = 1.0)
    # clear the list 
    used_squares.clear()

    print (used_squares)
    
    


wn.onkeypress(quadrent_1, "1")
wn.onkeypress(quadrent_2, "2")
wn.onkeypress(quadrent_3, "3")
wn.onkeypress(quadrent_4, "4")
wn.onkeypress(quadrent_5, "5")
wn.onkeypress(quadrent_6, "6")
wn.onkeypress(quadrent_7, "7")
wn.onkeypress(quadrent_8, "8")
wn.onkeypress(quadrent_9, "9")
wn.onkeypress(end_game, "space")

wn.listen()

wn.mainloop()
