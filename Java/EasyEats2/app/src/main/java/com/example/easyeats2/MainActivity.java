package com.example.easyeats2;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.SparseArray;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.vision.Frame;
import com.google.android.gms.vision.text.TextBlock;
import com.google.android.gms.vision.text.TextRecognizer;
import com.theartofdev.edmodo.cropper.CropImage;
import com.theartofdev.edmodo.cropper.CropImageView;

import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    Button button_capture, button_copy;
    TextView textview_data;
    Bitmap bitmap;
    String[] itemList;
    Map<String, Integer> giIndexList;
    Integer giScore;
    Integer count;
    private static final int REQUEST_CAMERA_CODE = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        makeGiIndexList();

        button_capture = findViewById(R.id.button_capture);
        button_copy = findViewById(R.id.button_copy);
        textview_data = findViewById(R.id.text_data);

        if (ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{
                    Manifest.permission.CAMERA
            }, REQUEST_CAMERA_CODE);
        }

        button_capture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CropImage.activity().setGuidelines(CropImageView.Guidelines.ON).start(MainActivity.this);

            }
        });

        button_copy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String scanned_text = textview_data.getText().toString();
                giScore = 0;
                count = 0;
                itemList = makeGiList(scanned_text);
                giScore = calGiScore(scanned_text);
                printGiResult(giScore);
            }
        });
    }

    private String[] makeGiList(String text) {
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

        return itemList;
    }

    private Integer calGiScore(String text) {
        // Count the GI index searching the item in giIndexList
        if (text == null || text.isEmpty()) {
            // Need to modify with TextView
            Toast.makeText(this, "Cannot decide.", Toast.LENGTH_LONG).show();
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
        return giScore;
    }

    private void printGiResult(Integer giScore) {
        if (count == 0) {
            // Need to modify with TextView
            Toast.makeText(this, "Cannot decide.", Toast.LENGTH_LONG).show();
        } else {
            if (giScore < 55) {
                // Need to modify with TextView
                Toast.makeText(this, "Good because of the sum of GI is " + giScore + " of this food.", Toast.LENGTH_LONG).show();
            } else if (giScore < 69) {
                Toast.makeText(this, "Normal because of the sum of GI is " + giScore + " of this food.", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "Not recommended because of the sum of GI is " + giScore + " of this food.", Toast.LENGTH_LONG).show();
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == CropImage.CROP_IMAGE_ACTIVITY_REQUEST_CODE) {
            CropImage.ActivityResult result = CropImage.getActivityResult(data);
            if (resultCode == RESULT_OK) {
                Uri resultUri = result.getUri();
                try {
                    bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), resultUri);
                    getTextFromImage(bitmap);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private void getTextFromImage(Bitmap bitmap) {
        TextRecognizer recognizer = new TextRecognizer.Builder(this).build();
        if (!recognizer.isOperational()) {
            Toast.makeText(MainActivity.this, "Error Occurred!!", Toast.LENGTH_SHORT).show();
        } else {
            Frame frame = new Frame.Builder().setBitmap(bitmap).build();
            SparseArray<TextBlock> textBlockSparseArray = recognizer.detect(frame);
            StringBuilder stringBuilder = new StringBuilder();
            for (int i=0; i<textBlockSparseArray.size(); i++) {
                TextBlock textBlock = textBlockSparseArray.valueAt(i);
                stringBuilder.append(textBlock.getValue());
                stringBuilder.append("\n");
            }
            textview_data.setText(stringBuilder.toString());
            button_capture.setText("Retake");
            button_copy.setVisibility(View.VISIBLE);
        }
    }

    private void copyToClipBoard(String text) {
        ClipboardManager clipBoard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
        ClipData clip = ClipData.newPlainText("Copied data", text);
        clipBoard.setPrimaryClip(clip);
        Toast.makeText(MainActivity.this, "Copied to clipboard!", Toast.LENGTH_SHORT).show();
    }

    private Map<String, Integer> makeGiIndexList() {
        giIndexList = new HashMap<String, Integer>();
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
        giIndexList.put("glycyrrhizin",0);
        giIndexList.put("hf cs",63);
        giIndexList.put("hsh",3);
        giIndexList.put("honey",50);
        giIndexList.put("hf corn syrup",87);
        giIndexList.put("inulin",1);
        giIndexList.put("isomalt",2);
        giIndexList.put("isomaltitol",2);
        giIndexList.put("lactitol",6);
        giIndexList.put("lactose",46);
        giIndexList.put("lactulose",0);
        giIndexList.put("miraculin",0);
        giIndexList.put("monellin",0);
        giIndexList.put("maltose",105);
        giIndexList.put("molasses",55);
        giIndexList.put("maple syrup",54);
        giIndexList.put("mannitol",2);
        giIndexList.put("maltodextrin",110);
        giIndexList.put("neotame",0);
        giIndexList.put("pentadin",0);
        giIndexList.put("palatinose",2);
        giIndexList.put("sucralose",0);
        giIndexList.put("saccharin",0);
        giIndexList.put("stevia",0);
        giIndexList.put("sorghum",50);
        giIndexList.put("sorbitol",9);
        giIndexList.put("sucrose",63);
        giIndexList.put("thaumatin",0);
        giIndexList.put("tagatose",0);
        giIndexList.put("trehalose",70);
        giIndexList.put("table sugar",80);
        giIndexList.put("xylitol",10);
        giIndexList.put("corn syrup",75);

        return giIndexList;
    };
}