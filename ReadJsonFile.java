package com.hitech51.bigdata.scenemanager.restapi;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Iterator;

public class ReadJsonFile {
    public static void main(String[] args) {
        JSONObject TestEsMetaData = new JSONObject();
        InputStream inputStream = Test.class.getResourceAsStream("/TestMetaData.json");
        BufferedReader reader = new BufferedReader (new InputStreamReader(inputStream));
        try {
            StringBuilder tmp = new StringBuilder();
            String line = null;
            while((line = reader.readLine()) != null){
                tmp.append(line);
            }
            TestEsMetaData = JSONObject.parseObject(tmp.toString());
//            System.out.println("TestEsMetaData : "+TestEsMetaData);
            Iterator iter = TestEsMetaData.keySet().iterator();
            while(iter.hasNext()){
                String key  = iter.next().toString();

                System.out.println("============key : "+key);
                System.out.println(TestEsMetaData.get(key).getClass().getName());


                Object value = TestEsMetaData.get(key);
//                System.out.println(value);
                if (value.getClass().equals(JSONArray.class)){
                    for(int i = 0; i < ((JSONArray) value).size(); i++){
                        JSONObject jsonObject = ((JSONArray) value).getJSONObject(i);
                        if (jsonObject.containsKey("Level1")){
                            System.out.println("===============================");

                        }
                        Iterator arrayIter = jsonObject.keySet().iterator();
                        while(arrayIter.hasNext()){
                            String arraykey  = arrayIter.next().toString();
                            Object arrayvalue  = jsonObject.get(arraykey);
                            if (arrayvalue.getClass().equals(JSONArray.class)){
                                for(int ii = 0; ii < ((JSONArray) arrayvalue).size(); ii++){
                                    String s = ((JSONArray) arrayvalue).getString(ii);
                                    System.out.println("arraykey : " + arraykey + ", arrayvalue : "+ s+"\n");
                                }
                            }else{
//                                System.out.println("arrayvalue type: "+ arrayvalue.getClass().getName()+"\n");
                                if (!arrayvalue.getClass().equals(String.class) || arrayvalue.toString().equals("any"))
                                    continue;
                                System.out.println("arraykey : " + arraykey + ", arrayvalue : "+ arrayvalue+"\n");

                            }
                        }
                    }
                } else if (value.getClass().equals(String.class)) {
                    System.out.println(value);
                } else if (value.getClass().equals(Integer.class)) {
                    System.out.println(value);
                }
            }
        }catch (Exception e){
        }
    }
}
