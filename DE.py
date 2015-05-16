#coding:UTF-8
'''
Created on 2015年5月12日

@author: zhaozhiyong
'''

from __future__ import division
from numpy import *
import random as rd

NP = 1000
size = 10
xMin = -10
xMax = 10
F = 0.5
CR = 0.8

#计算适应值函数
def calFitness(X):
    n = len(X)
    fitness = 0
    for i in xrange(n):
        fitness += X[i] * X[i]
    return fitness

def mutation(XTemp, F):
    m, n = shape(XTemp)
    XMutationTmp = zeros((m, n))
    for i in xrange(m):
        r1 = 0
        r2 = 0
        r3 = 0
        while r1 == i or r2 == i or r3 == i or r1 == r2 or r1 == r3 or r2 == r3:
            r1 = rd.randint(0, m - 1)
            r2 = rd.randint(0, m - 1)
            r3 = rd.randint(0, m - 1)
        
        for j in xrange(n):
            XMutationTmp[i, j] = XTemp[r1, j] + F * (XTemp[r2, j] - XTemp[r3, j])
        
    return XMutationTmp


def crossover(XTemp, XMutationTmp, CR):
    m, n = shape(XTemp)
    XCorssOverTmp = zeros((m,n))
    for i in xrange(m):
        for j in xrange(n):
            r = rd.random()
            if (r <= CR):
                XCorssOverTmp[i,j] = XMutationTmp[i,j]
            else:
                XCorssOverTmp[i,j] = XTemp[i,j]
    return XCorssOverTmp

def selection(XTemp, XCorssOverTmp, fitnessVal):
    m,n = shape(XTemp)
    fitnessCrossOverVal = zeros((m,1))
    for i in xrange(m):
        fitnessCrossOverVal[i,0] = calFitness(XCorssOverTmp[i])
        if (fitnessCrossOverVal[i,0] < fitnessVal[i,0]):
            for j in xrange(n):
                XTemp[i,j] = XCorssOverTmp[i,j]
            fitnessVal[i,0] = fitnessCrossOverVal[i,0]
    return XTemp, fitnessVal

def saveBest(fitnessVal):
    m = shape(fitnessVal)[0]
    tmp = 0
    for i in xrange(1,m):
        if (fitnessVal[tmp] > fitnessVal[i]):
            tmp = i
    
    print fitnessVal[tmp][0]

#初始化
XTemp = zeros((NP, size))
for i in xrange(NP):
    for j in xrange(size):
        XTemp[i, j] = xMin + rd.random()*(xMax - xMin)

#计算适应值
fitnessVal = zeros((NP, 1))
for i in xrange(NP):
    fitnessVal[i, 0] = calFitness(XTemp[i])
    
gen = 0
while gen <= 1000:
    print gen
    XMutationTmp = mutation(XTemp, F)
    XCorssOverTmp = crossover(XTemp, XMutationTmp, CR)
    XTemp, fitnessVal = selection(XTemp, XCorssOverTmp, fitnessVal)
    saveBest(fitnessVal)
    gen += 1
      
