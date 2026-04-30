
#include<stdio.h>
void main()
{
    int arr[]={10,20,30,40,50};
    int n=5, key=30, low=0, high=n-1, mid;
int found=0;
     while(low<=high)
     {
       mid=(low+high)/2;
       if(arr[mid]==key)
       {
	printf("Found at %d\n",mid);
	found=1;
	break;
       }
       else if(arr[mid]<key)
       low=mid+1;
       else high=mid-1;
     }
     if(!found)
     printf("Not found\n");
     getch();
}