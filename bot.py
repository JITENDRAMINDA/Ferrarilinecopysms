from pyrogram import Client, Filters,Emoji

app = Client("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")

@app.on_message(Filters.channel & Filters.text & ~Filters.edited)
def forward(client, message):
 fie = open("source.txt" , "r")
 lies = file.readlines()
 fie.close()
 for a in lies:
  if message.chat.id == int(a):
   f = False
   words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"LU","?","loda","lodu","telegram"]
   for word in words:
    if word.casefold() in message.text.casefold():
     f = True
   if not f:
    mes = client.send_message(-1001450959037 ,"**" + message.text + "**")
    files = open("sure.txt" , "a")
    files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
    files.close()
        
        
@app.on_message(Filters.channel & Filters.text & Filters.edited)
def forward(client, message):
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
      client.edit_message_text(-1001378725482,int(x[x.index(id)+1]),"**" + message.text + "**")
     
@app.on_message(Filters.command("clear"))
def main(client, message):
  files = open("sure.txt" , "w")
  files.write("001 002")
  files.close()
  message.reply("Done") 

     
@app.on_message(Filters.command("set"))
def main(client, message):
  with open("source.txt" , "w") as files:
   files.write(message.text.split(" ")[1])
   files.close()
   message.reply("Done") 
        
        
app.run()
