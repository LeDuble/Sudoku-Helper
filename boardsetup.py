def create2dlist(rows):
    print("create2dlist works") #debugging
    """Creates 2D-list (sudoku board) with a given input from createboard() function.

    Args:
        rows (list): numbers given by user input

    Returns:
        list: returns 2D-list
    """

    # creates 2D-list
    empty_board = []
    for row in rows:
        empt_lst = []
        for j in row:
            turn_into_int = int(j)
            empt_lst.append(turn_into_int)
        empty_board.append(empt_lst)
        # print(empty_board)
    return empty_board

def instructions():
    print("instructions works") #debugging
    """Instructions text for the user.

    Returns:
        str: instruction text is returned.
    """

    # instructions
    return """
    1) with "," separators (real sudoku length)
    2) without "," separators (real sudoku length)
    3) with "," separators (2x2 length)
    3) without "," separators (2x2 length)
    3) with zeros (2x2 length)
    """
 

def createboard():
    print("board works") #debugging
    """Takes user input of the sudoku puzzle either with the "," separator or without.
    Turns given input in to a 2D-list.

    For example (has been simplified):
    > user input = 12345678 is given
    > output turns in to = [[1, 2], [3,4], [5,6], [7,8]]

    Returns:
        list: sudoku_board, 2D-list
    """

    # print instructions
    print(instructions())
    try:
        ## using template instead of having to write each time in to input
        # user_input = input("Type your input here: ")

        # user_input = "530070000,600195000,098000060,800060003,400803001,700020006,060000280,000419005,000080079"
        # user_input = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
        # user_input = "12,34,56,78"
        # user_input = "12,34,56,78"
        user_input = "10045670"
        
        len_input = len(user_input)

        # user input given with ","
        if "," in user_input and len_input == 11:
            sudoku_board = create2dlist(user_input.split(","))
            # print("this",rows) # debugging

        # check if user input is empty, a string or doesn't equal to 81
        elif not user_input.isnumeric() or len(user_input) != 8:
            return "no values given or not right amount of numbers"

        # user input given without ","
        else:
            nth = 2
            sudoku_board = create2dlist([user_input[row:row+nth] for row in range(0, len(user_input), nth)])
            # print("this", sudoku_board) #debugging
        return sudoku_board

    except:
        return "Error occurred"
        # print(type(user_input)) #debugging
