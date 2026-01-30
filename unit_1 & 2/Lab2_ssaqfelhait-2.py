"""    Restaurant Trip Calculator 
       Sammy saqfelhait
       This program has been created to asks the user for a  bill total  
       and caluclates a 15% and 20% tip and shows the total bill with each tip has been chosen.
       01/22/2026
"""

print("this program will calculate tip suggestions for your dinner bill.")
 
bill = float(input("enter your bill amount: $"))
tip_15 = bill * 0.15 
tip_20 = bill * 0.20
total_15 = bill + tip_15
total_20 = bill + tip_20

print(f"\nbill amount: ${bill:.2f}")

print(f"15% tip:{tip_15:.2f}")
print(f"Total with 15% tip: ${total_15:.2f}") 
print(f"\n20% tip: ${tip_20:.2f}")
print(f"Total with 20% tip: ${total_20:.2f}")
             