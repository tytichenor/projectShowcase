import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // initializations 
        String[] petList = new String[10];  // caps the number of pets to 10
        // keeps a running count of the pets
        int petCount = 0;
        Scanner ui = new Scanner(System.in);
        String userInput = "";

        // while the user doesn't enter 'q', then ask the question
        while (!userInput.equals("q")) {
            System.out.println("What would you like to do? (a)dd, (i)nsert, (r)emove, Re(p)lace, (c)lear, (v)iew, or (q)uit");
            userInput = ui.nextLine();
            if (userInput.equals("a")) {
                petCount = addPet(petList, petCount, ui);
            } 
            else if (userInput.equals("i")) {
                petCount = insertPet(petList, petCount, ui);
            } 
            else if (userInput.equals("r")) {
                petCount = removePet(petList, petCount, ui);
            } 
            else if (userInput.equals("p")) {
                replacePet(petList, petCount, ui);
            } 
            else if (userInput.equals("c")) {
                petCount = clearList(petList);
            } 
            else if (userInput.equals("v")) {
                viewList(petList, petCount);
            } 
            else {
                System.out.println("Please choose a correct answer");
            }
        }
        System.out.println("Program ended.");
    }


    // ADD PET function
    private static int addPet(String[] petList, int petCount, Scanner ui) {
        if (petCount < petList.length) {
            // take in input (name)
            System.out.print("Enter pet name to add: ");
            String petName = ui.nextLine();
            petList[petCount] = petName;
            petCount++;
            System.out.println("Pet added: " + petName);
        } 
        else {
            System.out.println("Cannot add more pets - Maximum is 10");
        }
        return petCount;
    }


    // INSERT PET function
    private static int insertPet(String[] petList, int petCount, Scanner ui) {
        // take in input (index)
        System.out.print("Enter index to insert '0-9': ");
        int index = ui.nextInt();
        ui.nextLine();  

        if (index >= 0 && index <= petCount && petCount < petList.length) {
            // take in input (name)
            System.out.print("Enter pet name to insert: ");
            String petName = ui.nextLine();

            // move the elements to the right to make space for the new pet
            for (int i = petCount; i > index; i--) {
                petList[i] = petList[i - 1];
            }

            // update variables 
            petList[index] = petName;
            petCount++;
            System.out.println("Pet inserted at index " + index + ": " + petName);
        } 
        else {
            System.out.println("Invalid index or the Maximum of 10 pets has been reached");
        }
        return petCount;
    }


    // REMOVE PET function
    private static int removePet(String[] petList, int petCount, Scanner ui) {
        System.out.print("Enter index to remove '0-9': ");
        // take in input (index)
        int index = ui.nextInt();
        ui.nextLine();  

        if (index >= 0 && index < petCount) {
            System.out.println("Pet removed at index " + index + ": " + petList[index]);

            // move elements to the left to remove the pet
            for (int i = index; i < petCount - 1; i++) {
                petList[i] = petList[i + 1];
            }

            petList[petCount - 1] = null;  // set the last element to null
            petCount--;
        } 
        else {
            System.out.println("Invalid index '0-9'");
        }
        return petCount;
    }


    // REPLACE PET function
    private static void replacePet(String[] petList, int petCount, Scanner ui) {
        // take in input (index)
        System.out.print("Enter index to replace '0-9': ");
        int index = ui.nextInt();
        ui.nextLine();  

        if (index >= 0 && index < petCount) {
            // take in input (name)
            System.out.print("Enter new pet name: ");
            String newPetName = ui.nextLine();
            petList[index] = newPetName;
            System.out.println("Pet replaced at index " + index + ": " + newPetName);
        } 
        else {
            System.out.println("Invalid index");
        }
    }


    // CLEAR LIST function
    private static int clearList(String[] petList) {
        Arrays.fill(petList, null);
        System.out.println("All pets are cleared from list");
        return 0;
    }


    // VIEW LIST function
    private static void viewList(String[] petList, int petCount) {
        if (petCount == 0) {
            System.out.println("No pets in the list");
        } 
        else {
            // prints out [ and ] to make it look like a list
            System.out.print("Current pet list: [");
            for (int i = 0; i < petCount - 1; i++) {
                System.out.print(petList[i] + ", ");
            }
            System.out.println(petList[petCount - 1] + "]");
        }
    }
}
