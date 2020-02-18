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
  print ('Your current balance:\n$%.2f' % account_balance)

#deposit function
def deposit (deposit, balance):
  return float(deposit) + float(balance)

#withdraw function
def withdrawl (withdrawlAmt, balance):
    return balance - float(withdrawlAmt)

userchoice = input ("What would you like to do?\n")

#Deposit 
if (userchoice == 'D'):
    deposit_amount = input("How much would you like to deposit today?\n")
    deposit (deposit_amount, account_balance)
    #debug
    #print(str(account_balance))
    #print(str(deposit_amount))
    print("Deposit was $%.2f" % float(deposit_amount) + ', ' + 'current balance is $%.2f' % (account_balance+float(deposit_amount)))
#Balance Inquiry
if (userchoice == 'B'):
    balance ()
#Withdrawl
if (userchoice == 'W'):
    withdrawl_amount = input("How much would you like to withdraw today?\n")
    if float(withdrawl_amount) > account_balance:
      print("$%.2f" % float(withdrawl_amount) + " is greater than your account balance of $%.2f" % account_balance)
    else:  
      withdrawl (withdrawl_amount, account_balance)
      print("Withdrawal amount was $%.2f" %float(withdrawl_amount)+', ' + 'current balance is $%.2f' % (account_balance - float(withdrawl_amount)))
#Exit
if (userchoice == 'Q'):
    print("Thank you for banking with us.")
