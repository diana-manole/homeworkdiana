import mysql.connector
import sys


class DataHelp:
    def __init__(self):
        self.findb = mysql.connector.connect(
            host="localhost", user="python", password="!QA2ws3ed=-2"
        )
        # self.cursor = self.findb.cursor()

    def checkNoExist(self, year, month, business):
        self.cursor = self.findb.cursor()
        query = (
            "select * from Predicator.train where year ="
            + str(year)
            + " and month = "
            + str(month)
            + " and business = "
            + str(business)
        )
        self.cursor.execute(query)
        print(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return len(result) == 0

    def replaceData(self, year, month, business, income):
        query = f"update Predicator.train set income={income} where year={year} and month={month} and business={business}"
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()

    def insertData(self, year, month, business, income):
        query = f"insert into Predicator.train (year, month, business, income) values ({year},{month},{business},{income}) "
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()

    def readAllData(self):
        query = f"select year, month, business, income from Predicator.train order by year, month "
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def executeSomeQuery(self, query):
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def readSomeData(self, key, value):
        query = f"select year, month, business, income from Predicator.train where {key} = {value} order by year, month  "
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result


# def insertData(year, month, business, income):
d = DataHelp()
print(d.readAllData())
print(d.readSomeData("business", 1))
# print(d.checkNoExist(2002,2,2))


def inputImp(question):
    p = input(question + "\t")
    if p == ".":
        print("Operation cancelled ")
        sys.exit()
    try:
        n = int(p)
    except:
        print("Please enter number, nothing more!")
        return inputImp(question)
    return n


print("Hello. This is income processing unit")
print("you will be asked for values to enter")
print("For exit just enter .")


dataHelp = DataHelp()
while True:
    year = inputImp("Enter year: ")
    month = inputImp("Enter month: ")
    business = inputImp("Enter business: ")
    income = inputImp("Enter income: ")
    # All data saved
    if not dataHelp.checkNoExist(year, month, business):
        print("We already have record for those business and data!")
        y = input("if you want to replace input y   ")
        if y != "y":
            print("Going to next input!")
            next
        else:
            dataHelp.replaceData(year, month, business, income)
            print("Record updated!")
    else:
        dataHelp.insertData(year, month, business, income)
        print("Record inserted!")
