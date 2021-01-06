from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
#----------------------[funciones Tablero]------------------------

def crea_mat_num():

    mat_num = [[1,1,1,1,1,1,1,1,1,1],
               [1,0,0,3,1,3,0,0,0,1],
               [1,0,0,0,1,0,1,0,0,1],
               [1,0,2,0,1,0,1,1,2,1],
               [1,1,1,2,1,0,4,0,0,1],
               [1,3,0,0,0,0,4,2,0,1],
               [1,0,2,0,0,0,4,3,0,1],
               [1,0,1,1,0,0,0,1,0,1],
               [1,3,0,2,0,0,0,0,3,1],
               [1,1,1,1,1,1,1,1,1,1]]

    return mat_num


def crea_mat_img(f,c):

    mat_img = [None] * f

    for i in range(f):
        mat_img[i] = [None] * c

    return mat_img


def vector_img():

    vec_img = []
    file_name = "img/soko-"
    file_ext = ".png"

    for i in range(6):
        vec_img.append(PhotoImage(file= file_name + str(i) + file_ext))
    
    return vec_img


def crea_tablero(f, c, mat_img, vec_img, mat_num):

      for i in range(f):
        for j in range(c):

            mat_img[i][j] = ttk.Label(image=vec_img[mat_num[i][j]])
            
            mat_img[i][j].place(x=(32 * i) + 100, y=(32 * j) + 100, width=32, height=32)
    

#--------------------[funciones Jugabilidad]----------------------
def mover_jugador(event):
    print(event.keycode, l_jugador.winfo_x(), l_jugador.winfo_y())

# ===========================================[Key "Up"]========================================================

    if event.keycode == 38 and limites(event)== True:
        if mover_caja(event) == True:
            fijar_caja(event)

            mat_num[iv_col.get()][iv_fil.get() - 1] = 0
            mat_img[iv_col.get()][iv_fil.get() - 1].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() - 1]])
            win.update()

        l_jugador.place(x=l_jugador.winfo_x(), y=l_jugador.winfo_y() - 32)
        iv_fil.set(iv_fil.get() - 1)


# ===========================================[Key "Down"]========================================================

    elif event.keycode == 40 and limites(event)== True:
        if mover_caja(event) ==True:
            fijar_caja(event)

            mat_num[iv_col.get()][iv_fil.get() + 1] = 0
            mat_img[iv_col.get()][iv_fil.get() + 1].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() + 1]])
            win.update()

        l_jugador.place(x=l_jugador.winfo_x(), y=l_jugador.winfo_y() + 32)
        iv_fil.set(iv_fil.get() + 1)

# ===========================================[Key "Right"]========================================================

    elif event.keycode == 39 and limites(event)== True:
        if mover_caja(event) == True:
            fijar_caja(event)

            mat_num[iv_col.get() + 1][iv_fil.get()] = 0
            mat_img[iv_col.get() + 1][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() + 1][iv_fil.get()]])
            win.update()

        l_jugador.place(x=l_jugador.winfo_x() + 32, y=l_jugador.winfo_y())
        iv_col.set(iv_col.get() + 1)

# ===========================================[Key "Left"]========================================================

    elif event.keycode == 37 and limites(event) == True:
        if mover_caja(event) == True:
            fijar_caja(event)

            mat_num[iv_col.get() - 1][iv_fil.get()] = 0
            mat_img[iv_col.get() - 1][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() - 1][iv_fil.get()]])
            win.update()

        l_jugador.place(x=l_jugador.winfo_x() - 32, y=l_jugador.winfo_y())
        iv_col.set(iv_col.get() - 1)




def limites (event):

# ===========================================[Key "Up"]==========================================================

    if event.keycode == 38 and mat_num[iv_col.get()][iv_fil.get() - 1] != 1 and mat_num[iv_col.get()][iv_fil.get() - 1] != 4:
        return True
# ===========================================[Key "Down"]========================================================

    elif event.keycode == 40 and mat_num[iv_col.get()][iv_fil.get() + 1] != 1 and mat_num[iv_col.get()][iv_fil.get() + 1] != 4:
        return True
# ===========================================[Key "Right"========================================================

    elif event.keycode == 39 and mat_num[iv_col.get() + 1][iv_fil.get()] != 1 and mat_num[iv_col.get() + 1][iv_fil.get()] != 4:
        return True
# ===========================================[Key "Left"=========================================================

    elif event.keycode == 37 and mat_num[iv_col.get() - 1][iv_fil.get()] != 1 and mat_num[iv_col.get() - 1][iv_fil.get()] != 4:
        return True

def mover_caja(event):
# ===========================================[Key "Up"]==========================================================
    if event.keycode == 38:
         if mat_num[iv_col.get()][iv_fil.get() - 1] == 2:
            if mat_num[iv_col.get()][iv_fil.get() - 2] == 0 or mat_num[iv_col.get()][iv_fil.get() - 2] == 3:
                return True
# ===========================================[Key "Down"]========================================================

    elif event.keycode == 40:
        if mat_num[iv_col.get()][iv_fil.get() + 1] == 2:
            if mat_num[iv_col.get()][iv_fil.get() + 2] == 0 or mat_num[iv_col.get()][iv_fil.get() + 2] == 3:
                return True
# ===========================================[Key "Right"========================================================
    elif event.keycode == 39:
        if mat_num[iv_col.get() + 1][iv_fil.get()] == 2:
            if mat_num[iv_col.get() + 2][iv_fil.get()] == 0 or mat_num[iv_col.get() + 2][iv_fil.get()] == 3:
                return True
# ===========================================[Key "Left"=========================================================
    elif event.keycode == 37:
        if mat_num[iv_col.get() - 1][iv_fil.get()] == 2:
            if mat_num[iv_col.get() - 2][iv_fil.get()] == 0 or mat_num[iv_col.get() - 2][iv_fil.get()] == 3:
                return True

def fijar_caja(event):
# ===========================================[Key "Up"]==========================================================
    if event.keycode == 38:
        if mat_num[iv_col.get()][iv_fil.get() - 2] == 3:
            mat_num[iv_col.get()][iv_fil.get() - 2] = 4
            mat_img[iv_col.get()][iv_fil.get() - 2].configure(image=vec_img[4])
            win.update()
        else:
            mat_num[iv_col.get()][iv_fil.get() - 2] = 2
            mat_img[iv_col.get()][iv_fil.get() - 2].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() - 2]])

# ===========================================[Key "Down"]========================================================
    elif event.keycode == 40:
        if mat_num[iv_col.get()][iv_fil.get() + 2] == 3:
            mat_num[iv_col.get()][iv_fil.get() + 2] = 4
            mat_img[iv_col.get()][iv_fil.get() + 2].configure(image=vec_img[4])
        else:
            mat_num[iv_col.get()][iv_fil.get() + 2] = 2
            mat_img[iv_col.get()][iv_fil.get() + 2].configure(image=vec_img[mat_num[iv_col.get()][iv_fil.get() + 2]])

# ===========================================[Key "Right"========================================================
    elif event.keycode == 39:
        if mat_num[iv_col.get() + 2][iv_fil.get()] == 3:
            mat_num[iv_col.get() + 2][iv_fil.get()] = 4
            mat_img[iv_col.get() + 2][iv_fil.get()].configure(image=vec_img[4])
        else:
            mat_num[iv_col.get() + 2][iv_fil.get()] = 2
            mat_img[iv_col.get() + 2][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() + 2][iv_fil.get()]])

# ===========================================[Key "Left"=========================================================
    elif event.keycode == 37:
        if mat_num[iv_col.get() - 2][iv_fil.get()] == 3:
            mat_num[iv_col.get() - 2][iv_fil.get()] = 4
            mat_img[iv_col.get() - 2][iv_fil.get()].configure(image=vec_img[4])
        else:
            mat_num[iv_col.get() - 2][iv_fil.get()] = 2
            mat_img[iv_col.get() - 2][iv_fil.get()].configure(image=vec_img[mat_num[iv_col.get() - 2][iv_fil.get()]])
        
        
#----------------------[programa principal]---------------
win= Tk()
win.geometry("500x500")
win.title("Juego Sokoban")
win.configure(background = "blue")


iv_fil = IntVar()
iv_col = IntVar()
iv_col.set(5)
iv_fil.set(5)

mat_img = crea_mat_img(10,10)
mat_num = crea_mat_num()
vec_img = vector_img()

crea_tablero(10, 10, mat_img, vec_img, mat_num)

l_jugador = ttk.Label(image=vec_img[5])
l_jugador.place(x=(32 * iv_col.get()) + 100, y=(32 * iv_fil.get()) + 100, width=32, height=32)


win.bind("<Key>", mover_jugador)

win.mainloop()
