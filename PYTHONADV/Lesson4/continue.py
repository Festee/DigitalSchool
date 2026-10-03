scores = [68,42,57,78,35,62,50,92]
##Average for numbers > 50
total = 0
count = 0

for score in scores:

    if score < 50:
        continue

    total+=score
    count+=1

average = total/count if count > 0 else 0

print ("Average score: ",average)

#total 68  count 1
#total 125 count 2
#total 203 count 3
#total 265 count 4
#total 315 count 5
#total 407 count 6
#407/6