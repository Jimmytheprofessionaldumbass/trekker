# This file will be run continuously for you to implement any instincts such as if zombie is nearby or falling into lava. You will need to write ways to detect with the mineflayer api and then corresponding action code. It should be written somewhere what instinctive action is running before it starts and they all should be able to stop by the other processes
while True:
    if falling_into_lava(): # Can be replaced by callback functions if a running mineflayer instance has those and that the agents can modify instincts live
        open('w', 'instinct.txt').write('falling into lava running')
        message = clutch() #Includes what it did and at what time exactly it happened
        log(message) #parses message

