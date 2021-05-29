import pywhatkit 
m1 = input("Please Enter the Mobile Number:")
t1=input("Please type the message:")
tm1= int(input("Please Enter the time frame hour:"))
ss1= int(input("Please Enter the time frame minutes "))
try:
  pywhatkit.sendwhatmsg(m1,t1,tm1,ss1)
  print("Message sent successfully!")
  except:
    print("Error!")
