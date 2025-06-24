import java.util.Scanner;
import java.util.ArrayList;

public class ToDoList{
    static Scanner input = new Scanner(System.in);
    static ArrayList<String> tasks = new ArrayList<String>();
    public static void main(String[] args) {
        int choice;
        do{
            //menu
            System.out.println("************");
            System.out.println(" TO DO LIST ");
            System.out.println("************");
            System.out.println("1. Add tasks.");
            System.out.println("2. Remove tasks.");
            System.out.println("3. View tasks.");
            System.out.println("4. Complete tasks.");
            System.out.println("5. Exit menu.");
            //process input
            System.out.print("Enter what you'd like to do: ");
            choice = input.nextInt();
            input.nextLine();
            switch (choice){
                case 1:
                    addTasks();
                    break;
                case 2:
                    removeTasks();
                    break;
                case 3:
                    viewTasks();
                    break;
                case 4:
                    completeTasks();
                    break;
                case 5:
                    System.out.println("Thank you for using the to-do list.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while(choice != 5);
    }
    public  static void viewTasks(){
        if(tasks.isEmpty()){
            System.out.println("Empty list.");
        }
        System.out.println("Current tasks: ");
        for(int i=0;i<tasks.size();i++){
            System.out.println((i+1) + ". "+ tasks.get(i));
        }
    }
    public static void addTasks(){
        System.out.print("Enter task to add: ");
        String task = input.nextLine();
        tasks.add(task);
        System.out.println("Task added.");
    }
    public static void removeTasks(){
        if(tasks.isEmpty()){
            System.out.println("Empty list.");
        }
        viewTasks();
        System.out.print("Enter the task to remove: ");
        int index = input.nextInt() -1;
        input.nextLine();
        if(index>=0 && index<tasks.size()){
            tasks.remove(index);
            System.out.println("Task removed.");
        } else{
            System.out.println("Invalid task number.");
        }
    }
    public static void completeTasks(){
        if(tasks.isEmpty()){
            System.out.println("All tasks completed.");
        }
        viewTasks();
        System.out.print("Enter the task that is completed: ");
        int index = input.nextInt() -1;
        input.nextLine();
        if(index>=0 && index<tasks.size()){
            tasks.remove(index);
            System.out.println("Task has been completed.");
        }else{
            System.out.println("Invalid task number.");
        }
    }
}