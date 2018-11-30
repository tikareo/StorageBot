import discord
import discord.ext.command.ext.commands 
from dicord.ext import commands
import asyncio
password= ""
attempt=0
flag=0
      while (attempt!=3):
       password = input("Please enter your password")

        if password is 1234 :
         flag = flag +1
           break
        else:
        attempt = attempt+1
          if (attempt==3):
           print("You have reached maximum attempts")
           if (flag==1):
             print ("Welcome", username +"to the Storage Bot, you have logged in successfully!")
     

#add token
client.run("


