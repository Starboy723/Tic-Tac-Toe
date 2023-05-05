from tkinter import *
from tkinter import messagebox
win=Tk()
global count,w,c,start
def clearc():
	global c1,c2,c3,c4,c5,c6,c7,c8,c9
	c1=0
	c2=0
	c3=0
	c4=0
	c5=0
	c6=0
	c7=0
	c8=0
	c9=0
	
def clearB():
			global B1,B2,B3,B4,B5,B6,B7,B8,B9
			B1=''
			B2=''
			B3=''
			B4=''
			B5=''
			B6=''
			B7=''
			B8=''
			B9=''
clearB()
w=0
start=0
win['bg']="#FF4066"
def color(a,b):
	if (b1['text']==b2['text']==b3['text']==a):
			b1['bg']=b2['bg']=b3['bg']=b
	elif (b1['text']==b4['text']==b7['text']==a):
			b1['bg']=b4['bg']=b7['bg']=b
	elif (b1['text']==b5['text']==b9['text']==a):
			b1['bg']=b5['bg']=b9['bg']=b
	elif (b2['text']==b5['text']==b8['text']==a):
			b2['bg']=b5['bg']=b8['bg']=b
	elif (b3['text']==b6['text']==b9['text']==a):
			b3['bg']=b6['bg']=b9['bg']=b
	elif (b3['text']==b5['text']==b7['text']==a):
			b3['bg']=b5['bg']=b7['bg']=b
	elif (b4['text']==b5['text']==b6['text']==a):
			b4['bg']=b5['bg']=b6['bg']=b
	elif (b7['text']==b8['text']==b9['text']==a):
			b7['bg']=b8['bg']=b9['bg']=b

def restart():
	global count,B1,B2,B3,B4,B5,B6,B7,B8,B9,c1,c2,c3,c4,c5,c6,c7,c8,c9
	b1['text']=''
	b2['text']=''
	b3['text']=''
	b4['text']=''
	b5['text']=''
	b6['text']=''
	b7['text']=''
	b8['text']=''
	b9['text']=''
	clearB()
	count=1
	w=0
	c1=0
	c2=0
	c3=0
	c4=0
	c5=0
	c6=0
	c7=0
	c8=0
	c9=0
	
	
def resume():#resume
	global mb,B1,B2,B3,B4,B5,B6,B7,B8,B9,w,count,rc1
	mb=messagebox.askyesno('askquestion','Do you want resume the game?')
	if mb==0:
		clearB()
		newb_click()
		
	else:
		if w==1 or rc1==10:
			clearB()
		pastb_click()
		b1['text']=B1
		b2['text']=B2
		b3['text']=B3
		b4['text']=B4
		b5['text']=B5
		b6['text']=B6
		b7['text']=B7
		b8['text']=B8
		b9['text']=B9
		
	
	
def  display(a):
	global count,b1,b2,b3,b4,b5,b6,b7,b8,b9,w,B1,B2,B3,B4,B5,B6,B7,B9,B8,win2,c1,c2,c3,c4,c5,c6,c7,c8,c9,rc1
	if a=='b1':
		c1=c1+1
		if c1==1:
			count+=1
			if count%2==0:
				B1=b1['text']='X'
			else:
				B1=b1['text']='O'
	elif a=='b2':
		c2=c2+1
		if c2==1:
			count+=1
			if count%2==0:
				B2=b2['text']='X'
			else:
				B2=b2['text']='O'
	elif a=='b3':
		c3=c3+1
		if c3==1:
			count+=1
			if count%2==0:
				B3=b3['text']='X'
			else:
				B3=b3['text']='O'
	elif a=='b4':
		c4=c4+1
		if c4==1:
			count+=1
			if count%2==0:
				B4=b4['text']='X'
			else:
				B4=b4['text']='O'
	elif a=='b5':
		c5=c5+1
		if c5==1:
			count+=1
			if count%2==0:
				B5=b5['text']='X'
			else:
				B5=b5['text']='O'
	elif a=='b6':
		c6=c6+1
		if c6==1:
			count+=1
			if count%2==0:
				B6=b6['text']='X'
			else:
				B6=b6['text']='O'
	elif a=='b7':
		c7=c7+1
		if c7==1:
			count+=1
			if count%2==0:
				B7=b7['text']='X'
			else:
				B7=b7['text']='O'
	elif a=='b8':
		c8=c8+1
		if c8==1:
			count+=1
			if count%2==0:
				B8=b8['text']='X'
			else:
				B8=b8['text']='O'
	elif a=='b9':
		c9=c9+1
		if c9==1:
			count+=1
			if count%2==0:
				B9=b9['text']='X'
			else:
				B9=b9['text']='O'
	rc1=count
		
	if ((b1['text'] == b2['text'] == b3['text']=='X')or  (b1['text'] == b4['text'] == b7['text']=='X') or   (b1['text'] == b5['text'] == b9['text']=='X') or
(b2['text'] == b5['text'] == b8['text']=='X') or 
(b3['text'] == b5['text'] == b7['text']=='X' )or (b4['text'] == b5['text'] == b6['text']=='X')or (b7['text'] == b8['text'] == b9['text']=='X')or (b3['text'] == b6['text'] == b9['text']=='X' )):
		w+=1
		color('X','green')
		messagebox.showinfo('WINNER',"X IS WINNER")
		count=1
		clearc()
	elif  ((b1['text'] == b2['text'] == b3['text']=='O') or
	(b1['text'] == b4['text'] == b7['text']=='O' )or
	(b1['text'] == b5['text'] == b9['text']=='O') or
	(b2['text'] == b5['text'] == b8['text']=='O')or
	(b3['text'] == b5['text'] == b7['text']=='O' )or
	(b4['text'] == b5['text'] == b6['text']=='O' )or
	(b7['text'] == b8['text'] == b9['text']=='O') or
	(b3['text'] == b6['text'] == b9['text']=='O' )) :
		w+=1
		color('O','green')
		messagebox.showinfo('WINNER','O IS THE WINNER')
		count=1
		clearc()
	if w==0:
			if count==10:
				messagebox.showinfo('WINNER','DRAW MATCH!!!')
				count=1
				clearc()

def pastb_click():
	global b1,b2,b3,b4,b5,b6,b7,b8,b9,count,w,win2,c1,c2,c3,c4,c5,c6,c7,c8,c9,start
	w=0
	win2=Toplevel(bd=20,bg='blue')
	win2.title("tic tac toe")
	win2.maxsize(1040,2150)
	win2.minsize(1040,2150)
	win2.geometry('1040x2150')
	b1=Button(win2,text=B1,width=7,height=4,command=lambda:display('b1'))
	b2=Button(win2,text=B2,width=7,height=4,command=lambda:display('b2'))
	b3=Button(win2,text=B3,width=7,height=4,command=lambda:display('b3'))
	b4=Button(win2,text=B4,width=7,height=4,command=lambda:display('b4'))
	b5=Button(win2,text=B5,width=7,height=4,command=lambda:display('b5'))
	b6=Button(win2,text=B6,width=7,height=4,command=lambda:display('b6'))
	b7=Button(win2,text=B7,width=7,height=4,command=lambda:display('b7'))
	b8=Button(win2,text=B8,width=7,height=4,command=lambda:display('b8'))
	b9=Button(win2,text=B9,width=7,height=4,command=lambda:display('b9'))
	rb=Button(win2,text='RESTART',width=10 ,command=restart,bg='#34282C',fg='white')
	qb=Button(win2,text='QUIT',width=10,command=win2.destroy,bg='#34282C',fg='white')
	#window2 packing
	b1.place(x=50,y=500)
	b2.place(x=350,y=500)
	b3.place(x=650,y=500)
	b4.place(x=50,y=770)
	b5.place(x=350,y=770)
	b6.place(x=650,y=770)
	b7.place(x=50,y=1040)
	b8.place(x=350,y=1040)
	b9.place(x=650,y=1040)
	rb.place(x=50,y=1500)
	qb.place(x=580,y=1500)
def newb_click():
	global b1,b2,b3,b4,b5,b6,b7,b8,b9,count,w,win2,c1,c2,c3,c4,c5,c6,c7,c8,c9
	clearc()
	w=0
	clearB()
	count=1
	win2=Toplevel(bd=20,bg='blue')
	win2.title("tic tac toe")
	win2.maxsize(1040,2150)
	win2.minsize(1040,2150)
	win2.geometry('1040x2150')
	b1=Button(win2,width=7,height=4,command=lambda:display('b1'))
	b2=Button(win2,width=7,height=4,command=lambda:display('b2'))
	b3=Button(win2,width=7,height=4,command=lambda:display('b3'))
	b4=Button(win2,width=7,height=4,command=lambda:display('b4'))
	b5=Button(win2,width=7,height=4,command=lambda:display('b5'))
	b6=Button(win2,width=7,height=4,command=lambda:display('b6'))
	b7=Button(win2,width=7,height=4,command=lambda:display('b7'))
	b8=Button(win2,width=7,height=4,command=lambda:display('b8'))
	b9=Button(win2,width=7,height=4,command=lambda:display('b9'))
	rb=Button(win2,text='RESTART',width=10 ,command=restart,bg='#34282C',fg='white')
	qb=Button(win2,text='QUIT',width=10,command=win2.destroy,bg='#34282C',fg='white')
	#window2 packing
	b1.place(x=50,y=500)
	b2.place(x=350,y=500)
	b3.place(x=650,y=500)
	b4.place(x=50,y=770)
	b5.place(x=350,y=770)
	b6.place(x=650,y=770)
	b7.place(x=50,y=1040)
	b8.place(x=350,y=1040)
	b9.place(x=650,y=1040)
	rb.place(x=50,y=1500)
	qb.place(x=580,y=1500)
#widgets()
newb=Button(win,text='NEW GAME',command=newb_click,fg='white',bg='black')
resb=Button(win,text='RESUME',command=resume,fg='white',bg='black',font=( '',8),padx=78)
exitb=Button(win,text='EXIT',command=win.quit,bg='black',fg='white',padx=(120))
#packing
newb.pack(pady=(800,0))
resb.pack(pady=(30,0))
exitb.pack(pady=(30,0))
win.mainloop()
