#include <iostream>
#include <fstream>


using namespace std;


int inversion(int Arr[],int temp[], int l, int r);
int splitInv(int Arr[], int temp [],int left, int mid , int right);
  
int Inversion(int arr[], int array_size) 
{ 
    int temp[array_size]; 
    return inversion(arr, temp, 0, array_size - 1); 
} 

int inversion(int Arr[],int temp[], int l, int r){
    unsigned long long int inversion_count = 0;
    int mid;
    if (r > l) {
         int m = (l+r)/2;
         inversion_count += inversion(Arr, temp ,l, m);
         inversion_count += inversion(Arr, temp ,m+1, r);
         inversion_count += splitInv(Arr, temp, l, m+1 , r);

     }
        return inversion_count;

}

int splitInv(int Arr[], int temp [],int left, int mid , int right){

    int i,j,k;
    unsigned long long int inversion_count = 0;

    i = left;
    j = mid;
    k = left;

    while ((i<= mid-1) && (j <= right))
    {
        if(Arr[i] <= Arr[j]){
            temp[k++] = Arr[i++];

        }
        else
        {
            temp[k++] = Arr[j++];
            inversion_count = inversion_count+(mid-i);
        }

        
    }
    /* Copy the remaining elements of left subarray  
(if there are any) to temp*/
    while (i <= mid - 1) 
        temp[k++] = Arr[i++]; 
  
    /* Copy the remaining elements of right subarray  
(if there are any) to temp*/
    while (j <= right) 
        temp[k++] = Arr[j++]; 
  
    /*Copy back the merged elements to original array*/
    for (i = left; i <= right; i++) 
        Arr[i] = temp[i]; 
  
    return inversion_count; 

}
int main()
{   
   
      int data[100000];
    
     int n = sizeof(data) / sizeof(data[0]); 
     ifstream is("data.txt");
   
    int x;
    int cnt = 0;
    while (cnt <= n && is>>x)
    {
       
       data[cnt++] = x;
    }
   
    
//     cout<<"The integers are:"<<"\n";
//    for(int i = 0; i < n; i++)
//        cout<<data[i]<<endl;
       cout<< data[99999]<<endl;

    unsigned long long int ans = Inversion(data, n); 
    cout << " Number of inversions are " << ans<<endl; 
   
     is.close();     
    return 0;
}
