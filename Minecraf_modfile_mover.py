import shutil
import os


#Funtion below checks if there are Files previously in the mod folder of minecraft, if found files can be cleared, printed or just left as it is, as per the comfort of the user
def del_checker():
    mod_folder_lists = os.listdir(mod_folder_path)
    if mod_folder_lists != []:
        print("\nFiles were found inside the mods folder, Would you lke to empty it? [Y/N] [L(Print files)]")
        x = str.upper(input(">"))
        if x == "L":
            counter = 1
            for i in mod_folder_lists:
                print(f'[{counter}] ' + i)
                counter += 1
            del_checker()
        else:
            if x == "Y":
                for i in mod_folder_lists:
                    os.remove(os.path.join(mod_folder_path, i))
                print("The mods folder was emptied")
            elif x == "N":
                print("\nFolder was not cleared, proceeding with runtime!\n")
            else:
                pass


def maincopy(modlist):
    for i in modlist:
        shutil.copy(os.path.join(modlistpath, i), mod_folder_path)
    print("Runtime completed and the files are in place!")       #This print to the console confirms this block of code was executed succesfully
    return


#Could not for the life of me figure out how to make a switch statement in Python so I made a manual switch with if and else.
def switch(mcversion):      #TO ADD A NEW VERSION OR FEATURE ADD A NUMBER TO THE LIST FOR THE USER TO SELECT(SEE THE RANGE FUNCTION BELOW FIRST) AND WRITE THE CODE FOR IT.
    if mcversion == 1:
        modlistpath = os.path.join(rFolder, ".minecraft\\Mods_standby\\1.8 normally used mods")
        return modlistpath
    elif mcversion == 2:
        modlistpath = os.path.join(rFolder, ".minecraft\\Mods_standby\\1.12.2")
        return modlistpath
    elif mcversion == 3:
        modlistpath = os.path.join(rFolder, ".minecraft\\Mods_standby\\1.16.5\\fabric")
        return modlistpath
    elif mcversion == 4:
        modlistpath = os.path.join(rFolder, ".minecraft\\Mods_standby\\1.16.5 Forge")
        return modlistpath
    else:
        return None


print("Welcome to minecraft mod loader\n(Utility to copy mods from one folder to Another) \n\nEnter version you'd "
      "like to load from: \n(1) 1.8.9 \n(2) 1.12.2 \n(3) 1.16.5[Fabric] \n(4) 1.16.5[Forge] \n") #just a block to show the user a menu

rFolder = os.getenv('APPDATA')
mod_folder_path = os.path.join(rFolder,".minecraft\\mods\\")
modlistpath = ""
Mcversion = 0

while Mcversion not in range(1, 5):         #IMP: THIS RANGE FUNCTION DEFINES THE NUMBER OF "OPTIONS" IN THE MENU, TO ADD A NEW VERSION, FIRST INCREASE THE RANGE BY AND THEN SCROLL UP TO THE SWITCH FUNCTION.
    try:
        Mcversion = int((input("Enter an option from above: ")))
    except ValueError:
        print("You didn't enter a number, idiot!")
    else:
        pass

modlistpath = switch(Mcversion)
modlist = os.listdir(modlistpath)
del_checker()
maincopy(modlist)
exit(input("\nPRESS ENTER TO CLOSE!"))
