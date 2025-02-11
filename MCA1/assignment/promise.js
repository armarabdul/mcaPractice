function fetchUserData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: 1, name: "John Doe", age: 25 });
        }, 2000);
    });
}

fetchUserData().then(data => console.log(data));
