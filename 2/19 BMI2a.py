groesse = float(input("Bitte gib Deine Größe (in m) ein:"))
gewicht = float(input("Bitte gib Dein Gewicht (in kg) ein:"))
bmi = gewicht / (groesse**2)

if bmi < 16:
  status = "starkes Untergewicht"
else:
  if bmi < 17:
    status = "mäßiges Untergewicht"
  else:
    if bmi < 18.5:
      status = "leichtes Untergewicht"
    else:
      if bmi < 25:
        status = "Normalgewicht"
      else:
        if bmi < 30:
          status = "Präadipositas"
        else:
          if bmi < 35:
            status = "Adipositas 1"
          else:
            if bmi < 40:
              status = "Adipositas 2"
            else:
              status = "Adipositas 3"

print("Dein BMI beträgt", bmi, "damit hast Du", status, ".")
