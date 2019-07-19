from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
app =  Client("session",728044,"a41ddadc9696482aff94a4b37221574a")
s = -1001478751161
d = -1001389627457
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','Surendra","yuvraj",'karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"LU","?","loda","lodu","telegram","chor","singh"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(d ,"**" + message.text + "**")
  files = open("sure.txt" , "a")
  files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
  files.close()
        
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client, message):
 fie = open("source.txt" , "r")
 lies = fie.readlines()
 fie.close()
 for a in lies:
  if message.chat.id == int(a):
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(d,int(x[x.index(id)+1]),"**" + message.text + "**")
     except FloodWait as e:
      time.sleep(e.x)

@app.on_deleted_messages(Filters.chat(s))
def main(client, message):
 for v in message.messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
     client.delete_messages(d,int(x[x.index(id)+1]))
 
@app.on_message(Filters.command("clear"))
def main(client, message):
  files = open("sure.txt" , "w")
  files.write("001 002")
  files.close()
  message.reply("Done") 


app.run()
