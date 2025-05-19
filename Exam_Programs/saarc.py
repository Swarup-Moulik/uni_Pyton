saarc = ["India", "Pakistan", "Bangladesh", "Nepal", "Bhutan", "Afghanistan", "Srilanka"]
country = input("Enter the country name :- ")
f = False
for c in saarc:
    if c == country:
        f = True
        break

if f:
    print(f"{country} is a member of SAARC")
else:
    print(f"{country} is not a member of SAARC")

