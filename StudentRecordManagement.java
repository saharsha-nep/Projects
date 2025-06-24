import java.util.ArrayList;
import java.util.Scanner;

public class StudentRecordManagement {
    static Scanner input = new Scanner(System.in);
    static ArrayList<Student> list = new ArrayList<Student>();

    public static void main(String[] args) {
        int choice;
        do{
            System.out.println("*************************");
            System.out.println("Student Record Management");
            System.out.println("*************************");
            System.out.println("1. Add Student.");
            System.out.println("2. Remove Student.");
            System.out.println("3. View Students.");
            System.out.println("4. Exit menu.");
            System.out.print("Enter what you'd like to do: ");
            choice = input.nextInt();
            input.nextLine();
            switch(choice){
                case 1:
                    add();
                    break;
                case 2:
                    remove();
                    break;
                case 3:
                    view();
                    break;
                case 4:
                    System.out.println("Thank you for using the system.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while(choice!=4);
    }
    public static void add(){
        System.out.println("Welcome, please enter student details.");
        System.out.print("Enter student name: ");
        String name = input.nextLine();
        System.out.print("Enter student age: ");
        int age = input.nextInt();
        input.nextLine();
        System.out.print("Enter student gender: ");
        String gender = input.nextLine();
        list.add(new Student(name, age, gender));
    }
    public static void remove(){
        if(list.isEmpty()){
            System.out.println("No student in records.");
            return;
        }
        view();
        System.out.println("Enter student you'd like to remove: ");
        int index = input.nextInt();
        input.nextLine();
        if (index > 0 && index <= list.size()) {
            list.remove(index - 1);
            System.out.println("Student removed.");
        } else {
            System.out.println("Invalid student number.");
        }
    }
    public static void view(){
        if(list.isEmpty()){
            System.out.println("No students in records.");
            return;
        }
        for(int i=0; i<list.size();i++){
            Student s = list.get(i);
            System.out.println((i+1) + ". Name: " +s.getName() + ", Age: " + s.getAge() + ", Gender: " + s.getGender());
        }
    }
}
