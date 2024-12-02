package utils;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Validators {

    public int validateIntegerInput(String prompt, boolean nullable) {
        // Method to validate integer input
        Scanner scanner = new Scanner(System.in);
        int validInput = 0;
        boolean isValid = false;

        while (!isValid) {
            System.out.print(prompt);
            if (scanner.hasNextInt()) {
                validInput = scanner.nextInt(); // Read the integer input
                isValid = true;  // Input is valid, break out of the loop
            } else {
                System.out.println("Invalid input. Please enter a valid integer.");
                scanner.next();  // Consume the invalid input
            }
        }

        return validInput;
    }


    public String validateStringInput(String prompt, boolean nullable) {
        Scanner scanner = new Scanner(System.in);
        String validInput = null;
        boolean isValid = false;

        while (!isValid) {
            System.out.print(prompt);
            validInput = scanner.nextLine();  // Read the string input

            if (validInput != null && !validInput.trim().isEmpty()) {
                isValid = true;  // Input is valid, break out of the loop
            } else if (nullable && (validInput == null || validInput.isEmpty())) {
                isValid = true;
            } else {
                System.out.println("Invalid input!");
            }
        }

        return validInput;
    }
}
