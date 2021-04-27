package src_blank;

import java.util.Objects;

public class equalPrac {
    private String name;
    private int year;

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (obj instanceof SomeClass) {
            SomeClass test = (SomeClass) obj;
            if (name == test.name) {
                return true;
            }            
        }
        return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}

class SomeClass {
    public String name;
    public int year;
}