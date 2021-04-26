package src_blank;

import java.util.*;
import java.util.ArrayList;
import java.util.Collections;

// Comparable, Comparator example
// House class for comparing objects by price
class House implements Comparable<House> {
    private int price;
    private int year;
    private String name;

    // Constructor
    public House(int p, int y, String n) {
        this.price = p;
        this.year = y;
        this.name = n;
    }

    @Override
    public int compareTo(House h) {
        return this.price - h.price;
    }

    public int getPrice() {
        return this.price;
    }

    public void setPrice(int p) {
        this.price = p;
    }

    public int getYear() {
        return this.year;
    }

    public void setYear(int y) {
        this.year = y;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String n) {
        this.name = n;
    }
}

// Class to compare House by year
class CompareYear implements Comparator<House> {
    public int compare(House h1, House h2) {
        if (h1.getYear() > h2.getYear()) { return 1; }
        if (h1.getYear() < h2.getYear()) { return -1; }
        else return 0;
    }
}

// Class to compare House by name
class CompareName implements Comparator<House> {
    public int compare(House h1, House h2) {
        return h1.getName().compareTo(h2.getName());
    }
}

// Driver class
class Main {
    public static void main(String[] args) {
        ArrayList<House> HouseLst = new ArrayList<House>();
        HouseLst.add(new House(800, 5, "World on yonge"));
        HouseLst.add(new House(600, 15, "Olive avenue"));
        HouseLst.add(new House(1500, 24, "Private House"));

        // Compare by price
        System.out.println("Compare by price");
        Collections.sort(HouseLst);
        for (House h : HouseLst) {
            System.out.println("House price: " + h.getPrice() +
                               ", House year: " + h.getYear() +
                               ", House name: " + h.getName());
        }
        System.out.println();

        // Compare by year
        System.out.println("Compare by year");
        CompareYear cy = new CompareYear();
        Collections.sort(HouseLst, cy);
        for (House h : HouseLst) {
            System.out.println("House price: " + h.getPrice() +
                               ", House year: " + h.getYear() +
                               ", House name: " + h.getName());
        }
        System.out.println();

        // Compare by name
        System.out.println("Compare by name");
        CompareName cn = new CompareName();
        Collections.sort(HouseLst, cn);
        for (House h : HouseLst) {
            System.out.println("House price: " + h.getPrice() +
                               ", House year: " + h.getYear() +
                               ", House name: " + h.getName());
        }
    }
}