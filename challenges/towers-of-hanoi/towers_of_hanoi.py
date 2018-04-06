def moveTower(n,fromPole, toPole, withPole):
    if n >= 1:
        moveTower(n-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(n-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

# def towers_of_hanoi(n):
#    return

# def moveDisk(fp,tp):
#     iterations = []
#     for n in moveTower:
#         towers_of_hanoi.append(iterations)

# # moveTower(3,"A","B","C")