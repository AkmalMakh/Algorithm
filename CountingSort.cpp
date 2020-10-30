#include <iostream>
#include <fstream>
#include <string>

#include <typeinfo>
using namespace std;
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

int main()
{
     ifstream MyReadFile("data.txt");
     int i=0,j=0; //size of array


     string word;
     while (MyReadFile >> word)   i++; // 
     int arr[i];
      while (MyReadFile >> word)   {
        
        int m = stoi(word);
        arr[j++] = m;
        cout<<m<<" ";
     }
   
    //  for(int n =0;n<i;n++){
    //      cout<<arr[n]<< " ";
    //  }

    return 0;
}