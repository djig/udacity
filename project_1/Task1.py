"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
phoneList = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        phoneList.add(text[0])
        phoneList.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        phoneList.add(call[0])
        phoneList.add(call[1])

noOfRecords = len(phoneList)
print("There are " + str(noOfRecords) +" different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#  Big o : time: o[n] and space: o[n]
# time complexity worst case n because it's loop through both texts and calls once 
#  no nested loop. 