from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time

app =  Client("mnnn",bot_token="918985036:AAGuOy3Z00pcdp761gDouf5iEmnGz7rivR0",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")

#f("mxx",870831,"115641a0211dbd60dfdce6f367010e5f")

s = -1001316526418
d = -1001464551111
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = [" id","स",'dekho',"TRUSTED" 'fix','😱','😢','😳','fixer','👆','👇','match','pass','sab ','chase','defend','Surendra',"yuvraj",'karvana','link','loss','audio','varna','pura','puri','open','paid','yaha','aayega','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya',"rajput",'bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋',"🐴",'😝','🥺','members','🖕','member','only','chut','lund','gand','ma ','maa ','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND'," LU","?","loda","lode","lodu","telegram","chor","join","$","singh"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  if '🕵🏻'.casefold() in message.text.casefold():
   mes = client.send_message(d,"**" + message.text.replace('🕵🏻' , '💘') + "**")
   files = open("sure.txt" , "a")
   files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()
  elif '☎️' in message.text:
   mes = client.send_message(d,"**" + message.text.replace('☎️' , '🏝️') + "**")
   files = open("sure.txt" , "a")
   files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()
  elif 'WIDE'.casefold() in message.text.casefold():
   mes = client.send_message(d,"**🙇 WIDE BALL 🙇**")
   files = open("sure.txt" , "a")
   files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()
  else:
   mes = client.send_message(d,"**" + message.text.replace('🎾' , '⚾') + "**")
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
    if '☎️' in message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),"**"+message.text.replace('☎️' , '🏝️')+"**")
    elif '🕵🏻' in message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),"**"+message.text.replace('🕵🏻' , '💘')+"**")
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),"**"+message.text.replace('🎾' , '⚾')+"**")
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
     client.edit_message_text(d,int(x[x.index(id)+1]),".")
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
