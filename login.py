from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Login:
     def __init__(self,root):
          self.root = root
          self.root.title("Login")
          self.root.minsize(height=700,width=1280)
          self.root.resizable(False,False)
          self.root.focus_force()
          self.root.config(bg="#fff")
          # Icon
          image_icons=PhotoImage(file="./img/voiture.png")
          self.root.iconphoto(False,image_icons)
          # Add BgImage file
          self.root.bg = PhotoImage(file = "./img/car.png")
          # Show BgImage using label
          bgImage = Label( self.root, image = self.root.bg)
          bgImage.place(x = 790, y = 40)
          # Frame
          frame1 = Frame(self.root , bg="#000",highlightbackground="#fff", highlightthickness=4)
          frame1.place(x=80,y=60,width=600,height=570)
          # champs du formulaire
          title=Label(root,text="L o g i n",fg="#fff",bg="#000",font=("times new roman", 23, "bold")).place(x=320,y=150)
          # label emAIL
          lbl_email = Label(frame1, text="E-mail :", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=100,y=200)
          self.lbl_email = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.lbl_email.place(x=260,y=200,width=270)
          # label password
          lbl_password = Label(frame1, text="Password :", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=100,y=280)
          self.lbl_password = Entry(frame1,show="*", bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.lbl_password.place(x=260,y=280,width=270)
          # les buttons
          btn = Button(frame1, text="Creer un nouveau compte", command=self.fenetre_formulaire ,cursor="hand2",font=("times new roman",11,"bold"), bd=0,bg="#000", fg="#D6F7FF").place(x=340,y=320,width=200)
          btn = Button(frame1, text="mot de pass oublie", command=self.psw_oublie_fenetre ,cursor="hand2",font=("times new roman",11,"bold"), bd=0 ,bg="#000", fg="#D6F7FF").place(x=317,y=350,width=200)
          btn_connect = Button(frame1, text="Connexion", command=self.connexion, cursor="hand2",font=("times new roman",15,"bold"),bg="#FFF", fg="purple").place(x=230,y=400,width=150)
          # Icons
          ########ICONS###############################
          self.root.btnfac=PhotoImage(file='./img/facebook.png')
          facbtn=Button(self.root,image=self.root.btnfac,activeforeground='#000',
                        activebackground='#000',bg='#000',bd=0,cursor='hand2')
          facbtn.place(x=200,y=550)
          #________________________________________
          self.root.btngoo=PhotoImage(file='./img/google.png')
          goobtn=Button(self.root,image=self.root.btngoo,activeforeground='#000',
                        activebackground='#000',bg='#000',bd=0,cursor='hand2')
          goobtn.place(x=300,y=550)
          #________________________________________
          self.root.btnlin=PhotoImage(file='./img/linkedin.png')
          linbtn=Button(self.root,image=self.root.btnlin,activeforeground='#000',
                        activebackground='#000',bg='#000',bd=0,cursor='hand2')
          linbtn.place(x=400,y=550)
          #________________________________________
          self.root.btngit=PhotoImage(file='./img/instagram.png')
          gitbtn=Button(self.root,image=self.root.btngit,activeforeground='#000',
                        activebackground='#000',bg='#000',bd=0,cursor='hand2')
          gitbtn.place(x=500,y=550)
     def connexion(self):
          if self.lbl_email.get() == "" or self.lbl_password.get() =="" :
               messagebox.showerror("Erreur !!","Veillez saisir l'email et mot de passe", parent=self.root)
          else:
               try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
                    cur = con.cursor()
                    cur.execute("select * from inscription where email=%s and password=%s",(self.lbl_email.get(), self.lbl_password.get()))
                    row = cur.fetchone()
                    if row== None :
                         messagebox.showerror("Ereur !!","Invalide l'email et le password", parent=self.root)
                    else:
                         messagebox.showinfo("Success", "Bienvenue")
                         con.close()
                         self.root.destroy()
                         import accueil
               except Exception as ex:
                    messagebox.showerror("Erreur !!", f"Erreur de Connexion: {str(ex)}", parent=self.root)
     def psw_oublie_fenetre(self):
          if self.lbl_email.get()=="":
               messagebox.showerror("Erreur !!","Veillez donner un email valid !!", parent=self.root)
          else:
               try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
                    cur=con.cursor()
                    cur.execute("select * from inscription where email=%s", self.lbl_email.get())
                    row=cur.fetchone()
                    if row == None:
                         messagebox.showerror("Erreur !!", "Veillez entrer un Email Valid", parent=self.root)
                    else:
                         con.close()
                         self.root2 = Toplevel()
                         self.root2.title("Mot de Passe Oublie")
                         self.root2.minsize(height=570,width=600)
                         self.root2.resizable(False,False)
                         self.root2.config(bg="#000")
                         self.root2.focus_force()
                         self.root2.grab_set()
                         # Icon
                         image_icons=PhotoImage(file="./img/voiture.png")
                         self.root2.iconphoto(False,image_icons)
                         
                         title = Label(self.root2, text="Mot de Passe Oublie ", font=("algerian",18,"bold"),fg="#fff",bg="#000")
                         title.pack(side=TOP, fill=X)
                         
                         # Question
                         aff_Question = Label(self.root2, text=" Question:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=190,y=100)
                         self.ecr_Question = ttk.Combobox(self.root2,  font=("times new roman",15,"bold"), state="readonly")
                         self.ecr_Question["values"]=("Selectionnez Une Question", "Ton SurNom", "Lieu de Naissance", "Meilleur ami", "Film Prefere")
                         self.ecr_Question.current(0)
                         self.ecr_Question.place(x=190,y=150,width=250)
                         
                         # Reponse
                         aff_Reponse = Label(self.root2, text="Reponse:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=190,y=200)
                         self.ecr_Reponse = Entry(self.root2, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
                         self.ecr_Reponse.place(x=190,y=250,width=250)
                         
                         # Ch_psw
                         aff_Ch_psw = Label(self.root2, text="Nouveau mot de passe:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=190,y=300)
                         self.ecr_Ch_psw = Entry(self.root2, show="*", bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
                         self.ecr_Ch_psw.place(x=190,y=350,width=250)
                         
                         # button changer mot de passe
                         Ch_psw =Button(self.root2, text="Modifier", command=self.psw_oublie ,cursor="hand2" ,font=("algerian",22,"bold"), fg="purple", bg="#fff").place(x=240,y=430)
               except Exception as ex:
                    messagebox.showerror("Erreur !!", f"Erreur de Connexion: {str(ex)}", parent=self.root)
     def reini(self):
          self.ecr_Question.current(0)
          self.ecr_Reponse.delete(0, END)
          self.ecr_Ch_psw.delete(0, END)
          
     def psw_oublie(self):
          if self.ecr_Question.get()=="" or self.ecr_Reponse.get()=="" or self.ecr_Ch_psw.get()=="":
               messagebox.showerror("Erreur !!", "Remplir tous les Champs", parent=self.root2)
          else:
               try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
                    cur=con.cursor()
                    cur.execute("select * from inscription where email=%s and Question=%s and Reponse=%s", (self.lbl_email.get(), self.ecr_Question.get(), self.ecr_Reponse.get()))
                    row=cur.fetchone()
                    if row == None:
                         messagebox.showerror("Erreur !!", "Vous n'avez pas bien repondu a la Question selectionne ", parent=self.root2)
                    else:
                         cur.execute("update inscription set password=%s where email=%s", (self.ecr_Ch_psw.get(), self.lbl_email.get()))
                         con.commit()
                         con.close()
                         messagebox.showinfo("Success", "Vous avez modifie votre mot de passe", parent=self.root2)
                         self.reini()
                         # destroy katxed dek fenetre
                         self.root2.destroy()
               except Exception as es:
                    messagebox.showerror("Erreur !!", f"Erreur de connexion : {str(es)}", parent=self.root2)
     
     def fenetre_formulaire(self):
          self.root.destroy()
          import formulaire
     
     
     
     
root=Tk()
obj = Login(root)
root.mainloop()