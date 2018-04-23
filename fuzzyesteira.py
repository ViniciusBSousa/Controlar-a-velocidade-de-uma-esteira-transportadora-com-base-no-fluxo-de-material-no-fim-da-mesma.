# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:25:51 2017

@authores: Vinícius de Barros Sousa
"""


#Definição das funções de pertinência

def Acumulado(acc):
    vazio=pouco=medio=quaseCheio=cheio=0;
    if (acc < 0):
        vazio = 1;
    elif (acc >= 2):
        vazio = 0;
    elif (acc < 2):
        vazio = 1-(acc/2);
        
    if ((acc < 1) or (acc > 3)):
        pouco = 0; 
    elif (acc <= 2):
        pouco = acc-1;
    elif (acc > 2):
        pouco = 3-acc;
        
    if ((acc < 2) or (acc > 4)):
        medio = 0;
    elif (acc < 3):
        medio = acc-2;
    elif (acc >= 3):
        medio = 4-acc;
        
    if ((acc < 3) or (acc > 5)):
        quaseCheio = 0;
    elif (acc <= 4):
        quaseCheio = acc-3;
    elif (acc > 4):
        quaseCheio = 5-acc;
        
    if acc < 4:
        cheio = 0;
    elif acc > 5:
        cheio = 1;
    elif acc >= 4:
        cheio = acc-4;
        
        
   # print(vazio, pouco, medio, quaseCheio, cheio)
    return vazio, pouco, medio, quaseCheio, cheio

def diffAcumulado(dacc):
    neg=pneg=nulo=ppos=pos=0;
    if dacc < -2:
        neg = 1;
    elif dacc > -1:
        neg = 0;
    elif dacc >= -2:
        neg = -dacc - 1;
        
    if dacc < -2 or dacc > 0:
        pneg = 0;
    elif dacc < -1:
        pneg = dacc + 2;
    elif dacc > -1:
        pneg = -dacc;
        
    if dacc < -1 or dacc > 1:
        nulo = 0;
    elif dacc < 0:
        nulo = dacc + 1;
    elif dacc > 0:
        nulo = 1 - dacc;
        
    if dacc < 0 or dacc > 2:
        ppos = 0;
    elif dacc < 1:
        ppos = dacc;
    elif dacc > 1:
        ppos = 2 - dacc;
        
    if dacc < 1:
        pos = 0;
    elif dacc > 2:
        pos = 1;
    elif dacc >1:
        pos = dacc - 1;
        
   # print(neg, pneg, nulo, ppos, pos)
    return neg, pneg, nulo, ppos, pos


def area(h,w):
    Area = w*(h-((h**2)/2));
    return Area

def regraAND(a,b):
    
    if a<b:
        if (a or b)==0:
            a = 0.0001;
        return a
    elif b<a:
        if (a or b)==0:
            b = 0.0001;
        return b
    elif a == b:
        if (a or b)==0:
            a = 0.0001;
        return a;

def regrasNebulosas(e1,e2):
    vazio, pouco, medio, quaseCheio, Cheio = Acumulado(e1);
    neg, pneg, nulo, ppos, pos = diffAcumulado(e2);
    
    
    #regras nebulosas
    regra1 = regraAND(vazio,neg);
    regra2 = regraAND(vazio,pneg);
    regra3 = regraAND(vazio,nulo);
    regra4 = regraAND(vazio,ppos);
    regra5 = regraAND(vazio,pos);
    
    regra6 = regraAND(pouco,neg);
    regra7 = regraAND(pouco,pneg);
    regra8 = regraAND(pouco,nulo);
    regra9 = regraAND(pouco,ppos);
    regra10 = regraAND(pouco,pos);
    
    regra11 = regraAND(medio,neg);
    regra12 = regraAND(medio,pneg);
    regra13 = regraAND(medio,nulo);
    regra14 = regraAND(medio,ppos);
    regra15 = regraAND(medio,pos);
    
    regra16 = regraAND(quaseCheio,neg);
    regra17 = regraAND(quaseCheio,pneg);
    regra18 = regraAND(quaseCheio,nulo);
    regra19 = regraAND(quaseCheio,ppos);
    regra20 = regraAND(quaseCheio,pos);
    
    regra21 = regraAND(Cheio,neg);
    regra22 = regraAND(Cheio,pneg);
    regra23 = regraAND(Cheio,nulo);
    regra24 = regraAND(Cheio,ppos);
    regra25 = regraAND(Cheio,pos);
    
    area1 = area(regra1, 4);
    area2 = area(regra2, 4);
    area3 = area(regra3, 4);
    area4 = area(regra4, 4);
    area5 = area(regra5, 4);
    
    area6 = area(regra6, 4);
    area7 = area(regra7, 4);
    area8 = area(regra8, 4);
    area9 = area(regra9, 4);
    area10 = area(regra10, 4);
    
    area11 = area(regra11, 4);
    area12 = area(regra12, 4);
    area13 = area(regra13, 4);
    area14 = area(regra14, 4);
    area15 = area(regra15, 2);
    
    area16 = area(regra16, 4);
    area17 = area(regra17, 4);
    area18 = area(regra18, 4);
    area19 = area(regra19, 4);
    area20 = area(regra20, 2);
    
    area21 = area(regra21, 2);
    area22 = area(regra22, 2);
    area23 = area(regra23, 2);
    area24 = area(regra24, 2);
    area25 = area(regra25, 2);
    
    barea1 = 8*area(regra1, 4);
    barea2 = 8*area(regra2, 4);
    barea3 = 8*area(regra3, 4);
    barea4 = 8*area(regra4, 4);
    barea5 = 8*area(regra5, 4);
    
    barea6 = 8*area(regra6, 4);
    barea7 = 6*area(regra7, 4);
    barea8 = 4*area(regra8, 4);
    barea9 = 2*area(regra9, 4);
    barea10 = 2*area(regra10, 4);
    
    barea11 = 6*area(regra11, 4);
    barea12 = 4*area(regra12, 4);
    barea13 = 2*area(regra13, 4);
    barea14 = 2*area(regra14, 4);
    barea15 = 1*area(regra15, 2);
    
    barea16 = 4*area(regra16, 4);
    barea17 = 2*area(regra17, 4);
    barea18 = 2*area(regra18, 4);
    barea19 = 2*area(regra19, 4);
    barea20 = 1*area(regra20, 2);
    
    barea21 = 1*area(regra21, 2);
    barea22 = 1*area(regra22, 2);
    barea23 = 1*area(regra23, 2);
    barea24 = 1*area(regra24, 2);
    barea25 = 1*area(regra25, 2);
    
    uCrisp = (barea1+barea2+barea3+barea4+barea5+barea6+barea7+barea8+barea9+barea10+barea11+barea12+barea13+barea14+barea15+barea16+barea17+barea18+barea19+barea20+barea21+barea22+barea23+barea24+barea25)/(area1+area2+area3+area4+area5+area6+area7+area8+area9+area10+area11+area12+area13+area14+area15+area16+area17+area18+area19+area20+area21+area22+area23+area24+area25);
    
    print ("O valor de saída uCrisp é:", uCrisp)
inf = 1;    
while(inf==1):
    Entrada1=float(input("Digite o valor do total acumulado\n"));
    Entrada2=float(input("Digite o valor da derivada de acumulado\n"));
    regrasNebulosas(Entrada1,Entrada2);
    inf = int(input("Deseja continuar?: Se sim tecle 1 se não tecle 0\n"))
    if inf == 0:
        print("Obrigado")

     