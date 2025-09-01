# checks how many plates you ordered and enters in prices into begining total 
# finds out how many people are in your group, more than 8, finds out the 12% tax of your  betotal and 
#adds it to your betotal, then takes your ttotal(before sales tax) and finds out how much sales tax is 
#there, then adds tax to ttotal. which is now your total
#if less than 8, skips the step with 12% tax and spits out total

numOfPeople = float(input("how many people are in your group "))

# inputs:
# Price of each each plate
# number of people

betotal = 5 * numOfPeople # what is betootL?

if numOfPeople > 8:    
    ptax = betotal * 0.12 # what is ptax? grautity
    ttotal  = ptax + betotal # used extra vaiables.. ptax & ttotal.. coould we avoid these?
  
tax = betotal * 0.09 
total = tax + betotal    
print(f"your total is, ${total}") 

    
    ### test cases
    ## people
    # input: 7: objectives: $38.15: output: 38.15 program # given a number that adds up all the people and taxes; $38.15, 
    # does the computer's final answer match 38.15? 
    # input: 8: objectives: $43.60 output: 43.60: program # given a number that adds up all the people and taxes; 43.60,
    #  does the computer's final answer match 43.60? 
    # input: 9: objectives: $54.45 output: 54.45: program # given a number that adds up all the people and taxes; 54.45,
    #  does the computer's final answer match 54.45? 








