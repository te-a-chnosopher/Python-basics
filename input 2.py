time = input("What time is it?")
print(time)
sleepy = input("Are you Sleepy?")
print(sleepy)

if time == "night" and sleepy == "yes":
    pajamas = "put on your pajamas"
elif time == "morning" and sleepy == "no" :
    pajamas = "fold your pajamas"
else:
    pajamas =" wash your pajamas"

print(pajamas)
