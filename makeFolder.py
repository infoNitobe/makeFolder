import csv
import os
import shutil

BASE_PATH = os.getcwd() + "/makeFolder"
# OUTPUT_PATH = "./makeFolder/Output"
OUTPUT_PATH = os.getcwd() + "/makeFolder/Output"

def main():
    #delete a output folder
    deleteOutputFolder()

    #first, make a output folder
    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)

    with open(BASE_PATH + "/" + 'input.csv', newline='') as inF1:
        reader1 = list(csv.reader(inF1))
        colNow = 0
        nowPath = OUTPUT_PATH
        nextPath = ""
        for colmns in reader1:
            #quit a script, when multiple inputs.
            isOneInput(colmns)
            for iCol, cell in enumerate(colmns):
                #pass blank cells
                if cell == "":
                    pass
                else:
                    dif = iCol - colNow
                    if dif == 0:
                        nextPath = nowPath + "/" + cell
                        os.mkdir(nextPath)
                        # colNow = iCol - 1
                    elif dif == 1:
                        os.chdir(nextPath)
                        nowPath = nextPath
                        nextPath = nowPath + "/" + cell
                        os.mkdir(nextPath)
                        colNow = iCol
                    elif dif >= 2:
                        print("The contents of csv are not in the correct tree structure.")
                        print("quit this script")
                        quit()
                    elif dif < 0:
                        temp = -dif
                        os.chdir("../"*temp)
                        nowPath = os.getcwd() + "/" + cell
                        nextPath = nowPath
                        os.mkdir(nextPath)
                        colNow = iCol

#clar dirs
def deleteOutputFolder():
    if os.path.exists(OUTPUT_PATH):
        print("there is output folder.")
        print("input 1 = delete a folder, input 2 = quit this script")

        temp = int(input())
        if temp == 1:
            shutil.rmtree(OUTPUT_PATH)
        elif temp == 2:
            print("quit this script.")
            quit()

#check there are no inputs in multiple columns.
def isOneInput(oneRow):
    inputCnt = len(oneRow) - oneRow.count("")
    if inputCnt > 1:
        print("Error: multiple inputs in a line.")
        print("quit this script.")
        quit()

if __name__ == "__main__":
    main()