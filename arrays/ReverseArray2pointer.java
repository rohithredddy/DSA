import java.util.Scanner;

class ReverseArray2pointer {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int a[] = new int[size];
        
        for (int i = 0; i < a.length; i++) {
            a[i] = sc.nextInt();
        }

        int start=0;
        int end=a.length-1;
        int temp; 
        while (start < end) 
        { 
            temp = a[start]; 
            a[start] = a[end]; 
            a[end] = temp; 
        } 
        for(int i=0;i<a.length;i++)
          System.out.print(a[i]+" ");
    }

}



