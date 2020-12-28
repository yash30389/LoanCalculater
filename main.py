import math
print("Enter Loan amount")
p=input()
print("Enter an annual interest rate")
r=input()
print("Enter a loan length in year")
t=input()
p=float(p)
r=float(r)
t=float(t)
m=(p*(r/12)*(math.pow(1+r/12,12*t)))/( math.pow(1+r/12,12*t)-1)
print("Your Payment will be : Rs"+str(m))
print("Month \t\tStartingBalance\t\tInterestCharge\t\t\tPayment\t\t\tEndingBalance")
month=12*t
month=int(month)
startingBalance=p
endingBalance=p
for i in range (1,month+1):
	interestCharge=r/12*startingBalance
	endingBalance=startingBalance+interestCharge-m
	print(str(i)+"\t\tRs"+str(round(startingBalance,2))+"\t\tRs"+str(round(interestCharge,2))+"\t\t\tRs"+str(round(m,2))+"\t\tRs"+str(round(endingBalance,2)))
	startingBalance=endingBalance












# https:("https://www.youtube.com/watch?v=nv7KnjG5Pxg")