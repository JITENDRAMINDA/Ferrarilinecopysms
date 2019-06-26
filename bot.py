from pyrogram import Client, Filters,Emoji
app = Client ("mnnn",768402,"f6420bf67303614279049d48d3e670f6")
@app.on_message(Filters.chat(-1001262096355) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = ['dekho','fix','😱','😢','😳','fixer','👆','👇','match','pass','sab','chase','defend','hai','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','market','load','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','😀','😑','😐','😊','😜','😇','😎','😂','😘','😋','😝','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔','LUND',"LU","?","loda","lodu","telegram"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(-1001378725482,"**" + message.text + "**")
  files = open("sure.txt" , "a")
  files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
  files.close()
        
@app.on_deleted_messages(Filters.chat(-1001262096355))
def main(client, message):
 for v in message.messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    client.edit_message_text(-1001378725482,int(x[x.index(id)+1]), "." )
    client.delete_messages(-1001378725482,int(x[x.index(id)+1]))
        
@app.on_message(Filters.chat(-1001262096355)& Filters.text & Filters.edited)
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
        
app.run()
