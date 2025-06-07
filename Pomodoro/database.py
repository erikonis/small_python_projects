import json

class Database():
    def __init__(self, directory='data/data.json'):
        self.directory = directory
        with open(self.directory, 'r') as file:
           try:
                self.data = json.load(file)
           except:
               self.data = {'pomos':0}



    def read(self, param):
        try:
            return self.data[param]
        except:
            self.data[param] = 0
        finally:
            return self.data[param]

    def write(self, param, value):
        self.data[param] = value
        string = json.dumps(self.data)
        with open(self.directory, 'w') as f:
            f.write(string)