package src;

import java.util.*;

public class HashMapSetPrac {
    public static void main(String[] args) {

        //List
        Integer[] lst = new Integer[10];
        lst[1] = 10;
        System.out.println(lst[1]);
        
        double[] lst2 = new double[10];
        lst2[1] = 10.5;
        for (double db : lst2) {
            System.out.println(db);
        }

        // https://docs.oracle.com/javase/7/docs/api/java/util/HashSet.html - HashSet oracle
        // HashSet
        Set<String> set = new HashSet<String>();
        set.add("Jashon");
        set.add("Moon");
        set.add("Jack");
        System.out.println(set);
        System.out.println();

        // https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html - Iterator oracle
        // HashSet iterator
        Iterator iter = set.iterator();
        System.out.println("\"Iterator, iterate hashSet values\"");
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
        System.out.println();

        // https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html - HashMap oracle
        // HashMap
        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("Jashon", 33);
        map.put("Jhon", 23);
        map.put("Moon", 30);
        map.put("Jan", 24);
        System.out.println(map);
        // HashMap entrySet()
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ", " + entry.getValue());
        }
        System.out.println();

        // Put new <key, value> in HashMap
        map.put("Moon", 20);
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ", " + entry.getValue());
        }
        System.out.println();

        // replace value of HashMap
        map.replace("Jhon", 200);
        System.out.println(map);
        System.out.println();

        // Print keySet()
        System.out.println(map.keySet());
        System.out.println(map.values());
        System.out.println();


        // Extract keys in HashMap and save them in a HashSet
        Set<String> names = new HashSet<String>();
        for (String name : map.keySet()) {
            names.add(name);
        }
        // for (String name : names) {
        //     System.out.println(name);
        // }

        // // Convert HashSet to a List
        // String[] namesArray = names.toArray(new String[names.size()]);
        // for (String name : namesArray) {
        //     System.out.println(name);
        // }
    }
}
