import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // initialize grand total and all the order details with a blank string
        double grandTotalAllOrders = 0;
        String allOrderDetails = "";

        // main running code - loops until the user stops ordering
        while (true) {
            // reset prices to 0
            double sandwichPrice = 0;
            double friesPrice = 0;
            double drinkPrice = 0;
            double ketchupPrice = 0;

            // print out the sandwich options and prices
            System.out.println("Sandwiches:");
            System.out.println("1 - Tofu: $5.75");
            System.out.println("2 - Chicken: $5.25");
            System.out.println("3 - Beef: $6.25");
            System.out.print("Would you like a sandwich? (y/n): ");
            char wantSandwich = scanner.next().charAt(0);

            // if the user enters 'y' then get the number of sandwich thay they want
            if (wantSandwich == 'y' || wantSandwich == 'Y') {
                System.out.print("Enter the number of the sandwich you'd like (1, 2, 3): ");
                int sandwichChoice = scanner.nextInt();

                if (sandwichChoice == 1) {
                    // add the price of the sandwich to the variable
                    sandwichPrice = 5.75;
                    System.out.println("\nTofu sandwich ordered.\n");
                } else if (sandwichChoice == 2) {
                    sandwichPrice = 5.25;
                    System.out.println("\nChicken sandwich ordered.\n");
                } else if (sandwichChoice == 3) {
                    sandwichPrice = 6.25;
                    System.out.println("\nBeef sandwich ordered.\n");
                // the user inputs something other than 1,2, or 3
                } else {
                    System.out.println("\nInvalid sandwich choice.\n");
                }
            }

            // print out the fry options and prices
            System.out.println("Fries:");
            System.out.println("1 - Small: $1.00");
            System.out.println("2 - Medium: $1.75");
            System.out.println("3 - Large: $2.25");
            System.out.print("Would you like fries? (y/n): ");
            char wantFries = scanner.next().charAt(0);

            if (wantFries == 'y' || wantFries == 'Y') {
            System.out.print("Enter the number of the fries you'd like (1, 2, 3): ");
            int friesChoice = scanner.nextInt();

            if (friesChoice == 1) {
                friesPrice = 1.00;
                System.out.println("\nSmall fries ordered.\n");
            } else if (friesChoice == 2) {
                friesPrice = 1.75;
                System.out.println("\nMedium fries ordered.\n");
            } else if (friesChoice == 3) {
                friesPrice = 2.25;
                System.out.println("\nLarge fries ordered.\n");
            } else {
                System.out.println("\nInvalid fry choice.\n");
            }
        }

            // print out the drink options and prices
            System.out.println("Drinks:");
            System.out.println("1 - Small: $1.00");
            System.out.println("2 - Medium: $1.50");
            System.out.println("3 - Large: $2.00");
            System.out.print("Would you like a drink? (y/n): ");
            char wantDrink = scanner.next().charAt(0);

            if (wantDrink == 'y' || wantDrink == 'Y') {
                System.out.print("Enter the number of the drink you'd like (1, 2, 3): ");
                int drinkChoice = scanner.nextInt();

                if (drinkChoice == 1) {
                    drinkPrice = 1.00;
                    System.out.println("\nSmall drink ordered.\n");
                } else if (drinkChoice == 2) {
                    drinkPrice = 1.50;
                    System.out.println("\nMedium drink ordered.\n");
                } else if (drinkChoice == 3) {
                    drinkPrice = 2.00;
                    System.out.println("\nLarge drink ordered.\n");

                    // ask if the user if they want to upgrade
                    System.out.print("Would you like to upgrade to child size for $0.38 more? (y/n): ");
                    char upgradeDrink = scanner.next().charAt(0);
                    if (upgradeDrink == 'y' || upgradeDrink == 'Y') {
                        drinkPrice += 0.38;
                        System.out.println("\nDrink upgraded to child size.\n");
                    }
                } else {
                    System.out.println("\nInvalid drink choice.\n");
                }
            }


            // ketchup packets
            int ketchupPackets;
            do {
                System.out.print("How many ketchup packets would you like? Enter a positive whole number: ");
                while (!scanner.hasNextInt()) {
                    System.out.print("That's not a whole number. Enter a positive whole number: ");
                    // delete the invalid input
                    scanner.next(); 
                    }

                ketchupPackets = scanner.nextInt();
                // if its less than 0, ask again
                if (ketchupPackets < 0) {
                    // keep asking the question until the user inputs a whole number
                    System.out.print("Please enter a positive whole number for ketchup packets. ");
                    }
                } while (ketchupPackets < 0);


            ketchupPrice = ketchupPackets * 0.25;
            System.out.printf("\n%d ketchup packets ordered.\n\n", ketchupPackets);

            // add up all the prices of the items to find the toal for this order
            double orderTotal = sandwichPrice + friesPrice + drinkPrice + ketchupPrice;

            // discount 
            if (sandwichPrice > 0 && friesPrice > 0 && drinkPrice > 0) {
                orderTotal -= 1.00;
                System.out.println("Discount applied.");
            }

            // calculate tax and subtotal
            double tax = orderTotal * 0.07;
            double subtotal = orderTotal - tax;

            // add this order total to grand total
            grandTotalAllOrders += orderTotal;

            // add these details to the empty string 
            allOrderDetails += "\n---------------------------------------------------------------------------------------";
            allOrderDetails += "\nOrder Summary:";
            allOrderDetails += String.format("\nSandwich: $%.2f", sandwichPrice);
            allOrderDetails += String.format("\nFries: $%.2f", friesPrice);
            allOrderDetails += String.format("\nDrink: $%.2f", drinkPrice);
            allOrderDetails += String.format("\nKetchup Packets: $%.2f", ketchupPrice);
            allOrderDetails += String.format("\nSubtotal: $%.2f", subtotal);
            allOrderDetails += String.format("\nTax (7%%): $%.2f", tax);
            allOrderDetails += String.format("\nTotal for this Order: $%.2f", orderTotal);

            // print out the current order's details
            System.out.println("\nSubtotal: $" + String.format("%.2f", subtotal));
            System.out.println("Tax (7%): $" + String.format("%.2f", tax));
            System.out.println("Total for this Order: $" + String.format("%.2f \n", orderTotal));

            // ask the user if they want to make another order
            System.out.print("Do you want to place another order? (y/n): ");

            // get the first character from the input, then store it in anotherOrder
            char anotherOrder = scanner.next().charAt(0);

            // break the program and ask what sandwich they want (back to the top of the program)
            if (anotherOrder != 'y' && anotherOrder != 'Y') {
                break;
            }
        }

        // print out the details for all the orders and print the grand total
        System.out.println(allOrderDetails);
        System.out.println("\nGrand Total of All Orders: $" + String.format("%.2f", grandTotalAllOrders));

        scanner.close();
    }
}
