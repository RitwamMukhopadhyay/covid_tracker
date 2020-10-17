import http.client
import ast

import http.client

while True:

 conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")
 headers = {
     'x-rapidapi-host': "covid-193.p.rapidapi.com",
     'x-rapidapi-key': "6864988fbbmshdfa941e44bf2d90p105b8ajsn204514284808"
     }
 country = input("Enter your Country name: ")
 conn.request("GET", "/statistics?country="+ country, headers=headers)

 res = conn.getresponse()
 data = res.read()

 dicdata = data.decode("utf-8")
 ddata = ast.literal_eval(dicdata)

 country = ddata["response"][0]["country"]
 newCase = ddata["response"][0]["cases"]["new"]
 newDeath = ddata["response"][0]["deaths"]["new"]
 totalCase = ddata["response"][0]["cases"]["total"]
 totalDeath = ddata["response"][0]["deaths"]["total"]
 recovery = ddata["response"][0]["cases"]["recovered"]

 print("new case: "+ newCase)
 print("new death: "+ newDeath)
 print("total case: "+ str(totalCase))
 print("total death: "+ str(totalDeath))
 print("Recoveres: "+ str(recovery))

 a = input("Do you want to find out more y/n >>>")
 if a== "n":
         break


