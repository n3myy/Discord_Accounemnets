import requests
#=========================================#
#    N3my's Dicord quick announcements    #
#        v1.0.0|harry@room01.co.uk        #
#=========================================#

#Add your webhook urls from the channels you wish to message to. (follow the format)
urls = ["https://discordapp.com/api/webhooks/721823541535703111/k4I67e-M9p4Bfo3YqdrKUhk7VEt1NUW5DRz3cEhGyhiBE_jCwHjwU641VwejZ-8IzhPS", "https://discordapp.com/api/webhooks/722117835983421561/XBJpJ2zfPSoYoVHpx7xTLkIqGDkAhWIrM5BavHtfiem9PoKUUEJfvM6X9jAB477bn0qN" ]

#You can change the bot name here.
botname = "N3my's Bot"

#Input from the user to add custom message to the channels.
message = input("Please add message:")

#Short key to send a predefine message when cba to come up with a custom notice. :D
if message == "1":
    message = "N3my is now LIVE on Twitch :cheers: Join in the sesh at :link: https://twitch.tv/n3my_"

# If you wish to add more predefined messages.
#elif message == "blah":
#    message = "blah blah blah"
    
else:
    continue

#This is fun part, goes through each url in the list and sends the message to each channel.
for x in range(len(urls)):
    res = requests.get(urls[x])
    payload = { 'username' : botname,
                'content' : message }
    headers = {}
    res = requests.post(urls[x], data=payload, headers=headers)
    print("Message Sent.")
print("All Messages Sent.")
