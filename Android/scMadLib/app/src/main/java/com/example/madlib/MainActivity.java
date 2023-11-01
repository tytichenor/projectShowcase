package com.example.madlib;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import java.util.Random;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        // components
        EditText input1EX = findViewById(R.id.input1);
        EditText input2EX = findViewById(R.id.input2);
        EditText input3EX = findViewById(R.id.input3);
        EditText input4EX = findViewById(R.id.input4);
        EditText input5EX = findViewById(R.id.input5);
        EditText input6EX = findViewById(R.id.input6);
        EditText input7EX = findViewById(R.id.input7);
        EditText input8EX = findViewById(R.id.input8);
        Button buttonOption1 = findViewById(R.id.buttonOption1);
        Button buttonOption2 = findViewById(R.id.buttonOption2);
        Button buttonOption3 = findViewById(R.id.buttonOption3);
        Button randomBTN = findViewById(R.id.buttonOptionRandom);
        TextView instructionText = findViewById(R.id.instructionText);
        TextView outputText = findViewById(R.id.outputText);



        // buttonOption1
        buttonOption1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                instructionText.setText("1-plural noun  2-adjective  3-adjective  4-verb  5-adjective  6-noun  7-adjective  8-noun");

                String input1 = String.valueOf(input1EX.getText());
                String input2 = String.valueOf(input2EX.getText());
                String input3 = String.valueOf(input3EX.getText());
                String input4 = String.valueOf(input4EX.getText());
                String input5 = String.valueOf(input5EX.getText());
                String input6 = String.valueOf(input6EX.getText());
                String input7 = String.valueOf(input7EX.getText());
                String input8 = String.valueOf(input8EX.getText());

                outputText.setText("A group of "+input1+" were having a "+input2+" party by the "+input3+" lake. They "+input4+" under the "+input5+" moon. They drank "+input6+" with a "+input7+input8);
            }
        });



        // buttonOption2
        buttonOption2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                instructionText.setText("1-proper noun  2-verb  3-adjective  4-adjective  5-noun(place)  6-adjective  7-verb  8-adjective");

                String input1 = String.valueOf(input1EX.getText());
                String input2 = String.valueOf(input2EX.getText());
                String input3 = String.valueOf(input3EX.getText());
                String input4 = String.valueOf(input4EX.getText());
                String input5 = String.valueOf(input5EX.getText());
                String input6 = String.valueOf(input6EX.getText());
                String input7 = String.valueOf(input7EX.getText());
                String input8 = String.valueOf(input8EX.getText());

                outputText.setText("A person named "+input1+input2+" through the "+input3+" red light by the "+input4+input5+". Then a "+input6+" spaceship "+input7+" in the "+input8+" sky.");
            }
        });



        // buttonOption3
        buttonOption3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                instructionText.setText("1-adjective  2-adjective  3-noun  4-adjective  5-noun  6-noun  7-proper noun  8-verb(past)");

                String input1 = String.valueOf(input1EX.getText());
                String input2 = String.valueOf(input2EX.getText());
                String input3 = String.valueOf(input3EX.getText());
                String input4 = String.valueOf(input4EX.getText());
                String input5 = String.valueOf(input5EX.getText());
                String input6 = String.valueOf(input6EX.getText());
                String input7 = String.valueOf(input7EX.getText());
                String input8 = String.valueOf(input8EX.getText());

                outputText.setText("There once was a "+input1+" cat from a "+input2+" place far from "+input3+". It was a part of "+input4+" mafia and worked with dealing exports such as "+input5+" and "+input6+". The right-hand man named "+input7+" was "+input8+" because of the feds.");
            }
        });

        randomBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Random randy = new Random();

                String input1 = String.valueOf(input1EX.getText());
                String input2 = String.valueOf(input2EX.getText());
                String input3 = String.valueOf(input3EX.getText());
                String input4 = String.valueOf(input4EX.getText());
                String input5 = String.valueOf(input5EX.getText());
                String input6 = String.valueOf(input6EX.getText());
                String input7 = String.valueOf(input7EX.getText());
                String input8 = String.valueOf(input8EX.getText());

                // random code - chooses a random number, then chooses a madlib
                int randInt = randy.nextInt(3);
                if(randInt == 1){
                    instructionText.setText("1-adjective  2-adjective  3-noun  4-adjective  5-noun  6-noun  7-proper noun  8-verb(past)");

                    outputText.setText("There once was a "+input1+" cat from a "+input2+" place far from "+input3+". It was a part of "+input4+" mafia and worked with dealing exports such as "+input5+" and "+input6+". The right-hand man named "+input7+" was "+input8+" because of the feds.");
                }else if(randInt==2){
                    instructionText.setText("1-proper noun  2-verb  3-adjective  4-adjective  5-noun(place)  6-adjective  7-verb  8-adjective");

                    outputText.setText("A person named "+input1+input2+" through the "+input3+" red light by the "+input4+input5+". Then a "+input6+" spaceship "+input7+" in the "+input8+" sky.");
                }else{
                    instructionText.setText("1-plural noun  2-adjective  3-adjective  4-verb  5-adjective  6-noun  7-adjective  8-noun");

                    outputText.setText("A group of "+input1+" were having a "+input2+" party by the "+input3+" lake. They "+input4+" under the "+input5+" moon. They drank "+input6+" with a "+input7+input8);
                }

            }
        });


    }
}