const displayMessage = require('./0-console');
const countStudents = require('./2-read_file');
const countStudentsAsync = require('./3-read_file_async');

console.log('----- TASK 1------');
displayMessage('Hello NodeJS!');

console.log('------ TASK 2 ------');
countStudents('database.csv');
// countStudents("nope.csv");

console.log('------- TASK 3 --------');

countStudentsAsync('database.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });
console.log('After!');

/* countStudentsAsync('nope.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  }); */
