from Tkinter import *
from datetime import *
import time
from tkSimpleDialog import askstring


def chatpopup(event):
		chatmenu.post(event.x_root, event.y_root)

def chatclerk_Enter(event):
	chatclerk()
	
def chatclerk():
	global channel
	TT1 = datetime.now().strftime('%d %H:%M:%S') 
	Chbb = Blabla.get()
	chatent.delete(0,END)
	Chcc = 'T' + '-' + TT1+ '-' + player+ '-' + Chbb + '\n'
	Chfile = open(channel,'a')
	Chfile.write(Chcc)
	Chfile.close()
	chatextract()

def chatreset_F5(event):
	chatreset()
	
def chatreset():
	global channel, chatUserBin, chatTalkBin
	chreset = open(channel,'w')
	chreset.close()
	txt.delete('1.0',END)
	chatUserText.delete(1.0,END)
	chatUserBin = []
	chatTalkBin = []
	
	chatextract()

def chatfootprint():
	global channel, ChLL
	a = 0
	while True:
		if a > 10:
			a = 0
			Chfile = open(channel,'a')
			fp = 'F' + '-' + 'TT1' + '-' + player + '-\n'
			Chfile.write(fp)
			Chfile.close()
			if len(ChLL) > 10:
				chatTextCutter()
				print 'line cut'
			else:pass
		else: 
			a += 1
		chatextract()
		time.sleep(0.3)
		txt.update()
		print 'a is',a
	
	
def chatTextCutter():
	global ChLL, chatUserBin
	ChRLL = ChLL[5:]
	Chfile = open(channel,'w')
	for ReTxt in ChRLL:
		ReTxt +'\n'
		Chfile.write(ReTxt)
	Chfile.close()
	chatUserBin = []
	chatUserText.delete(1.0,END)
	
def chatextract():
	global channel, ChLL
	 
	Chfile = open(channel,'r')
	ChLL = Chfile.readlines()
	Chfile.close()
	for ChL in ChLL:
		frag = ChL.split('-')
		
		if frag[0] is 'T':
			chatline = frag[1] +'['+ frag[2]+'] '+ frag[3]
			if chatline in chatTalkBin:pass
			else:
				chatTalkBin.append(chatline)
				chatTalkBin.reverse()
				txt.delete('1.0',END)
				for LL in chatTalkBin:
					txt.insert(END,LL)
				chatTalkBin.reverse()
					
		elif frag[0] is 'F':
			user = frag[2]
			if user in chatUserBin:pass
			else:
				ChAnnounce = 'T' + '-' + ' ' + '-' + user+ '-' + 'has joined the Channel' + '\n'
				Chfile = open(channel,'a')
				Chfile.write(ChAnnounce)
				Chfile.close()
				chatUserBin.append(user)
				chatUserText.delete(1.0,END)
				for name in chatUserBin:
					name = name+'\n'
					chatUserText.insert(END,name)
		

def RadioPro():
	global channel, ChRadio, chatTalkBin, chatUserBin
	txt.delete('1.0',END)
	chatUserText.delete(1.0,END)
	if ChRadio.get() == '1':
		channel = channel1
	elif ChRadio.get() == '2':
		channel = channel2
	elif ChRadio.get() == '3':
		channel = channel3	
	chatTalkBin = []
	chatUserBin = []
	chatfootprint()

chatwin = Tk()
chatwin.title('Chat')

# Player and Defualt Setting
player = askstring('Name', 'Input your name \nex)Dodo.B')
chatBin = []
chatUserBin = []
chatTalkBin = []
a2 = 0

# Frame 1,2,3,4	
chfr1 = Frame(chatwin)
chfr2 = Frame(chatwin)
chfr3 = Frame(chatwin)
chfr4 = Frame(chatwin)
chfr1.grid(row =0, column = 0)
chfr2.grid(row =1, column = 0)
chfr3.grid(row =2, column = 0)
chfr4.grid(row =0, column = 1, rowspan = 3)


# Frame 1: Main text window and Scrollbar
ScBar1 = Scrollbar(chfr1)
ScBar1.pack(side = RIGHT, fill = Y)
txt = Text(chfr1, height = 15, width = 38, bg = 'light grey',yscrollcommand = ScBar1.set)
txt.pack()
ScBar1.config(command = txt.yview)


# Frame 2: Entry and Send Button

Blabla = StringVar()
chatent = Entry(chfr2, textvariable = Blabla, bg = 'light grey', width = 25)
chatbut = Button(chfr2, text = "Send", command = chatclerk, bg = 'red', width = 5)
chatent.grid(row = 0, column = 0)
chatbut.grid(row = 0, column = 1)


# Frame 3: Radio Button 1,2,3
ChRadio = StringVar()
rdB1 = Radiobutton(chfr3, variable = ChRadio, value = '1', command = RadioPro, text = 'channel 1')
rdB2 = Radiobutton(chfr3, variable = ChRadio, value = '2', command = RadioPro, text = 'channel 2')
rdB3 = Radiobutton(chfr3, variable = ChRadio, value = '3', command = RadioPro, text = 'channel 3')
rdB1.grid(row =0, column =0)
rdB2.grid(row =0, column =1)
rdB3.grid(row =0, column =2)

# Frame 4: User Label and Text window
chatUserLabel = Label(chfr4, text = 'Current\nUsers', width = 9, height = 2)
chatUserText = Text(chfr4, width = 9, height = 15, bg = 'grey')
chatUserLabel.grid(row = 0, column = 0)
chatUserText.grid(row = 1, column = 0)

# Chat Popup Menu
chatmenu = Menu(chfr1,tearoff = 0)
chatmenu.add_command(label = 'Clear Window <F5>',command = chatreset)

# Key Binding
txt.bind('<Button-3>',chatpopup)
txt.bind('<F5>',chatreset_F5)
chatent.bind('<Return>',chatclerk_Enter)	
chatent.bind('<F5>',chatreset_F5)



# Text Channel Pilot
standby = 'C:/Python27/C5_Single_standby'
channel1 = 'C:/Python27/C5_Single_Channel1'
channel2 = 'C:/Python27/C5_Single_Channel2'
channel3 = 'C:/Python27/C5_Single_Channel3'

standby_start = open('C:/Python27/C5_Single_standby','w')
txt.insert(END,'\n\n\n		Pick a Channel')
channel1_start = open('C:/Python27/C5_Single_Channel1','a')
channel2_start = open('C:/Python27/C5_Single_Channel2','a')
channel3_start = open('C:/Python27/C5_Single_Channel3','a')

standby_start.close()
channel1_start.close()
channel2_start.close()
channel3_start.close()

channel = standby

print("Don't forget to press \"F5\" once in a while to ease the computer")

# Loop Triger
chatfootprint()

chatwin.mainloop()



