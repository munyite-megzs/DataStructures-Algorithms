/**
 * First Problem Statement: Given an array, we have to find the largest element in the array.

 

Examples

Plain Text
Example 1:Input: arr[] = {2,5,1,3,0};Output: 5Explanation: 5 is the largest element in the array. 
Example2:Input: arr[] = {8,10,5,7,9};Output: 10Explanation: 10 is the largest element in the array.
 */


function findLargest(arr){

    if(arr.length===0){
        return -1
    }else{
 return Math.max(...arr);
    }
}

//test
let array=[2,5,1,3,0]
let num=findLargest(array)
console.log(num)