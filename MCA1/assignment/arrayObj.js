const students = [
    { name: "Ali", marks: 85 },
    { name: "Sara", marks: 92 },
    { name: "John", marks: 92 },
    { name: "Aisha", marks: 88 }
];

function findTopStudents(students) {
    let maxMarks = Math.max(...students.map(student => student.marks));
    let topStudents = students.filter(student => student.marks === maxMarks);
    
    return `Highest scoring students: ${topStudents.map(s => s.name).join(", ")} (${maxMarks} marks)`;
}

console.log(findTopStudents(students));
