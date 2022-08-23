time = "night"
sleepy = True
pajamas = "off"
inbed = True
if time == "night" and sleepy == True:
    pajamas = "on"
elif time == "morning" and sleepy == False :
    pajamas = "off"
else:
    pajamas ="off"
print(pajamas)