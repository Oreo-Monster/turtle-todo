import todolist as l
import task as ta
from datetime import datetime
import random

def test_add_remove():
    tester = ta.Task("find salvation", "despair",0,"#001320","dawn of time", False)
    tl = l.todolist()
    tl.add(tester)
    tl.check(0)
    assert tester.getCompleted()
    tl.remove(0)
    assert tl.getSize() == 0

def test_toHTML():
    time = datetime.now()
    test_task = ta.Task("task1", "tag1", "high", "#0000FF", time, False)
    test_task2 = ta.Task("task2", "tag2", "low", "#00FF00", time, True)
    test_list = l.todolist()
    test_list.add(test_task)
    test_list.add(test_task2)
    assert test_list.toHTML() == [["task1", "tag1", "high", "#0000FF", time.strftime("%a %m/%d/%y %I:%M %p"), 'unchecked',0],["task2", "tag2", "low", "#00FF00", time.strftime("%a %m/%d/%y %I:%M %p"), 'checked',1]]

def test_toString():
    time = datetime.now()
    test_task = ta.Task("task1", "tag1", "high", "#0000FF", time, False)
    test_task2 = ta.Task("task2", "tag2", "low", "#00FF00", time, False)
    test_list = l.todolist()
    test_list.add(test_task)
    test_list.add(test_task2)
    assert test_list.__str__() == f"0\n----------------\n{test_task}\n1\n----------------\n{str(test_task2)}\n"


def test_addTask():
    test_list = l.todolist()
    random.seed(0)
    test_list.addTask('sample task input #with tag', "none")
    test0 = test_list.todolist[0]
    assert test0.getTask() == 'sample task input <div class=tag style="border-color:#67B296">with</div> tag'

    test_list.addTask('reusing old tag, should have same color #with', "none")
    test1 = test_list.todolist[1]
    assert test1.getTask() == 'reusing old tag, should have same color <div class=tag style="border-color:#67B296">with</div>'

    test_list.addTask('no tags', "none")
    test2 = test_list.todolist[2]
    assert test2.getTask() == 'no tags'
    
    