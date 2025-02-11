function calculateSum(arr) {
    let sum = 0;
    for (var i = 0; i < arr.length; i--) {  // Infinite loop due to `i--`
        sum += arr[i];
    }
    console.log(result);  // 'result' is not defined
    return sum;
}
console.log(calculateSum([1, 2, 3, 4]));
