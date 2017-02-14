#! /usr/bin/python
# -*- coding: utf8 -*-
import redis
import time
import urllib
import re

Env_Mod = {'Stable_User': redis.ConnectionPool(host='', port=6379)};


#########################################################
def stringGet(key,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    if Redis.get(key):
        return Redis.get(key)
    else:
        return 'NULL'

##################
def stringDel(key,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    if Redis.delete(key):
        return 'OK!'
    else:
        return 'FAIL!'


##################
def stringSet(key,value,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    print Redis.set(key, value)


##################
def hashGet(hname,hkey,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    if Redis.hget(hname,hkey):
        return Redis.hget(hname,hkey)
    else:
        return 'NULL'


##################
def hashDel(hname,hkey,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    if Redis.hdel(hname, hkey):
        return 'OK!'
    else:
        return 'FAIL!'


##################
def executeCommand(cmd,pool):
    Redis = redis.Redis(connection_pool=Env_Mod[pool])
    Command = cmd.rstrip()
    Command = Command.split(' ')
    # print Command
    try:
        Command = Redis.execute_command(*Command)
        if Command:
            return Command
        else:
            return 'null'
    except:
        return 'error'

##########################################

