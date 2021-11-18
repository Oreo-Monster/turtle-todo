import jinja2
import datetime
import re
class Task:
    def __init__(self, task, tags, priority, color, creationTime, completed=False):
        self.task = task
        self.tags = tags # list of tags
        self.creationTime = creationTime
        self.priority = priority
        if color == "":
            self.determineColor()
        else:
            self.color = color #Hexstring for RGB
        self.completed = completed

    def determineColor(self):
        priorityColors = {
            'low':'#E8CD44',
            'medium': '#D78E02',
            'high': '#AE3828'
        }
        if self.priority in priorityColors:
            self.color = priorityColors[self.priority]
        else:
            self.color = '#006494'
        return


    #Write accessor methods for all of the task's attributes.
    def getTask(self):
        return self.task
    
    def getTags(self):
        return self.tags

    def getCreationTime(self):
        return self.creationTime
    
    def getPriority(self):
        return self.priority
    
    def getColor(self):
        return self.color
    
    def getCompleted(self):
        return self.completed
    
    #Write mutator methods for all of the task's attributes.
    def setTask(self, task):
        self.task = task

    def addTag(self, tag):
        self.tags.append(tag)
    
    def setCreationTime(self, creationTime):
        self.creationTime = creationTime

    def setPriority(self, priority):
        self.priority = priority

    def setColor(self, color):
        self.color = color

    def setCompleted(self, completed):
        self.completed = completed

    def check(self):
        self.completed = not self.completed

    def __str__(self):
        str = ""
        str += f'Task: {self.task}\n'
        str += f'Tag: {self.tags}\n'
        str += f'Priority: {self.priority}\n'
        str += f'Color: {self.color}\n'
        str += f'Creation Time: {self.creationTime.strftime("%a %m/%d/%y %I:%M %p")}\n'
        str += f'Completed: {self.completed}\n'
        return str

    def toHTML(self):
        time = self.creationTime.strftime("%a %m/%d/%y %I:%M %p")
        check = "unchecked"
        if self.completed:
            check = "checked"
        return [self.task, self.tags, self.priority, self.color, time, check]
    

