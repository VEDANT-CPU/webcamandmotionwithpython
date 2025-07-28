#Importing from another file from same directory.
from motiondetect import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnarDataSource

cds=ColumnarDataSource(df) #Creating a ColumnDataSource object to pass data to plot.

#When loop in line 68 in motiondetect ends df is created and then plotting.py starts.
#No need to execute motiondetect.py now just execute this file.
p=figure(x_axis_type="datetime", width=500, height=400)
p.title.text="Motion Graph"
p.sizing_mode="scale_width"
p.yaxis.minor_tick_line_color=None
#To remove the horizontal grid lines from the graph, This is a trick.
p.ygrid.ticker=[0,1] #Pass a list of desired tickers

#Creating a Hover object, tooltips parameter expects a list of tuples
# @Start refers to the Start column of DataFrame table
#You don't need to add colon because bokeh adds them by default to field names
hover=HoverTool(tooltips=[("Start ","@Start"),("End ","@End")])
#Adding the hover object into the figure.
p.add_tools(hover)

#To pass the data to plot, pass the ColumnDataSource object in source parameter.
#If you have passed source parameter then just pass name of columns in left and right.
q=p.quad(left="Start", right="End", bottom=0, top=1, color="red", source=cds)

output_file("TimePlot2.html")
show(p)