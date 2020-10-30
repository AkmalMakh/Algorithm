#include <iostream>
#include <vector> 
using namespace std;

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
void printArray(float A[], int size) 
{ 
    for(int i = 0; i < size; i++) 
        cout << A[i] << " "; 
        
    cout<<endl;    
} 
int main()
{
    float arr1[] = { 0.397, 0.55, 0.3256, 0.1134, 0.645, 0.434 };  
    int arr_size1 = sizeof(arr1) / sizeof(arr1[0]); 




    bucketSort(arr1,arr_size1); 
    printArray(arr1,arr_size1);

    return 0;
}