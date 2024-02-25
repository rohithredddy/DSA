import java.util.Scanner;

class Reversearray {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int a[] = new int[size];
        
        for (int i = 0; i < a.length; i++) {
            a[i] = sc.nextInt();
        }

        int k = 0;
        int b[] = new int[a.length];
        
        for (int i = a.length - 1; i >= 0; i--) {
            b[k] = a[i];
            k++;
        }

        for (int i = 0; i < b.length; i++) {
            a[i] = b[i];
        }

        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
