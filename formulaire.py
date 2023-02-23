from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import *
import os
import pymysql
from pymysql import *


class Formulaire:
     def __init__(self, root):
          self.root = root
          self.root.title("Inscription")
          self.root.minsize(height=700,width=1280)
          self.root.resizable(False,False)
          # Icon
          image_icons=PhotoImage(file="./img/voiture.png")
          self.root.iconphoto(False,image_icons)
          self.root.config(bg="#000")
          # Add BgImage file
          self.root.bg = PhotoImage(file = "./img/test.png")
          # Show BgImage using label
          bgImage = Label( self.root, image = self.root.bg, border=4)
          bgImage.place(x = 670, y = 60)
          # champs du formulaire
          frame1 = Frame(self.root , bg="#000",highlightbackground="#fff", highlightthickness=4)
          frame1.place(x=40,y=60,width=600,height=570)
          title=Label(frame1,text="Creee un Compte",fg="#fff",bg="#000",font=("times new roman", 23, "bold")).place(x=180,y=20)
          Frame(root,width=280,height=1, bg='#fff').place(x=200,y=125)
          # Prenom
          aff_Prenom = Label(frame1, text="Prenom:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=60,y=80)
          self.ecr_prenom = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_prenom.place(x=60,y=115,width=180)
          # Nom
          aff_nom = Label(frame1, text="Nom:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=360,y=80)
          self.ecr_nom = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_nom.place(x=360,y=115,width=180)
          # Telephone
          aff_Telephone = Label(frame1, text="Telephone:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=60,y=155)
          self.ecr_Telephone = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_Telephone.place(x=60,y=190,width=180)
          # Email
          aff_Email = Label(frame1, text="Email:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=360,y=155)
          self.ecr_Email = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_Email.place(x=360,y=190,width=180)
          # Question
          aff_Question = Label(frame1, text=" Question:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=60,y=230)
          self.ecr_Question = ttk.Combobox(frame1,  font=("times new roman",15,"bold"), state="readonly")
          self.ecr_Question["values"]=("Selectionnez Une Question", "Ton SurNom", "Lieu de Naissance", "Meilleur ami", "Film Prefere")
          self.ecr_Question.current(0)
          self.ecr_Question.place(x=60,y=270,width=180)
          # Reponse
          aff_Reponse = Label(frame1, text="Reponse:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=360,y=230)
          self.ecr_Reponse = Entry(frame1, bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_Reponse.place(x=360,y=270,width=180)
          # Password
          aff_Password = Label(frame1, text="Password:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=60,y=310)
          self.ecr_Password = Entry(frame1,show="*", bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_Password.place(x=60,y=345 ,width=180)
          # Confirme Password
          aff_Confirme_Password = Label(frame1, text="Confirme Password:", font=("times new roman",18,"bold"),fg="#fff",bg="#000").place(x=360,y=310)
          self.ecr_Confirme_Password = Entry(frame1, show="*" , bg="#fff" , bd=4 , fg="#000", font=("times new roman",15,"bold"))
          self.ecr_Confirme_Password.place(x=360,y=345 ,width=180)
          # Condition
          self.var_check = IntVar()
          chk = Checkbutton(frame1, variable=self.var_check, onvalue=1, offvalue=0, text="J'accepte les conditions et les termes", font=("times new roman",12), bg="#000", fg="grey",cursor="hand2").place(x=70,y=390)
          # les buttons
          btn = Button(frame1, text="Creer", command=self.Inscription , cursor="hand2",font=("times new roman",15,"bold"),bg="#D6F7FF").place(x=100,y=460,width=150)
          btn = Button(frame1, text="Connexion",command=self.fenetre_connexion ,cursor="hand2",font=("times new roman",15,"bold"),bg="#D6F7FF").place(x=360,y=460,width=150)
     def Inscription(self):
          if self.ecr_prenom.get() == "" or self.ecr_nom.get() =="" or self.ecr_Telephone.get() =="" or self.ecr_Email.get()== "" or self.ecr_Question.get()=="" or self.ecr_Reponse.get()=="" or self.ecr_Password.get()=="" or self.ecr_Confirme_Password.get()=="" :
               messagebox.showerror("erreur !!","Remplir les Champs", parent=self.root)
          elif self.ecr_Password.get() != self.ecr_Confirme_Password.get():
               messagebox.showerror("erreur !!" , "Les mots de pass ne sont pas conformes", parent=self.root)
          elif self.var_check.get()==0:
               messagebox.showerror("erreur !!","Veillez accepter les termes et les conditions", parent=self.root)
          else:
               try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
                    cur = con.cursor()
                    cur.execute("select * from inscription where email=%s", self.ecr_Email.get())
                    row = cur.fetchone()
                    
                    if row!= None:
                         messagebox.showerror("Erreur !!", "Ce mail existe deja", parent=self.root)
                    else:
                         cur.execute("insert into inscription (prenom, nom, Telephone, email, Question, Reponse, password) values(%s,%s,%s,%s,%s,%s,%s)",
                         (
                              self.ecr_prenom.get(),
                              self.ecr_nom.get(),
                              self.ecr_Telephone.get(),
                              self.ecr_Email.get(),
                              self.ecr_Question.get(),
                              self.ecr_Reponse.get(),
                              self.ecr_Password.get()
                         ))
                         messagebox.showinfo("success", "Votre Compte a ete cree", parent=self.root)
                    con.commit()
                    self.reini()
                    con.close
                    self.root.destroy()
                    import login
               except Exception as es:
                    messagebox.showerror("Erreur !!", f"Erreur de Connexion: {str(es)}", parent=self.root)
     def reini(self):
          self.ecr_prenom.delete(0, END)
          self.ecr_nom.delete(0, END)
          self.ecr_Telephone.delete(0, END)
          self.ecr_Email.delete(0, END)
          self.ecr_Question.delete(0, END)
          self.ecr_Reponse.delete(0, END)
          self.ecr_Password.delete(0, END)
          self.ecr_Confirme_Password.delete(0, END)
     def fenetre_connexion(self):
          self.root.destroy()
          import login

root=Tk()
obj = Formulaire(root)
root.mainloop()
