
#include <iostream>

using namespace std;



void Merge(int A[], int start,int middle,int end){
    
    int n1 = middle-start+1; // plus 1 because our array starts from 0 
    int n2 = end-middle; 
   
    int L[n1], R[n2];  // dividing into 2 parts our array
    
    for(int i = 0; i < n1; i++) // copping 
        L[i] = A[start + i]; 
    for(int j = 0; j < n2; j++) 
        R[j] = A[middle + 1 + j]; 
        
    int i = 0, j= 0;
         
    int k = start; 
    
    while(i< n1 && j< n2){  //n1 is middle-start+1 while n2 is end-middle
        if(L[i]<=R[j]){
            A[k++]= L[i++]; 
        }else{
            A[k++] = R[j++];
        }
        
        
    }
    while(i<n1){
            A[k++] = L[i++];
        }
        while(j<n2){
            A[k++] = R[j++];
        }
    
}

void printArray(int A[], int size) 
{ 
    for(int i = 0; i < size; i++) 
        cout << A[i] << " "; 
        
    cout<<endl;    
} 

void MergeSort(int arr[],int start,int end){
    if(start<end){
        int middle = start+(end-start)/2; // dividing into 2 part our array
        
        MergeSort(arr,start,middle); //sorting left side  
        MergeSort(arr,middle+1,end); //sorting right side 
        
        Merge(arr,start,middle,end);
    }
    
}


void swap(int a, int b){
    int  temp=a;
    a = b;
    b = temp;
    
}

int patrition (int Arr[], int l, int r){
    int pivot = Arr[r];
    int i  = l-1; // i starts from -1
    
    for(int j=l; j<r; j++){ // j starts from begining to before pivot as pivot is last index
        if(Arr[j]<pivot){
            i++;
            int temp = Arr[i];
                Arr[i] = Arr[j];
                Arr[j] = temp;
        }
        
        
    }    
     int temp = Arr[i + 1];
        Arr[i + 1] = Arr[r];
        Arr[r] = temp;
    return i+1;
}

void QuickSort(int Arr[], int l, int r){
    if(r<=l){
        return;
      }
      int p =  patrition(Arr, l, r);
      QuickSort(Arr, l, p-1);  //left side of patrition
      QuickSort(Arr,p+1,r );    // right side of patrition 
   
}



int main()
{
   int arr []={4,2,3,7,5};   
    int arr_size = sizeof(arr) / sizeof(arr[0]); 
   int n;
   
    
   
   do{
        cout<<"Choose sorting algorithm 1: Merge Sort \n2: Heap Sort \n3: Quick Sort\n4: Print Array "<<endl;
        cin>>n;
       switch(n){
           
           case 1: // merge sorting nlogn 
                MergeSort(arr,0,arr_size-1);
                break;
           case 2: //Heap sorting  nlogn
                break;
           case 3: //quick sorting nlogn best one 
                
                QuickSort(arr, 0, arr_size-1);
                break;
           case 4: 
                printArray(arr,arr_size);
                break;
           default:
             break;
       }
   }while(n!=0);
   
   
    
    return 0;
}
