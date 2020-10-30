
#include <iostream>
#include <vector> 
using namespace std;


// Merge Sort Algorith implementation
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

void printArray(float A[], int size) 
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



//// quick sort algorithm implementation 
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

// Counting Sort Algorithm Implementation 

void CountingSort(int ArrA[], int k,int s){ // int k -> is maximum value of array 

    int n = s; //size of array
    int ArrB[n];   
    int count[k];

    for(int i =0; i< k; i++) //initillizing to 0 
        count[i] = 0;

    for(int i =0;i<n;i++) // counting values and adding +1 
         ++count[ArrA[i]];
    
       
    for(int i=1; i<k;i++) // adding each number accumalativly 
        count[i] +=count[i-1];

    for(int i =n-1 ; i>=0 ; i--){  
        ArrB[count[ArrA[i]]-1] = ArrA[i];
        --count[ArrA[i]];
    }     
    
    for(int i = 0; i<n; i++)
        ArrA[i] = ArrB[i];



}
void bucketSort(float arr[], int n) 
{ 
    // 1) Create n empty buckets 
    vector<float> b[n]; 
  
    // 2) Put array elements in different buckets 
    for (int i = 0; i < n; i++) { 
        int bi = n * arr[i]; // Index in bucket 
        b[bi].push_back(arr[i]); 
    } 
  
    // 3) Sort individual buckets 
    for (int i = 0; i < n; i++) 
        sort(b[i].begin(), b[i].end()); 
  
    // 4) Concatenate all buckets into arr[] 
    int index = 0; 
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < b[i].size(); j++) 
            arr[index++] = b[i][j]; 
} 
int main()
{
   int arr []={4,5,3,7,5};  
   float arr1[] = { 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434 };  
   int arr_size1 = sizeof(arr1) / sizeof(arr1[0]); 
    int arr_size = sizeof(arr) / sizeof(arr[0]); 
   int n;
   
    
   
   do{
        cout<<"Choose sorting algorithm \n1: Merge Sort \n2: Heap Sort \n3: Quick Sort\n4: Counting Sort \n5: Bucket Sorting \n6: Print Array "<<endl;
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
                CountingSort(arr,8,arr_size);
                break;

           case 5:
               bucketSort(arr1,arr_size1); 
               break;
           case 6:
               printArray(arr1,arr_size);
                break;
           default:
             break;
       }
   }while(n!=0);
   
   
    
    return 0;
}
