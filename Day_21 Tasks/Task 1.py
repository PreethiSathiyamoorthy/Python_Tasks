def file_Handle():
    file = open("H:\Free Python Class Preethi\Daily_Tasks_Preethi\Day_21 Tasks\File Handling\demo1.txt","w")
    file.write("Welcome To Python World..!")
    print("File is Create and written")

    file = open("H:\Free Python Class Preethi\Daily_Tasks_Preethi\Day_21 Tasks\File Handling\demo1.txt","r")
    print("Content is read:",file.read())

    file = open("H:\Free Python Class Preethi\Daily_Tasks_Preethi\Day_21 Tasks\File Handling\demo1.txt","a")
    file.write("\n Hi I'm Preethi! I am from madurai. I Have Completed my Bacholers in B sc Physics.")
    print("Your written is append")

    file = open("H:\Free Python Class Preethi\Daily_Tasks_Preethi\Day_21 Tasks\File Handling\demo1.txt","r")
    print("Content is read:", file.read())
    
    file.close()
file_Handle()    
    
    
