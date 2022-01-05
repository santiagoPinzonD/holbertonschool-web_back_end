const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase('database.csv')
      .then((v) => {
        response.writeHead(200);
        response.write(`Number of students: ${v.counter}\n`);
        let len = 0;
        for (const key in v.inFields) {
          if (Object.prototype.hasOwnProperty.call(v.inFields, key)) {
            response.write(`Number of students in ${key}: ${v.inFields[key].counter}. List: ${v.inFields[key].students}`);
            if (len !== Object.keys(v.inFields).length - 1) response.write('\n');
            len += 1;
          }
        }
        response.end();
      })
      .catch(() => response.end('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    if (request.params.major === 'CS' || request.params.major === 'SWE') {
      readDatabase('database.csv')
        .then((v) => {
          response.status(200).send(`List: ${v.inFields[request.params.major].students}`);
        })
        .catch(() => response.status(500).send('Cannot load the database'));
    } else {
      response.status(500).send('Major parameter must be CS or SWE');
    }
  }
}

module.exports = StudentsController;
