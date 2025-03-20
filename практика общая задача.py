from tkinter import * #подключение библиотеки
from tkinter import ttk #подключаем пакет ttk
from tkinter.messagebox import showerror
import smtplib
import hashlib
import re

root = Tk()
root.title("База данных")
root.geometry("800x700")

canvas=Canvas(bg="white", width=800, height=700)
canvas.pack()

surname_entry = ttk.Entry()
name_entry = ttk.Entry()
otchestvo_entry = ttk.Entry()
phonenumber_entry = ttk.Entry()
email_entry = ttk.Entry()
login_entry = ttk.Entry()
password_entry = ttk.Entry()
        
clicks=0
def add():
    global click_see, click_email,click_sort
    click_email=0
    click_see=0
    canvas.delete('sort')
    click_sort=0
    canvas.delete('see')
    canvas.delete('email')
    global clicks
    if clicks%2==0:
        canvas.create_text(420,90,text="Фамилия: ",tag='key')
        canvas.create_window(600, 90, window=surname_entry, width=300, height=25,tag='key')

        canvas.create_text(420,120,text="Имя: ",tag='key')
        canvas.create_window(600, 120, window=name_entry, width=300, height=25,tag='key')

        canvas.create_text(420,150,text="Отчество: ",tag='key')
        canvas.create_window(600, 150, window=otchestvo_entry, width=300, height=25,tag='key')

        canvas.create_text(400,180,text="Номер телефона: ",tag='key')
        canvas.create_window(600, 180, window=phonenumber_entry, width=300, height=25,tag='key')

        canvas.create_text(420,210,text="e-mail: ",tag='key')
        canvas.create_window(600, 210, window=email_entry, width=300, height=25,tag='key')

        canvas.create_text(420,240,text="Логин: ",tag='key')
        canvas.create_window(600, 240, window=login_entry, width=300, height=25,tag='key')

        canvas.create_text(420,270,text="Пароль: ",tag='key')
        canvas.create_window(600, 270, window=password_entry, width=300, height=25,tag='key')

        clicks+=1
    else:
        canvas.delete('key')
        clicks+=1

def regex_phone(s):
    f=0
    if (s[0]=="+" and len(s)==12 or s[0]=="8" and len(s)==11):
        regex="^((\+7|7|8)+([0-9]){10})$"
        if re.match(regex,s) is not None:
            f=1
    return f

def regex_SNO(s):
    f=0
    regex="^[А-ЯЁA-Z][а-яёa-z]+$"
    if re.match(regex,s) is not None:
        f=1
    return f

def regex_password(s):
    f=0
    regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(regex,s) is not None:
        f=1
    return f

def regex_email(s):
    f=0
    regex="^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$"
    if re.match(regex,s) is not None:
        f=1
    return f

def writting():
    if (len(surname_entry.get())==0 or len(name_entry.get())==0 or len(otchestvo_entry.get())==0 or len(phonenumber_entry.get())==0 or len(email_entry.get())==0 or len(login_entry.get())==0 or len(password_entry.get())==0):
        showerror(title="Ошибка", message="Заполните все поля")
    elif (regex_SNO(surname_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода фамилии")
    elif(regex_SNO(name_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода имени")
    elif(regex_SNO(otchestvo_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода отчества")
    elif (regex_phone(phonenumber_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода номера телефона")
    elif (regex_email(email_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода e-mail")
    elif (regex_password(password_entry.get())==0):
        showerror(title="Ошибка", message="Неправильно заполнено поле ввода пароля")
    else:
        fi=open("database.txt","a")
        fi.write("Фамилия: ")
        fi.write(surname_entry.get())
        fi.write('\n')
        fi.write("Имя: ")
        fi.write(name_entry.get())
        fi.write('\n')
        fi.write("Отчество: ")
        fi.write(otchestvo_entry.get())
        fi.write('\n')
        fi.write("Номер телефона: ")
        
        spisok=[]
        spisok.extend(phonenumber_entry.get())
        if (spisok[0]=="8"):
            spisok[0]="+"
            spisok.insert(1,"7")
        spisok.insert(2,'(')
        spisok.insert(6,")")
        spisok.insert(2,"-")
        spisok.insert(8,"-")
        spisok.insert(-4,"-")
        spisok.insert(-2,"-")
        s=''.join(spisok)
        
        fi.write(s)
        fi.write('\n')
        fi.write("e-mail: ")
        fi.write(email_entry.get())
        fi.write('\n')
        fi.write("Логин: ")
        fi.write(login_entry.get())
        fi.write('\n')
        fi.write("Пароль: ")
        hash_object=hashlib.md5(password_entry.get().encode())
        fi.write(hash_object.hexdigest())
        fi.write('\n')
        fi.write('\n')

        surname_entry.delete(0,END)
        name_entry.delete(0,END)
        otchestvo_entry.delete(0,END)
        phonenumber_entry.delete(0,END)
        email_entry.delete(0,END)
        login_entry.delete(0,END)
        password_entry.delete(0,END)
        fi.close()

click_see=0
def see():
    global clicks,click_email,click_sort
    click_email=0
    clicks=0
    canvas.delete('sort')
    click_sort=0
    canvas.delete('key')
    canvas.delete('email')
    global click_see, pr
    pr=0
    if (click_see%2==0):
        f=open("database.txt")
        spisok=f.readlines()
        spisok_var=StringVar(value=spisok)
        listbox=Listbox(listvariable=spisok_var)
        canvas.create_window(550,300,window=listbox,width=400, height=500,tag='see')
        listbox.yview_scroll(number=1, what="units")
        click_see+=1
        f.close()
    else:
        canvas.delete('see')
        click_see+=1

def back():
    click = ttk.Button(text="Посмотреть список пользователей",command=see)
    canvas.create_window(180, 90, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Добавить пользователя",command=add)
    canvas.create_window(180, 140, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Удалить пользователя", command=del_dop_click)
    canvas.create_window(180, 190, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Изменить пользователя", command=change_dop_click)
    canvas.create_window(180, 240, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Сохранить изменения в файл",command=writting)
    canvas.create_window(180, 290, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Отправить сообщение на e-mail пользователя",command=dop_click_email)
    canvas.create_window(180, 340, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Отсортировать по выбранному полю",command=dop_click_sort)
    canvas.create_window(180, 390, window=click, width=300, height=40,tag='key1')

    click = ttk.Button(text="Выход",command=root.quit)
    canvas.create_window(180, 440, window=click, width=300, height=40,tag='key1')

    canvas.delete('click_del')
    canvas.delete('click_change')
    canvas.delete('del_click_back')
    canvas.delete('del_login')
    canvas.delete('del_phone_number')
    canvas.delete('del_surname_name')
    canvas.delete('change_click_back')
    canvas.delete('change_login')
    canvas.delete('change_phone_number')
    canvas.delete('change_surname_name')
    canvas.delete('dalee')

def del_file():
    fi=open("database.txt")
    spisok=fi.readlines()
    fi.close()
    index=[]
    del_new_index=[]
    password=[]
    k=0
    if (click_del_login):
        if (len(del_login_entry.get())):
            l=del_login_entry.get()
            for i in range(len(spisok)):
                if spisok[i]=='Логин: {login}\n'.format(login=l):
                    index.append(i)
                    password.append(spisok[i+1])
                   
            if (len(check_password.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с такой фамилией-именем не найден")
                else:
                    k=0
                    hashobject=hashlib.md5(check_password.get().encode())
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            del_new_index.append(index[j])
                            k=1
                    if k==1:
                        del_new_index.sort(reverse=True)
                        for i in del_new_index:
                            del spisok[i-4-1:i+2+1]
                    else:
                        showerror(title="Ошибка", message="Неверный пароль")
            
            check_password.delete(0,END)
            del_login_entry.delete(0,END)
                
        else:
            showerror(title="Ошибка", message="Заполните поле ввода")
            
    if (click_del_surname_name):
        if (len(del_surname_entry.get()) and len(del_name_entry.get())):
            s=del_surname_entry.get()
            n=del_name_entry.get()
            for i in range(len(spisok)-1):
                if spisok[i]=='Фамилия: {surname}\n'.format(surname=s) and spisok[i+1]=='Имя: {name}\n'.format(name=n):
                    index.append(i)
                    password.append(spisok[i+6])

            if (len(check_password_name.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с такой фамилией-именем не найден")
                else:
                    k=0
                    hashobject=hashlib.md5(check_password_name.get().encode())
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            del_new_index.append(index[j])
                            k=1
                    if k==1:
                        del_new_index.sort(reverse=True)
                        for i in del_new_index:
                            del spisok[i:i+8]
                    else:
                        showerror(title="Ошибка", message="Неверный пароль")
                        
            del_surname_entry.delete(0,END)
            del_name_entry.delete(0,END)
            check_password_name.delete(0,END)
        else:
            showerror(title="Ошибка", message="Заполните все поля")

    if (click_del_phone_number):
        if (len(del_phone_number_entry.get())):
            sp=[]
            sp.extend(del_phone_number_entry.get())
            if (sp[0]=="8"):
                sp[0]="+"
                sp.insert(1,"7")
            sp.insert(2,'(')
            sp.insert(6,")")
            sp.insert(2,"-")
            sp.insert(8,"-")
            sp.insert(-4,"-")
            sp.insert(-2,"-")
            p=''.join(sp)
            for i in range(len(spisok)):
                if spisok[i]=='Номер телефона: {phone_number}\n'.format(phone_number=p):
                    index.append(i)
                    password.append(spisok[i+3])

            if (len(check_password_phone.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с таким номером телефона не найден")
                else:
                    k=0
                    hashobject=hashlib.md5(check_password_phone.get().encode())
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            del_new_index.append(index[j])
                            k=1
                    if k==1:
                        del_new_index.sort(reverse=True)
                        for i in del_new_index:
                            del spisok[i-3:i+4+1]
                    else:
                        showerror(title="Ошибка", message="Неверный пароль")
                        
            del_phone_number_entry.delete(0,END)
            check_password_phone.delete(0,END)
        else:
            showerror(title="Ошибка", message="Заполните поле ввода")
                
    fi=open('database.txt','w')
    for i in spisok:
        fi.write(i)
    fi.close()
            
click_del_surname_name=0
def del_surname_name():
    global click_del_phone_number
    global click_del_login
    click_del_phone_number=0
    click_del_login=0
    global click_del_surname_name
    if click_del_surname_name%2==0:
        click = ttk.Button(text="Удалить",command=del_file)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_del')
    
        canvas.delete('del_login')
        canvas.delete('del_phone_number')

        global del_surname_entry
        del_surname_entry=ttk.Entry()
        canvas.create_text(420,210,text="Фамилия: ",tag='del_surname_name')
        canvas.create_window(600, 210, window=del_surname_entry, width=300, height=25,tag='del_surname_name')

        global del_name_entry
        del_name_entry=ttk.Entry()
        canvas.create_text(420,240,text="Имя: ",tag='del_surname_name')
        canvas.create_window(600, 240, window=del_name_entry, width=300, height=25,tag='del_surname_name')

        global check_password_name
        check_password_name=ttk.Entry()
        canvas.create_text(400,270,text="Введите пароль: ",tag='del_surname_name')
        canvas.create_window(600, 270, window=check_password_name, width=300, height=25,tag='del_surname_name')
        
        click_del_surname_name+=1
    else:
        canvas.delete('del_surname_name')
        canvas.delete('click_del')
        click_del_surname_name+=1
            
click_del_login=0
def del_login():
    global click_del_phone_number
    global click_del_surname_name
    click_del_surname_name=0
    click_del_phone_number=0
    global click_del_login
    if click_del_login%2==0:
        click = ttk.Button(text="Удалить",command=del_file)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_del')
    
        canvas.delete('del_phone_number')
        canvas.delete('del_surname_name')

        global del_login_entry
        del_login_entry=ttk.Entry()
        canvas.create_text(420,220,text="Логин: ",tag='del_login')
        canvas.create_window(600, 220, window=del_login_entry, width=300, height=25,tag='del_login')

        global check_password
        check_password=ttk.Entry()
        canvas.create_text(400,250,text="Введите пароль: ",tag='del_login')
        canvas.create_window(600, 250, window=check_password, width=300, height=25,tag='del_login')
            
        click_del_login+=1
    else:
        canvas.delete('del_login')
        canvas.delete('click_del')
        click_del_login+=1

click_del_phone_number=0
def del_phone_number():
    global click_del_login
    global click_del_surname_name
    click_del_surname_name=0
    click_del_login=0
    global click_del_phone_number
    if click_del_phone_number%2==0:
        click = ttk.Button(text="Удалить",command=del_file)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_del')
    
        canvas.delete('del_surname_name')
        canvas.delete('del_login')

        global del_phone_number_entry
        del_phone_number_entry=ttk.Entry()
        canvas.create_text(400,220,text="Номер телефона: ",tag='del_phone_number')
        canvas.create_window(600, 220, window=del_phone_number_entry, width=300, height=25,tag='del_phone_number')

        global check_password_phone
        check_password_phone=ttk.Entry()
        canvas.create_text(400,250,text="Введите пароль: ",tag='del_phone_number')
        canvas.create_window(600, 250, window=check_password_phone, width=300, height=25,tag='del_phone_number')
        
        click_del_phone_number+=1
    else:
        canvas.delete('del_phone_number')
        canvas.delete('click_del')
        click_del_phone_number+=1
       
def del_dop_click():
    global clicks, click_see,click_email
    click_email=0
    click_see=0
    clicks=0
    canvas.delete('sort')
    click_sort=0
    canvas.delete('email')
    canvas.delete('key')
    canvas.delete('see')
    canvas.delete('key1')
    click = ttk.Button(text="По фамилии-имени",command=del_surname_name)
    canvas.create_window(180, 190, window=click, width=300, height=40)
    click = ttk.Button(text="По логину",command=del_login)
    canvas.create_window(180, 240, window=click, width=300, height=40)
    click = ttk.Button(text="По номеру телефона",command=del_phone_number)
    canvas.create_window(180, 290, window=click, width=300, height=40)
    click = ttk.Button(text="Назад",command=back)
    canvas.create_window(80, 650, window=click, width=100, height=40,tag='del_click_back')

def change_file():
    fi=open("database.txt")
    spisok=fi.readlines()
    fi.close()
    index=[]
    password=[]
    if (click_change_login):
        if (len(change_surname_entry.get()) and len(change_name_entry.get()) and len(change_otchestvo_entry.get())
            and len(change_phonenumber_entry.get()) and len(change_email_entry.get()) and len(change_login_entry.get())
            and len(change_password_entry.get())):
            l=what_change_login_entry.get()

            if (regex_SNO(change_surname_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода фамилии")
            elif(regex_SNO(change_name_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода имени")
            elif(regex_SNO(change_otchestvo_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода отчества")
            elif (regex_phone(change_phonenumber_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода номера телефона")
            elif (regex_email(change_email_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода e-mail")
            elif (regex_password(change_password_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода пароля")
            else:    
                
                for i in new_index:
                    spisok[i-5]="Фамилия: {surname}\n".format(surname=change_surname_entry.get())
                    spisok[i-4]="Имя: {name}\n".format(name=change_name_entry.get())
                    spisok[i-3]="Отчество: {otchestvo}\n".format(otchestvo=change_otchestvo_entry.get())
                    sp=[]
                    sp.extend(change_phonenumber_entry.get())
                    if (sp[0]=="8"):
                        sp[0]="+"
                        sp.insert(1,"7")
                    sp.insert(2,'(')
                    sp.insert(6,")")
                    sp.insert(2,"-")
                    sp.insert(8,"-")
                    sp.insert(-4,"-")
                    sp.insert(-2,"-")
                    p=''.join(sp)
                    spisok[i-2]="Номер телефона: {phone_number}\n".format(phone_number=p)
                    spisok[i-1]="email: {email}\n".format(email=change_email_entry.get())
                    spisok[i]="Логин: {login}\n".format(login=change_login_entry.get())
                    hash_object=hashlib.md5(change_password_entry.get().encode())
                    spisok[i+1]="Пароль: {password}\n".format(password=hash_object.hexdigest())
            what_change_login_entry.delete(0,END)
            change_surname_entry.delete(0,END)
            change_name_entry.delete(0,END)
            change_otchestvo_entry.delete(0,END)
            change_phonenumber_entry.delete(0,END)
            change_email_entry.delete(0,END)
            change_login_entry.delete(0,END)
            change_password_entry.delete(0,END)
        else:
            showerror(title="Ошибка", message="Заполните все поля")
            
    if (click_change_surname_name):
        if (len(what_change_surname_entry.get()) and len(what_change_name_entry.get()) and len(change_surname_entry.get())
            and len(change_name_entry.get()) and len(change_otchestvo_entry.get()) and len(change_phonenumber_entry.get())
            and len(change_email_entry.get()) and len(change_login_entry.get()) and len(change_password_entry.get())):
            s=what_change_surname_entry.get()
            n=what_change_name_entry.get()

            if (regex_SNO(change_surname_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода фамилии")
            elif(regex_SNO(change_name_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода имени")
            elif(regex_SNO(change_otchestvo_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода отчества")
            elif (regex_phone(change_phonenumber_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода номера телефона")
            elif (regex_email(change_email_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода e-mail")
            elif (regex_password(change_password_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода пароля")
            else:
                
                for i in new_index:
                    spisok[i]="Фамилия: {surname}\n".format(surname=change_surname_entry.get())
                    spisok[i+1]="Имя: {name}\n".format(name=change_name_entry.get())
                    spisok[i+2]="Отчество: {otchestvo}\n".format(otchestvo=change_otchestvo_entry.get())
                    sp=[]
                    sp.extend(change_phonenumber_entry.get())
                    if (sp[0]=="8"):
                        sp[0]="+"
                        sp.insert(1,"7")
                    sp.insert(2,'(')
                    sp.insert(6,")")
                    sp.insert(2,"-")
                    sp.insert(8,"-")
                    sp.insert(-4,"-")
                    sp.insert(-2,"-")
                    p=''.join(sp)
                    spisok[i+3]="Номер телефона: {phone_number}\n".format(phone_number=p)
                    spisok[i+4]="email: {email}\n".format(email=change_email_entry.get())
                    spisok[i+5]="Логин: {login}\n".format(login=change_login_entry.get())
                    hash_object=hashlib.md5(change_password_entry.get().encode())
                    spisok[i+6]="Пароль: {password}\n".format(password=hash_object.hexdigest())
            what_change_surname_entry.delete(0,END)
            what_change_name_entry.delete(0,END)
            change_surname_entry.delete(0,END)
            change_name_entry.delete(0,END)
            change_otchestvo_entry.delete(0,END)
            change_phonenumber_entry.delete(0,END)
            change_email_entry.delete(0,END)
            change_login_entry.delete(0,END)
            change_password_entry.delete(0,END)
        else:
            showerror(title="Ошибка", message="Заполните все поля")

    if (click_change_phone_number):
        if (len(what_change_phone_number_entry.get()) and len(change_surname_entry.get()) and len(change_name_entry.get())
            and len(change_otchestvo_entry.get()) and len(change_phonenumber_entry.get()) and len(change_email_entry.get())
            and len(change_login_entry.get()) and len(change_password_entry.get())):
            s=what_change_phone_number_entry.get()
            sp=[]
            sp.extend(s)
            if (sp[0]=="8"):
                sp[0]="+"
                sp.insert(1,"7")
            sp.insert(2,'(')
            sp.insert(6,")")
            sp.insert(2,"-")
            sp.insert(8,"-")
            sp.insert(-4,"-")
            sp.insert(-2,"-")
            p=''.join(sp)

            if (regex_SNO(change_surname_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода фамилии")
            elif(regex_SNO(change_name_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода имени")
            elif(regex_SNO(change_otchestvo_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода отчества")
            elif (regex_phone(change_phonenumber_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода номера телефона")
            elif (regex_email(change_email_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода e-mail")
            elif (regex_password(change_password_entry.get())==0):
                showerror(title="Ошибка", message="Неправильно заполнено поле ввода пароля")
            else:
                for i in new_index:
                    spisok[i-3]="Фамилия: {surname}\n".format(surname=change_surname_entry.get())
                    spisok[i-2]="Имя: {name}\n".format(name=change_name_entry.get())
                    spisok[i-1]="Отчество: {otchestvo}\n".format(otchestvo=change_otchestvo_entry.get())
                    sp=[]
                    sp.extend(change_phonenumber_entry.get())
                    if (sp[0]=="8"):
                        sp[0]="+"
                        sp.insert(1,"7")
                    sp.insert(2,'(')
                    sp.insert(6,")")
                    sp.insert(2,"-")
                    sp.insert(8,"-")
                    sp.insert(-4,"-")
                    sp.insert(-2,"-")
                    p=''.join(sp)
                    spisok[i]="Номер телефона: {phone_number}\n".format(phone_number=p)
                    spisok[i+1]="email: {email}\n".format(email=change_email_entry.get())
                    spisok[i+2]="Логин: {login}\n".format(login=change_login_entry.get())
                    hash_object=hashlib.md5(change_password_entry.get().encode())
                    spisok[i+3]="Пароль: {password}\n".format(password=hash_object.hexdigest())
            what_change_phone_number_entry.delete(0,END)
            change_surname_entry.delete(0,END)
            change_name_entry.delete(0,END)
            change_otchestvo_entry.delete(0,END)
            change_phonenumber_entry.delete(0,END)
            change_email_entry.delete(0,END)
            change_login_entry.delete(0,END)
            change_password_entry.delete(0,END)
        else:
            showerror(title="Ошибка", message="Заполните все поля")
                
    fi=open('database.txt','w')
    for i in spisok:
        fi.write(i)
    fi.close()

def dalee():
    f=open('database.txt')
    spisok=f.readlines()
    index=[]
    global new_index
    new_index=[]
    password=[]
    global what_change_login_entry,what_change_phone_number_entry,what_change_surname_entry,what_change_name_entry
    global change_surname_entry,change_name_entry,change_otchestvo_entry, change_phonenumber_entry,change_email_entry,change_login_entry,change_password_entry
    if (click_change_login):
        if (len(what_change_login_entry.get())!=0):
            l=what_change_login_entry.get()
            for i in range(len(spisok)):
                if spisok[i]=='Логин: {login}\n'.format(login=l):
                    index.append(i)
                    password.append(spisok[i+1])

            if (len(password_login.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с таким логином не найден")
                else:
                    hashobject=hashlib.md5(password_login.get().encode())
                    k=0
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            new_index.append(index[j])
                            k=1
                    if k==0:
                        showerror(title="Ошибка", message="Неверный пароль")
                    else:
                        new_index.sort(reverse=True)
                        
                        canvas.delete('change_surname_name')
                        canvas.delete('change_login')
                        canvas.delete('change_phone_number')
                        canvas.delete('click_change')

                        click = ttk.Button(text="Изменить",command=change_file)
                        canvas.create_window(720, 650, window=click, width=100, height=40,tag='dalee')
                                
                        canvas.create_text(600,120,text="Изменить на:",tag='dalee')
                                
                        change_surname_entry=ttk.Entry()
                        canvas.create_text(420,150,text="Фамилия: ",tag='dalee')
                        canvas.create_window(600, 150, window=change_surname_entry, width=300, height=25,tag='dalee')

                        change_name_entry=ttk.Entry()
                        canvas.create_text(420,180,text="Имя: ",tag='dalee')
                        canvas.create_window(600, 180, window=change_name_entry, width=300, height=25,tag='dalee')

                        change_otchestvo_entry=ttk.Entry()
                        canvas.create_text(420,210,text="Отчество: ",tag='dalee')
                        canvas.create_window(600, 210, window=change_otchestvo_entry, width=300, height=25,tag='dalee')

                        change_phonenumber_entry=ttk.Entry()
                        canvas.create_text(400,240,text="Номер телефона: ",tag='dalee')
                        canvas.create_window(600, 240, window=change_phonenumber_entry, width=300, height=25,tag='dalee')

                        change_email_entry=ttk.Entry()
                        canvas.create_text(420,270,text="e-mail: ",tag='dalee')
                        canvas.create_window(600, 270, window=change_email_entry, width=300, height=25,tag='dalee')

                        change_login_entry=ttk.Entry()
                        canvas.create_text(420,300,text="Логин: ",tag='dalee')
                        canvas.create_window(600, 300, window=change_login_entry, width=300, height=25,tag='dalee')

                        change_password_entry=ttk.Entry()
                        canvas.create_text(420,330,text="Пароль: ",tag='dalee')
                        canvas.create_window(600, 330, window=change_password_entry, width=300, height=25,tag='dalee')

    if (click_change_phone_number):                    
        if (len(what_change_phone_number_entry.get())!=0):
            l=what_change_phone_number_entry.get()
            sp=[]
            sp.extend(l)
            if (sp[0]=="8"):
                sp[0]="+"
                sp.insert(1,"7")
            sp.insert(2,'(')
            sp.insert(6,")")
            sp.insert(2,"-")
            sp.insert(8,"-")
            sp.insert(-4,"-")
            sp.insert(-2,"-")
            p=''.join(sp)
            for i in range(len(spisok)):
                if spisok[i]=='Номер телефона: {phone_number}\n'.format(phone_number=p):
                    index.append(i)
                    password.append(spisok[i+3])

            if (len(password_phone_number.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с таким номером телефона не найден")
                else:
                    hashobject=hashlib.md5(password_phone_number.get().encode())
                    k=0
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            new_index.append(index[j])
                            k=1
                    if k==0:
                        showerror(title="Ошибка", message="Неверный пароль")
                    else:
                        new_index.sort(reverse=True)
        
                        canvas.delete('change_surname_name')
                        canvas.delete('change_login')
                        canvas.delete('change_phone_number')
                        canvas.delete('click_change')
                        
                        click = ttk.Button(text="Изменить",command=change_file)
                        canvas.create_window(720, 650, window=click, width=100, height=40,tag='dalee')
                                
                        canvas.create_text(600,120,text="Изменить на:",tag='dalee')
                                
                        change_surname_entry=ttk.Entry()
                        canvas.create_text(420,150,text="Фамилия: ",tag='dalee')
                        canvas.create_window(600, 150, window=change_surname_entry, width=300, height=25,tag='dalee')

                        change_name_entry=ttk.Entry()
                        canvas.create_text(420,180,text="Имя: ",tag='dalee')
                        canvas.create_window(600, 180, window=change_name_entry, width=300, height=25,tag='dalee')

                        change_otchestvo_entry=ttk.Entry()
                        canvas.create_text(420,210,text="Отчество: ",tag='dalee')
                        canvas.create_window(600, 210, window=change_otchestvo_entry, width=300, height=25,tag='dalee')

                        change_phonenumber_entry=ttk.Entry()
                        canvas.create_text(400,240,text="Номер телефона: ",tag='dalee')
                        canvas.create_window(600, 240, window=change_phonenumber_entry, width=300, height=25,tag='dalee')

                        change_email_entry=ttk.Entry()
                        canvas.create_text(420,270,text="e-mail: ",tag='dalee')
                        canvas.create_window(600, 270, window=change_email_entry, width=300, height=25,tag='dalee')

                        change_login_entry=ttk.Entry()
                        canvas.create_text(420,300,text="Логин: ",tag='dalee')
                        canvas.create_window(600, 300, window=change_login_entry, width=300, height=25,tag='dalee')

                        change_password_entry=ttk.Entry()
                        canvas.create_text(420,330,text="Пароль: ",tag='dalee')
                        canvas.create_window(600, 330, window=change_password_entry, width=300, height=25,tag='dalee')
                            
    if (click_change_surname_name):
        if (len(what_change_surname_entry.get())!=0 and len(what_change_name_entry.get())!=0):
            s=what_change_surname_entry.get()
            n=what_change_name_entry.get()
            for i in range(len(spisok)):
                if (spisok[i]=='Фамилия: {surname}\n'.format(surname=s) and spisok[i+1]=='Имя: {name}\n'.format(name=n)):
                    index.append(i)
                    password.append(spisok[i+6])
            if (len(password_name.get())!=0):
                if (len(index)==0):
                    showerror(title="Ошибка", message="Пользователь с такой фамилией-именем не найден")
                else:
                    hashobject=hashlib.md5(password_name.get().encode())
                    k=0
                    for j in range(len(password)):
                        if password[j][8:-1:]==hashobject.hexdigest():
                            new_index.append(index[j])
                            k=1
                    if k==0:
                        showerror(title="Ошибка", message="Неверный пароль")
                    else:
                        new_index.sort(reverse=True)
        
                        canvas.delete('change_surname_name')
                        canvas.delete('change_login')
                        canvas.delete('change_phone_number')
                        canvas.delete('click_change')

                        click = ttk.Button(text="Изменить",command=change_file)
                        canvas.create_window(720, 650, window=click, width=100, height=40,tag='dalee')
                                
                        canvas.create_text(600,120,text="Изменить на:",tag='dalee')
                            
                        change_surname_entry=ttk.Entry()
                        canvas.create_text(420,150,text="Фамилия: ",tag='dalee')
                        canvas.create_window(600, 150, window=change_surname_entry, width=300, height=25,tag='dalee')

                        change_name_entry=ttk.Entry()
                        canvas.create_text(420,180,text="Имя: ",tag='dalee')
                        canvas.create_window(600, 180, window=change_name_entry, width=300, height=25,tag='dalee')

                        change_otchestvo_entry=ttk.Entry()
                        canvas.create_text(420,210,text="Отчество: ",tag='dalee')
                        canvas.create_window(600, 210, window=change_otchestvo_entry, width=300, height=25,tag='dalee')

                        change_phonenumber_entry=ttk.Entry()
                        canvas.create_text(400,240,text="Номер телефона: ",tag='dalee')
                        canvas.create_window(600, 240, window=change_phonenumber_entry, width=300, height=25,tag='dalee')

                        change_email_entry=ttk.Entry()
                        canvas.create_text(420,270,text="e-mail: ",tag='dalee')
                        canvas.create_window(600, 270, window=change_email_entry, width=300, height=25,tag='dalee')

                        change_login_entry=ttk.Entry()
                        canvas.create_text(420,300,text="Логин: ",tag='dalee')
                        canvas.create_window(600, 300, window=change_login_entry, width=300, height=25,tag='dalee')

                        change_password_entry=ttk.Entry()
                        canvas.create_text(420,330,text="Пароль: ",tag='dalee')
                        canvas.create_window(600, 330, window=change_password_entry, width=300, height=25,tag='dalee')        
        
    
click_change_surname_name=0
def change_surname_name():
    global click_change_phone_number
    global click_change_login
    click_change_phone_number=0
    click_change_login=0
    global click_change_surname_name
    if click_change_surname_name%2==0:
        click = ttk.Button(text="Далее",command=dalee)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_change')
    
        canvas.delete('change_login')
        canvas.delete('change_phone_number')
        canvas.delete('dalee')

        global what_change_surname_entry,what_change_name_entry

        what_change_surname_entry=ttk.Entry()
        what_change_name_entry=ttk.Entry()
        
        change_surname_entry=ttk.Entry()
        canvas.create_text(420,210,text="Фамилия: ",tag='change_surname_name')
        canvas.create_window(600, 210, window=what_change_surname_entry, width=300, height=25,tag='change_surname_name')

        change_name_entry=ttk.Entry()
        canvas.create_text(420,240,text="Имя: ",tag='change_surname_name')
        canvas.create_window(600, 240, window=what_change_name_entry, width=300, height=25,tag='change_surname_name')

        global password_name
        password_name=ttk.Entry()
        canvas.create_text(400,270,text="Введите пароль: ",tag='change_surname_name')
        canvas.create_window(600, 270, window=password_name, width=300, height=25,tag='change_surname_name')
        
        click_change_surname_name+=1
    else:
        canvas.delete('change_surname_name')
        canvas.delete('click_change')
        canvas.delete('dalee')
        click_change_surname_name+=1

click_change_login=0
def change_login():
    global click_change_phone_number
    global click_change_surname_name
    click_change_surname_name=0
    click_change_phone_number=0
    global click_change_login
    if click_change_login%2==0:
        click = ttk.Button(text="Далее",command=dalee)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_change')
    
        canvas.delete('change_phone_number')
        canvas.delete('change_surname_name')
        canvas.delete('dalee')
        
        global what_change_login_entry

        what_change_login_entry=ttk.Entry()
        canvas.create_text(420,220,text="Логин: ",tag='change_login')
        canvas.create_window(600, 220, window=what_change_login_entry, width=300, height=25,tag='change_login')

        global password_login
        password_login=ttk.Entry()
        canvas.create_text(400,250,text="Введите пароль: ",tag='change_login')
        canvas.create_window(600, 250, window=password_login, width=300, height=25,tag='change_login')
        
        click_change_login+=1
    else:
        canvas.delete('change_login')
        canvas.delete('click_change')
        canvas.delete('dalee')
        click_change_login+=1

click_change_phone_number=0
def change_phone_number():
    global click_change_login
    global click_change_surname_name
    click_change_surname_name=0
    click_change_login=0
    global click_change_phone_number
    if click_change_phone_number%2==0:
        click = ttk.Button(text="Далее",command=dalee)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='click_change')
    
        canvas.delete('change_surname_name')
        canvas.delete('change_login')
        canvas.delete('dalee')

        global what_change_phone_number_entry
        what_change_phone_number_entry=ttk.Entry()
        
        change_phone_number_entry=ttk.Entry()
        canvas.create_text(400,220,text="Номер телефона: ",tag='change_phone_number')
        canvas.create_window(600, 220, window=what_change_phone_number_entry, width=300, height=25,tag='change_phone_number')

        global password_phone_number
        password_phone_number=ttk.Entry()
        canvas.create_text(400,250,text="Введите пароль: ",tag='change_phone_number')
        canvas.create_window(600, 250, window=password_phone_number, width=300, height=25,tag='change_phone_number')

        click_change_phone_number+=1
    else:
        canvas.delete('change_phone_number')
        canvas.delete('click_change')
        canvas.delete('dalee')
        click_change_phone_number+=1

def change_dop_click():
    global clicks, click_see,click_email
    click_email=0
    click_see=0
    clicks=0
    canvas.delete('sort')
    click_sort=0
    canvas.delete('email')
    canvas.delete('key')
    canvas.delete('see')
    canvas.delete('key1')
    click = ttk.Button(text="По фамилии-имени",command=change_surname_name)
    canvas.create_window(180, 190, window=click, width=300, height=40)
    click = ttk.Button(text="По логину",command=change_login)
    canvas.create_window(180, 240, window=click, width=300, height=40)
    click = ttk.Button(text="По номеру телефона",command=change_phone_number)
    canvas.create_window(180, 290, window=click, width=300, height=40)
    click = ttk.Button(text="Назад",command=back)  
    canvas.create_window(80, 650, window=click, width=100, height=40,tag='change_click_back')

def send_email():
    f=open('database.txt')
    spisok=f.readlines()
    f.close()
    flag=False
    for i in spisok:
        if (i[8:-1:]==email_entry.get()):
            flag=True
    if flag==True:
        server=smtplib.SMTP('smtp.mail.ru',25)
        server.starttls()
        server.login('agadzhanyan_alyona@mail.ru','cJhXtbE4Z4EpzzdhMBp1')
        server.sendmail('agadzhanyan_alyona@mail.ru',email_entry.get(),message.get("1.0","end"))
        server.quit()
    else:
        showerror(title="Ошибка", message="Пользователь с такой почтой не найден") 
    email_entry.delete(0,END)
    message.delete("1.0",END)

click_email=0              
def dop_click_email():
    global click_see,clicks,click_sort
    click_see=0
    clicks=0
    canvas.delete('sort')
    click_sort=0
    canvas.delete('key')
    canvas.delete('see')
    global email_entry,message,click_email
    if (click_email%2==0):
        canvas.create_text(425,130,text="e-mail: ",tag='email')
        email_entry=ttk.Entry()
        canvas.create_window(600,130,window=email_entry,width=300, height=25,tag='email')
        canvas.create_text(410,170,text="Сообщение: ",tag='email')
        message=Text(bg="light yellow")
        canvas.create_window(600,300,window=message,width=300, height=300,tag='email')
        click = ttk.Button(text="Отправить",command=send_email)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='email')
        click_email+=1
    else:
        canvas.delete('email')
        click_email+=1

def sort():
    fi=open('database.txt')
    spisok=fi.readlines()
    fi.close()
    f=open('database.txt','w')
    if (len(combobox1.get())==0 and len(combobox2.get())==0):
        showerror(title="Ошибка", message="Заполните все поля")
    else:
        if (combobox2.get()=="По фамилии"):
            surname_spisok=[]
            for i in spisok:
                if (i[0:7]=="Фамилия"):
                    surname_spisok.append(i)
            if (combobox1.get()=="По возрастанию"):
                surname_spisok.sort(reverse=True)
            else:
                surname_spisok.sort()
            for i in surname_spisok:
                for j in range(len(spisok)):
                    if (i==spisok[j]):
                        f.write(''.join(spisok[j:j+7])+'\n')
                            
        if (combobox2.get()=="По имени"):
            name_spisok=[]
            for i in spisok:
                if (i[0:3]=="Имя"):
                    name_spisok.append(i)
            if (combobox1.get()=="По возрастанию"):
                name_spisok.sort(reverse=True)
            else:
                name_spisok.sort()
            for i in name_spisok:
                for j in range(len(spisok)):
                   if (i==spisok[j]):
                        f.write(''.join(spisok[j-1:j+6])+'\n')
                            
        if (combobox2.get()=="По логину"):
            login_spisok=[]
            for i in spisok:
                if (i[0:5]=="Логин"):
                    login_spisok.append(i)
            if (combobox1.get()=="По возрастанию"):
                login_spisok.sort(reverse=True)
            else:
                login_spisok.sort()
            for i in login_spisok:
                for j in range(len(spisok)):
                    if (i==spisok[j]):
                        f.write(''.join(spisok[j-5:j+2])+'\n')
    f.close()
    combobox1.delete(0,END)
    combobox2.delete(0,END)

click_sort=0
def dop_click_sort():
    global click_sort,click_email, click_see,clicks
    click_email=0
    click_see=0
    clicks=0
    canvas.delete('see')
    canvas.delete('email')
    canvas.delete('key')
    if (click_sort%2==0):
        canvas.create_text(435,240,text="Выберете:",tag='sort')
        canvas.create_text(435,280,text="Выберете:",tag='sort')
        click = ttk.Button(text="Сортировать",command=sort)
        canvas.create_window(720, 650, window=click, width=100, height=40,tag='sort')
        values1=["По возрастанию","По убыванию"]
        values2=["По фамилии","По имени","По логину"]
        global combobox1,combobox2
        combobox1=ttk.Combobox(values=values1)
        canvas.create_window(600,240,window=combobox1,width=250,height=25,tag='sort')
        combobox2=ttk.Combobox(values=values2)
        canvas.create_window(600,280,window=combobox2,width=250,height=25,tag='sort')
        click_sort+=1
    else:
        canvas.delete('sort')
        click_sort+=1
    
click = ttk.Button(text="Посмотреть список пользователей",command=see)
canvas.create_window(180, 90, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Добавить пользователя",command=add)
canvas.create_window(180, 140, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Удалить пользователя", command=del_dop_click)
canvas.create_window(180, 190, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Изменить пользователя", command=change_dop_click)
canvas.create_window(180, 240, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Сохранить изменения в файл",command=writting)
canvas.create_window(180, 290, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Отправить сообщение на e-mail пользователя",command=dop_click_email)
canvas.create_window(180, 340, window=click, width=300, height=40,tag='key1')

click = ttk.Button(text="Отсортировать по выбранному полю",command=dop_click_sort)
canvas.create_window(180, 390, window=click, width=300, height=40,tag='key1')
    
click = ttk.Button(text="Выход",command=root.quit)
canvas.create_window(180, 440, window=click, width=300, height=40,tag='key1')

root.mainloop()
exit(0)
