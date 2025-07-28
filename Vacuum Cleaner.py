initial_state = ("A" , "Dirty" , "Dirty")
goal_states = [("A" , "Clean" , "Clean") , ("B" , "Clean" , "Clean")]


def vacuum_cleaner(state):
    location , roomA , roomB = state
    action = []

    if location == "A" and roomA == "Dirty":
        action.append(("Suck ", ("A", "Clean" , roomB)))
    elif location == "B" and roomB == "Dirty":
        action.append (('Suck' , ('B' , roomA , 'Clean')))

    if location == 'A':
        action.append(("Move Right " , ("B" , roomA, roomB)))
    else:
        action.append(("Move Left" , ("A" , roomA , roomB)))
    return action

def dfs(state , visited , path):
    if state in goal_states:
        return path
    visited.add(state)

    for action , new_state in vacuum_cleaner(state):
        if new_state not in visited:
            result = dfs(new_state , visited , path +[(action , new_state)])
            if result:
                return result
    return None

visited_state = set()
solution_path = dfs(initial_state , visited_state , [])

print("Steps to clean the room : ")
for step in solution_path:
    print(step)
        

        
        
