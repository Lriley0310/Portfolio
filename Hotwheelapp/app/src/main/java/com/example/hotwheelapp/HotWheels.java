package com.example.hotwheelapp;

public class HotWheels {
    private String make;
    private String model;

    private String color;

    private String year;
    public HotWheels(){}
    public HotWheels(String make, String model, String color, String year)
    {
        this.make = make;
        this.model = model;
        this.color = color;
        this.year = year;
    }

    public String getName() {
        return make;
    }

    public void setName(String make) {
        this.make = make;
    }

    public String getPosition() {
        return model;
    }

    public void setPosition(String model) {
        this.model = model;
    }

    public String getColor(){return color;}

    public void setColor(){this.color = color;}

    public String getYear(){return year;}

    public void setYear(){this.year = year;}

}
