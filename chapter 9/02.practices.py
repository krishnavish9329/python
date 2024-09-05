def game():
    return 18

newscore=game()
with open("hiscore.txt","r") as f:
    hiscore=f.read()
    
if newscore=="":
    with open("hiscore.txt",'w') as p:
        p.write(str(newscore))
elif hiscore<str(newscore):
    with open("hiscore.txt",'w') as p:
        p.write(str(newscore))

