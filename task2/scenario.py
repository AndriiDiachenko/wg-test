import botControler
import os
from time import sleep
import re
import module01 as log
from tasks import *


class DATA:
    def getData(self):
        data = {
            'movemtPoints': ['11.11 12.3 123.4',
                             '13.14 12.3 127.4',
                             '13.14 12.3 127.4',
                             '17.14 12.1 127.4',
                             '13.14 12.3 127.4',
                             ],
            'login': 'bot1@qa.qa|q1w2e3r4t5',
            'pntsShoot': {
                't-26': ['17.14 12.1 127.4', 2, 'HE'],
                'pz4': ('45.02 778.4 127.4', 3, 'AP'),
                'IS2': ['60.02 5.4 127.4', 5, 'APCR'],
            },
            'tanks': ('t-44'),
            'reloadTime': 1.5
        }
        return data

class Bot(object):
    name = None
    p = {}
    gun_point = p
    tank = None
    login = ''
    state = None

    def loginInHangar(self, login):
        self.state = 'loginin'
        name = login.split('|')[0]
        pswd = login.split('|')[1]
        log.LOG_INFO(name, 'Strart loginin Bot %s with login: %s, pswd: %s' % (name, login, pswd))
        sleep(1)
        self.name = name
        self.state = 'inHangar'
        log.LOG_INFO(name, 'Bot state: ' + self.state)

    def get_tank(self, tank):
        self.state = 'buying tank'
        log.LOG_INFO(self.name, 'Buying tank: ' + tank)
        sleep(2)
        self.tank = tank
        log.LOG_INFO(self.name, '... OK')
        self.state = 'inHangar'

    def goToBattle(self):
        self.state = 'load map'
        log.LOG_INFO(self.name, 'LOADING...')
        sleep(5)
        self.p['x'] = self.gun_point['x'] = 0.0
        self.p['y'] = self.gun_point['y'] = 0.0
        self.p['z'] = self.gun_point['z'] = 0.0
        log.LOG_DEBUG(self.name, '...OK')


scenarioData = DATA()
b = Bot()
LOG_INFO('', '~~START~~')
log.LONG_DEBUG(scenarioData.getData())
b.loginInHangar(scenarioData.getData()['login'])
b.get_tank(scenarioData.getData()['tanks'])
b.goToBattle()
controler = botControler.BotController()
teleport_point = tuple(scenarioData.getData()['movemtPoints'][0].split(' '))
first_mission_point = movementTask(controler.getTaskUid(), b, scenarioData.getData()['movemtPoints'][1:3], 'move to first battle point')
first_mission_point.teleport(*teleport_point)
firsTarget = shootTask(bot=b, uid=controler.getTaskUid(), ammo=scenarioData.getData()['pntsShoot']['t-26'][2],
                       target_position=scenarioData.getData()['pntsShoot']['t-26'][0], info='destroy t-26',
                       reload_time=scenarioData.getData()['reloadTime'], shotsToKill=scenarioData.getData()['pntsShoot']['t-26'][1])

second_mission_point = movementTask(controler.getTaskUid(), b, scenarioData.getData()['movemtPoints'][2:4])
secondTarget = shootTask(bot=b, uid=controler.getTaskUid(), ammo=scenarioData.getData()['pntsShoot']['pz4'][2],
                       target_position=scenarioData.getData()['pntsShoot']['pz4'][0],
                       reload_time=scenarioData.getData()['reloadTime'],
                       shotsToKill=scenarioData.getData()['pntsShoot']['pz4'][1])
last_mission_point = movementTask(controler.getTaskUid(), b, scenarioData.getData()['movemtPoints'][4:], 'move to last battle point')
lastTarget = shootTask(bot=b, uid=controler.getTaskUid(), ammo=scenarioData.getData()['pntsShoot']['IS2'][2],
                       target_position=scenarioData.getData()['pntsShoot']['IS2'][0], info='destroy IS2',
                       reload_time=scenarioData.getData()['reloadTime'], shotsToKill=scenarioData.getData()['pntsShoot']['IS2'][1])

SCENARIO = (
    first_mission_point, firsTarget,
    second_mission_point, secondTarget,
    last_mission_point, lastTarget)

for t in SCENARIO:
    controler.addTask(t)
controler.printExecutionStack()
controler.run()
LOG_INFO(b.name, '~~FINISH~~')