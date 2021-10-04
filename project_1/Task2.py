"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
dictPhone={}
maxDuration =0
maxTelephoneNumber = None
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
   
    for call in calls:
        callDuration = int(call[3])
        if call[0] in dictPhone:
            dictPhone[call[0]] += callDuration
        else:
            dictPhone[call[0]] = callDuration
        if call[1] in dictPhone:
            dictPhone[call[1]] += callDuration
        else:
            dictPhone[call[1]] = callDuration 
        if maxDuration < dictPhone[call[0]]:
            maxDuration = dictPhone[call[0]]
            maxTelephoneNumber = call[0]
        if maxDuration < dictPhone[call[1]]:
            maxDuration = dictPhone[call[1]]
            maxTelephoneNumber = call[1]

# print(dictPhone)
print(maxTelephoneNumber +  " spent the longest time, " +str(dictPhone[maxTelephoneNumber]) + " seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#  Big o : time: o[n] and space: o[n]
# time complexity worst case O(n2) (quadric)
# because disctionary(hashmap) search average o(1) and for every record we are searching key
# worst case finding key in hashmap/disctionary is n hence worst case time complexity O(n2))(quadric)