'''class Computer:
    def config(self):
        print("i5,16GB,1TB")


com1= Computer()
com1.config()'''  #1st type
#Computer.config(com1) # 2nd type to run obj
#com2 = Computer()
#Computer.config(com2)




'''class Computer:
    def __init__(self,cpu,RAM): [Ye Auto call HAi.] 
        self.cpu = cpu
        self.RAM = RAM
        print("config is",self.cpu,self.RAM)


com1= Computer("RAzen3","16GB")'''



class Computer:
    def __init__(self,cpu,RAM):
        self.cpu = cpu
        self.RAM = RAM
        
    def config(self):
        print("config is",self.cpu,self.RAM)


com1= Computer("RAzen3","16GB")
com1.config()
com2 = Computer("intel","1TB")
com2.config()


