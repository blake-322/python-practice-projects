#These are the two lists that store tasks
#Functionality for lists of both unfinished and finised tasks will be added later
unfinished_tasks = []
finished_tasks = []

#A welcome message for the program
print('Welcome to the ToDo Program')
print('Type "help" for more information')

#The done boolean will continue the loop until the user wants to exit
done = False

#The user_input variable will store what the user has entered
user_input = ''

#This is the menu system
#The while loop will continuously repeat until the user specifies the exit command
while done == False:
    user_input = input('---> ')
    user_input = user_input.strip()
    
    if user_input == '':
        print('Please enter a command')
    
    elif user_input == 'help':
        print('You can use the following commands')
        print('add - to add a task')
        print('view - to view your tasks')
        print('del - to delete a task')
        print('exit - to exit the program')
        
    elif user_input == 'add':
        user_input = input('Name of task ---> ')
        if user_input.strip() == '':
            print('You need to specify a task name')
        else:
            unfinished_tasks.append(user_input)
            print(f'Your task of "{unfinished_tasks[-1]}" has been added')
    
    elif user_input == 'view':
        if len(unfinished_tasks) == 0:
            print('You have no tasks')
        else:
            print('You have the following tasks:')
            for index, task in enumerate(unfinished_tasks):
                print(f'{index + 1}. {task}')
                
    elif user_input == 'del':
        if len(unfinished_tasks) == 0:
            print('You have no tasks to delete')
        else:
            user_input = input('Type the number of the task you wish to delete ---> ')
            del_index = int(user_input)
            if del_index > 0 and del_index <= len(unfinished_tasks):
                del(unfinished_tasks[del_index - 1])
                print(f'Task number {del_index} has been deleted')
                print(f'You now have {len(unfinished_tasks)} tasks remaining')
            else:
                print(f'Task of number {del_index} does not exist')
                
    elif user_input == 'exit':
        print('Thank you for using the ToDo program')
        done = True
                
    else:
        print(f'The command "{user_input}" is not recognized')
        print('Type "help" for a list of commands')
