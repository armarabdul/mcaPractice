async function fetchUserData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: 1, name: "John Doe", age: 25 });
        }, 2000);
    });
}

async function displayUserData() {
    try {
        let data = await fetchUserData();
        console.log(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

displayUserData();
