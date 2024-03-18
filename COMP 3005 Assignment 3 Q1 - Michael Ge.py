import psycopg2
from psycopg2 import OperationalError

def createConnection(dbName, dbUser, dbPassword, dbHost, dbPort):
    connection = None
    try:
        connection = psycopg2.connect(
            database=dbName,
            user=dbUser,
            password=dbPassword,
            host=dbHost,
            port=dbPort,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def getAllStudents():
    return "SELECT * FROM students;"

def addStudent(firstName, lastName, email, enrollmentDate):
    return """
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES 
        ('{}', '{}', '{}', '{}')""".format(firstName, lastName, email, enrollmentDate)

def updateStudentEmail(studentId, newEmail):
    return """
        UPDATE students SET email = '{}' WHERE student_id = '{}'
        """.format(newEmail, studentId)

def deleteStudent(studentId):
    return """
        DELETE FROM students WHERE student_id = '{}'
        """.format(studentId)

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")

        if(query.find("SELECT") != -1):
            result = cursor.fetchall()
            return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def getInput():
    print("Input a number to select an option:")
    print("1. Print all students")
    print("2. Add a new student")
    print("3. Update a student's email")
    print("4. Delete a student")
    print()
    print("0. Exit")

    try:
        intput = int(input())

        while(intput < 0 or intput > 4):
            print("Invalid input. Please try again.")
            intput = int(input())
        
        return intput

    except ValueError:
        print("Input should be an integer. Please try again.")
        return getInput()

def main():
    connection = createConnection("students", "postgres", "tent6squad", "127.0.0.1", "5432")

    option = getInput()
    while(option != 0):
        match option:
            case 1:
                table = executeQuery(connection, getAllStudents())
                for row in table:
                    print(row)
            
            case 2:
                print("Enter the new student's first name:")
                firstName = input()
                print("Enter the new student's last name:")
                lastName = input()
                print("Enter the new student's email:")
                email = input()
                print("Enter the new student's enrollment date:")
                enrollmentDate = input()
                executeQuery(connection, addStudent(firstName, lastName, email, enrollmentDate))
            
            case 3:
                print("Enter the student's id to update:")
                studentId = input()
                print("Enter the student's new email:")
                newEmail = input()
                executeQuery(connection, updateStudentEmail(studentId, newEmail))
            
            case 4:
                print("Enter the student's id to delete:")
                studentId = input()
                executeQuery(connection, deleteStudent(studentId))
        
        option = getInput()
    
    print("Program exited.")

if __name__ == "__main__":
    main()