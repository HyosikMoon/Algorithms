import java.util.*;

public class TestArray {

    public static void main(String[] args) {
        Map<String, Integer> giIndexList = new HashMap<String, Integer>();;

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

        String text = "Ingredients: agave syrup, Milk chocolate (sugar, COcoa butter, milk ingredients, unsweetened chocolate, soy lecithin, salt, natural flavour), Almonds (roasted in canola oil), Gum Arabic, dextrose, Sugar (qlucose solids), Shellac. Contains: Milk, Soy, Almonds. May contain: Peanuts, Other tree nuts. Ingredients. Choce";

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
    }
}