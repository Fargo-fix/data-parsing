import time

from datetime import datetime
from database import DataBase
from parse import ParseSite

class Chief:

    def __init__(self):
    
        self.stop = False

    def launch(self):

        man = ParseSite()
        manager_db = DataBase()

        id = 0

        self.now = datetime.now()
        date_request = self.now.strftime('%d-%m-%Y')
        time_request = self.now.strftime('%H:%M:%S')
        
        while not self.stop:

            manager_db.count_id()
            id = len(manager_db.c_id) + 1
            
            man.run()

            rate = man.euro
            entities = (id, date_request, time_request, rate)
            manager_db.write_to_table(entities)

            self.stop = True
            time_work = time.time()
            print()
            print("--- Script running time: %s seconds ---\n" % (time.time() - time_work))

l = Chief()
l.launch()
