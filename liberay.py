
import datetime as dt

def get_date():
      a = dt.date.today()
      d = str( a.day )
      m = str( a.month )
      y = str( a.year )
      return d + "-" + m + "-" + y

def issue_book():
  enr=input("enter your enrollment number: ")
  bnum=input("enter your book number: ")
  idate=get_date()
  rdate="N/A"
  obj=open("all_issued.txt","a")
  obj.write(enr+","+bnum+","+idate+","+rdate+"\n")
  print("book issued successfully")

def return_book():
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()
    data_found = False

    ind = 0
    bnum = input("Enter Book Number : ")
    while ind < len(all_lines):
        oneline = all_lines[ind]
        ls = oneline.split(",")
        if ls[1] == bnum and ls[3] == "NA\n":
            ls[3] = get_date() + "\n"
            newline = ",".join(ls)
            all_lines[ind] = newline
            data_found = True
            break
        ind = ind + 1
    else:
        print("Invalid Book Number")

    if data_found == True:
        fobj = open("all_issued.txt", "w")
        fobj.writelines(all_lines)
        fobj.close()
        print("Book Returned..")
    input()


def view_not_ret_books():
    obj = open("all_issued.txt", "r")

    for line in obj:
        data = line.split(",")

        if data[3] == "N/A\n":
            print(" ".join([data[0], data[1], data[2]]))

    obj.close()

def search_stud():
  enr=input("enter your enrollment number: ")
  obj = open("all_students.txt", "r")
  for oneline in obj:
      sdata=oneline.split(",")
      if enr == sdata[0] :
          print(sdata[0],sdata[1],sdata[2],sdata[3],sdata[4])
  obj.close()

def search_book():
  bnum= input("enter your book number: ")
  obj2 = open("all_books.txt", "r")
  for line in obj2 :
      bdata= line.split(",")
      if bnum == bdata[0]:
          print(bdata[0],bdata[1],bdata[2],bdata[3])
  obj2.close()

def add_new_stud():
  eno=input("enter erollment number: ")
  sn=input("enter your name: ")
  scl=input("enter your class: ")
  em=input("enter your email: ")
  sno=input("enter your mob number: ")
  obj1=open("all_students.txt","a")
  obj1.write(eno + "," + sn + "," + scl + "," + em + "," + sno + "\n")
  obj1.close()

def add_new_book():
  bn=input("emter book number: ")
  bt=input("enter book title: ")
  ba=input("enter book author: ")
  bp=input("enter book publication: ")
  obj2=open("all_books.txt","a")
  obj2.write(bn+","+bt+","+ba+","+bp+"\n")
  obj2.close()

def stud_history():
    enr = input("Enter Enrollment Number : ")

    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[0] == enr:
            print(ls[1], ls[2], ls[3], sep="\t")
    input()


def book_history():
    bnum = input("Enter Book Number : ")
    count = 0

    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[1] == bnum:
            print(ls[0], ls[2], ls[3], sep="\t")
            count += 1
    print("This Book was issued", count, "times.")
    input()


while True:
      print("Select Operation")
      print("1 - Issue Book")
      print("2 - Return Book")
      print("3 - View Not Returned Books")
      print("4 - Search Student")
      print("5 - Search Book")
      print("6 - Add New Student")
      print("7 - Add New Book")
      print("8 - Student History")
      print("9 - Book History")
      print("0 - Exit")
      ch = int(input("Provide your Choice : "))

      if ch==1: issue_book()
      elif ch==2: return_book()
      elif ch==3: view_not_ret_books()
      elif ch==4: search_stud()
      elif ch==5: search_book()
      elif ch==6: add_new_stud()
      elif ch==7: add_new_book()
      elif ch==8: stud_history()
      elif ch==9: book_history()
      elif ch==0: exit(0)
