import pandas
from bokeh.plotting import figure, output_file, show
df=pandas.read_excel("http://pythonhow.com/verlegenhuken.xlsx",sheetname=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
p=figure(plot_width=500,plot_height=400,tools='pan,resize',logo=None)
p.title="Temperature and Air Pressure"
p.title_text_color="Gray"
p.title_text_font="arial"
p.title_text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"
p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(p)