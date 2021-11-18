import task as t
import re
from flask import escape
import random
from datetime import datetime

class todolist:
    def __init__(self):
        self.todolist = []
        self.tags = {}

    def add(self,task):
        #pass a task object in to add to  user's todolist
        self.todolist.append(task)
    
    def addTask(self, taskText, taskPriority):
        #Sanitize the input
        cleanText = escape(taskText)
        tags = re.findall('#[a-zA-Z0-9]+', cleanText)
        for tag in tags:
            tag = tag[1:]
            if tag not in self.tags:
                randColor = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
                self.tags[tag] = randColor
            tagHTML = f'<div class=tag style="border-color:{self.tags[tag]}">{tag}</div>'
            cleanText = re.sub('#'+tag,tagHTML, cleanText)
        task = t.Task(cleanText, tags, taskPriority, color="", creationTime=datetime.now())
        self.add(task)

        

            
            
            
         
    def remove(self,index):
        self.todolist.pop(index)

    def check(self,index):
        self.todolist[index].check()

    def getSize(self):
        return len(self.todolist)

    def toHTML(self):
        todos=[]
        idx = 0
        for todo in self.todolist:
            todos.append(todo.toHTML())
            todos[idx].append(idx)
            idx += 1
        return todos
        
    #Write a to string function that returns a string of the todolist
    def __str__(self):
        todolist_str = ""
        for i in range(len(self.todolist)):
            todolist_str += str(i) + "\n----------------\n" + str(self.todolist[i]) + "\n"
        return todolist_str
    
