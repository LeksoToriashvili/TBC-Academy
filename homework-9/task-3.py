input_date = input("Input date: ")

_date = input_date[8:10] + "-" + input_date[5:7] + "-" + input_date[0:4]
_time = str(int(input_date[11:13]) % 12) + input_date[13:19]
_zone = input_date[26] + str(int(input_date[27:29]))

print("Changed format:", _date, _time, _zone)
