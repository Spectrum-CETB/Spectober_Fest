from tkinter import *
import mysql.connector
import sys
import os

connection1 = mysql.connector.connect(host='localhost', database='teacher', user='root', password='Sainanda@59',
                                      auth_plugin='mysql_native_password')

connection2 = mysql.connector.connect(host='localhost', database='student', user='root', password='Sainanda@59',

                                      auth_plugin='mysql_native_password')
global stu_name, stu_regd_no, quiz_score


def submit_score(box):
    global stu_name, stu_regd_no, quiz_score
    box.destroy()
    cursor = connection2.cursor()
    query = "INSERT INTO leaderboard(name,regd_num,score) VALUES(%s, %s, %s)"
    cursor.execute(query, (stu_name, stu_regd_no, quiz_score))
    connection2.commit()
    cursor.close()
    leaderboard_page()


def exit_app():
    window.destroy()


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def add_ques_page():
    add_ques = Toplevel(window)
    add_ques.title("Add Questions")
    add_ques.geometry('1990x900')
    add_ques.config(bg='#3EDBF0')

    def update_database():
        question = ques_box.get()
        opt1 = opt1_box.get()
        opt2 = opt2_box.get()
        opt3 = opt3_box.get()
        opt4 = opt4_box.get()
        optcrt = optcrt_box.get()

        cursor = connection1.cursor()
        query = "INSERT INTO questions(ques, opt_a, opt_b, opt_c, opt_d,correct_opt) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (question, opt1, opt2, opt3, opt4, optcrt))
        connection1.commit()
        cursor.close()
        add_ques.destroy()

    Label(add_ques, text="NEW QUESTION", bg='black', fg="white", borderwidth=4, relief="groove",
          font=("Arial Bold", 36)).grid(row=1, padx=(200, 0), pady=50)

    ques_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=40,
                     justify='center', fg="black", font=("Arial Bold", 26))
    ques_box.grid(row=2, padx=(200, 0), pady=(30, 30))
    ques_box.insert(0, "Enter the Question Here!!!")

    opt1_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt1_box.grid(row=3, padx=(0, 500), pady=(30, 30))
    opt1_box.insert(0, "Option A!!!")

    opt2_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt2_box.grid(row=3, padx=(900, 0), pady=(30, 30))
    opt2_box.insert(0, "Option B!!!")

    opt3_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt3_box.grid(row=5, padx=(0, 500), pady=(30, 30))
    opt3_box.insert(0, "Option C!!!")

    opt4_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt4_box.grid(row=5, padx=(900, 0), pady=(30, 30))
    opt4_box.insert(0, "Option D!!!")

    optcrt_box = Entry(add_ques, borderwidth=9, bg="#FFA900", width=25,
                       justify='center', fg="black", font=("Arial Bold", 26))
    optcrt_box.grid(row=7, padx=(200, 0), pady=(30, 30))
    optcrt_box.insert(0, "Correct Option(A,B,C,D)!!!")

    add_btn = Button(add_ques, text="Add Question", borderwidth=9, bg="#FFA900", width=15,
                     fg="black", font=("Arial Bold", 26), command=update_database)
    add_btn.grid(row=9, padx=(200, 0), pady=(30, 30))


def edit_ques_page(num, dry):
    edit_ques = Toplevel(window)
    edit_ques.title("Edit Questions")
    edit_ques.geometry('1990x900')
    edit_ques.config(bg='#3EDBF0')
    dry.destroy()
    cursor = connection1.cursor()
    query = "SELECT * FROM questions WHERE id=%s"
    cursor.execute(query, (num,))
    result = cursor.fetchall()
    cursor.close()

    def update_database():
        question = ques_box.get()
        opt1 = opt1_box.get()
        opt2 = opt2_box.get()
        opt3 = opt3_box.get()
        opt4 = opt4_box.get()
        optcrt = optcrt_box.get()

        cursor1 = connection1.cursor()
        query1 = "UPDATE questions SET ques=%s, opt_a=%s, opt_b=%s, opt_c=%s, opt_d=%s,correct_opt=%s WHERE id=%s"
        cursor1.execute(query1, (question, opt1, opt2, opt3, opt4, optcrt, num))
        connection1.commit()
        cursor1.close()
        edit_ques.destroy()

    Label(edit_ques, text="EDIT QUESTION AND OPTIONS", bg='black', fg="white", borderwidth=4, relief="groove",
          font=("Arial Bold", 36)).grid(row=1, padx=(200, 0), pady=50)

    ques_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=40,
                     justify='center', fg="black", font=("Arial Bold", 26))
    ques_box.grid(row=2, padx=(200, 0), pady=(30, 30))
    ques_box.insert(0, result[0][1])

    opt1_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt1_box.grid(row=3, padx=(0, 500), pady=(30, 30))
    opt1_box.insert(0, result[0][2])

    opt2_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt2_box.grid(row=3, padx=(900, 0), pady=(30, 30))
    opt2_box.insert(0, result[0][3])

    opt3_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt3_box.grid(row=5, padx=(0, 500), pady=(30, 30))
    opt3_box.insert(0, result[0][4])

    opt4_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=20,
                     justify='center', fg="black", font=("Arial Bold", 26))
    opt4_box.grid(row=5, padx=(900, 0), pady=(30, 30))
    opt4_box.insert(0, result[0][5])

    optcrt_box = Entry(edit_ques, borderwidth=9, bg="#FFA900", width=20,
                       justify='center', fg="black", font=("Arial Bold", 26))
    optcrt_box.grid(row=7, padx=(200, 0), pady=(30, 30))
    optcrt_box.insert(0, result[0][6])

    update_btn = Button(edit_ques, text="Update Question", borderwidth=9, bg="#FFA900", width=15,
                        fg="black", font=("Arial Bold", 26), command=update_database)
    update_btn.grid(row=9, padx=(200, 0), pady=(30, 30))


def list_all_ques(action, num):
    all_ques = Toplevel(window)
    all_ques.title("All Questions")
    all_ques.geometry('1990x900')
    all_ques.config(bg='#3EDBF0')
    cursor = connection1.cursor()
    query = "SELECT ques FROM questions ORDER BY id ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    Label(all_ques, text="Choose Question to " + str(action), borderwidth=4, relief="raised", bg='#F6AE99',
          fg='black', font=("Arial Bold", 20)).grid(row=0, pady=(10, 5), padx=(300, 150))

    count = 0
    for ques in result:
        count += 1
        ques_btn = Button(all_ques, text=(str(count) + ")" + ' '.join(ques)), borderwidth=9, bg="black",
                          fg="#FFA900", font=("Arial Bold", 15))
        ques_btn.grid(row=count, padx=(600, 450), pady=2)

    select_box = Entry(all_ques, borderwidth=9, bg="#FFA900", width=25,
                       justify='center', fg="black", font=("Arial Bold", 15))
    select_box.grid(row=count+1, padx=(600, 450), pady=2)
    select_box.insert(0, "Enter Number 1-" + str(count))
    if num == 1:
        update_btn = Button(all_ques, text="Attempt!!!", borderwidth=9, bg="#FFA900", width=10, font=("Arial Bold", 10),
                            fg="black", command=lambda: display_ques_page(select_box.get()))
        update_btn.grid(row=count+2, padx=(480, 450))
        submit_btn = Button(all_ques, text="End Test!!!", borderwidth=9, bg="#FFA900", width=10, fg="black",
                            font=("Arial Bold", 10), command=lambda: submit_score(all_ques))
        submit_btn.grid(row=count + 2, padx=(720, 450))
    if num == 2:
        update_btn = Button(all_ques, text="Edit!!!", borderwidth=9, bg="#FFA900", width=10, fg="black",
                            font=("Arial Bold", 10), command=lambda: edit_ques_page(select_box.get(), all_ques))
        update_btn.grid(row=count+2, padx=(600, 450))


def display_ques_page(num):
    display_ques = Toplevel(window)
    display_ques.title("Edit Questions")
    display_ques.geometry('1990x900')
    display_ques.config(bg='#3EDBF0')

    cursor = connection1.cursor()
    query = "SELECT * FROM questions WHERE id=%s"
    cursor.execute(query, (num,))
    result = cursor.fetchall()
    cursor.close()

    def ans_checker(ans, box):
        global quiz_score
        if ans == result[0][6]:
            quiz_score += 1
            box.configure(bg='green')
        else:
            box.configure(bg='red')
        opt1_box.configure(state='disabled')
        opt2_box.configure(state='disabled')
        opt3_box.configure(state='disabled')
        opt4_box.configure(state='disabled')

    Label(display_ques, text="QUESTION " + str(num), bg='black', fg="white", borderwidth=4, relief="groove",
          font=("Arial Bold", 36)).grid(row=1, padx=(200, 0), pady=50)

    ques_box = Label(display_ques, text=result[0][1], borderwidth=9, relief="groove", bg="#FFA900", width=50,
                     justify='center', fg="black", font=("Arial Bold", 26))
    ques_box.grid(row=2, padx=(200, 0), pady=(30, 30))

    opt1_box = Button(display_ques, text=result[0][2], borderwidth=9, bg="#FFA900", width=20, justify='center',
                      fg="black", font=("Arial Bold", 26), command=lambda: ans_checker('A', opt1_box))
    opt1_box.grid(row=3, padx=(0, 500), pady=(30, 30))

    opt2_box = Button(display_ques, text=result[0][3], borderwidth=9, bg="#FFA900", width=20, justify='center',
                      fg="black", font=("Arial Bold", 26), command=lambda: ans_checker('B', opt2_box))
    opt2_box.grid(row=3, padx=(900, 0), pady=(30, 30))

    opt3_box = Button(display_ques, text=result[0][4], borderwidth=9, bg="#FFA900", width=20, justify='center',
                      fg="black", font=("Arial Bold", 26), command=lambda: ans_checker('C', opt3_box))
    opt3_box.grid(row=5, padx=(0, 500), pady=(30, 30))

    opt4_box = Button(display_ques, text=result[0][5], borderwidth=9, bg="#FFA900", width=20, justify='center',
                      fg="black", font=("Arial Bold", 26), command=lambda: ans_checker('D', opt4_box))
    opt4_box.grid(row=5, padx=(900, 0), pady=(30, 30))

    next_box = Button(display_ques, text="Done", borderwidth=9, bg="#FFA900", width=20,
                      justify='center', fg="black", font=("Arial Bold", 20), command=lambda: display_ques.destroy())
    next_box.grid(row=7, padx=(200, 0), pady=(30, 30))


def question_manager():
    qm_window = Toplevel(window)
    qm_window.title("Question Manager")
    qm_window.geometry('1990x900')
    qm_window.config(bg='#BCFFB9')

    Label(qm_window, text="QUESTION MANAGER DASHBOARD", borderwidth=4, relief="raised", bg='#F6AE99',
          fg='black', font=("Arial Bold", 50)).grid(row=1, pady=(50, 0), padx=(170, 150))

    add_ques_btn = Button(qm_window, text="ADD QUESTION", borderwidth=9, bg="black", fg="#FFA900",
                          font=("Arial Bold", 27), command=add_ques_page)
    add_ques_btn.grid(row=5, padx=(0, 900), pady=250)

    edit_ques_btn = Button(qm_window, text="EDIT QUESTION", borderwidth=9, bg="black", fg="#FFA900",
                           font=("Arial Bold", 27), command=lambda: list_all_ques("Edit", 2))
    edit_ques_btn.grid(row=5, padx=(450, 450), pady=250)

    leaderboard_btn = Button(qm_window, text="LEADERBOARD", borderwidth=9, bg="black", fg="#FFA900",
                             font=("Arial Bold", 27), command=leaderboard_page)
    leaderboard_btn.grid(row=5, padx=(900, 0), pady=250)


def stu_page():
    student = Toplevel(window)
    student.title("Student Login")
    student.geometry('1990x900')
    student.config(bg='#3EDBF0')

    name_label = Label(student, text="Student Name:", bg='#3EDBF0', fg="black", borderwidth=4, relief="groove",
                       font=("Arial Bold", 27))
    name_label.grid(row=2, padx=(275, 200), pady=(300, 0))
    name = Entry(student, width=27, borderwidth=9, bg="#FFA900",
                 justify='center', fg="black", font=("Arial Bold", 16))
    name.grid(row=2, pady=(300, 0), ipady=15, padx=(750, 0))
    name.insert(0, "Student Name")

    regd_label = Label(student, text="Student Regd No:", bg='#3EDBF0', fg="black", borderwidth=4, relief="groove",
                       font=("Arial Bold", 27))
    regd_label.grid(row=3, padx=(275, 200), pady=(0, 0))
    regd_no = Entry(student, width=27, borderwidth=9, bg="#FFA900",
                    justify='center', fg="black", font=("Arial Bold", 16))
    regd_no.grid(row=3, pady=(0, 0), ipady=15, padx=(750, 0))
    regd_no.insert(0, "Enter Registration Number")

    def func_call():
        global stu_name, stu_regd_no, quiz_score
        stu_name = name.get()
        stu_regd_no = regd_no.get()
        quiz_score = 0
        list_all_ques("Attempt", 1)
        student.destroy()

    login_btn = Button(student, text="LET'S BEGIN WITH QUIZZZ", borderwidth=9, bg="black", fg="#FFA900",
                       font=("Arial Bold", 18), command=func_call)
    login_btn.grid(row=6, padx=(750, 0), pady=10)


def teach_page():
    teacher = Toplevel(window)
    teacher.title("Teacher Login")
    teacher.geometry('1990x900')
    teacher.config(bg='#3EDBF0')

    def login_auth(uname, passwd):
        cursor = connection1.cursor()
        query = "SELECT * FROM login WHERE username=%s AND password=%s"
        cursor.execute(query, (uname, passwd))
        result = cursor.fetchall()
        cursor.close()
        if len(result) > 0:
            display_msg = Label(teacher, text="Login Successful", bg='black', fg="orange", font=("Arial Bold", 36))
            display_msg.grid(row=0, padx=(450, 0), pady=(45, 0))
            display_msg.after(10000, display_msg.destroy)
            question_manager()
            teacher.destroy()

        else:
            display_msg = Label(teacher, text="Login Unsuccessful Try Again", bg='black', fg="orange",
                                font=("Arial Bold", 36))
            display_msg.grid(row=0, padx=(450, 0), pady=(45, 0))
            display_msg.after(3000, display_msg.destroy)

    user_label = Label(teacher, text="Username:", bg='#3EDBF0', fg="black", borderwidth=4, relief="groove",
                       font=("Arial Bold", 36))
    user_label.grid(row=2, padx=(300, 200), pady=(250, 0))
    username = Entry(teacher, width=27, borderwidth=9, bg="#FFA900",
                     justify='center', fg="black", font=("Arial Bold", 16))
    username.grid(row=2, pady=(250, 0), ipady=15, padx=(750, 0))

    pass_label = Label(teacher, text="Password:", bg='#3EDBF0', fg="black", borderwidth=4, relief="groove",
                       font=("Arial Bold", 36))
    pass_label.grid(row=3, padx=(300, 200), pady=(0, 0))
    password = Entry(teacher, width=27, borderwidth=9, bg="#FFA900",
                     justify='center', fg="black", font=("Arial Bold", 16))
    password.grid(row=3, pady=(0, 0), ipady=15, padx=(750, 0))

    login_btn = Button(teacher, text="LOG INTO SERVER", borderwidth=9, bg="black", fg="#FFA900",
                       font=("Arial Bold", 18), command=lambda: login_auth(username.get(), password.get()))
    login_btn.grid(row=6, padx=(750, 0), pady=10)


def leaderboard_page():
    leaderboard = Toplevel(window)
    leaderboard.title("Leaderboard Page")
    leaderboard.geometry('1990x900')
    leaderboard.config(bg='#3EDBF0')

    cursor = connection2.cursor()
    query = "SELECT * FROM leaderboard ORDER BY score DESC"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    Label(leaderboard, text="LEADERBOARD", borderwidth=4, relief="raised", bg='#F6AE99', width=30,
          fg='black', font=("Arial Bold", 30)).grid(row=0, pady=(10, 5), padx=(400, 300))

    count = 0
    for ques in result:
        count += 1
        output = str(count) + ')' + " " + ques[0] + " || " + ques[1] + " || Score: " + str(ques[2])
        name_btn = Button(leaderboard, text=output, borderwidth=9, bg="black",
                          fg="#FFA900", font=("Arial Bold", 20))
        name_btn.grid(row=count, padx=(400, 300), pady=2)


window = Tk()
window.title("SID-TASK-3")
welcome = Label(window, text="QuiZzzIt!", bg='#45FFCA', fg="black", borderwidth=4, relief="groove",
                font=("Arial Bold", 50))
welcome.grid(row=1, padx=620, pady=(300, 0))
window.config(bg='#45FFCA')
window.geometry('1990x1440')
teach_btn = Button(window, text="TEACHER LOGIN", borderwidth=9, bg="black", fg="#FFA900", font=("Arial Bold", 18),
                   command=teach_page)
teach_btn.grid(row=6, padx=(10, 250), pady=50)

stu_btn = Button(window, text="STUDENT LOGIN", borderwidth=9, bg="black", fg="#FFA900", font=("Arial Bold", 18),
                 command=stu_page)
stu_btn.grid(row=6, padx=(250, 10), pady=50)
window.mainloop()
