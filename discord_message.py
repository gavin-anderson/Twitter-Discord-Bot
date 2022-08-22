import discord 
from wrapper import silence_event_loop_closed

def run_bot(message):
    class MyClient(discord.Client):

        async def on_connect(self):
            
            channel = client.get_channel("Enter Discord Channel ID") 
            await channel.send(message)
            print("Message sent")
            await client.close()
            
            
      
    client = MyClient()
    print("Start Client")
    silence_event_loop_closed(client.run(' Enter Discord Token'))

        
        


        
