'''2 ввод данных в базу из формы
все в СВОЙ git'''
import mysql.connector
import sys
import flet as ft
from flet import Page, IconButton, Text, TextField
"""
class DataHelp:
    def __init__(self):
        self.findb = mysql.connector.connect(
            host='localhost',
            user='python',
            password='!QA2ws3ed=-2'
        )
        #self.cursor = self.findb.cursor()

    def checkNoExist(self, year, month, business):
        self.cursor = self.findb.cursor()
        query = 'select * from Predicator.train where year =' + \
            str(year) + ' and month = ' + str(month) + \
            ' and business = ' + str(business)
        self.cursor.execute(query)
        print(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return len(result) == 0
    def replaceData(self, year, month, business, income):
        query = f'update Predicator.train set income={income} where year={year} and month={month} and business={business}'
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()
        """

def main(page:Page):

    def submit1(e):
        try:
            year = int(yearText.value)
            monthText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            yearText.focus()
            page.update()

        
    def submit2(e):
        try:
            month = int(monthText.value)
            businessText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            monthText.focus()
            page.update()
            
    def submit3(e):
        try:
            bussines = int(businessText.value)
            incomeText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            businessText.focus()
            page.update()
            
    def close_dlg(e):
        dlg.open=False
        page.update()    

    dlg = ft.AlertDialog(modal=True,
                         title=ft.Text("Data error"),
                         content=ft.Text("Please check if data is integer"),
                         actions=[ft.TextButton("Ok", on_click=close_dlg)])
    
    yearLabel = Text("Year: ", color=ft.colors.RED, size=40)
    yearText  = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submit1)
    yearRow = ft.Row([yearLabel,yearText],alignment='center')

    monthLabel = Text("Month: ", color=ft.colors.RED, size=40)
    monthText = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submit2)
    monthRow = ft.Row([monthLabel, monthText], alignment='center')

    businessLabel = Text("Business: ", color=ft.colors.RED, size=40)
    businessText = TextField(value="", color=ft.colors.BLUE, text_size=40,on_submit=submit3)
    businessRow = ft.Row([businessLabel, businessText], alignment='center')

    incomeLabel = Text("Income: ", color=ft.colors.RED, size=40)
    incomeText = TextField(value="", color=ft.colors.BLUE, text_size=40)
    incomeRow = ft.Row([incomeLabel, incomeText], alignment='center')
    
    page.add(ft.Column([yearRow,monthRow, businessRow, incomeRow]))
    
    


#ft.app(target=main)
