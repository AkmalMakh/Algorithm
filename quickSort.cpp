#include <iostream>
#include <fstream>

using namespace std;

int comp=0;
int max(int a, int b){
    return a>b ? a : b;  
}
int min(int a, int b){
    return a<b ? a : b;  
}
int median_of_3(int num[], int low, int high, int medium) {
 
	if (num[low] > max(num[medium], num[high])) {
		if (num[medium] > num[high])
			return medium;
		else
			return high;
	}
	else if (num[low] < min(num[medium], num[high])) {
		if (num[medium] > num[high])
			return high;
		else
			return medium;
	}
	else
		return low; 
}
int partitionM(int num[], int low, int high) {
 
	int index = median_of_3(num, low, high, (low+high)/2);
	int pivot = num[index];
	swap(num[low], num[index]);
	int i = low + 1;
	int j;
	for (j = low + 1; j <= high; ++j) {
		if (num[j] < pivot) {
			swap(num[i], num[j]);
			++i;
		}
        
		/* else do nothing */
	}
	swap(num[i-1], num[low]);
	return (i-1);
}
 


// int PartitionWithFirst(int Arry[] ,int left, int right){
//     int pivot = Arry[left];
//     int i  = left+1;
    
//     for (int j = left+1; j <= right; j++){
        
//         if(Arry[j]<pivot){
//             int temp  = Arry[i];
//                 Arry[i] = Arry[j];
//                 Arry[j] = temp; 
//                 i++;
//         }comp++;
//     }

//     int temp = Arry[i - 1];
//         Arry[i - 1] = Arry[left];
//         Arry[left] = temp;
//     return (i-1);
// }
// void swap(int* a, int* b)  
// {  
//     int t = *a;  
//     *a = *b;  
//     *b = t;  
// } 
// int PartitionWithLast(int Arry[], int left,int right){
//     swap(&Arry[left],&Arry[right]);
// int pivot = Arry[left]; // pivot  
//     int i = left + 1; // Index of smaller element  
   
//      for (int j = left+1; j <= right; j++){
        
//         if(Arry[j]<pivot){
//             int temp  = Arry[i];
//                 Arry[i] = Arry[j];
//                 Arry[j] = temp; 
//                 i++;
//         }comp++;
//     }

//     int temp = Arry[i - 1];
//         Arry[i - 1] = Arry[left];
//         Arry[left] = temp;
//     return (i-1);
// }

// void QuickSortLast(int Arr[], int l, int r){
//     if(r<=l)
//         return ;
  
//     int p = PartitionWithLast(Arr, l, r);
//     QuickSortLast(Arr, l, p-1);
//      QuickSortLast(Arr, p+1, r);
    
  
// } 

// void QuickSort(int Arr[], int l, int r){
//     if(r>l)
        
// {
//     int p = PartitionWithFirst(Arr, l, r);
//     QuickSort(Arr, l, p-1);
//     QuickSort(Arr, p+1, r);
//  }
// } 

void QuickSortM(int Arr[], int l, int r){
    if(r<=l)
        return;
    comp += r - l;
    int p = partitionM(Arr, l, r);
    QuickSortM(Arr, l, p-1);
    QuickSortM(Arr, p+1, r);
} 

void printArray(int A[], int size) 
{  
    for(int i = 0; i < size; i++) {
        cout << A[i] <<" "; 
        }
        
    cout<<endl;    
} 
int main()
{

int data[10000];
int n = sizeof(data) / sizeof(data[0]); 
ifstream is("data2.txt");
    int x;
    int cnt = 0;

    while (cnt <= n && is>>x)
    {
       
       data[cnt++] = x;
    }



 //QuickSortLast(data, 0, n-1);  
//first element as partition 162085
//last element as partition  164123
//QuickSortM(data,0,n-1); 138382

QuickSortM(data, 0, n-1);
cout<< comp<<endl;


//  is.close();

    return 0;
}