class Project:
    num:int
    title:str
    desc:str
    progress:int
    status:int

    def __init__(self, num:int=None, title:str=None, desc:str=None, progress:int=None, status:int=None, icon=None):
        self.num = num
        self.title = title
        self.desc = desc
        self.progress = progress
        self.status = status
        self.icon = icon

class Task:
    num:int
    project_num:int
    title:str
    content:str
    status:int

    def __init__(self, num:int=None, project_num:int=None, title:str=None, content:str=None, status:int=None):
        self.num = num
        self.project_num = project_num
        self.title = title
        self.content = content
        self.status = status

class Doc:
    num:int
    project_num:int
    title:str
    content:str

    def __init__(self, num:int=None, project_num:int=None, title:str=None, content:str=None):
        self.num = num
        self.project_num = project_num
        self.title = title
        self.content = content
