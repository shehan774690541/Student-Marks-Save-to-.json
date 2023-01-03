import json

Data = "data.json"

def Choices():
    print("S T U D E N T S   M A R K S   T A B L E")
    print("Data Management System")
    print("(1) View Data")
    print("(2) Add Data")
    print("(3) Delete Data")
    print("(4) final Data")
    print("(5) Exit")

def view_data():
    with open(Data, "r") as f:
        temp = json.load(f)
        i = 0
        print("_________________________________________________________________________________")
        print("|\t| Name\t\t| First Subject\t| Secound Subject\t| Third Subject\t|")

        for entry in temp:
            name = entry["name"]
            s1 = entry["first_Subject"]
            s2 = entry["secound_Subject"]
            s3 = entry["third_Subject"]
            print(f"|{i}\t",end='')
            print(f"| {name}\t",end='')
            print(f"| marks : {s1}", end="\t| ")
            print(f"marks : {s2}", end="\t\t| ")
            print(f"marks : {s3}", end="\t| \n")
            i = i + 1
        print("\n")

def view_total():
    with open (Data, "r") as f:
        temp = json.load(f)
        i = 0
        high = 0
        highStu = ""
        print("_________________________________________________________________________________")

        for entry in temp:
            name = entry["name"]
            s1 = entry["first_Subject"]
            s2 = entry["secound_Subject"]
            s3 = entry["third_Subject"]
            i = i + 1    

            mark = int(s1) + int(s2) + int(s3)
            mark = int(mark)
            if high < mark:
                highN = name
                sub1 = s1
                sub2 = s2
                sub2 = s2
                

                


        print("Rank 1st : ", highN, "\t Equal Marks of"" : ", mark)
        print("student count \t : \t" , i)
        print("")

def add_data():
    ithem_data = {}
    with open (Data, "r") as f:
        temp = json.load(f)
    ithem_data["name"] = input("Name of Student: ")
    ithem_data["first_Subject"] = input("Enter marks of First subject: ")
    ithem_data["secound_Subject"] = input("Enter marks of secound subject: ")
    ithem_data["third_Subject"] = input("Enter marks of third subject: ")

    temp.append(ithem_data)
    with open (Data, "w") as f:
        json.dump(temp, f, indent=4)
    print("\n")

def delete_data():
    view_data()
    new_data = []
    with open (Data, "r") as f:
        temp = json.load(f)
        deta_length = len(temp) -1
    print ("which index number would you like to delete?")
    delete_option = input(f"Select a number 0-{deta_length} : ")
    i = 0
    for entry in temp:
        if i == int(delete_option):
            pass
            i = i + 1
        else:
            new_data.append(entry)
            i = i + 1
    with open (Data, "w") as f:
        json.dump(new_data, f, indent=4)
    print("")


while True:
    Choices()
    choice = input("\nEnter Number : ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        view_total()
    elif choice == "5":
        break
    else:
        print("You did not select a number, please read more carefully.")
