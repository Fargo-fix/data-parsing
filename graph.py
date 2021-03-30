import matplotlib.pyplot as plt
import numpy as np


from database import DataBase


class Graph:

    def __init__(self):
        # self.x = np.linspace(0, 40, 31)
        # self.x = []
        # self.y = []
        self.date_list = []
        self.rate_list = []
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.man = plt.get_current_fig_manager()
        self.man.canvas.set_window_title("My GRAPH")

 
    def draw_graph(self):

        manager_db = DataBase()
        manager_db.get_rate()
        manager_db.get_date()
        
        self.rate_list = manager_db.all_rate_values

        plt.title("Курс евро 2021", fontsize=22)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Rate", fontsize=14, rotation=0)
        plt.grid(True)

        for i in range(len(manager_db.all_date_values)):
            date_ = list(manager_db.all_date_values[i])
            print(type(date_))
            date_ = ''.join(date_)
            
            

            date_ = list(date_)
            date_ = date_[0:5]
            date_ = ''.join(date_)
            date_int = int(''.join(c for c in date_ if c.isdigit()))
            self.date_list.append(date_int)    

        plt.plot(self.date_list, self.rate_list)
        plt.plot(self.date_list, self.rate_list, 'bo')
        # plt.xticks(range(len(self.date_list)), self.date_list)
        # plt.yticks(range(len(self.rate_list)), self.rate_list)

        # i = ()
        # v = ()

        # for i, v in enumerate(self.rate_list):
        #     self.ax.text(i, v+25, "%d" %v, ha="center")
        # plt.xlim(0, 3103)
        # plt.ylim(0, 40)
        
        plt.show()

launch = Graph()
launch.draw_graph()