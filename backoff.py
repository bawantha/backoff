#backoff algortithm
#coded by bawwa
#160509B


import random;
# initial packets number

Na=4;
Nb=9;
Tslot=42.356 # time slot 


# get random waiting time for packet number n
def randomWaitingTime(n):
    randomPickList=[]
    for i in range(0,2**n):
        randomPickList.append(i);
    return random.choice(randomPickList);


TxpcktNumberA=1;
TxpcktNumberB=1;
while Na!=0 and Nb!=0:
    waitingTimeA=randomWaitingTime(TxpcktNumberA);
    waitingTimeB=randomWaitingTime(TxpcktNumberB);
    if waitingTimeA==waitingTimeB:
        print('collison occured')
        pass
    elif waitingTimeA<waitingTimeB:
        print("A's pckt"+str(TxpcktNumberA)+"Transfred")
        TxpcktNumberA=TxpcktNumberA+1;
        Na=Na-1;
    elif waitingTimeA>waitingTimeB:
        print("B's pckt"+str(TxpcktNumberB)+"Transfred")
        TxpcktNumberB=TxpcktNumberB+1;
        Nb=Nb-1;
    
