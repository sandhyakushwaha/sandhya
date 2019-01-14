import java.util.*;
public class OddEven 
{
    public static void main(String[] args) 
    {
        
      
      Scanner s=new Scanner(System.in);
      System.out.println("enter number");
      int n=s.nextInt();
      if(n<0)
      {
          System.out.println("Invalid");
      }
      else
          if(n%2==0)
              System.out.println("Even");
          else
              System.out.println("Odd");
    }
  
}
