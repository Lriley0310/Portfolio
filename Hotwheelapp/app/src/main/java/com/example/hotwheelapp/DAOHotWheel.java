package com.example.hotwheelapp;

import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DAOHotWheel
{
    private DatabaseReference databaseReference;
    public DAOHotWheel()
    {
        FirebaseDatabase db = FirebaseDatabase.getInstance();
        databaseReference = db.getReference(HotWheels.class.getSimpleName());
    }
    public Task<Void> add(HotWheels hot)
    {
        return databaseReference.push().setValue(hot);
    }

}
