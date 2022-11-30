"""Server for movie ratings app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)


# SELECT *
# FROM students
#     JOIN grades ON (students.github = grades.student_github);


#  SELECT students.first_name,
#        students.last_name,
#        grades.project_title,
#        grades.grade
# FROM students
# JOIN grades ON (students.github = grades.student_github);
   

# SELECT *
# FROM students
#   JOIN grades ON (students.github = grades.student_github)
#   JOIN projects ON (grades.project_title = projects.title);