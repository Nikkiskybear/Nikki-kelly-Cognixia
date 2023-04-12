def userinput(string):
    uinput = -2
    while not(0 < uinput and uinput < 100):
        uinput = input(string)
        try:
            uinput = int(uinput)
            
        except:
            print("Not a int")
            uinput = -2

    return uinput

class emplyee():
    name = ""
    age = 0
    codingYears = 0
    firstLanguages = []
    FavoriteLanguages = []
    def __init__(self, userdict, FavoriteLanguages, firstLanguages):
        self.name = userdict["name"]
        self.age = userdict["age"]
        self.codingYears = userdict["years coding"]

        self.firstLanguages = firstLanguages

        self.FavoriteLanguages = FavoriteLanguages

    def __str__(self):
        x = self.name + " " + str(self.age) + " " + str(self.codingYears) + " First Languages are: "
        for i in self.firstLanguages:
            x += i + " "
        x += "Favorite Languages: "
        for i in self.FavoriteLanguages:
            x += i + " "
        x += "\n"
        return x
        
        




name = input("please enter your name: ")

age = userinput("please enter your age: ")
codingYears = userinput("please enter the amount of years you have coded for: ")

userdict = {"name" : name,
           "age" : age, 
           "years coding" : codingYears}

print("please enter for first three programing languages")

userinput1 = input("language one: ")
userinput2 = input("language two: ")
userinput3 = input("language three: ")

firstLanguages = (userinput1, userinput2, userinput3)

favoriteLanguages = []
for i in range(3):
    userinput = input("please enter your " + str(i+1) + " " + "favorite programming language: " )
    favoriteLanguages.append(userinput)

setintersection = set(firstLanguages) & set(favoriteLanguages)

collectiondict = {"userdict" : userdict,
                  "firstLanguages" : firstLanguages,
                  "favoriteLanguages" : favoriteLanguages, 
                  "setintersection" : setintersection }
try:
    files = open("employees.txt", "a")
except:
    files = open("employees.txt", "w")
    files.close()
    files = open("employees.txt", "a")

def makeSTR(n):
    n = n + " This is one of the employes first Languages"
    return str(n)

def realLang(n):
    if n == "python" or n == "java" or n == "c":
        return True
    return False



frank = emplyee(collectiondict["userdict"], collectiondict["favoriteLanguages"], collectiondict["firstLanguages"])

print(frank)
files.write(str(collectiondict["userdict"].items()) + "\n")

files.write(str(collectiondict["firstLanguages"])  + "\n")

files.write(str(collectiondict["favoriteLanguages"])  + "\n")

files.write(str(collectiondict["setintersection"])  + "\n")
files.close()