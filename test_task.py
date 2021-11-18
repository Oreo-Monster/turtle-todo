from task import Task
from datetime import datetime


def test_task():
	# test the accessor and mutator methods of the Task class
    #task, tag, priority, color, creationTime, completed=False
    task1 = Task("task1", ["tag1"], "high", "#0000FF", "2019-01-01", False)
    assert task1.getTask() == "task1"
    assert task1.getTags() == ["tag1"]
    assert task1.getPriority() == "high"
    assert task1.getColor() == "#0000FF"
    assert task1.getCreationTime() == "2019-01-01"
    assert task1.getCompleted() == False
    task1.setTask("task2")
    task1.addTag("tag2")
    task1.setPriority("low")
    task1.setColor("#00FF00")
    task1.setCreationTime("2019-02-02")
    task1.setCompleted(True)
    assert task1.getTask() == "task2"
    assert task1.getTags() == ["tag1", "tag2"]
    assert task1.getPriority() == "low"
    assert task1.getColor() == "#00FF00"
    assert task1.getCreationTime() == "2019-02-02"
    assert task1.getCompleted() == True

def test_determineColor():
    task1 = Task("task1", ["tag1"], "high", "", "2019-01-01", False)
    assert task1.color == '#AE3828'
    task2 = Task("task2", ["tag2"], "low", "", "2019-01-01", False)
    assert task2.color == '#E8CD44'
    task3 = Task("task3", ["tag3"], "medium", "", "2019-01-01", False)
    assert task3.color == '#D78E02'

def test_2HTML():
    time = creationTime=datetime.now()
    task1 = Task("task1", "tag1", "high", "#0000FF", time, False)
    assert task1.toHTML() == ["task1", "tag1", "high", "#0000FF", time.strftime("%a %m/%d/%y %I:%M %p"), "unchecked"]

def test_toString():
    time = creationTime=datetime.now()
    task1 = Task("task1", "tag1", "high", "#0000FF", time, False)
    assert task1.__str__() == f'Task: task1\nTag: tag1\nPriority: high\nColor: #0000FF\nCreation Time: {time.strftime("%a %m/%d/%y %I:%M %p")}\nCompleted: False\n'
