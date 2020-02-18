import sys
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')


#required base cost variables
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00


##Collect Customer Data decide which rental plan they had
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
##Time Period if/elseif Logic
if rentalCode == str('D'): #Daily
  rentalPeriod = input("Number of Days Rented: \n")
elif rentalCode == str('W'): #Weekly
  rentalPeriod = input("Number of Weeks Rented: \n")
elif rentalCode == str('B'): #Budget
  rentalPeriod = input("Number of Days Rented: \n")

#Debug Section
#print(rentalCode)
#print(rentalPeriod)

##Collected Mileage Information, input the odometer reading when the vehicle left
odoStart = input("Starting Odometer Reading:\n")
##Prompt for ending reading, input the odometer reading when the vehicle returned
odoEnd = input("Ending Odometer Reading:")

#Calculate Total Miles
totalMiles = int(odoEnd) - int(odoStart)


#Debug
#print(odoStart)
#print(odoEnd)
#print(totalMiles)


#Calculate Charges for per mile
#Code 'B' .25/mile
if rentalCode == 'B':    #Budget Selection, if user selected budget, calculate the costs here
    baseCharge = float(rentalPeriod) * float(budgetCharge)   #Base Charge for Budget
    mileCharge = float(totalMiles) * 0.25                    #Mile Charge for Budget
    #Final Calculation of cost
    amtDue = float(baseCharge) + float(mileCharge)
#Code 'D' no charge if avg is under 100 miles/day or if over 100 miles/day calculate extraMiles, .25/mile
elif rentalCode == 'D': # Daily Selection if user selected daily, calculate the costs here
    baseCharge = float(rentalPeriod) * float(dailyCharge)  #Base Charge for Daily
    avgDayMile = float(totalMiles)/float(rentalPeriod)     #Avg Mile Calculation
    #Extra Miles Calculation
    if avgDayMile <= 100:
        extraMiles = 0
    elif avgDayMile > 100:
        extraMiles = avgDayMile - 100
    mileCharge = float(extraMiles) * 0.25
    #Final Calculation of cost
    amtDue = float(baseCharge) + float(mileCharge)
        
#Code 'W' no charge if under 900 miles/wk avgwkmiles = totalMiles/rentalPeriod mileCharge is 100/wk if exceed 900 miles/wk
elif rentalCode == 'W': #Weekly Selection if user selected weekly, calculate the costs here
    baseCharge = float(rentalPeriod) * float(weeklyCharge)   #Base Charge for Weekly
    avgWeekMile = float(totalMiles)/float(rentalPeriod)       #Avg Mile Calculation
    #Extra Miles Calculation
    if avgWeekMile <= 900:
        mileCharge = 0.00
    elif avgWeekMile > 900:
        mileCharge = 100.00
    #Final Calculation of cost
    amtDue = float(baseCharge) + float(mileCharge)

#Debug Section
#print(baseCharge)
#print(mileCharge)
#print(amtDue)

#Summary Report Generated
print("Rental Summary")
print("Rental Code:     " + rentalCode)
print("Rental Period:    " + rentalPeriod)
print("Starting Odometer:    " + odoStart)
print("Ending Odometer:     " + odoEnd)
print("Miles Driven:     " + str(totalMiles))
print("Amount Due:     " + str(locale.currency(amtDue, grouping = True)))

