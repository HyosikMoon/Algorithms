import java.util.*;

public class TestCode {
    static Map<List<String>, String> sweeteners;
    static List<String> allSwLit;
    ArrayList<String> reprSwLists;
    static Map<String, Integer> descriptions;

    public static void main(String[] args) {
        Map<String, Integer> giIndexList = new HashMap<String, Integer>();

        giIndexList.put("alitame",0);
        giIndexList.put("aspertame",0);
        giIndexList.put("agave syrup",11);
        giIndexList.put("brazzein",0);
        giIndexList.put("brown rice syrup",25);
        giIndexList.put("curculin",0);
        giIndexList.put("cyclamate",0);
        giIndexList.put("dextrose",100);
        giIndexList.put("erythritol",0);
        giIndexList.put("glucose",100);
        giIndexList.put("fructose",21);

        System.out.println(giIndexList);

        String text = "Ingredients: sodium cyclamate, aminosweet, agave syrup, Milk chocolate (sugar, COcoa butter, milk ingredients, unsweetened chocolate, soy lecithin, salt, natural flavour), Almonds (roasted in canola oil), Gum Arabic, dextrose, Sugar (qlucose solids), Shellac. Contains: Milk, Soy, Almonds. May contain: Peanuts, Other tree nuts. Ingredients. Choce";

        // Change to lowercase text
        text = text.toLowerCase();

        // Delete unnecessary characters
        if (text.contains(":")) {
            text = text.replace(":", ",");
        }
        
        if (text.contains("(")) {
            text = text.replace("(", ",");
        }
        
        if (text.contains(")")) {
            text = text.replace(")", ",");
        }
        
        if (text.contains(".")) {
            text = text.replace(".", ",");
        }

        if (text.contains("[")) {
            text = text.replace("[", ",");
        }

        if (text.contains("]")) {
            text = text.replace("]", ",");
        }

        if (text.contains(".")) {
            text = text.replace(".", ",");
        }

        // Delete all spaces between comma, but not the spaces between words
        text = text.replaceAll("(\\s*,\\s*)(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", ",");

        // Extract the items from the text
        String[] itemList = text.split(",[ ]*");
        System.out.println(itemList);

        for (String item : itemList) {
            System.out.println(item);
        }

        // Count the GI index searching the item in giIndexList
        Integer giScore = 0;
        Integer count = 0;

        if (text == null || text.isEmpty()) {
            // Need to modify with TextView
            System.out.println("Cannot decide.");
        } else {
            for (String item : itemList) {
                Iterator<Map.Entry<String, Integer>> iterator = giIndexList.entrySet().iterator();
                while (iterator.hasNext()) {
                    Map.Entry<String, Integer> entry = iterator.next();
                    if (item.equals(entry.getKey())) {
                        giScore = giScore + entry.getValue();
                        count += 1;
                    }
                }
            }
        }

        if (count == 0) {
            // Need to modify with TextView
            System.out.println("Cannot decide.");
        } else {
            if (giScore < 55) {
                // Need to modify with TextView
                System.out.println("Good because of the sum of GI is " + giScore + " of this food.");
            } else if (giScore < 69) {
                System.out.println("Normal because of the sum of GI is " + giScore + " of this food.");
            } else {
                System.out.println("Not recommended because of the sum of GI is " + giScore + " of this food.");
            }
        }

        // All kinds of sweetener list
        List<String> allSwLit = Arrays.asList("acesulfame potassium", "nutrasweet", "spponful", "sodium cyclamate", "aminosweet", "aspartame", "sodium cyclamate", "sucaryl", "cologran","cyclamate", "lesys", "altisweet", "sweetpearl", "hydrogenated glucose syrup","maltitol");

        // Recognize sweeteners
        ArrayList<String> reprSwLists = new ArrayList<String>(200);
        if (text == null || text.isEmpty()) {
            // Need to modify with TextView
            System.out.println("Cannot decide.");
        } else {
            for (String item : itemList) {
                if (allSwLit.contains(item)) {
                    String reprSw = getReprSweetener(item);
                    String nomatching = "nomatching";
                    if (!reprSw.equals(nomatching)) {
                        reprSwLists.add(reprSw);
                    }
                }
            }
            for (String sw : reprSwLists) {
                System.out.println("Sweetener: " + sw);
            }
        }

        // When click the button, it prints descriptions about the sweeteners.
        ArrayList<String> descList = new ArrayList<String>(200);
        if (reprSwLists == null || reprSwLists.isEmpty()) {
            // Need to modify with TextView
            System.out.println("No sweeteners");
        } else {
            for (String rpSw : reprSwLists) {
                String ds = getSwDescription(rpSw);
                String nomatching = "nomatching";
                if (!ds.equals(nomatching)) {
                    descList.add(ds);
                }
            }
            for (String ds : descList) {
                System.out.println(ds);
            }
        }

        // for (String sw : allSwLit) {
        //     System.out.println(sw);
        // }
        printa();
    }

    
    // return a representative sweetener
    private static String getReprSweetener(String recognizedSweetener) {

        // Initialize Hashmap for finding the representative sweentener of the recognized sweetener
        sweeteners = new HashMap<List<String>, String>();

        List<String> aspartame = Arrays.asList("acesulfame potassium", "nutrasweet", "spponful", "aminosweet", "aspartame");
        sweeteners.put(aspartame, "aspartame");

        List<String> cyclamate = Arrays.asList("sodium cyclamate", "sucaryl", "cologran","cyclamate");
        sweeteners.put(cyclamate, "cyclamate");

        List<String> maltitol = Arrays.asList("lesys", "altisweet", "sweetpearl", "hydrogenated glucose syrup","maltitol");
        sweeteners.put(maltitol,"maltitol");
        
        // Find the representative sweentener and return it
        if (recognizedSweetener == null || recognizedSweetener.isEmpty()) {
            // Need to modify with TextView
            // System.out.println("Cannot decide.");
            return "nomatching";
        } else {
            Iterator<Map.Entry<List<String>, String>> iterator = sweeteners.entrySet().iterator();
            while (iterator.hasNext()) {
                Map.Entry<List<String>, String> entry = iterator.next();
                List<String> sameSwList = entry.getKey();
                if (sameSwList.contains(recognizedSweetener)) {
                    String reprSweetener = entry.getValue();
                    return reprSweetener;
                }
            }
        }
        return "nomatching";
    }

    // Return description about the input sweetener
    private static String getSwDescription(String inputReprSw) {
        // Sweetener descriptions 
        // descriptors' first argument is the representative sweetener and the second argument is the description of the sweetener.
        // The first argument is decided by Matching
        Map<String, String> descriptions = new HashMap<String, String>();
        descriptions.put("aspartame", "Avoid!. Aspartame causes more adverse symptoms, health conditions, and disease than all food additives combined.");
        descriptions.put("cyclamate", "Avoid!. Cyclamate is now believed not to cause cancer directly, but to increase the potency of other carcinogens and to harm the testes.");
        descriptions.put("maltitol", "Avoid!. Maltitol is found in many processed foods, a diet high in maltodextrin is likely also high in sugar and salt, and low in fiber. Such a diet can lead to weight gain, higher levels of cholesterol, and type 2 diabetes.");

        Iterator<Map.Entry<String, String>> iterator = descriptions.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, String> entry = iterator.next();
            String reprSw = entry.getKey();
            if (reprSw.equals(inputReprSw)) {
                String description = entry.getValue();
                return description;
            }
        }
        return "nomatching";
    }

    private static void printa() {
        ArrayList<String> teststring = new ArrayList<String>(10);
        String[] abc = {};
        // teststring.add("ASD");
        // teststring.add("NAS");
        // teststring.add("FOR");
        System.out.println(teststring.isEmpty());

        String stSum = "";
        for (String wd : teststring) {
            stSum = wd + " " + stSum;
        }
        System.out.println(descriptions);
        System.out.println(teststring.toString().replaceAll("(\\[|\\])", "").isEmpty());
        System.out.println(teststring.toString().replaceAll("(\\[|\\])", "") == null);
        System.out.println(stSum);
        String bb = "";
        System.out.println(abc == null);

        String one = "This is";
        String two = "This is";
        String three = "this is";
        System.out.println(one.toUpperCase());
        System.out.println(one.equals(two));

    }
}
