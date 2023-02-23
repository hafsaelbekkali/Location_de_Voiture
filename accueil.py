from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from pymysql import cursors


class Accueil:
    def __init__(self, root):

        self.root = root
        self.root.title("Affichage des Voitures")
        self.root.minsize(height=700, width=1280)
        self.root.resizable(False, False)
        self.root.config(bg="#000")
        # Icon
        image_icons = PhotoImage(file="./img/voiture.png")
        self.root.iconphoto(False, image_icons)

        # Menu bar

        self.root.MenuBar = Menu(root)
        nav = Menu(self.root.MenuBar, tearoff=0, bg="#000", fg="red")
        nav.add_command(label='Ajouter Voiture',  command=self.ajouter_voiture, font=(
            "times new roman", 15, "bold"))
        nav.add_command(label='Afficher Voiture ',
                        font=("times new roman", 15, "bold"))
        nav.add_separator()
        nav.add_command(label="Exit", command=root.quit,
                        font=("times new roman", 15, "bold"))
        self.root.MenuBar.add_cascade(label='Gestion Voiture',  font=(
            "times new roman", 15, "bold"), menu=nav)

        nav = Menu(self.root.MenuBar, tearoff=0, bg="#000", fg="red")
        nav.add_command(label='Ajouter Utilisateur',
                        font=("times new roman", 15, "bold"))
        nav.add_command(label='Afficher Utilisateur',
                        font=("times new roman", 15, "bold"))
        self.root.MenuBar.add_cascade(
            label='Gestion Utilisateur', menu=nav,  font=("times new roman", 15, "bold"))
        nav.add_separator()
        nav.add_command(label="Exit", command=root.quit,
                        font=("times new roman", 15, "bold"))
        root.configure(menu=self.root.MenuBar)

        nav = Menu(self.root.MenuBar, tearoff=0, bg="#000", fg="red")
        nav.add_command(label='Ajouter Client',  font=(
            "times new roman", 15, "bold"))
        nav.add_command(label='Afficher Client',
                        font=("times new roman", 15, "bold"))
        self.root.MenuBar.add_cascade(
            label='Gestion Client', menu=nav,  font=("times new roman", 15, "bold"))
        nav.add_separator()
        nav.add_command(label="Exit", command=root.quit,
                        font=("times new roman", 15, "bold"))
        root.configure(menu=self.root.MenuBar)

        nav = Menu(self.root.MenuBar, tearoff=0, bg="#000", fg="red")
        nav.add_command(label='Ajouter Location',
                        font=("times new roman", 15, "bold"))
        nav.add_command(label='Afficher Location',
                        font=("times new roman", 15, "bold"))
        self.root.MenuBar.add_cascade(
            label='Gestion Location', menu=nav,  font=("times new roman", 15, "bold"))
        nav.add_separator()
        nav.add_command(label="Exit", command=root.quit,
                        font=("times new roman", 15, "bold"))
        root.configure(menu=self.root.MenuBar)
        # Variables
        self.immatricule = StringVar()
        self.mrq = StringVar()
        self.car = StringVar()
        self.mdl = StringVar()
        self.pu = StringVar()
        self.Tp = StringVar()

        self.recherchePar = StringVar()
        self.recherche = StringVar()

        # Affichage
        title = Label(self.root, text="G e s t i o n     V o i t u r e", fg="#fff",
                      bg="#000", font=("algerian", 30, "bold")).place(x=400, y=10)

        Details_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#fff").place(
            x=20, y=80, width=1235, height=580)

        Affiche_resultat = Label(Details_Frame, text="Recherche par :", font=(
            "algerian", 17), bg="#fff", fg="red")
        Affiche_resultat.place(x=200, y=100)

        rech = ttk.Combobox(Details_Frame, textvariable=self.recherchePar, font=(
            "times new roman", 20), state="readonly")
        rech["values"] = ("immatriculation", "marque", "modèle")
        rech.current(0)
        rech.place(x=450, y=100, width=200)

        rech_txt = Entry(Details_Frame, textvariable=self.recherche, font=(
            "times new roman", 20), bd=3, fg="red")
        rech_txt.place(x=670, y=100, width=280)
        
        self.root.lapbtn = PhotoImage(file='./img/laptop.png')
        btnlaptop = Button(self.root, image=self.root.lapbtn, activeforeground='#000',
                           activebackground='#fff', bg='#fff', bd=0, cursor='hand2')
        btnlaptop.place(x=970, y=90)

        self.root.searchbtn = PhotoImage(file='./img/detective.png')
        btnsearch = Button(self.root, image=self.root.searchbtn, activeforeground='#000',
                           activebackground='#fff', bg='#fff', bd=0, cursor='hand2')
        btnsearch.place(x=1040, y=90)


        btn_create = Button(Details_Frame, text="Ajouter Voiture", command=self.ajouter_voiture, cursor="hand2", font=(
            "algerian", 18, "bold"), fg="red", bg="#fff", bd=4).place(x=200, y=580)
        btn_modifier = Button(Details_Frame, command=self.Modifier_voiture, text="Modifier", cursor="hand2", font=(
            "algerian", 18, "bold"), fg="green", bg="#fff", bd=4).place(x=500, y=580, width=250)
        btn_supprimer = Button(Details_Frame, command=self.Supprimer, text="Supprimer", cursor="hand2", font=(
            "algerian", 18, "bold"), fg="orange", bg="#fff", bd=4).place(x=800, y=580, width=250)

        # Frame

        result_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#000")
        result_Frame.place(x=30, y=150, width=1200, height=400)

        scroll_x = Scrollbar(result_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Frame, orient=VERTICAL)
        self.tabl_resul = ttk.Treeview(result_Frame, columns=(
            "immatricule", "mrq", "car", "mdl", "pu", "Tp"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tabl_resul.heading("immatricule", text="immatriculation")
        self.tabl_resul.heading("mrq", text="marque")
        self.tabl_resul.heading("car", text="carburant")
        self.tabl_resul.heading("mdl", text="modèle")
        self.tabl_resul.heading("pu", text="puissance_fiscale")
        self.tabl_resul.heading("Tp", text="Type")

        self.tabl_resul["show"] = "headings"

        self.tabl_resul.column("immatricule", width=194)
        self.tabl_resul.column("mrq", width=190)
        self.tabl_resul.column("car", width=190)
        self.tabl_resul.column("mdl", width=190)
        self.tabl_resul.column("pu", width=190)
        self.tabl_resul.column("Tp", width=190)

        self.tabl_resul.pack()

        self.tabl_resul.bind("<ButtonRelease-1>", self.information)
        
        self.AfficherVoiture()
        
    # Ajouter 

    def ajouter_voiture(self):
     
        self.root2 = Toplevel()
        self.root2.title("Ajouter des Voitures")
        self.root2.minsize(height=650, width=1200)
        self.root2.resizable(False, False)
        self.root2.config(bg="#000")
        self.root2.focus_force()
        self.root2.grab_set()
        # Icon
        image_icons = PhotoImage(file="./img/voiture.png")
        self.root2.iconphoto(False, image_icons)

        # Frame
        frame1 = Frame(self.root2, bg="#000",
                       highlightbackground="#fff", highlightthickness=4)
        frame1.place(x=30, y=50, width=1129, height=540)
        title = Label(self.root2, text=" A j o u t e      V o i t u r e", fg="red", bg="#000", font=(
            "algerian", 23, "bold")).place(x=100, y=30, width=500)
        # les champs

        # immatriculation

        ajouter_immatricule = Label(frame1, text=" I m m a t r i c u l a t i o n :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=50)
        GST_immatricule = Entry(frame1, textvariable=self.immatricule, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=100, width=300)
        # marque

        ajouter_Marque = Label(frame1, text=" M a r q u e :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=50)
        GST_Marque = Entry(frame1, textvariable=self.mrq, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=730, y=100, width=300)
        # carburant

        ajouter_carburant = Label(frame1, text=" C a r b u r a n t :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=150)
        GST_carburant = Entry(frame1, textvariable=self.car, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=200, width=300)
        # modèle

        ajouter_modèle = Label(frame1, text=" M o d è l e :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=150)
        GST_modèle = Entry(frame1, bg="#fff", textvariable=self.mdl, bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=730, y=200, width=300)
        # puissance fiscale

        ajouter_PU_fiscal = Label(frame1, text=" P u i s s a n c e  F i s c a l e:", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=250)
        GST_PU_fiscal = Entry(frame1, textvariable=self.pu, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=300, width=300)
        # Type

        ajouter_Type = Label(frame1, text=" T Y P E :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=250)
        type = ttk.Combobox(frame1,  textvariable=self.Tp, font=(
            "times new roman", 20), state="readonly")
        type["values"] = (
            "Type de voiture", "4*4", "SUV,", " minibus", " limousine", "gamme", "Sport")
        type.current(0)
        type.place(x=730, y=300, width=300)

        # BTN

        btn_create = Button(frame1, text="Ajouter", command=self.Ajou_voiture ,cursor="hand2", font=(
            "algerian", 22, "bold"), fg="red", bg="#fff").place(x=370, y=400, width=350, height=50)
        
        
    def Modifier_voiture(self):

        self.root2 = Toplevel()
        self.root2.title("Modifier des Voitures")
        self.root2.minsize(height=650, width=1200)
        self.root2.resizable(False, False)
        self.root2.config(bg="#000")
        self.root2.focus_force()
        self.root2.grab_set()
        # Icon
        image_icons = PhotoImage(file="./img/voiture.png")
        self.root2.iconphoto(False, image_icons)

        # Frame
        frame1 = Frame(self.root2, bg="#000",
                       highlightbackground="#fff", highlightthickness=4)
        frame1.place(x=30, y=50, width=1129, height=540)
        title = Label(self.root2, text=" M O D I F I E R      V o i t u r e", fg="red", bg="#000", font=(
            "algerian", 23, "bold")).place(x=100, y=30, width=500)
        # les champs

        # immatriculation

        ajouter_immatricule = Label(frame1, text=" I m m a t r i c u l a t i o n :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=50)
        GST_immatricule = Entry(frame1, textvariable=self.immatricule, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=100, width=300)
        # marque

        ajouter_Marque = Label(frame1, text=" M a r q u e :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=50)
        GST_Marque = Entry(frame1, textvariable=self.mrq, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=730, y=100, width=300)
        # carburant

        ajouter_carburant = Label(frame1, text=" C a r b u r a n t :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=150)
        GST_carburant = Entry(frame1, textvariable=self.car, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=200, width=300)
        # modèle

        ajouter_modèle = Label(frame1, text=" M o d è l e :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=150)
        GST_modèle = Entry(frame1, bg="#fff", textvariable=self.mdl, bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=730, y=200, width=300)
        # puissance fiscale

        ajouter_PU_fiscal = Label(frame1, text=" P u i s s a n c e  F i s c a l e:", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=50, y=250)
        GST_PU_fiscal = Entry(frame1, textvariable=self.pu, bg="#fff", bd=4, fg="#000", font=(
            "times new roman", 15, "bold")).place(x=50, y=300, width=300)
        # Type

        ajouter_Type = Label(frame1, text=" T Y P E :", font=(
            "times new roman", 19, "bold"), fg="#fff", bg="#000").place(x=730, y=250)
        type = ttk.Combobox(frame1,  textvariable=self.Tp, font=(
            "times new roman", 20), state="readonly")
        type["values"] = (
            "Type de voiture", "4*4", "SUV,", " minibus", " limousine", "gamme", "Sport")
        type.current(0)
        type.place(x=730, y=300, width=300)

        # BTN

        btn_create = Button(frame1, text="Modifier", command=self.modifier ,cursor="hand2", font=(
            "algerian", 22, "bold"), fg="red", bg="#fff").place(x=370, y=400, width=350, height=50)

    def Ajou_voiture(self):
          if self.immatricule.get()== "" or self.car.get()== "" or self.mdl.get()=="" or self.pu=="" or self.Tp=="":
             messagebox.showerror("Erreur !!", "Vous n'avez pas rempli les champs", parent=self.root2)
          else:
               con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
               cur = con.cursor()
               cur.execute("insert into ajoute_voiture values(%s,%s,%s,%s,%s,%s)", (self.immatricule.get(), self.mrq.get() ,self.car.get(), self.mdl.get(), self.pu.get(), self.Tp.get()))
               con.commit()
               self.AfficherVoiture()
               con.close()
               messagebox.showinfo("Success", "Enregistrement Effectue")
               self.root2.destroy()
    def AfficherVoiture(self):
          con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
          cur = con.cursor()
          cur.execute("select * from ajoute_voiture")
          rows = cur.fetchall()
          if len(rows)!=0:
               self.tabl_resul.delete(*self.tabl_resul.get_children())
               for row in rows:
                    self.tabl_resul.insert("", END, values=row)
          con.commit()
          con.close()
          
    def information(self, ev):
            cursors_row = self.tabl_resul.focus()
            contents = self.tabl_resul.item(cursors_row)
            row = contents["values"]
            self.immatricule.set(row[0])
            self.mrq.set(row[1])
            self.car.set(row[2])
            self.mdl.set(row[3])
            self.pu.set(row[4])
            self.Tp.set(row[5])
    def modifier(self):
            con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
            cur = con.cursor()
            cur.execute("update ajoute_voiture set mrq=%s, car=%s, mdl=%s, pu=%s, Tp=%s where immatricule=%s", (self.mrq.get(), self.car.get(), self.mdl.get(), self.pu.get(), self.Tp.get(), self.immatricule.get()))
            con.commit()
            self.AfficherVoiture()
            messagebox.showinfo("Success", "Modification Effectue")
            self.root2.destroy()
            con.close()
    def Supprimer(self):
            con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
            cur = con.cursor()
            cur.execute("delete from ajoute_voiture where immatricule=%s", self.immatricule.get() )
            con.commit()
            messagebox.showwarning("Warning !!", "Suppression Effectue")
            self.AfficherVoiture()
            con.close()
            
    # def recherch_info(self):
    #         con = pymysql.connect(host="localhost", user="root", password="", database="location_de_voiture")
    #         cur = con.cursor()
    #         cur.execute("select * from ajoute_voiture where "+str(self.recherchePar.get())+"LIKE'%"+str(self.recherche.get())+"%'")
    #         rows = cur.fetchall()
    #         if len(rows)!=0:
    #                  self.tabl_resul.delete(*self.tabl_resul.get_children())
    #                  for row in rows:
    #                           self.tabl_resul.insert('', END, values=row)
    #         con.commit()
    #         con.close()

root = Tk()
obj = Accueil(root)
root.mainloop()
