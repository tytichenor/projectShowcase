package com.example.scifiname;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Connect a java object to the widget
        EditText firstETXT = findViewById(R.id.firstEditText);
        EditText lastETXT = findViewById(R.id.lastEditText);
        EditText cityETXT = findViewById(R.id.cityEditText);
        EditText schoolETXT = findViewById(R.id.schoolEditText);
        EditText petETXT = findViewById(R.id.petEditText);
        EditText siblingETXT = findViewById(R.id.siblingEditText);
        Button generateBTN = findViewById(R.id.generateButton);
        TextView outputTXT = findViewById(R.id.outputTextView);

        generateBTN.setOnClickListener(new View.OnClickListener() {
            @Override
                    public void onClick(View view) {

                Random randy = new Random();

                String firstName = String.valueOf(firstETXT.getText());
                String lastName = String.valueOf(lastETXT.getText());
                String city = String.valueOf(cityETXT.getText());
                String school = String.valueOf(schoolETXT.getText());
                String petName = String.valueOf(petETXT.getText());
                String siblingName = String.valueOf(siblingETXT.getText());

                int firstPortion = randy.nextInt(firstName.length());
                int lastPortion = randy.nextInt(lastName.length());
                String SciFiFirstName = firstName.substring(0,firstPortion) + lastName.substring(0,lastPortion);
                firstPortion = randy.nextInt(city.length());
                lastPortion = randy.nextInt(school.length());
                String SciFiLastName = city.substring(0,firstPortion) + school.substring(0,lastPortion);
                firstPortion = randy.nextInt(petName.length());
                lastPortion = randy.nextInt(siblingName.length());
                String SciFiOrigin = firstName.substring(0,firstPortion) + lastName.substring(0,lastPortion);
                outputTXT.setText(SciFiFirstName+" "+SciFiLastName+" of the planet "+SciFiOrigin);


            }
        });
    }




    }
