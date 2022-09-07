print("This programme takes seconds in input and gives the output in Hours, Minutes and seconds!!")
sec = int(input("Enter the number of seconds to be converted here..."))

secon = sec % 60
min = sec // 60
hr = min // 60
minutes = (min % 60)

print("Hours = " + str(hr))
print("Minutes = " + str(minutes))
print("Seconds = " + str(secon))
