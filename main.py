from class_stack import Stack

print("\nLet's play Towers of Hanoi!")

#Initialize the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the game
num_disks = 0
while num_disks < 3:
    nd_str = input("\nHow many disks would you like to play with?\n>>")
    if nd_str.isnumeric():
        num_disks = int(nd_str)
    else:
        print("Invalid Entry")
    if num_disks <= 3:
        print("\nPlease enter a number greather than or equal to 3.")

for i in range(num_disks,0,-1):
    left_stack.push(i)

num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves.")

#Get User Move
def get_input(stack_list):
    choices = [st.get_name()[0] for st in stack_list]
    input_valid = False
    while not input_valid:
        user_input = input(f"\nSelect a stack: {choices}\n>>").capitalize()
        for i in range(len(choices)):
            if user_input == choices[i]:
                input_valid = True
                break
        if input_valid == False:
            print("Invalid entry.")
    return stack_list[i]

# get_input(stacks)

#Play The Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n------Current Stacks------")
    for stack in stacks:
        stack.print_items()

    move_complete = False
    while not move_complete:
        print("Which stack would you like to use as your source?")
        srce_stack = get_input(stacks)

        print("Which stack would you like to be your destination?")
        dest_stack = get_input(stacks)

        if not srce_stack.is_empty():
            if dest_stack.is_empty() or (dest_stack.peek() > srce_stack.peek()):
                moved_disk = srce_stack.pop()
                dest_stack.push(moved_disk)
                num_user_moves += 1
                move_complete = True
            else:
                print("\nInvalid Move: You cannot place a larger disk on a smaller one.")
        else:
            print("\nInvalid Move: Source stack is empty.")

print(f"\nCongratulations!  You compelted the game in {num_user_moves} moves. The optimal number of moves is {num_optimal_moves}.")