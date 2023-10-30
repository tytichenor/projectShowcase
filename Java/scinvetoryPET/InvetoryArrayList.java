import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // initializations
        ArrayList<String> petList = new ArrayList<>();
        Scanner ui = new Scanner(System.in);
        String userInput = "";

        // while the user doesn't enter 'q', then ask the question
        while (!userInput.equals("q")) {
            System.out.println("What would you like to do? (a)dd, (i)nsert, (r)emove, Re(p)lace, (c)lear, (v)iew, or (q)uit");
            userInput = ui.nextLine();
            if (userInput.equals("a")) {
                addPet(petList, ui);
            } else if (userInput.equals("i")) {
                insertPet(petList, ui);
            } else if (userInput.equals("r")) {
                removePet(petList, ui);
            } else if (userInput.equals("p")) {
                replacePet(petList, ui);
            } else if (userInput.equals("c")) {
                clearList(petList);
            } else if (userInput.equals("v")) {
                viewList(petList);
            } else if (userInput.equals("q")) {
                System.out.println("Program ended.");
            } else {
                System.out.println("Please choose a correct answer");
            }
        }

    }

    // ADD PET function
    private static void addPet(ArrayList<String> petList, Scanner ui) {
        // take in input (name)
        System.out.print("Enter pet name to add: ");
        String petName = ui.nextLine();
        petList.add(petName);
        System.out.println("Pet added: " + petName);
    }

    // INSERT PET function
    private static void insertPet(ArrayList<String> petList, Scanner ui) {
        // take in input (index)
        System.out.print("Enter index to insert 0-9");
        int index = ui.nextInt();
        ui.nextLine();

        if (index >= 0 && index <= petList.size()) {
            // take in input (name)
            System.out.print("Enter pet name to insert: ");
            String petName = ui.nextLine();
            petList.add(index, petName);
            System.out.println("Pet inserted at index " + index + ": " + petName);
        } 
        else {
            System.out.println("Invalid index or the Maximum of " + petList.size() + " pets has been reached");
        }
    }

    // REMOVE PET function
    private static void removePet(ArrayList<String> petList, Scanner ui) {
        // take in input (index)
        System.out.print("Enter index to remove 0-9");
        int index = ui.nextInt();
        ui.nextLine();

        if (index >= 0 && index < petList.size()) {
            String removedPet = petList.remove(index);
            System.out.println("Pet removed at index " + index + ": " + removedPet);
        } 
        else {
            System.out.println("Invalid index 0-9");
        }
    }

    // REPLACE PET function
    private static void replacePet(ArrayList<String> petList, Scanner ui) {
        // take in input (index)
        System.out.print("Enter index to replace 0-9");
        int index = ui.nextInt();
        ui.nextLine();

        if (index >= 0 && index < petList.size()) {
            // take in input (name)
            System.out.print("Enter new pet name: ");
            String newPetName = ui.nextLine();
            petList.set(index, newPetName);
            System.out.println("Pet replaced at index " + index + ": " + newPetName);
        } 
        else {
            System.out.println("Invalid index 0-9");
        }
    }

    // CLEAR LIST function
    private static void clearList(ArrayList<String> petList) {
        petList.clear();
        System.out.println("All pets are cleared from the list");
    }

    // VIEW LIST function
    private static void viewList(ArrayList<String> petList) {
        // checks if there are pets in the list
        if (petList.isEmpty()) {
            System.out.println("No pets in the list");
        } 
        // if there are pets, print out the list
        else {
            System.out.print("Current pet list: [");
            // for item in the list, print
            for (int i = 0; i < petList.size() - 1; i++) {
                System.out.print(petList.get(i) + ", ");
            }
            System.out.println(petList.get(petList.size() - 1) + "]");
        }
    }
}