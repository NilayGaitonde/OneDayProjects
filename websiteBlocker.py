from tkinter import *

host_path=r"C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"
websites=[]
with open(host_path,"r+") as file:
    content=file.readlines()
    file.seek(0)
    for line in content:
        websites.append(line[line.find(" "):line.find("\n")])
    websites=list(filter(None,websites))

class websiteBlocker:
    def __init__(self,root):
        global websites
        self.root=root
        root.title('Website Blocker')
        root.geometry("400x250")
        addWebsite=Frame(root)
        self.websiteEntry=Entry(addWebsite,width=40)
        self.websiteEntry.grid(row=0,column=1)
        site=StringVar()
        self.addWebsiteButton=Button(addWebsite,text='Add',command=self.addSite).grid(row=0,column=2)
        self.removeWebsiteButton=Button(addWebsite,text='Remove',command=self.delSite).grid(row=0,column=3)
        self.removeAllWebsiteButton=Button(addWebsite,text='Remove all',command=self.delAll).grid(row=0,column=4)
        addWebsite.grid(row=0)

        blockedSiteFrame=Frame(root)
        self.count=0
        self.blockedSiteList=Listbox(blockedSiteFrame,font='hlevetica 12 bold',width=40)
        for pos,site in enumerate(websites):
            self.blockedSiteList.insert(pos,site)
            self.count=pos
        self.blockedSiteList.pack()
        blockedSiteFrame.grid(row=1)
    
    def delAll(self):
        with open(host_path,'r+') as file:  
            content = file.readlines();  
            file.seek(0)  
            for line in content:  
                if not any(website in line for website in  websites):  
                    file.write(line)  
            file.truncate()
        self.blockedSiteList.delete(0,self.count)

    def reloadList(self):
        self.blockedSiteList.delete(0,self.count)
        for pos,site in enumerate(websites):
            self.blockedSiteList.insert(pos,site)
            self.count=pos

    def addSite(self):
        site=self.websiteEntry.get()
        websites.append(site)
        with open(host_path,"r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
                    file.write(redirect+" "+"https://"+website+"\n")
        print(websites)
        self.reloadList()

    def delSite(self):
        with open(host_path,"r+") as file:
            site=self.websiteEntry.get()
            content=file.readlines()
            file.seek(0)
            for line in content:
                if (site not in line):
                    file.write(line)
            file.truncate()
        websites.remove(self.websiteEntry.get())
        self.reloadList()
        
        


root=Tk()
website=websiteBlocker(root)
root.mainloop()
