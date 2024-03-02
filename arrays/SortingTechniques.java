//bubble sort
public class Main
{
    void bubbleSort(int a[])
    {
        for(int i=0;i<a.length;i++)
        {
            for(int j=0;j<a.length-1-i;j++)
            {
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
    }
	public static void main(String[] args) {
	    int a[]={3,5,1,8,5,9,6};
	    Main b=new Main();
	    b.bubbleSort(a);
	    for(int i=0;i<a.length;i++){
	        System.out.print(a[i]+" ");
	    }
	}
}

//selection sort

class Main{
    public static void selection(){
        int a[]={5,4,6,7,3,8,2,1};
        for(int i=0;i<a.length;i++){
            int minpos=i;
            for(int j=i+1;j<a.length;j++){
                if(a[j]<a[minpos])
                minpos=j;
            }
            int temp=a[i];
            a[i]=a[minpos];
            a[minpos]=temp;
        }
        for(int i=0;i<a.length;i++)
        System.out.print(a[i]+" ");
    }
}


// insertion sort

class Main{
    public static void insertion(){
        int a[]={5,4,6,7,3,8,2,1};
        for(int i=0;i<a.length-1;i++){
            int j=i+1;
            while(j>0&&a[j]<a[j-1]){
                int temp=a[j];
                a[j]=a[j-1];
                a[j-1]=temp;
                j--;
            }
        }
        for(int i=0;i<a.length;i++)
        System.out.print(a[i]+" ");
    }
}
