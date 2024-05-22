function updateStudentGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students)) {
      return [];
    }
    if (!Array.isArray(newGrades)) {
      return [];
    }

    const stCity = students.filter((student) => student.location === city);

    const studentsGraded = stCity.map((student) => {
      const gradeObj = newGrades.find((newGrade) => newGrade.studentId === student.id);
      const grade = gradeObj ? gradeObj.grade : 'N/A';

      return {
        ...student,
        grade,
      };
    });

    return studentsGraded;
  }

  export default updateStudentGradeByCity;
