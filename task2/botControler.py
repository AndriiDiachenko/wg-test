import time as t
from module01 import *
import random

global uid
uid = random.randint(1000, 9999)  # complex hash function

class BotController():
    tsks = []
    working_time = 0
    start_time = int(t.time())

    def addTask(self, task):
        self.tsks.append(task)

    def getAllTasks(self):
        res = None
        if len(self.tsks) > 0:
            res = self.tsks
        return res

    def printExecutionStack(self):
        i = 0
        for task in self.tsks:
            LOG_INFO('BotController', 'Task #' + str(i) + ' task name: ' + str(task.info))
            i = i + 1

    def run(self):
        LOG_DEBUG('BotController', 'Start runs %d tasks' % len(self.tsks))
        for task in self.tsks:
            print('RUN TASK #' + str(task.uid))
            task.__process__()
        LOG_INFO('BotController', 'All tasks finished...')

    def getTaskUid(self):
        global uid
        uid = uid + 1
        return uid