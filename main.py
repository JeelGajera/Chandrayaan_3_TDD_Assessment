from spacecraft_control import execute_commands

initial_position = (0, 0, 0)
initial_direction = "N"
commands = ["l", "f"]

final_position, final_direction = execute_commands(initial_position, initial_direction, commands)

print("Final Position:", final_position)
print("Final Direction:", final_direction)