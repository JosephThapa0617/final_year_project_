from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
import time

# all simIK.* type of functions and constants
simIK = client.getObject('simIK')
sim = client.getObject('sim')
simBase = sim.getObject('/base_dyn')
simTip = sim.getObject('/base_dyn/tip')
simTarget = sim.getObject('/base_dyn/target')
sphere= sim.getObject('/base_dyn/manipSphere')
g_joint1=sim.getObjectHandle('/base_dyn/gripper_joint1')
g_joint2=sim.getObjectHandle('/base_dyn/gripper_joint2')
cup=sim.getObjectHandle('/Cup[0]/visible_transparent')





ikEnv = simIK.createEnvironment()
ikGroup_undamped = simIK.createGroup(ikEnv)
simIK.setGroupCalculation(ikEnv, ikGroup_undamped,
                          simIK.method_pseudo_inverse, 0, 10)
simIK.addElementFromScene(ikEnv, ikGroup_undamped,
                          simBase, simTip, simTarget, simIK.constraint_position+simIK.constraint_alpha_beta)
ikGroup_damped = simIK.createGroup(ikEnv)
simIK.setGroupCalculation(ikEnv, ikGroup_damped,
                          simIK.method_damped_least_squares, 0.3, 99)
simIK.addElementFromScene(ikEnv, ikGroup_damped, simBase,
                          simTip, simTarget, simIK.constraint_position+simIK.constraint_alpha_beta)





# cnt=1
def ik():
    position1 = [round(num, 4) for num in sim.getObjectPosition(simTip,simBase)]
    position=position1


    while position1==position :

        # position=sim.getObjectPosition(simTip,simBase)
        # print(position)
        position = [round(num, 4) for num in sim.getObjectPosition(simTip,simBase)]

        print (position)
        if simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)==simIK.result_fail :
            simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_damped)
        

    # simIK.eraseEnvironment(ikEnv)



#sim.setObjectPosition(sphere, sim.handle_world, [0.87955,-0.06001,1.05219])


sim.setObjectPosition(sphere, sim.handle_world, [0.82631,+0.7466,0.96367])
ik()
time.sleep(4)
sim.setObjectPosition(sphere, sim.handle_world, [0.82631,+0.7466,0.76367])
ik() 

time.sleep(4)
sim.setJointTargetPosition(g_joint1,30*3.14/180)
sim.setJointTargetPosition(g_joint2,-30*3.14/180)
time.sleep(4)

# sim.setObjectPosition(sphere, sim.handle_world, [0.45108,-0.8466,0.96367])
# ik() 
# time.sleep(4)
# sim.setObjectPosition(sphere, sim.handle_world, [0.45108,-0.8466,0.76367])
# ik() 
# time.sleep(4)

sim.setObjectPosition(sphere, sim.handle_world, [0.87608,0.0284,0.96367])
ik()
time.sleep(4)
sim.setObjectPosition(sphere, sim.handle_world, [0.87608,0.0284,0.86367])
time.sleep(4)


sim.setShapeColor(cup,None, sim.colorcomponent_ambient_diffuse,[0,1,0])
# sim.setObjectPosition(sphere, sim.handle_world, [0.87608,0.0284,0.96367])
# ik()
time.sleep(4)



sim.setShapeColor(cup,None, sim.colorcomponent_ambient_diffuse,[1,1,1])
