import os
import sys
print("WELCOME TO THECODE764 SYSTEM")
platform = sys.platform
print("INSTALLING THECODE764 SYSTEM IN",platform)
print("SELECT TOOL")
print("1(DISCORD INSTALL IN PLATFORM",platform )
print("2(TERMINAL")
print("3(TERMINAL ROOT")
print("4(CMD (POWERSHELL)")
print("5(VIM")
print("7(VSCODE")
print("8(UPDATE system.py")
print("9(INSTALL ALL REPOSITORY IN GITHUB THECODE764")
tool = input("Enter Tool Number:")
if tool == "1":
    os.system("sudo apt-get install discord")
if tool == "2":
    print("WELCOME TO TERMINAL! PLEASE DONT USE COMMAND CD IN PYTHON TERMINAL!!!!!")
    command = input("Please Enter a Command:")
    os.system(command)
    while command != "end":
        command = input("Please Enter a Command:")
        os.system(command)
if tool == "3":
    os.system("sudo su")
if tool == "4":
    os.system("sudo snap install powershell --classic; powershell")
if tool == "5":
    os.system("vim")
if tool == "7":
    os.system("code")
if tool == "8":
    os.system("git clone https://github.com/Thecode764/system; cd system; python3 system2.py")
if tool == "9":
    print("Error Please try again in 1 month ago")