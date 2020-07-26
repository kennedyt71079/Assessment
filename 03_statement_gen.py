# statement generator function
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# main routine
print()
incorrect = hl_statement("^^ Too low, try a higher number.    |    "
                       "Guesses Left: 3 ^^", "^")
print()
correct = hl_statement("vv Too high, try a lower number.    |  "
                        "Guesses Left: 2 vv", "v")
print()
well_done = hl_statement("*** Well done! you got it in 3 guesses ***", "*")
