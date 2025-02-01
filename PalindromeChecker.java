import java.util.Scanner;

public class PalindromeChecker
{
    private int num; // To store the number entered by the user
    private int revnum; // To store the reversed number

    // Constructor to initialize data members with default values
    public PalindromeChecker() {
        num = 0;
        revnum = 0;
        sc.close();
    }

    // Method to accept the number
    public void accept() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        num = sc.nextInt();
    }

    // Recursive method to reverse the number
    public int reverse(int y) {
        // Base case: if the number is 0, return 0
        if (y == 0) {
            return 0;
        }

        // Calculate the reversed number recursively
        revnum = (revnum * 10) + (y % 10);
        reverse(y / 10);

        return revnum;
    }

    // Method to check if the number is a palindrome
    public void check() {
        revnum = 0; // Reset revnum before reversing
        int reversed = reverse(num); // Reverse the number

        if (num == reversed) {
            System.out.println(num + " is a palindrome.");
        } else {
            System.out.println(num + " is not a palindrome.");
        }
    }

    public static void main(String[] args) {
        PalindromeChecker obj = new PalindromeChecker();
        obj.accept();
        obj.check();
    }
}
