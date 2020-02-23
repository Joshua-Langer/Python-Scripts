import sys
import math

#account balance 
account_balance = float(500.25)
#deposit var
deposit_amount = float(0.00)
#withdrawl var
withdrawl_amount = float(0.00)

#<--------functions go here-------------------->
#printbalance function
def balance ():
  print ('Your current balance:\n$%.2f' % account_balance)  #printing the users account balance

#deposit function
def deposit (deposit, balance):
  return float(deposit) + float(balance)

#withdraw function
def withdrawl (withdrawlAmt, balance):
    return balance - float(withdrawlAmt)

userchoice = input ("What would you like to do?\n") # requesting input from the user

#Deposit
# if the user has entered 'D' it will request an amount from the user and call the deposit function then print the users deposit and updated balance.
if (userchoice == 'D'): #user choice var
    deposit_amount = input("How much would you like to deposit today?\n") #requesting deposit amount from the user
    deposit (deposit_amount, account_balance)
    #debug
    #print(str(account_balance))
    #print(str(deposit_amount))
    print("Deposit was $%.2f" % float(deposit_amount) + ', ' + 'current balance is $%.2f' % (account_balance+float(deposit_amount))) #printing the users deposit with the updated account balance.
    
#Balance Inquiry
#if the user has entered 'B' it will call the print balance function.
if (userchoice == 'B'): 
    balance ()
    
#Withdrawl
#if the user has entered 'W' it will request an amount from the user and then determine if funds are available or not.
#if funds are not available it will advise them their requested amount is greater than the account balance.
#else it will withdraw and advise of the remaining account balance.
if (userchoice == 'W'):
    withdrawl_amount = input("How much would you like to withdraw today?\n")
    if float(withdrawl_amount) > account_balance:
      print("$%.2f" % float(withdrawl_amount) + " is greater than your account balance of $%.2f" % account_balance)
    else:  
      withdrawl (withdrawl_amount, account_balance)
      print("Withdrawal amount was $%.2f" %float(withdrawl_amount)+', ' + 'current balance is $%.2f' % (account_balance - float(withdrawl_amount)))
#Exit
#if the user enters 'Q' it will exit them from the system and print a Thank you.
if (userchoice == 'Q'):
    print("Thank you for banking with us.")
