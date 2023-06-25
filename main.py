import random

""" 
GENERAL OVERALL NOTES: 

1. Using the _ in the for loops: 
    The _ can be used because that variable is not being used for anything 
    other than iterating through the loop. If you were needing to use that variable for example: 
    for i in range(10)
       do_something(i)
    then an actual variable name would need to be declared.  In this program you will see a lot of uses of 
    the _ in the for loops. 
    
 2. using the 'f' in the print or input statements: 
    This is being done to allow for interprolated variables 
    to be used within the string.  Many times this is much easier than the traditional ("string" + variable + "remainder of the string").  Although it may not always be able to be used, in the cases in this program when including variables in the strings that will be printed to the screen, it is much easier. 
   
"""

# these are global variables and typically in good practice we would captialize these variable names
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3

# This is a dictionary syntax which offers a key - value pair
# This is the amount of these symbols available for each reel. 
symbol_count = {
    "A": 2,
    "J": 8,
    "Q": 6,
    "K": 4
}

# This dictionary represents the value of each symbol if there is a match across a row. 
# If there is a row match then bet will be multiplied by the number here. 
symbol_value = {
    "A": 5,
    "J": 2,
    "Q": 3,
    "K": 4
}

#This function is checking to see if there are any winning
def check_winnings(columns, lines, bet, values):
    winnings = 0
    # because line will always start at 0, its fine for the range
    # range will be up to but not including the number in the ()
    # so if the user bets 1 line, line starts at zero and it iterates up to but not including the 1 in the range.
    for line in range(lines):
        symbol = columns[0][line]
        # this is iterating through to see if there is a matching symbol across the row that has been betted on. 
        for column in columns: 
            symbol_to_check = column[line]
            # if there first and second symbols don't match then no need to go on 
            if symbol != symbol_to_check:
                break
        # normally the else would be right below the if, but in this case we want to break if no match
        # else we want to calculate the winnings
        else: 
            winnings += values[symbol] * bet
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    # First we are loading the symbols into a list from the dictionary
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Normally we would think of this as rows, but since we are generating each column on a reel, 
    # we are creating a list of lists to refer to the reels. 
    columns = []
    # this outer loop handles each of the columns as we are using 3 reels this would be 3 columns
    for _ in range(COLS):
        column=[]
        
        # Using the [:] actually copies the list instead of referencing 
        # This is needed to keep from changes affecting the original list of all_symbols
        current_symbols = all_symbols[:]
        
        # This inner loop is getting the symbols for each row for each column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#Function to print out the reels
def print_slot_machine(columns):
    # this for loop will be transposing the matrix
    for row in range(len(columns[0])):
        # The enumerate will index which we can use to determine if we are at the end of a list
        for i, column in enumerate(columns): 
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")
        print()

# function to get the deposit amount from the user             
def deposit(): 
    while True: 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: 
                break
            else: 
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")
    return amount

# function to get the number of lines user wants to bet on. 
def get_number_of_lines(): 
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES: 
                break
            else: 
                print("Enter a valid number of lines")
        else: 
            print("Please enter a number.")
    return lines

# function to get the amount the user wants to bet on each line
def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                break
            else: 
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}." )
        else: 
            print("Please enter a number.")
    return amount 

# this is the main function where all the others are called from 
def main():
    balance = deposit()
    lines = get_number_of_lines()
    # this statement is checking to see if the amount the user wants to bet is more than the 
    # available balance. 
    while True: 
        bet= get_bet()
        total_bet= lines * bet
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else: 
            break
    
    
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()