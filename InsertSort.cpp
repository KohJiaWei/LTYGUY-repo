#include <iostream>

void insertSort(int arr[],int arrSize);

int main() {
    std::cout << "Hello World!\n";
    int arr[] = {10,90,30,40,50,60};
    int arrSize = sizeof(arr)/sizeof(arr[0]);
    insertSort(arr,arrSize);
    for(int i = 0 ; i< arrSize ; i++){
        printf("%d ",arr[i]);
    }
}
void insertSort(int arr[],int arrSize){
        int i,j; //using sizeof in function doesnt work
        int temp;
        for(int i = 1; i< arrSize;i++){
            for(int j = i; j>0 ; j--){
                if(arr[j-1] > arr[j]){
                    temp = arr[j];  //swap
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                }
                else{
                    break;
                }
            }
        }
    }