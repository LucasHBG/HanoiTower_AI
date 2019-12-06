#Assignment submitted by Ahalya Mandana and Suhail Pallath Sulaiman'
from copy import deepcopy
import time as sysTime

class Node:
  def __init__(self):
    self.state=[[],[],[]]
    self.nodeNumber=0
    self.status='idle'
    self.neighbours=[]
    self.parent=None
    self.children=[]
    self.point=10



def evalFunc(node):
    largest=0
    l=[]
    for peg in initialState:
        if len(peg)>0:
            l.append(max(peg))

    largest=max(l)
    #print 'largest=',largest
    node.point=10
    setPnts(node,largest)

def setPnts(node,largest):
    global finalState
    #print '\n starting setpnts with largest= ',largest,' nodestate=',node.state
    if largest>0:

        for fpeg in finalState:
            if largest in fpeg:

                pos=finalState.index(fpeg)
     #           print largest, 'the largest is on peg no ', pos ,fpeg,' in finalstate. finalstate[pos]='#,finalstate[pos]
                if largest in node.state[pos]:
      #              print largest, 'the largest is on peg no ', pos ,' in node.state. node.state[pos]=',node.state[pos]
       #             print 'reducing point from ', node.point, ' to ', (node.point-1)
                    node.point=node.point-1
        #            print 'starting recursive with largest as ', largest-1
                    setPnts(node,largest-1)



def move(st1,st2):

    s1=st1[:]
    s2=st2[:]

    if len(s1)>0:
        topDisc=s1[len(s1)-1]
        lastofS2=len(s2)-1

        if len(s2)==0 or s2[lastofS2]>topDisc:
            s2.append(topDisc)
            s1.pop()

            return s1,s2
        else:
            return None
    else:
        return None


def moveDisc(n):
    global noOfPegs
    stacks=[]

    for x in xrange(0,noOfPegs):
        for y in xrange(0,noOfPegs):

            stacks=move(n.state[x],n.state[y])


            if stacks!=None:
                # print 'states after move', states
                nextnode=Node()
                nextnode=deepcopy(n)
                nextnode.state[x]=deepcopy(stacks[0])
                nextnode.state[y]=deepcopy(stacks[1])


                # print 'states', states
                # print '\n'
                # print 'next node',nextnode.state
                if nextnode.state  in states:
                    #print 'nextnode in states'
                    a=1#dumb value
                else:
                    nodenumber=nextnode.nodeNumber
                    # print nextnode.state, 'next not in states'
                    states.append(nextnode.state)
                    return nextnode
    #print 'DEAD END'
    return None

def printPath(node):
    print 'Tracing back the Path'
    while True:
        print 'Numero node: ', node.nodeNumber,'  Estado:  ', node.state
        if node.parent!=None:
            node=node.parent
        else:
            break


def bestFS():
    print '\n'
    global parentList,nodenumber,childList,targetFound,step,largestInTarget,largest
    leastPoint=10
    for node in parentList:
        #setPoints(node)
        evalFunc(node)

        #print 'Node: ',node.nodeNumber, node.state,node.point
        if node.point<leastPoint:
            leastPoint=node.point



    for node in parentList:

        #To get the time from system
        start_time = sysTime.clock()

        if targetFound==False and node.point==leastPoint:
            print 'Node Pai:',node.nodeNumber,' Estado :',node.state, 'Custo = ', node.point
            exhausted=False
            parent=deepcopy(node)

            i=1
            while exhausted==False :

                i+=1
                childnode=moveDisc(node)

                if childnode!=None:
                    nodenumber+=1
                    childnode.nodeNumber=nodenumber
                    childnode.parent=node
                    parent.children.append(childnode)
                    childList.append(childnode)
                    print '     Node Filho:',childnode.nodeNumber,'Estado:', childnode.state
                    #print 'states', states
                    if childnode.state==finalState:
                        print 'Objetivo final encontrado'
                        print '--- %s segundos ---' % (sysTime.clock() - start_time)
                        printPath(childnode)
                        targetFound=True


                else:
                    exhausted=True
    parentList=deepcopy(childList)
    childList=[]
    if targetFound==False :
        bestFS()



def readState():
    global noOfPegs
    state=[]
    for x in xrange(0,noOfPegs):
        print 'Discos na Haste',x+1,' : ',
        a = [int(x) for x in raw_input().split()]
        state.append(a)

    return state

noOfPegs=3
shouldContinue=True
while shouldContinue:
    print '\n\nAssignment submitted by Ahalya Mandana and Suhail Pallath Sulaiman'

    print '\n1. Best First Search'
    print '2. Sair'


    algoNumber = raw_input("Escolha o algoritmo de busca --> ")


    if algoNumber=='2':
        print '\nSaindo'
        quit()

    print '\nInstrucoes para o Input:'
    print '-->Um exemplo de input para discos em uma Haste >>> 3 2 1'
    print '-->Isso significa que sua Haste tem 3 discos com um disco de tamanho 3 embaixo and um disco de tamanho 1 no topo'
    print '-->Se a Haste esta vazia, apenas aperte ENTER; Nao coloque nada nesse caso'
    noOfPegs =int(raw_input("\nDigite o numero de Hastes--> "))

    print '\nDigite os detalhes do Estado Inicial'
    initialState=readState()
    print '\nDigite os detalhes do Estado Final'
    finalState=readState()

    print '\nEstado Inicial : ',initialState
    print 'Estado Final  : ',finalState

    # initialState=[[1],[3],[2]]
    # finalState=[[3,1],[2],[]]

    # initialState=[[3],[1],[2]]
    # finalState=[[3,2,1],[],[]]
    states=[]
    states=[initialState]
    nodenumber=1
    time=1
    targetFound=False

    node=Node()
    node.state=initialState
    node.nodeNumber=nodenumber
    parentList=[node]
    childList=[]
    targetFound=False
    largestInTarget=False

    step=1


    parentList=[node]
    childList=[]




    if algoNumber=='1':
        print '\nVoce selecionou Best First Search'
        bestFS()

    elif algoNumber=='2':
        print '\nSaindo'
        quit()

    else:
        print 'Por favor selecione uma opcao valida'
        continue
