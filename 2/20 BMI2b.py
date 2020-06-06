groesse = float(input("Bitte gib Deine Größe (in m) ein:"))
gewicht = float(input("Bitte gib Dein Gewicht (in kg) ein:"))
bmi = gewicht / (groesse**2)

if bmi < 16:
  status = "starkes Untergewicht"
elif bmi < 17:
  status = "mäßiges Untergewicht"
elif bmi < 18.5:
  status = "leichtes Untergewicht"
elif bmi < 25:
  status = "Normalgewicht"
elif bmi < 30:
  status = "Präadipositas"
elif bmi < 35:
  status = "Adipositas 1"
elif bmi < 40:
  status = "Adipositas 2"
else:
  status = "Adipositas 3"

print("Dein BMI beträgt", bmi, "damit hast Du", status, ".")
