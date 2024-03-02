
class Main
{
	public static void main(String[] args)
	{
	int a[]={4,4,4,1,2};
	int votes=0;
	int maj=-1;
	int count=0;
	for(int i=0;i<a.length;i++)
	{
	    if(votes==0)
	    {
	        maj=a[i];
	        votes=1;
	    }
	    else
	    {
	        if(a[i]==maj)
	        votes++;
	        else
	        votes--;
	    }
	}
	for(int i=0;i<a.length;i++)
	{
	 if (a[i]==maj)  
	 count++;
	}
	 if(count>a.length/2)
	 System.out.println(maj);
	 else
	 System.out.println(-1);
	}
}
