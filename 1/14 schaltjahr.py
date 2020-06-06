import sys

jahr = int(sys.argv[1])

# jedes durch vier teilbare Jahr ist Schaltjahr ...
istSchaltjahr = jahr % 4 == 0

# ... aber alle hundert Jahre fällt das Schaltjahr aus 
istSchaltjahr = istSchaltjahr and jahr % 100 != 0

# ... aber alle vierhundert Jahre findet es doch statt
istSchaltjahr = istSchaltjahr or jahr % 400 == 0

print(istSchaltjahr)
