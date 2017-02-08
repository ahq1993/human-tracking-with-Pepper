# Pepper robot tracks people and interact with them.
This project has the following contributions:
1- Human tracking using Pepper robot.
2- Procedure of turning on the awareness, in Pepper robot, of its physical surroundings.
3- Reading and storing images from 3D sensor and VGA forehead camera of the Pepper robot.
4- Pepper Interact with people with four set of actions
	1- Doing nothing (also called waiting in social terms)
	2- Looking towards human through tracking human with head motion.
	3- Waving hand and saying hello 
	4- Handshaking: The robot also grabs the hand of the person if the FSR touch sensor on the robot's hand detects the touch.

Requirements:

	1- Pepper Robot (https://www.ald.softbankrobotics.com/en/cool-robots/pepper)
	
	2- [Optional] Mbed microcontroller (https://developer.mbed.org/platforms/mbed-LPC1768/)
 	
	3- [Optional] FSR Touch sensor (https://www.sparkfun.com/products/9376)

Procedure:

	1- Bring FSR into action through integration with mbed or any microcontroller (please burn the code 'uC.cpp' on mbed).
	
	2- Paste FSR on Pepper's right hand.
	
	3- Run mbed_usb.py and then main.py on two seperate terminals


We utilized this project together with a deep neural network based policy network to enable a robot to learn social norms through interaction with people in public places. The network tells the robot which action to choose (Waiting, look towards human, wave hand and handshake) in any given scenario.

Please refer to the following paper for more details:

Qureshi AH, Nakamura Y, Yoshikawa Y, Ishiguro H. Robot gains social intelligence through multimodal deep reinforcement learning. InHumanoid Robots (Humanoids), 2016 IEEE-RAS 16th International Conference on 2016 Nov 15 (pp. 745-751). IEEE. 
