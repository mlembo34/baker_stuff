import PySimpleGUI as sg

storyboard_size = (533,900)

layout = [[sg.Graph(canvas_size = storyboard_size, graph_bottom_left = (0,0), 
                    graph_top_right = storyboard_size, enable_events = True, 
                    background_color = "black", key = "-graph-", pad = 0)],
                    [sg.Button("Undecided", button_color=("gray","black"), size=(9,1)),
                    sg.Button("Happy", button_color=("yellow","black"), size=(5,1)),
                    sg.Button("Sad", button_color=("red", "black"), size=(3,1))]]


window = sg.Window("Comic", layout, finalize = True, margins = (0,0))
graph = window["-graph-"]
x = ""

def main():
    global x
    borders()
    cell1()
    """ if ans == "happy":
        cell_happy()
    else:
        cell_sad() """
    
    
def borders():
    border_hor = graph.draw_line((0,450), (1600,450), color="white", width=3)
    border_vert1 = graph.draw_line((533,0), (533,900), color="white", width=3)
    border_vert2 = graph.draw_line((1066,0), (1066,900), color="white", width=3)
    
    
def cell1():
    background = graph.draw_rectangle((0,452), (531,900), fill_color="lightgray")
    ground = graph.draw_rectangle((0,452), (531,560), fill_color="#649169")
    house = graph.draw_rectangle((120,560), (300,760), fill_color="#162d61")
    roof = graph.draw_polygon([(110,760), (310,760), (210,820)], fill_color="#592d18")
    door = graph.draw_rectangle((190,560), (240,630), fill_color="gray")
    dude_body = graph.draw_rectangle((330,560), (350,600), fill_color="beige")
    dude_head = graph.draw_circle((340,610), 10, fill_color="gold")
    words = graph.draw_text("Dude left his house. Is he happy or sad?", (225,860), color="black",
                            font=15, text_location="center")
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Happy":
            new_background = graph.draw_rectangle((0,0), (531,450), fill_color="#15cfe8")
            ground = graph.draw_rectangle((0,0), (531,108), fill_color="green")
            house = graph.draw_rectangle((120,108), (300,308), fill_color="#11bf23")
            roof = graph.draw_polygon([(110,308), (310,308), (210,368)], fill_color="#91031d")
            door = graph.draw_rectangle((190,108), (240,178), fill_color="#ed0731")
            sun = graph.draw_circle((75,350), 25, fill_color="gold")
            dude_body = graph.draw_rectangle((330,108), (350,148), fill_color="purple")
            dude_head = graph.draw_circle((340,158), 10, fill_color="gold")
            words = graph.draw_text("HAPPY!", (225,400), color="yellow", 
                                    font=20, text_location="center")
        if event == "Sad":
            death = graph.draw_rectangle((0,0), (531,450), fill_color="#850c3c")
            ground = graph.draw_rectangle((0,0), (531,108), fill_color="#2c2e33")
            house = graph.draw_rectangle((150,108), (330,308), fill_color="black")
            roof = graph.draw_polygon([(140,308), (340,308), (240,368)], fill_color="black")
            door = graph.draw_rectangle((220,108), (270,178), fill_color="darkgray")
            dude_body = graph.draw_rectangle((360,108), (420,128), fill_color="purple")
            dude_head = graph.draw_circle((430,118), 10, fill_color="gold")
            sun = graph.draw_circle((100,380), 50, fill_color="#d42629")
            words = graph.draw_text("SAD", (225,400), color="black", 
                                    font=20, text_location="center")
        if event == "Undecided":
            background = graph.draw_rectangle((0,0), (531,450), fill_color="beige") 
    
    
if __name__ == "__main__":
    main()


