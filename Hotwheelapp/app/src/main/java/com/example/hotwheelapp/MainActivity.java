package com.example.hotwheelapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText edit_make = findViewById(R.id.edit_make);
        final EditText edit_model = findViewById(R.id.edit_model);
        final EditText edit_color = findViewById(R.id.edit_color);
        final EditText edit_year = findViewById(R.id.edit_year);
        Button btn = findViewById(R.id.btn_submit);
        DAOHotWheel dao =new DAOHotWheel();
        btn.setOnClickListener(v->
        {
            HotWheels hot = new HotWheels(edit_make.getText().toString(),edit_model.getText().toString(), edit_color.getText().toString(), edit_year.getText().toString());
            dao.add(hot).addOnSuccessListener(suc ->
            {
                Toast.makeText(this, "Record is inserted", Toast.LENGTH_SHORT).show();
            }).addOnFailureListener(er ->
            {
                Toast.makeText(this, ""+er.getMessage(), Toast.LENGTH_SHORT).show();
            });
        });
    }
}