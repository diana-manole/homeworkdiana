'''1 сделать график - вводим в поле строку выражения с переменной подумайте 
как ee правильно там передавать точнее когда считаем значения вместо переменной ставить текущее значение икс
sin(@x) [1,2,3,4,5,6,7] [sin(1),sin(2),sin(3),...]           str.replace('@x', )'''


import plotly.express as px
from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go
import flet as ft
import pandas
import solver
from flet import Page, Text , TextField

def main(page: Page):
    def submit1(e):
        function = int(functionText.value)
        startscaleText.focus()
        
    def submit2(e):
        startscale = int(startscaleText.value)
        endscaleText.focus()
        
    
     
    functionLabel = Text("Function: ", color=ft.colors.PINK, size=20)
    functionText  = TextField(value="", color=ft.colors.PURPLE, text_size=20,on_submit=submit1)
    functionRow =ft.Row([functionLabel,functionText],alignment='center')
    
     
    startscaleLabel = Text("Start scale: ", color=ft.colors.PINK, size=20)
    startscaleText  = TextField(value="", color=ft.colors.PURPLE, text_size=20,on_submit=submit2)
    startscaleRow = ft.Row([startscaleLabel ,startscaleText],alignment='center')
    
    
    endscaleLabel = Text("End scale: ", color=ft.colors.PINK, size=20)
    endscaleText  = TextField(value="", color=ft.colors.PURPLE, text_size=20)
    endscaleRow = ft.Row([endscaleLabel ,endscaleText],alignment='center')
    
    
    #xdata =list(range(startscaleRow,endscaleRow))
    xdata=list(range(-100,100))
    #xlabels = list(map(lambda t: str(t), xdata))
    ydata = list(map(lambda t: solver.solve(f"sin({t})+{t}*cos(({t})*2)") , xdata))
    #ydata = list(map(lambda t: solver.solve() , xdata))
    df = pandas.DataFrame(dict(
        x = xdata,
        y = ydata
    ))
    fig = px.line(df, x="x", y="y", title="Squares")
    
    
    page.add(functionRow, startscaleRow,endscaleRow ,Text('Test'),PlotlyChart(fig,expand=False))
    

ft.app(target=main)
