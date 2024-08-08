// JavaScript To-Do List Application

// Array to store tasks
let tasks = [];

// Function to add a task
function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();

    // Pattern matching to check if input is not empty
    if (taskText === '') {
        alert('Please enter a task.');
        return;
    }

    // Add task to array
    tasks.push({ text: taskText, completed: false });

    // Clear input field
    taskInput.value = '';

    // Render tasks
    renderTasks();
}

// Function to render tasks
function renderTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';

    // Loop through tasks array and create list items
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
            ${task.text}
            <button class="remove" onclick="removeTask(${index})">Remove</button>
        `;
        li.addEventListener('click', () => toggleTask(index));
        taskList.appendChild(li);
    });
}

// Function to toggle task completion
function toggleTask(index) {
    tasks[index].completed = !tasks[index].completed;
    renderTasks();
}

// Function to remove a task
function removeTask(index) {
    tasks.splice(index, 1);
    renderTasks();
}

// Example of using control statements
for (let i = 0; i < 3; i++) {
    console.log('Example control statement', i);
}
