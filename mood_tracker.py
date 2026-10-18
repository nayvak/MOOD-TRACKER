import customtkinter as ctk
window=ctk.CTk()
window.title("Final App V1")
window.geometry("380x700")
window.configure(fg_color="Black")
card1=ctk.CTkFrame(window,fg_color="#2D3A47",width=350,height=110,corner_radius=20)
label1=ctk.CTkLabel(card1,text="Mood Check-in",text_color="White",fg_color="#2D3A47",font=("Comic Sans MS",18))
label1.grid(row=0,column=0,pady=0,padx=0)
card1.grid(row=0,column=0,pady=12,padx=15)
card1.grid_propagate(False)
card1.grid_rowconfigure(0,weight=1)
card1.grid_columnconfigure(0,weight=1)
card2=ctk.CTkFrame(window,fg_color="#A8B58A",width=350,height=110,corner_radius=20)
label2=ctk.CTkLabel(card2,text="Journal",text_color="White",fg_color="#A8B58A",font=("Comic Sans MS",18))
label2.grid(row=1,column=1,pady=0,padx=0)
card2.grid(row=1,column=0,pady=12,padx=15)
card2.grid_propagate(False)
card2.grid_rowconfigure(1,weight=1)
card2.grid_columnconfigure(1,weight=1)
card3=ctk.CTkFrame(window,corner_radius=20,fg_color="#A9B7C6",width=350,height=110)
label3=ctk.CTkLabel(card3,text="Sticky Notes",text_color="White",fg_color="#A9B7C6",font=("Comic Sans MS",18))
label3.grid(row=1,column=1,pady=0,padx=0)
card3.grid(row=2,column=0,pady=12,padx=15)
card3.grid_propagate(False)
card3.grid_rowconfigure(1,weight=1)
card3.grid_columnconfigure(1,weight=1)
card4=ctk.CTkFrame(window,fg_color="#8E88A3",width=350,height=110,corner_radius=20)
label4=ctk.CTkLabel(card4,text="To-do List",text_color="White",fg_color="#8E88A3",font=("Comic Sans MS",18))
label4.grid(row=1,column=1,pady=0,padx=0)
card4.grid(row=3,column=0,pady=12,padx=15)
card4.grid_propagate(False)
card4.grid_rowconfigure(1,weight=1)
card4.grid_columnconfigure(1,weight=1)
card5=ctk.CTkFrame(window,fg_color="#F7C8D3",width=350,height=110,corner_radius=20)
label5=ctk.CTkLabel(card5,text="Weekly Analysis",text_color="White",fg_color="#F7C8D3",font=("Comic Sans MS",18))
label5.grid(row=1,column=1,pady=0,padx=0)
card5.grid(row=4,column=0,pady=12,padx=15)
card5.grid_propagate(False)
card5.grid_rowconfigure(1,weight=1)
card5.grid_columnconfigure(1,weight=1)
def showframe(frame):
    card1.grid_remove()
    card2.grid_remove()
    card3.grid_remove()
    card4.grid_remove()
    card5.grid_remove()
    if frame == analysis:
        refresh_analysis()
    frame.place(x=0,y=0,relwidth=1,relheight=1)
card1.bind("<Button-1>",lambda event:showframe(mood))
card2.bind("<Button-1>",lambda event:showframe(journal))
card3.bind("<Button-1>",lambda event:showframe(stickynotes))
card4.bind("<Button-1>",lambda event:showframe(todolist))
card5.bind("<Button-1>",lambda event:showframe(analysis))
mood=ctk.CTkFrame(window,fg_color="#A9B7C6")
journal=ctk.CTkFrame(window,fg_color="#8FAF9A")
stickynotes=ctk.CTkFrame(window,fg_color="#F6E7A6")
todolist=ctk.CTkFrame(window,fg_color="#B8B0D9")
analysis=ctk.CTkFrame(window,fg_color="#B46A72")
mood_history=ctk.CTkFrame(window,fg_color="#A9B7C6")
journal_history=ctk.CTkFrame(window,fg_color="#8FAF9A")
moodhistory=ctk.CTkButton(mood,fg_color="#2D3A47",text="Check Previous History",text_color="black",font=("Georgia",20),command=lambda:[showmoodhistory(),showframe(mood_history)])
moodhistory.place(x=150,y=650)
historylabel=ctk.CTkLabel(mood_history,text="PREVIOUS HISTORY",text_color="Black",fg_color="#A9B7C6",font=("Georgia",20))
historylabel.place(x=10,y=80)
def showmoodhistory():
    if os.path.exists(mood_file):
        saved_moods=load()
    else:
        saved_moods=[]
    if len(saved_moods)==0:
        emptylabel=ctk.CTkLabel(mood_history,text="No previous mood entries yet!",font=("Georgia", 18),text_color="Black")
        emptylabel.place(x=20, y=120)
        return
    y =120
    for entry in reversed(saved_moods):
        entrylabel = ctk.CTkLabel(mood_history,text=entry[0] + "  -  " + entry[1],font=("Georgia", 17),text_color="Black",fg_color="#A9B7C6")
        entrylabel.place(x=15, y=y)
        y += 45
def gotohome(frame):
    frame.place_forget()
    card1.grid(row=0,column=0,pady=12,padx=15)
    card2.grid(row=1,column=0,pady=12,padx=15)
    card3.grid(row=2,column=0,pady=12,padx=15)
    card4.grid(row=3,column=0,pady=12,padx=15)
    card5.grid(row=4,column=0,pady=12,padx=15) 
def addgotohome(frame):
    goback=ctk.CTkButton(frame,text="⬅️",command= lambda:gotohome(frame),fg_color="#A9B7C6",text_color="Black",font=("Seoge Print",20))
    goback.place(x=10,y=20)
for frame in [mood,journal,stickynotes,todolist,analysis,mood_history,journal_history]:
    addgotohome(frame)
import os
moodsscore={"Depressed":1,"Sad":2,"Angry":3,"Anxious":4,"Neutral":5,"Happy":6,"Excited":7}
moods=["Depressed","Sad","Angry","Anxious","Neutral","Happy","Excited"]
emotions = ["\U0001F61E Depressed","\U0001F622 Sad","\U0001F620 Angry","\U0001F630 Anxious","\U0001F610 Neutral","\U0001F60A Happy","\U0001F929 Excited"]
name_file = os.path.join(os.path.dirname(__file__), "name_txt")
if  not os.path.exists(name_file):
   nameentry=ctk.CTkEntry(mood,placeholder_text="Enter your name:",text_color="Black",fg_color="#A9B7C6",font=("Georgia",20),width=200)
   nameentry.place(x=10,y=50)
   name=""
   def ontinue():
       global name
       name=nameentry.get()
       if name=="":
           label7=ctk.CTkLabel(mood,text="Error!!Name not entered",text_color="Black",fg_color="#A9B7C6",font=("Georgia",20))
           label7.place(x=10,y=150)
       else:
           label6=ctk.CTkLabel(mood,text="Heyy!!"+name+"\nHow are you feeling today?",text_color="Black",fg_color="#A9B7C6",font=("Georgia",20))
           label6.place(x=10,y=70)
           x=10
           y=160
           for emotion in emotions:
               buttonemotion=ctk.CTkButton(mood,text=emotion,font=("Georgia",20),fg_color="#A9B7C6",text_color="Black",command=lambda emotion=emotion:savemood(emotion))
               buttonemotion.place(x=x,y=y)
               y=y+60
           with open(name_file,"w") as file:
               file.write(name)
           nameentry.place_forget()
           buttoncontinue.place_forget()
           label9=ctk.CTkLabel(journal,text="Heyy! "+name+"\nHow did your day go?",text_color="Black",fg_color="#8FAF9A",font=("Georgia",20))
           label9.place(x=10,y=50)
   buttoncontinue=ctk.CTkButton(mood,text="Continue",font=("Georgia",20),fg_color="#A9B7C6",text_color="Black",command=ontinue)
   buttoncontinue.place(x=10,y=100)
else:
    with open(name_file,"r") as file:
        name=file.read()
        label6=ctk.CTkLabel(mood,text="Heyy!!"+name+"\nHow are you feeling today?",text_color="Black",fg_color="#A9B7C6",font=("Georgia",20))
        label6.place(x=10,y=70)
        x=10
        y=160
        for emotion in emotions:
            buttonemotion=ctk.CTkButton(mood,text=emotion,font=("Georgia",20),fg_color="#A9B7C6",text_color="Black",command=lambda emotion=emotion:savemood(emotion))
            buttonemotion.place(x=x,y=y)
            y=y+60
        label9=ctk.CTkLabel(journal,text="Heyy! "+name+"\nHow did your day go?",text_color="Black",fg_color="#8FAF9A",font=("Georgia",20))
        label9.place(x=10,y=50)
import ast
from datetime import date,timedelta
today=date.today()
mood_file = os.path.join(os.path.dirname(__file__), "weekly_mood.txt")
def load():
   with open(mood_file,"r") as file:
     data=file.read()
   return ast.literal_eval(data)
if os.path.exists(mood_file):
    weekly_mood=load()
else:
    weekly_mood=[]
def savemood(emotion):
    emotion=emotion.split(" ",1)[1]
    already_check=False
    for day in weekly_mood:
        if day[0]==str(today):
            already_check=True
            label8=ctk.CTkLabel(mood,text="Sorry!You've already checked in today.",text_color="#B46A72",fg_color="#A9B7C6",font=("Arial",20))
            label8.place(x=10,y=600)
            return
    score=moodsscore[emotion]
    weekly_mood.append([str(today),emotion,score])
    with open(mood_file,"w") as file:
        file.write(str(weekly_mood))
historyjounal=ctk.CTkLabel(journal_history,text="PREVIOUS HISTORY",text_color="Black",fg_color="#8FAF9A",font=("Georgia",20))
historyjounal.place(x=10,y=80)
journal_file=os.path.join(os.path.dirname(__file__), "daily_journal.txt")
def showjournalhistory():
    if os.path.exists(journal_file):
        savedjournal=load2()
    else:
        savedjournal={}
    if len(savedjournal)==0:
        emptylabel1=ctk.CTkLabel(journal_history,text="No previous journal entries yet!",font=("Georgia", 18),text_color="Black",fg_color="#8FAF9A")
        emptylabel1.place(x=20, y=120)
        return
    else:
        entrylistbox=ctk.CTkScrollableFrame(journal_history,width=300,height=500)
        for day,entry in reversed(list((savedjournal).items())):
            entrylabel1= ctk.CTkLabel(entrylistbox,text=day+ "  -  " + entry,font=("Georgia", 17),text_color="Black",fg_color="#8FAF9A",wraplength=250,corner_radius=12)
            entrylabel1.pack(pady=5,padx=5)
        entrylistbox.place(x=15,y=120)
journalhistory=ctk.CTkButton(journal,fg_color="#A9B7C6",text="Check Previous History",text_color="black",font=("Georgia",20),command=lambda:[showjournalhistory(),showframe(journal_history)])
journalhistory.place(x=150,y=650)
journalbox=ctk.CTkTextbox(journal,height=500,width=340,fg_color="#A9B7C6",text_color="#FFFFFF",font=("Lucida Handwriting", 16),wrap="word")
journalbox.place(x=10,y=110)
def removetext(event):
    if journalbox.get("0.0","end-1c")=="You can write about your day here.":
        journalbox.delete("0.0","end-1c")
def load2():
    with open(journal_file,"r") as file:
        data=file.read()
        return ast.literal_eval(data)
if os.path.exists(journal_file):
    daily_journal=load2()
else:
    daily_journal={}
already_check=str(today) in daily_journal
if already_check:
    data1=daily_journal[str(today)]
    journalbox.insert("0.0",data1)
else:
    daily_journal[str(today)]=""
    journalbox.insert("0.0","You can write about your day here.")
    journalbox.bind("<FocusIn>",removetext)
def savejournal():
    data2=journalbox.get("0.0","end")
    if data2=="You can write about your day here.":
        pass
    else:
        daily_journal[str(today)]=data2
        with open(journal_file,"w") as file:
            file.write(str(daily_journal))
journalbox.bind("<KeyRelease>",lambda event:savejournal())
file_path1=os.path.join(os.path.dirname(__file__),"Task")
entry=ctk.CTkEntry(todolist,width=300,font=("Georgia",20),fg_color="white",text_color="#49415F",placeholder_text="You can type your tasks here.")
entry.place(x=10,y=60)
listbox=ctk.CTkScrollableFrame(todolist,width=300,height=500)
listbox.place(x=10,y=130)
placeholderlistbox=ctk.CTkLabel(listbox,font=("Georgia",20),text_color="#49415F",width=300,text=" ")
placeholderlistbox.pack(pady=15)
import json
def load_task():
    try:
        with open(file_path1,"r") as file:
            data=json.load(file)
        for task, is_checked in zip(data["tasks"], data["checked"]):
                placeholderlistbox.pack_forget()
                showtask(task,is_checked)
    except:
        pass
def delete(task,taskrow):
    index=tasks.index(task)
    tasks.pop(index)
    checked.pop(index)
    taskrow.destroy()
    save_func()
def checktask(tasklabel,index):
    if tasklabel.get() == 1:
        tasklabel.configure(text_color="#858094")
        checked[index]=True
    else:
        tasklabel.configure(text_color="#49415F")
        checked[index]=False
    save_func()
def showtask(task,is_checked=False):
    taskrow=ctk.CTkFrame(listbox,fg_color="white")
    taskrow.pack(pady=5,padx=5,fill="x")
    deletebutton=ctk.CTkButton(taskrow,text="✕",width=30,fg_color="#B8B0D9",text_color="#49415F",command=lambda:delete(task,taskrow))
    deletebutton.pack(pady=5,padx=5,side="right")
    tasklabel=ctk.CTkCheckBox(taskrow,width=300,text=task,text_color="#49415F",fg_color="white",font=("Georgia",20),command=lambda:checktask(tasklabel,index))
    if is_checked:
        tasklabel.select()
        tasklabel.configure(text_color="#858094")
    tasks.append(task)
    checked.append(is_checked)
    index=len(tasks)-1
    tasklabel.pack(pady=5,padx=5)
tasks=[]
checked=[]
load_task()
def addtext():
    task=entry.get()
    if task.strip()!="":
        placeholderlistbox.pack_forget()
        showtask(task)
        entry.delete(0,ctk.END)
        save_func()
buttonaddtext=ctk.CTkButton(todolist,width=10,text="➕",fg_color="#49415F",text_color="white",command=addtext)
buttonaddtext.place(y=60,x=330)
def save_func():
    data={"tasks":tasks,"checked":checked}
    with open(file_path1,"w") as file:
        json.dump(data,file)
notes_file=os.path.join(os.path.dirname(__file__),"sticky_notes.json")
notestitle=ctk.CTkLabel(stickynotes,text="My Notes",font=("Georgia",25),text_color="black")
notestitle.place(x=10,y=60)
notescontainer=ctk.CTkScrollableFrame(stickynotes,width=330,height=450,fg_color="#F6E7A6")
notescontainer.place(x=10,y=200)
notesentry=ctk.CTkTextbox(stickynotes,width=330,height=100,fg_color="#C9DDF2",text_color="White",font=("Georgia",20),wrap="word")
notesentry.place(x=10,y=100)
notes=[]
def save_notes():
    with open(notes_file,"w") as file:
        json.dump(notes,file)
def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file,"r") as file:
            savednotes=json.load(file)
        for note in savednotes:
            notes.append(note)
            create_notecard(note)
def create_notecard(note):
    notecard=ctk.CTkFrame(notescontainer,fg_color="#F3C6D3",corner_radius=12)
    notecard.pack(pady=5,padx=5,fill="x")
    notelabel=ctk.CTkLabel(notecard,text=note,text_color="Black",font=("Georgia", 14),wraplength=280)
    notelabel.pack(pady=10,padx=2,side="left")
    deletenote=ctk.CTkButton(notecard,text="❌",fg_color="#A9B7C6",text_color="Black",command=lambda:delete_note(note,notecard),width=1)
    deletenote.place(y=8,x=290)
    editnote =ctk.CTkButton(notecard,text="EDIT",width=1,fg_color="#A9B7C6",text_color="Black",command=lambda: edit_note(note, notecard, notelabel))
    editnote.place(y=38,x=274)
    def edit_note(note, notecard, notelabel):
        notesentry.delete("1.0", "end")
        notesentry.insert("1.0", note)
        def update_note():
            new_note = notesentry.get("1.0", "end-1c")
            if new_note.strip() != "":
                index = notes.index(note)
                notes[index] = new_note
                notelabel.configure(text=new_note)
                editnote.configure(command=lambda:edit_note(new_note,notecard,notelabel))
                deletenote.configure(command=lambda:delete_note(new_note,notecard))
                save_notes()
                notesentry.delete("1.0", "end")
                savebutton.destroy()
        savebutton = ctk.CTkButton(stickynotes,text="Save Changes",command=update_note)
        savebutton.place(x=200,y=10)
def add_note():
    note = notesentry.get("1.0", "end-1c")
    if note.strip() != "":
        create_notecard(note)
        notesentry.delete("1.0", "end")
        notes.append(note)
        save_notes()
def delete_note(note,notecard):
    notes.remove(note)
    notecard.destroy()
    save_notes()
load_notes()
addnote=ctk.CTkButton(stickynotes,text="➕ADD NOTE",fg_color="#A9B7C6",text_color="Black",command=add_note)
addnote.place(x=200,y=60)
analysis_widget=[]
def refresh_analysis():
    for widget in analysis_widget:
        widget.destroy()
        analysis_widget.clear()
    thisweek=[]
    startofweek=today-timedelta(days=today.weekday())
    endofweek=startofweek+timedelta(days=6)
    def load_analysis():
       with open(mood_file,"r") as file:
         data=file.read()
       return ast.literal_eval(data)
    if os.path.exists(mood_file):
        weekly_mood=load_analysis()
    else:
        weekly_mood=[]
    already_check=False
    for day in weekly_mood:
       if day[0]==str(today):
          already_check=True
    total=0
    for day in weekly_mood:
       entrydate=date.fromisoformat(day[0])
       if startofweek<=entrydate<=endofweek:
          thisweek.append(day)
          total=total+day[2]
    comments = {1: "It seems like you had a difficult week. Take some time for yourself.",2: "Your week seemed a little low. I hope next week feels better.",3: "There were some challenging moments this week. Keep going!",4: "Your mood was a little unsettled this week. Take things one day at a time.",5: "You had a fairly neutral week. Keep taking care of yourself!",6: "Looks like you had a pretty happy week! Keep it up!",7: "You had an exciting week! That's wonderful!"}
    averagescore=""
    if len(thisweek)>0:
       average=total/len(thisweek)
       averagescore=round(average)
       for mood,score in moodsscore.items():
            if score==averagescore:
                avgmood=mood
       labelmood=ctk.CTkLabel(analysis,text="Heyy!"+name+" "+"Your average mood this week was"+" "+avgmood+".",fg_color="#B46A72",text_color="white",font=("Lucida Handwriting",20),wraplength=300)
       labelmood.place(x=10,y=450)
       analysis_widget.append(labelmood)
       comment=comments[averagescore]
       labelcomment=ctk.CTkLabel(analysis,text=comment,fg_color="#B46A72",text_color="white",font=("Lucida Handwriting",20),wraplength=300)
       labelcomment.place(x=10,y=540)
       analysis_widget.append(labelcomment)
    else:
        labelerror=ctk.CTkLabel(analysis,text="No mood entry made this week yet.",fg_color="#B46A72",text_color="white",font=("Lucida Handwriting",25),wraplength=300)
        labelerror.place(x=10,y=450)
        analysis_widget.append(labelerror)
    days_graph=[]
    scores_graph=[]
    for days in thisweek:
       days_graph.append(days[0])
    for score in thisweek:
       scores_graph.append(score[2])
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    label1comment=ctk.CTkLabel(analysis,text="WEEKLY ANALYSIS",fg_color="#B46A72",text_color="white",font=("Georgia",35))
    label1comment.place(x=0,y=70)
    fig =Figure(figsize=(4,3),dpi=100)
    ax = fig.add_subplot(111)
    dates = [day[0] for day in thisweek]
    scores = [day[2] for day in thisweek]
    ax.plot(dates, scores, marker="o")
    ax.set_title("My Weekly Mood")
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood Score")
    ax.set_ylim(1, 7)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=analysis)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=200)
    analysis_widget.append(canvas.get_tk_widget)
window.mainloop()


