from Tkinter import *
from tkMessageBox import *
from datetime import *
import time
from tkSimpleDialog import askstring
import getpass

class C5_single_chat:

	def chatpopup(self,event):
		self.chatmenu.post(event.x_root, event.y_root)

	def chatclerk_Enter(self,event):
		self.chatclerk()
		
	def chatclerk(self):
		global channel, Blabla, Chplayer
		TT1 = datetime.now().strftime('%d %H:%M:%S') 
		Chbb = Blabla.get()
		self.chatent.delete(0,END)
		Chcc = 'T' + '/' + TT1+ '/' + Chplayer+ '/' + Chbb + '\n'
		self.Chfile = open(channel,'a')
		self.Chfile.write(Chcc)
		self.Chfile.close()
		self.chatextract()
		print Chbb

	def chatreset_F5(self,event):
		self.chatreset()
		
	def chatreset(self):
		global channel, chatUserBin, chatTalkBin
		self.chreset = open(channel,'w')
		self.chreset.close()
		self.txt.delete('1.0',END)
		self.chatUserText.delete(1.0,END)
		chatUserBin = []
		chatTalkBin = []
		
		self.chatextract()

	def chatfootprint(self):
		global channel, ChLL, Chplayer
		a = 0
		while True:
			if a > 10:
				a = 0
				self.Chfile = open(channel,'a')
				fp = 'F' + '/' + 'TT1' + '/' + Chplayer + '/\n'
				self.Chfile.write(fp)
				self.Chfile.close()
				if len(ChLL) > 10:
					self.chatTextCutter()
					print 'line cut'
				else:pass
			else: 
				a += 1
			self.chatextract()
			time.sleep(0.3)
			self.txt.update()
			print 'a is',a
		
		
	def chatTextCutter(self):
		global ChLL, chatUserBin, channel
		ChRLL = ChLL[5:]
		self.Chfile = open(channel,'w')
		for ReTxt in ChRLL:
			ReTxt +'\n'
			self.Chfile.write(ReTxt)
		self.Chfile.close()
		chatUserBin = []
		self.chatUserText.delete(1.0,END)
		
	def chatextract(self):
		global channel, ChLL, user
		 
		self.Chfile = open(channel,'r')
		ChLL = self.Chfile.readlines()
		self.Chfile.close()
		for ChL in ChLL:
			frag = ChL.split('/')
			
			if frag[0] is 'T':
				chatline = frag[1] +'['+ frag[2]+'] '+ frag[3]
				if chatline in chatTalkBin:pass
				else:
					chatTalkBin.append(chatline)
					chatTalkBin.reverse()
					self.txt.delete('1.0',END)
					for LL in chatTalkBin:
						self.txt.insert(END,LL)
					chatTalkBin.reverse()
						
			elif frag[0] is 'F':
				user = frag[2]
				if user in chatUserBin:pass
				else:
					ChAnnounce = 'T' + '/' + ' ' + '/' + user+ '/' + 'has joined the Channel' + '\n'
					self.Chfile = open(channel,'a')
					self.Chfile.write(ChAnnounce)
					self.Chfile.close()
					chatUserBin.append(user)
					self.chatUserText.delete(1.0,END)
					for name in chatUserBin:
						name = name+'\n'
						self.chatUserText.insert(END,name)
			

	def RadioPro(self):
		global channel, ChRadio, chatTalkBin, chatUserBin, user
		ChAnnounce = 'T' + '/' + ' ' + '/' + user+ '/' + 'left the Channel' + '\n'
		self.Chfile = open(channel,'a')
		self.Chfile.write(ChAnnounce)
		self.Chfile.close()
		self.txt.delete('1.0',END)
		self.chatUserText.delete(1.0,END)
		if ChRadio.get() == '1':
			channel = channel1
		elif ChRadio.get() == '2':
			channel = channel2
		elif ChRadio.get() == '3':
			channel = channel3	
		chatTalkBin = []
		chatUserBin = []
		self.chatfootprint()

	def __init__(self):	
		global player, chatBin, chatUserBin, chatTalkBin, Blabla, ChRadio, channel, channel1, channel2, channel3, Chplayer
		chatwin = Tk()
		chatwin.title('Chat')

		# Player and Defualt Setting
		Chplayer = askstring('Name', 'Input your name \nex)Dodo.B')
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
		self.ScBar1 = Scrollbar(chfr1)
		self.ScBar1.pack(side = RIGHT, fill = Y)
		self.txt = Text(chfr1, height = 15, width = 38, bg = 'light grey',yscrollcommand = self.ScBar1.set)
		self.txt.pack()
		self.ScBar1.config(command = self.txt.yview)


		# Frame 2: Entry and Send Button

		Blabla = StringVar()
		self.chatent = Entry(chfr2, textvariable = Blabla, bg = 'light grey', width = 25)
		self.chatbut = Button(chfr2, text = "Send", command = self.chatclerk, bg = 'red', width = 5)
		self.chatent.grid(row = 0, column = 0)
		self.chatbut.grid(row = 0, column = 1)


		# Frame 3: Radio Button 1,2,3
		ChRadio = StringVar()
		self.rdB1 = Radiobutton(chfr3, variable = ChRadio, value = '1', command = self.RadioPro, text = 'channel 1')
		self.rdB2 = Radiobutton(chfr3, variable = ChRadio, value = '2', command = self.RadioPro, text = 'channel 2')
		self.rdB3 = Radiobutton(chfr3, variable = ChRadio, value = '3', command = self.RadioPro, text = 'channel 3')
		self.rdB1.grid(row =0, column =0)
		self.rdB2.grid(row =0, column =1)
		self.rdB3.grid(row =0, column =2)

		# Frame 4: User Label and Text window
		self.chatUserLabel = Label(chfr4, text = 'Current\nUsers', width = 9, height = 2)
		self.chatUserText = Text(chfr4, width = 9, height = 15, bg = 'grey')
		self.chatUserLabel.grid(row = 0, column = 0)
		self.chatUserText.grid(row = 1, column = 0)

		# Chat Popup Menu
		self.chatmenu = Menu(chfr1,tearoff = 0)
		self.chatmenu.add_command(label = 'Clear Window <F5>',command = self.chatreset)

		# Key Binding
		self.txt.bind('<Button-3>',self.chatpopup)
		self.txt.bind('<F5>',self.chatreset_F5)
		self.chatent.bind('<Return>',self.chatclerk_Enter)	
		self.chatent.bind('<F5>',self.chatreset_F5)



		# Text Channel Pilot
		standby = 'C:/Python27/C5_Single_standby'
		channel1 = 'C:/Python27/C5_Single_Channel1'
		channel2 = 'C:/Python27/C5_Single_Channel2'
		channel3 = 'C:/Python27/C5_Single_Channel3'

		standby_start = open('C:/Python27/C5_Single_standby','w')
		self.txt.insert(END,'\n\n\n		Pick a Channel')
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
		self.chatfootprint()

		chatwin.mainloop()
		
C5_single_chat()