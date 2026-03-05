# Ohm's Law Program

V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

I = V / R

print("Current =", I, "Ampere")

if I < 0.5:
    print("Low Current")
elif I >= 0.5 and I <= 2:
    print("Normal Current")
else:
    print("High Current")