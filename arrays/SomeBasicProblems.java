// right rightRotate
import java.util.*;
public class Main
{
  public static void rightRotate (int a[], int k)
  {
	for (int j = 0; j < k; j++)
	  {
		int temp = a[a.length - 1];
		for (int i = a.length - 2; i >= 0; i--)
		  {
			a[i + 1] = a[i];
		  }
		a[0] = temp;
  }}
  public static void main (String[]args)
  {
	Scanner s = new Scanner (System.in);
	int n = s.nextInt ();
	int a[] = new int[n];
	for (int i = 0; i < n; i++)
	  {
		a[i] = s.nextInt ();

	  }
	int k = s.nextInt ();
	Main.rightRotate (a, k);
	for (int i = 0; i < n; i++)
	  {
		System.out.print (a[i] + " ");

	  }
  }
}

// right rotate array 
import java.util.*;
class Main
{
  public static void reverse (int a[], int left, int right)
  {
	while (left < right)
	  {
		int temp = a[left];
		  a[left] = a[right];
		  a[right] = temp;
		  left++;
		  right--;
	  }


  }
  public static void rightRotate (int a[], int k)
  {
	int n = a.length;
	reverse (a, 0, n - k - 1);
	reverse (a, n - k, n - 1);
	reverse (a, 0, n - 1);
	for (int i = 0; i < n; i++)
	  {
		System.out.print (a[i] + " ");
	  }
  }
  public static void main (String[]args)
  {
	Scanner s = new Scanner (System.in);
	int n = s.nextInt ();
	int a[] = new int[n];
	for (int i = 0; i < n; i++)
	  {
		a[i] = s.nextInt ();

	  }
	int k = s.nextInt ();
	rightRotate (a, k);
  }
}

// left rotate array
import java.util.*;
class Main
{
  public static void reverse (int a[], int left, int right)
  {
	while (left < right)
	  {
		int temp = a[left];
		  a[left] = a[right];
		  a[right] = temp;
		  left++;
		  right--;
	  }


  }
  public static void rightRotate (int a[], int k)
  {
	int n = a.length;
	reverse (a, 0, k - 1);
	reverse (a, k, n - 1);
	reverse (a, 0, n - 1);
	for (int i = 0; i < n; i++)
	  {
		System.out.print (a[i] + " ");
	  }
  }
  public static void main (String[]args)
  {
	Scanner s = new Scanner (System.in);
	int n = s.nextInt ();
	int a[] = new int[n];
	for (int i = 0; i < n; i++)
	  {
		a[i] = s.nextInt ();

	  }
	int k = s.nextInt ();
	rightRotate (a, k);
  }
}

// find the unique element
import java.util.*;
class Main
{
  public static void unique (int a[], int n)
  {
	int xor = 0;
	  Arrays.sort (a);
	for (int i = 0; i < n; i++)
	  {
		xor = xor ^ a[i];

	  }
	System.out.println (xor);
  }
  public static void main (String[]args)
  {
	Scanner s = new Scanner (System.in);
	int n = s.nextInt ();
	int a[] = new int[n];
	for (int i = 0; i < n; i++)
	  {
		a[i] = s.nextInt ();

	  }

	unique (a, n);
  }
}


//find the emissing element 0 to n
import java.util.*;
class Main{
    public static void findele(int a[],int n)
    {
        int xor=a.length;
        for(int i=0;i<n;i++)
        {
            xor=xor^a[i]^i;
            
        }
        System.out.println(xor);
    }
    public static void main(String[] args)
    {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
        {
            a[i]=s.nextInt();
            
        }
        findele(a,n);
    }
}

// find missing element from 1 to n+1
import java.util.*;
class Main
{
  public static void findelement (int a[], int n)
  {
	int temp = n + 1;
	int sum = (temp * (temp + 1)) / 2;
	int sum1 = 0;
	for (int i = 0; i < n; i++)
	  {
		sum1 += a[i];

	  }

	System.out.println (sum - sum1);
  }
  public static void main (String[]args)
  {
	Scanner s = new Scanner (System.in);
	int n = s.nextInt ();
	int a[] = new int[n];
	for (int i = 0; i < n; i++)
	  {
		a[i] = s.nextInt ();

	  }
	findelement (a, n);
  }

}

