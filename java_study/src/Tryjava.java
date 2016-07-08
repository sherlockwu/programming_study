/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author sherlock
 */

import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.lang.Math;

public class Tryjava {
    String string_1;
    int int_1;
    
    Tryjava(String string_1, int int_1){
        this.string_1 = string_1;
        this.int_1 = int_1; 
        
    }
    
    void display(){
        String tmp = String.valueOf(int_1);
        System.out.print(string_1 + "\n" + tmp +"\n\n");
    }
    
    void change(){
        this.int_1 = 0; 
    }
    
    
    public static void main(String[] args){
        System.out.print("please input a string and a integer \n");
        Scanner scanner = new Scanner(System.in);
        String string_1 = scanner.next();
        int int_1 = scanner.nextInt();
        
        // 类 
        Tryjava just_try = new Tryjava(string_1, int_1); 
        Tryjava try_2 = just_try;         
        // change
        try_2.change();
        
        // display 
        just_try.display();
        try_2.display();
        /*
        System.out.print("please input number of randoms you need: \n");
               
        Scanner scanner = new Scanner(System.in);
        String tmp = scanner.next();
        int tmp_up;
        
        
        tmp_up = Integer.parseInt(tmp);
        
        // try object 
        
        // initial 
        Person tmp_p = new Person("KanWu", 20);
        // output 
        System.out.println("hello "+tmp_p.name+". happy "+tmp_p.age+" birthday");
        */
        
        
        /*
        int[] flag;
        flag = new int[tmp_up+1];
        
        int[] ans;
        ans = new int[tmp_up];
             
        for (int i = 0; i< ans.length; i++){
           int tmp_res;
           // search 
           do{
               tmp_res = (int)(Math.random() * tmp_up) +1;
           } while (flag[tmp_res] == 1);
           ans[i] = tmp_res;    
           flag[tmp_res] = 1;
           
           
        }
        for ( int j:ans ){
            System.out.printf("%5d", j);
        }
        */
        
        /*
        switch(tmp){
            case "hello":
                System.out.println("hello, too");
                break;
            case "bye":
                System.out.println("Byebye");
                break;
            default: 
                System.out.println("I cann't understand!");
                break; 
        }
        /*
        try{
            BufferedReader tmpin = new BufferedReader(new InputStreamReader(System.in) );  
            String s = tmpin.readLine();
            System.out.println(s);
        } catch (IOException e) {}
        
        char tmp1; 
        tmp1 = 't';
        
        Boolean tmp2; 
        tmp2 = true; 
        
        System.out.println("你好,第"+tmp2+"号用户");
        
        System.out.println(new java.util.Date());
       
        
        new Appframe();
        */        
    }
}
/*
class Appframe extends JFrame {
    JTextField in = new JTextField(10);
    JButton btn = new JButton("求平方");
    JLabel out = new JLabel("结果:");
   
   
    public Appframe(){
        setLayout(new FlowLayout() );
        setSize(400,350);
        add(in);
        add(btn);
        add(out);
        btn.addActionListener (e -> {
            String s = in.getText();
            double tmp = Double.parseDouble(s);
            tmp = tmp * tmp; 
            out.setText("结果: " + tmp );
        });
        setVisible( true );
    }
     
}

*/


// try class 
class Person{
    String name;
    int age;
    
    Person(String name_input, int age_input){
        name = name_input;
        age = age_input; 
    }
    
}