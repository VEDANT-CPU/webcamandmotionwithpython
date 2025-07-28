#Importing from another file from same directory.
from motiondetect import df
from bokeh.plotting import figure, output_file, show

#When loop in line 68 in motiondetect ends df is created and then plotting.py starts.
#No need to execute motiondetect.py now just execute this file.
p=figure(x_axis_type="datetime", width=500, height=400)
p.title.text="Motion Graph"
p.sizing_mode="scale_width"
p.yaxis.minor_tick_line_color=None
#To remove the horizontal grid lines from the graph, This is a trick.
p.ygrid.ticker=[0,1] #Pass a list of desired tickers

q=p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="red")

output_file("TimePlot2.html")
show(p)