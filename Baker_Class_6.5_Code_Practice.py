import PySimpleGUI as sg


graph_size = (600,600)
start = (200,200)
#background = "rgb(66,218,245)"

layout = [[sg.Graph(canvas_size = graph_size, graph_bottom_left = (0,0),
                   graph_top_right = graph_size, enable_events = True,
                   background_color = "#15cfe8", key = "-graph-", pad = 0)]]


window = sg.Window("House", layout, finalize = True, margins = (0,0))
graph = window["-graph-"]


def main():
    house = graph.draw_rectangle((250,150), (350,300), fill_color="#827d7e")
    door = graph.draw_rectangle((290,150), (310,200), fill_color="#ed0731")
    ground = graph.draw_rectangle((0,0), (600,150), line_color="green", fill_color="green")
    roof = graph.draw_polygon([(240,300), (360,300), (300,350)], fill_color="#91031d")
    sun = graph.draw_circle((50,500), 25, fill_color = "yellow")
    window.read(5000)
    

main()
window.close()