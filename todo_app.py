class ToDoApp():
    def __init__(self):
        self.tasks = []
        
#-----------------------------------------------------------------------    
#Add Task
#-----------------------------------------------------------------------
    
    def add_task(self):
        n = input("Enter add task: ").strip()
        if n not in self.tasks:
            self.tasks.append(n)
            print("Task added.")    
        else:
            print("Task already exists")  
     
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
        task_id = int(input("Enter Task number: "))
        for i , task in enumerate(self.tasks , start=1):
              if  i == task_id:
                  new_task = input("Enter new task: ")
                  self.tasks[i-1]= new_task                 
                  print("Task Update successfully!")
                  return
              
        print("Task not found")      

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


while True:
        print("\n============TODO APP===========\n")
        print("1: Add to task")
        print("2: View all task")
        print("3: Update task")
        print("4: Delete task")
        print("5: Mark Todo Complete")
        print("0: Exit")
    
        choose = int(input("Enter Your Choice : "))
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
            case 0:
                print("Exit")
                break
            case _:
                print("Invalid input. Please enter 1 to 5 or 0 to exit.")
    