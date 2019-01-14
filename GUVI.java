/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package guvi;
import java.util.*;

/**
 *
 * @author SANDHYA KUSHWAHA
 */
public class GUVI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        Scanner s=new Scanner(System.in);
        System.out.println("enter the number");
        int n=s.nextInt();
        
        if(n==0)
        {
            System.out.println("Zero");
                    
        }
        else if (n>0)
        {
            System.out.println("Positive");
            
        }
        else
            System.out.println("Negative");
        // TODO code application logic here
    }
    
}
