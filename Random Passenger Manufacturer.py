#本程序意在给EES随机的制造乘客流，方便程序测试。随机客流模型模板如下：
#中：
#    <Node Index="1">
#      <Time>105</Time>
#      <FlST>2</FlST>
#      <FlEd>7</FlEd>
#      <PeWe>81</PeWe>
#    </Node>
import os
import random
import tkinter as tk
from tkinter import filedialog


#基本信息获取
def getinfor():
    print('本程序可以模拟 -完全随机客流- 情况，请注意使用对应的程序创建你想创建的的客流！')
    print('程序内单位均为部、层、人、秒、千克，不存在其它的单位。')
    print('请根据提示输入数据并选择您希望释放文件的位置。\n\n')
    #电梯部数
    EN=input('您的程序有几部电梯？(默认6，限制1、2、3、6)')
    if EN.strip().isdigit() and (EN =='1' or EN =='2' or EN =='3' or EN =='6'):#是数字，且合乎规则
        EN=int(EN)
    else:
        EN=3
    print('您的选择：%d部电梯。\n'%EN)
    #电梯楼层数
    EF=input('您每部电梯的楼层数为多少？(默认10，限制6或10)')
    if EF.strip().isdigit() and (EF =='6' or EF =='10'):
        EF=int(EF)
    else:
        EF=10
    print('您的选择：电梯井共有%d层。\n'%EF)
    #初始化楼层数
    IF=input('您希望初始化到达哪个楼层？(默认当前最高层，限制1~最高层)')
    if IF.strip().isdigit() and (int(IF)>=1 and int(IF)<=EF):
        IF=int(IF)
    else:
        IF=EF
    print('您的选择：初始化到达%d层。\n'%IF)
    #初始化方向
    DE=input('您希望初始化的方向为？(填写数字，"1"代表向上，"2"代表向下)')
    if DE.strip().isdigit() and (int(DE)==1 or int(DE)==2):
        DE=int(DE)
    else:
        DE=1
    if DE==1:
        DE='False'
        print('您的选择：初始化方向向上。\n')
    else:
        DE='True'
        print('您的选择：初始化方向向下。\n')
    #初始化是否应该撞击第二限位
    ISC=input('您希望初始化是否撞击第二限位？(默认撞第一不撞第二，"0"代表不撞击，"1"反之)')
    if ISC.strip().isdigit() and int(ISC)==0:
        ISC='True'
        print('您的选择：撞击第一限位和第二限位。\n')
    else:
        ISC='False'
        print('您的选择：撞击第一限位，不撞击第二限位。\n')
    #搭乘总人数
    PN=input('您希望电梯在规定的时间内有多少人希望乘梯？(默认200，限制1~1000)')
    if PN.strip().isdigit() and (int(PN)>=1 and int(PN)<=1000):
        PN=int(PN)
    else:
        PN=200
    print('您的选择：乘梯人数%d人。\n'%PN)
    #初始化限制时间
    IEL=input('您希望电梯初始化限制多少时间内完成？(默认100，限制50~200)')
    if IEL.strip().isdigit() and (int(IEL)>=50 and int(IEL)<=200):
        IEL=int(IEL)
    else:
        IEL=100
    print('您的选择：初始化限制时间：%d秒。\n'%IEL)
    #第一位出现时间
    TS=input('您希望首位乘客在开始后多久可以出现？(默认初始化限制时间+1S)')
    if TS.strip().isdigit() and int(TS)>=IEL and int(TS)>IEL:
        TS=int(TS)
    else:
        TS=IEL+1
    print('您的选择：首位乘客出现在%d秒之后。\n'%TS)
    #最后一位出现时间
    TE=input('您希望末位乘客在开始后最晚多久出现？(默认每名0.5S，最小每名0.05S)')
    if TE.strip().isdigit() and int(TE)>=int(TS+PN*0.05):#意思是结束时间要≥开始时间+每个乘客最小0.05S
        TE=int(TE)
    else:
        TE=int(TS+PN*0.5)
    print('您的选择：末位乘客出现在%d秒之前。\n'%TE)
    #最重单人重量
    WMa=input('您希望最重的人的重量是？(默认90，限制60~120)')
    if WMa.strip().isdigit() and (int(WMa)>=60 and int(WMa)<=120):
        WMa=int(WMa)
    else:
        WMa=90
    print('您的选择：乘客最重%d千克\n'%WMa)
    #最轻单人重量
    WMi=input('您希望最轻的人的重量是？(默认30，限制16~40)')
    if WMi.strip().isdigit() and (int(WMi)>=16 and int(WMi)<=40):
        WMi=int(WMi)
    else:
        WMi=30
    print('您的选择：乘客最轻%d千克。\n'%WMi)
    #运行结束判分时间
    AEL=input('您希望在开始后多久强制判分？(末位乘客后默认60S，限制出现后+[30~1000]S)')
    if AEL.strip().isdigit() and (int(AEL)>=TE+30 and int(AEL)<=TE+1000):
        AEL=int(AEL)
    else:
        AEL=TE+60
    print('您的选择：判分时间为%d秒。\n'%AEL)
    return EN,EF,IF,DE,ISC,PN,TS,TE,WMa,WMi,IEL,AEL

#创建文件
def filecreate(en,ef):#先进行输入的字符串处理
    namt1=list(str(en*100+ef))
    namt1.insert(0,'/P')
    namt1.append('.ees')

    winchoose = tk.Tk()
    winchoose.withdraw()
    print('您想要将创建的文件放在什么位置？')
    location = filedialog.askdirectory() #获得选择好的文件夹

    namt2=list(location)
    for i in range(len(namt1)):
        namt2.append(namt1[i])
    targetpath=''.join(namt2)

    return targetpath

#头部写入
def headin(target,detail):
    f1=open(file=targetfile,mode='w',encoding='utf-8-sig')
    f1.write(detail)
    f1.close()
    return

#中部数据处理及写入
def maindata(targetf,Peoplenum,Initfloor,TimeC,TimeE,Efloor,WeightC,WeightE):

    str0='''\n    <Node Index="'''#排队顺序
    str1='''">
      <Time>'''#出现时间
    str2='''</Time>
      <FlST>'''#起始楼层
    str3='''</FlST>
      <FlEd>'''#结束楼层
    str4='''</FlEd>
      <PeWe>'''#乘客重量
    str5='''</PeWe>
    </Node>'''#结束

    #创建时间序列、起始结束层序列、体重序列
    timeline=list()
    F=list()
    T=list()
    Wei=list()
    for i in range(Peoplenum):
        timeline.append(random.randint(TimeC,TimeE))
        j=0;k=0
        while j==k:
            j=random.randint(1,Efloor)
            k=random.randint(1,Efloor)
        F.append(j)
        T.append(k)
        Wei.append(random.randint(WeightC,WeightE))
    timeline.sort()

    onepeo=list()
    combination=list()
    nownum=0
    for i in range(Peoplenum):
        nownum+=1
        onepeo.append(str0);onepeo.append(str(nownum))
        onepeo.append(str1);onepeo.append(str(timeline[i]))
        onepeo.append(str2);onepeo.append(str(F[i]))
        onepeo.append(str3);onepeo.append(str(T[i]))
        onepeo.append(str4);onepeo.append(str(Wei[i]))
        onepeo.append(str5)
        combination.append(''.join(onepeo))
        onepeo.clear()

    f1=open(targetf,mode='a',encoding='utf-8-sig')
    f1.write(''.join(combination))
    f1.close()
    return

#尾部数据处理及写入
def end(targetf,Initfloor,Initsecondcrush,InitTimeEnd,TimeEndTotal,InitDire,Enum,Efloor):
    endstr=list()
    endstrt=list()

    str1='''\n  </People>
  <Score>
    <Init_TargetFloor>'''#初始化目的
    str2='''</Init_TargetFloor>
    <Init_Velocity>10</Init_Velocity>
    <Init_LimitSignalFrist>True</Init_LimitSignalFrist>
    <Init_LimitSignalSecond>'''#初始化第二限位撞击
    str3='''</Init_LimitSignalSecond>
    <Init_TimeLimitEnd>'''#初始化限制时间
    str4='''</Init_TimeLimitEnd>
    <Init_Direction>'''#初始化方向
    str5='''</Init_Direction>
    <AutoRun_TimeLimitEnd>'''#全部结束时间限制
    str6='''</AutoRun_TimeLimitEnd>
  </Score>
  <Config>
    <ElevatorNum>'''#电梯部数
    str7='''</ElevatorNum>
    <ElevatorPile>'''#电梯层数
    str8='''</ElevatorPile>
  </Config>
</EES>'''

    endstr.append(str1);endstr.append(str(Initfloor))
    endstr.append(str2);endstr.append(str(Initsecondcrush))
    endstr.append(str3);endstr.append(str(InitTimeEnd))
    endstr.append(str4);endstr.append(str(InitDire))
    endstr.append(str5);endstr.append(str(TimeEndTotal))
    endstr.append(str6);endstr.append(str(Enum))
    endstr.append(str7);endstr.append(str(Efloor))
    endstr.append(str8)
    endstrt=''.join(endstr)
        
    f1=open(targetf,mode='a',encoding='utf-8-sig')
    f1.write(endstrt)
    f1.close()
    return

if __name__=="__main__":

    head='''<?xml version="1.0" encoding="utf-8"?>
<EES>
  <People>'''
    #信息取得。
    #电梯部数，电梯楼层数，初始化楼层数，初始化方向，初始化第二限位撞击，搭乘总人数，第一位出现时间，最后一位出现时间，最重单人重量，最轻单人重量，初始化限制时间，运行结束判分时间
    ENum,EFloor,InitFloor,InitDire,InitSecCru,PeopleNum,TimeStart,TimeEnd,WeiMax,WeiMin,InitEndLimit,AutoEndLimit=getinfor()
    #文件创建
    targetfile=filecreate(ENum,EFloor)
    #头部写入
    headin(targetfile,head)
    #中部数据处理及写入
    maindata(targetfile,PeopleNum,InitFloor,TimeStart,TimeEnd,EFloor,WeiMin,WeiMax)
    #尾部数据处理及写入
    end(targetfile,InitFloor,InitSecCru,InitEndLimit,AutoEndLimit,InitDire,ENum,EFloor)
    print('\n\n操作成功完成！\n\n')
    os.system('pause')