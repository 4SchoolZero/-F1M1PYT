import datetime
x = datetime.datetime.now()
print(x)

print("hello you, ik ben tijmen")
usr = input("Wat is je naam? ")
print("hello " + usr)

question1 = "Hoe verwachten mijn nieuwe klasgenoten hoe ik mij ga gedragen?"
a1 = "A. respectfol"
b1 = "B. vriendelijk"
c1 = "C. Gemeen"
question2 = "Wat ga ik doen nu ik op deze nieuwe opleiding zit?"
a2 = "A. elke dag te laat komen"
b2 = "B. de opleiding afmaken zonder probleem"
c2 = "C. stoppen met de opleiding na de eerste periode"
question3 = "Wat is voor jou het doel van de opleiding?"
a3 = "A. diploma halen"
b3 = "B. een game-developer worden"
c3 = "C. leerplicht"

ans1 = input(question1 + "\n" + a1 + "\n" + b1 + "\n" + c1 + "\nAntwoord: ")
if (ans1 == "A"): print("Goed! het is de bedoeling dat ik respectvol ben naar mijn klasgenoten\n")
else: print("Fout! Het juiste antwoord is A\n")
ans2 = input(question2 + "\n" + a2 + "\n" + b2 + "\n" + c2 +"\nAntwoord: ")
if (ans2 == "B"): print("Goed! Het is natuurlijk logisch dat ik de opleiding zal afkamen :)\n")
else: print("Fout! Het juiste antwoord is B\n")
ans3 = input(question3 + "\n" + a3 + "\n" + b3 + "\n" + c3 +"\nAntwoord: ")
if (ans3 == "A"): print("Goed! Ik ga er vanuit dat ik mijn diploma zal ontvangen over 4 jaar\n")
else: print("Fout! Het juiste antwoord is A\n")


