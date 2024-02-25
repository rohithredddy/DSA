import java.util.Scanner;

class ReverseArray2pointer {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int a[] = new int[size];
        
        for (int i = 0; i < a.length; i++) {
            a[i] = sc.nextInt();
        }
        int temp; 
        int start=0;
        int end=a.length-1;
        while (start < end) 
        { 
            temp = arr[start]; 
            arr[start] = arr[end]; 
            arr[end] = temp; 
            start++; 
            end--; 
        } 
        for(int i=0;i<a.length;i++)
          System.out.print(a[i]+" ");
    }
}
