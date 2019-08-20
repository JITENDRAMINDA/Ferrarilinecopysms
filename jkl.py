from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("my_acc",854941,"bf9632f82af99dc8c3b934ab48d54780")
s = -1001262096355
d = -1001316388816
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = ["kab","mani"," id","स",'dekho',"TRUSTED",'fix','😱','😳','fixer','👆','👇','match','pass','sab ','chase','defend','Surendra',"yuvraj",'karvana','link','loss','audio','varna','puri','open','paid','yaha','aayega','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teen','diya',"rajput",'bhai','😇','😎','😂','😋',"🐴",'🥺','🖕','member','only','chut','lund','gand','ma ','maa ','bhosdi','bahan','loude','lode','lavde','chutiya','☝️','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','line','who',"https://",'bullet','fuck','🤔','LUND'," LU","?","loda","lode","lodu","telegram","chor","join","$"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(d, "**" + message.text.replace("🇩🇪","🇳🇮").replace("🎾","🥎").replace("🖲","🧤").replace("📟","🛑").replace("WD","🔷 WIDE BALL 🔷").replace("/","~").replace("CHALU RAKHO","GAME STARTED, PLAYERS ON THE STEDIUM ") + "**")
  files = open("sure.txt" , "a")
  files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
  files.close()  
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(message.message_id)
  if id in x:
   try:
    client.edit_message_text(d,int(x[x.index(id)+1]),"**" + message.text.replace("🇩🇪","🇳🇮").replace("🎾","🥎").replace("🖲","🧤").replace("📟","🛑").replace("WD","🔷 WIDE BALL 🔷").replace("/","~").replace("CHALU RAKHO","GAME STARTED, PLAYERS ON THE STEDIUM ") + "**")
   except FloodWait as e:
    time.sleep(e.x)
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("clear"))
def main(client, message):
  files = open("sure.txt" , "w")
  files.write("001 002")
  files.close()
  message.reply("Done") 
app.run()
