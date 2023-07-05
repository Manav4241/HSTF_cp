from tkinter import *
import time

import datetime  
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("PRODCUTIVITY BOOSTER")
Label(root, text ='PRODCUTVITY BOOSTER' , font ='arial 20 bold').pack()
Label(root,text="Enter the starting time in the format HH:MM",font ='arial 12 ').place(x=2,y=150)
startentry=Entry(root)
startentry.place(x=350,y=150)
Label(root,text="Enter the clsoing time in the format HH:MM",font ='arial 12 ').place(x=2,y=180)
closeentry=Entry(root)
closeentry.place(x=350,y=180)
Label(root, text ='BLOCK YOUR DISTRACTING WEBSITE HERE' , font ='arial 10 bold').pack(side=BOTTOM)
hosts_path ='C:\Windows\System32\drivers\etc\hosts'
#host_path=/etc/hosts
redirect = '127.0.0.1'
#redirect='0.0.0.'
Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x=5 ,y=60)
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 140,y = 60)
#---------------------------------------------------------------------------------
choice1=IntVar()
choice2=IntVar()
choice3=IntVar()
c1=Checkbutton(root,text="www.instagram.com",variable=choice1, onvalue=1, offvalue=0)
c1.place(x=8,y=120)
c2=Checkbutton(root,text="www.youtube.com",variable=choice2, onvalue=1, offvalue=0)
c2.place(x=150,y=120)
c3=Checkbutton(root,text="www.facebook.com",variable=choice3, onvalue=1, offvalue=0)
c3.place(x=300,y=120)
#---------------------------------------------------------------------------------
def Blocker():
    starttime=startentry.get()
    starthour,startmin=tuple(starttime.split(":"))
    #starthour=int(starthour)
    #startmin=int(startmin)
    closetime=closeentry.get()
    closehour,closemin=tuple(closetime.split(":"))
    #closehour=int(closehour)
    #closemin=int(closemin)
    with open("timings.txt","w")as file1:
        file1.write(starthour+"\n")
        file1.write(startmin+"\n")
        file1.write(closehour+"\n")
        file1.write(closemin+"\n")
    starthour=int(starthour)
    startmin=int(startmin)
    closehour=int(closehour)
    closemin=int(closemin)
    
        
#---------------------------------------------------------------------------------
    website_lists = Websites.get(1.0,END)
    sample= list(website_lists.split(","))
    Website=[]
    if(choice1.get()==1):
         Website.append("www.instagram.com")
    if(choice2.get()==1):
         Website.append("www.youtube.com")
    if(choice3.get()==1):
         Website.append("www.facebook.com")
    Website.extend(sample)
    print(Website)
    #x=Website.pop()
    
    with open (hosts_path , 'r+') as hosts_file:
        file_content = hosts_file.read()
        for website in Website:
               if(datetime.time(starthour,startmin,0)<datetime.datetime.now().time()<datetime.time(closehour,closemin,0)):
                   if website in file_content:
                        continue
               
                   else:
                    with open(hosts_path, 'r+') as file:
                     content = file.read()
                     for website in Website:
                       if website in content:
                          pass
                       else:
                    # mapping hostnames to your localhost IP address
                        file.write(redirect + " " + website + "\n")
                        Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)
                 #time.sleep(5)
#---------------------------------------------------------------------------------
def UnBlocker():
    with open("timings.txt","r")as file1:
         starthour=file1.readline()
         startmin=file1.readline()
         closehour=file1.readline()
         closemin=file1.readline()
    starthour=int(starthour)
    startmin=int(startmin)
    closehour=int(closehour)
    closemin=int(closemin)
    website_lists = Websites.get(1.0,END)
    sample= list(website_lists.split(","))
    Website=[]
    if(choice1.get()==1):
         Website.append("www.instagram.com")
    if(choice2.get()==1):
         Website.append("www.youtube.com")
    if(choice3.get()==1):
         Website.append("www.facebook.com")
    Website.extend(sample)
    #x=Website.pop()
    for website in Website:
        if(datetime.datetime.now().time()>datetime.time(closehour,closemin,0)):
                with open(hosts_path, 'r+') as file:
                 content=file.readlines()
                 file.seek(0)
                 for line in content:
                  if not any(website in line for website in Website):
                    file.write(line)
  
            # removing hostnmes from host file
                 file.truncate()
  
                 print("Fun hours...")
#---------------------------------------------------------------------------------
block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 150, y = 220)
unblock=Button(root, text = 'UnBlock',font = 'arial 12 bold',pady = 5,command = UnBlocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
unblock.place(x = 250, y = 220)
root.mainloop()





