import json

class ToDoApp():
    def __init__(self):
        self.tasks = []
       
#-----------------------------------------------------------------------    
#Add Task
#-----------------------------------------------------------------------
    def add_task(self):
        n = input("Enter add task: ").strip()

        if not n:
            print("Task cannot be empty!")
        elif n not in self.tasks:
            self.tasks.append(n)
            print("Task added.")
        else:
            print("Task already exists")
             
#-------------------------------------------------------------------------
# Save Task    
#-------------------------------------------------------------------------    
    def save_task(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
               
        print("Tasks Save Successfully!")  
         
#-------------------------------------------------------------------------
# Load Task    
#-------------------------------------------------------------------------
    def load_task(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []        
#-----------------------------------------------------------------------    
#View Task    
#-----------------------------------------------------------------------
         
    def view_task(self):
        if not self.tasks:
            print("not found")
        else:
            print("\nYour Task")
            for i , task in enumerate(self.tasks, start=1):
                print(i, task)  
               
#-----------------------------------------------------------------------    
#Update Task
#-----------------------------------------------------------------------
               
    def  update_task(self):
       
        try:
            task_id = int(input("Enter Task number: "))
           
        except ValueError:
            print("Please enter a vilad number!")
            return  
       
         
        for i, task in enumerate(self.tasks, start=1):
           
            if i == task_id:
                new_task = input("Enter new task: ").strip()

                if not new_task:
                    print("Task cannot be empty!")
                    return

            self.tasks[i-1] = new_task
            self.save_task()

            print("Task updated successfully!")
            return

    print("Task not found!")      

#-----------------------------------------------------------------------                  
#Delete Task
#-----------------------------------------------------------------------                  
   
    def delete_task(self):
        delete_id = int(input("Enter task number: "))
        for i , task in enumerate(self.tasks, start=1):
            if i == delete_id:
                self.tasks.pop(i-1)
                print("Tasks deleted successfully!")
                return
        print("Task not found!")  
       
#-----------------------------------------------------------------------
#Mark Todo Complete
#-----------------------------------------------------------------------
    def complete_task(self):
        task_id = int(input("Enter task complete number: "))
        for i , task in enumerate(self.tasks, start=1):
            if i == task_id:
                print("Complete ✅")
                self.tasks[i -1] = task + "✅"
                print("Todo marked as complete!")
                return
           
        print("Task not found!")        
               
#-----------------------------------------------------------------------              
#Create an Object for ToDoApp
#----------------------------------------------------------------------                

todo = ToDoApp()
todo.load_task()


while True:
        print("\n============TODO APP===========\n")
        print("1: Add to task")
        print("2: View all task")
        print("3: Update task")
        print("4: Delete task")
        print("5: Mark Todo Complete")
        print("6: Save Tasks")
        print("0: Exit")

        try:
            choose = int(input("Enter Your Choice : "))
        except ValueError:
            print("Please enter a valid number!")
            continue
     
        match choose:
            case 1:
                todo.add_task()
            case 2:
                todo.view_task()  
            case 3:
                todo.update_task()  
            case 4:
                todo.delete_task()
            case 5:
                todo.complete_task()
            case 6:
                todo.save_task()
            case 0:
                print("Exit")
                break
            case _:
                print("Invalid input. Please enter 1 to 5 or 0 to exit.")
