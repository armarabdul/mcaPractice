function calculateSum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {  // Fixed infinite loop
        sum += arr[i];
    }
    console.log(sum);  // Fixed missing variable
    return sum;
}
console.log(calculateSum([1, 2, 3, 4]));
