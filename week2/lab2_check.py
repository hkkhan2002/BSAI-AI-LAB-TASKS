from lab2_model import ClassroomAgent

agent = ClassroomAgent()
percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False),
            (29, False), (24, True), (27, True)]

print('step | previous | percept | target | command')
for step, percept in enumerate(percepts, 1):
    prev = agent.last
    target, send = agent.act(*percept)
    if send:
        command = 'SEND ' + target
    else:
        command = 'NO COMMAND'
    print(step, prev, percept, target, command, sep=' | ')
