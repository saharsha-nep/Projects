import java.util.Scanner;

public class Calculator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        double num1 = input.nextDouble();
        System.out.print("Enter the operator: ");
        String op = input.next();
        System.out.print("Enter the second number: ");
        double num2= input.nextDouble();
        double result;
        switch (op){
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if(num2==0){
                    System.out.println("Error:Division by 0.");
                    return;
                } else{
                    result = num1/num2;
                }
                break;
            default:
                System.out.println("Invalid operator.");
                return;
        }
        System.out.println("Result is : " + result);
    }
}