# Working memory file structure so far. This is where every agent gets command as well as know so far what is going on
'''
Our current task is {current task}

progress: {progress}

Last read by: {agent}
Messages (write in your designated spot, delete others' messages after being read)
central executive:
propose_agent:
action_agent:
critique_agent:

Additional info (never overwrite beyond one line, only append and delete strategically):
'''
# One big issue if they read wm and decides to write something but still thinking, but at the same time central exec agent writes and the original agent is notified, so it is asked to write again and is still slower than central exec agent, and it just continuously gets stuck?
# Maybe a solution: having a central executive message that is sent to the agents

def init(): # Clear working memory? what happens when it quits a world? it would never intentionall quit a world, okay so no clearing, just get back into it


def propose_new_task(world_snapshot,available_skills,server):
    wm = open('w', 'wm.md')
    central_executive_gateway = open('r', 'central_executive_gateway.txt')
    chat_situation = open('r', 'chat_situation.txt')
    not_enough_info = true
    message = '''
    Propose the best next task based on the following information:
        Working memory (what got carried from past instances):
        chat situation (another process that )
    ''' # Need to workshop explanation of working memory. maybe just mention "inspired by psych memory architecture"
    # Is it necessary to put the current task into a seperate variable or it can just be put into working memory? what are issues with each? For now lets put them into working memory
    while not_enough_info:
        




def on_new_chat_message(world_snapshot,available_skills,server,message): # For now I'm thinking of nominating this as the Central Executive because it modifies working memory and knows everything
    chat_situation = open('w', 'chat_situation.txt')
    wm = open('w', 'working memory')
    prompt = '''
    You are playing on a minecraft server called {server name} and you are responsible for making sense of managing chat and processes
    Your job is to make sure the other processes understand what is going on by putting relevant information into a file they will read.
    They work in a loop as such:
        1. an agent retrieves information similar to you but can request as much until it is satisfied, then it will assign a task
        2. the next agent either works on writing new code, fixes existing code, or runs existing code to complete the task.
        3. the last agent determines whether the task completes, if it does, it adds the code into the skills library, if it doesn't, it provides feedback.

    Here is the context:
        Context regarding the server: {entry in LTM database that contains: how you are perceived in the server, what this server is about, who are the people on this server, any other information including relationships, builds, pets, etc}
        Working memory (what carried over from past instances): {working memory file pasted in here}
        Available skills (running code as action space in minecraft): {dictionary of skill:description/limitations}
        World snapshot: {everything a normal player sees}
        Last 50 chat messages: {message}
        

    Respond with the following format:
        Interpretaton: it appears that {what is going on and why it is relevant to the current task}
        Response: {a quick one sentence response to the players if necessary, otherwise leave blank}
        Extracted:
        {Player name}: {Player Message}
        Modify working memory: {ed-style commands that modify the working memory. leave blank if unnecessary}

    Interpretation is your current understanding of the situation, do not 

    ''' # Maybe workshop the definition of skills as code that can run
    # If it notices someone swinging at a sword while running towards voyager while voyager is still in the coding stage, it will write in his assigned slot in working memory (not in wm.txt that his notes are of high value) and since the action agent sees it, it can be told to be able to run a skill that immediately deals with it. if the proposal or critique agent sees it, then it will know to skip its' turn and let the action agent handle it by saying skip turn. so essentially what this agent does is tell everyone what's going on by modifying chat status and working memory.


    response = llm(MODEL, prompt)



# Ideas for LTM
'''
Its like a database (learn about sql databases first or just all types of databases and pros and cons)
Daily notes
'''

while True:
    propose_new_task(
