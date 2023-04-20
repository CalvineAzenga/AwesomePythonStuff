import sqlite3
from datetime import datetime

tablesSql = '''
CREATE TABLE userAdmin(idd int AUTO INCREMENT,userNamee VARCHAR(55) PRIMARY KEY, passWordd VARCHAR(500));
CREATE TABLE studentz(regNo VARCHAR(55) PRIMARY KEY,fullName VARCHAR(100),department VARCHAR(100), course VARCHAR(100),admYear VARCHAR(50),semester VARCHAR(55),gender VARCHAR(40),phoneNum VARCHAR(100),address VARCHAR(100),rollno VARCHAR(55), email VARCHAR(100), guardian VARCHAR(100));
CREATE TABLE unitZ(unitCode VARCHAR(20) PRIMARY KEY);
CREATE TABLE attendanceSheet(dateTimeOfAttendance VARCHAR(55), unitCode VARCHAR(20),regNo VARCHAR(55));
'''


class CreateDbTables:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("./database/faceRecDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.executescript(tablesSql)
        self.conn.commit()


class DbConnection:
    def __init__(self) -> None:
        try:
            CreateDbTables()
        except:
            pass
        self.conn = sqlite3.connect("./database/faceRecDB.db")
        self.cursor = self.conn.cursor()

    def addStudent(self, ID, Name, Dep, Course, Year, Sem, Gender, MobNo, Address, RollNo, Email, Guardian):
        self.cursor.execute("INSERT INTO studentz VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                            (
                                str(ID).upper(),
                                Name,
                                Dep,
                                Course,
                                Year,
                                Sem,
                                Gender,
                                MobNo,
                                Address,
                                RollNo,
                                Email,
                                Guardian
                            ))
        self.conn.commit()

    def addAdmin(self):
        pass

    def addCourseUnit(self):
        pass

    def addAttendance(self, regNo):
        results = self.cursor.execute("SELECT * FROM attendanceSheet WHERE regNo=? AND dateTimeOfAttendance=?",
                                      (str(regNo).upper(), str(datetime.now()).split(" ")[0]))
        rows = results.fetchall()
        if len(rows) < 1:
            self.cursor.execute("INSERT INTO attendanceSheet VALUES(?,?,?)",
                                (str(datetime.now()).split(" ")[0], "NULL", str(regNo).upper()))
            self.conn.commit()
            return True
        else:
            return False

    def deleteAttendace(self):

        self.cursor.execute("DELETE FROM attendanceSheet")
        self.conn.commit()

    def delete(self, regNo):

        self.cursor.execute("DELETE FROM studentz where regNo=?", (str(regNo).upper(),))
        self.conn.commit()


class DbRetrieve:
    def __init__(self) -> None:
        try:
            CreateDbTables()
        except:
            pass
        self.conn = sqlite3.connect("./database/faceRecDB.db")
        self.cursor = self.conn.cursor()

    def getFullAttendance(self, date):
        pass

    def getAllStudents(self):
        self.cursor.execute("SELECT * FROM studentz")
        results = self.cursor.fetchall()
        self.conn.commit()
        return results

    def send2Csv(self):
        self.cursor.execute("SELECT regNo FROM attendanceSheet WHERE dateTimeOfAttendance=?",
                            (str(datetime.now()).split(" ")[0],))
        results = self.cursor.fetchall()
        file = open("todayAtt.csv", 'w')
        for att in results:
            file.write(str(att[0]) + "\n")

        file.close()

    def searchStudenWithRegNo(self, RegNo):
        self.cursor.execute("SELECT * FROM studentz WHERE regNo=?", (RegNo,))
        results = self.cursor.fetchall()
        self.conn.commit()
        return results

    def getTreeviewData(self):
        self.cursor.execute("SELECT regNo FROM attendanceSheet WHERE dateTimeOfAttendance=?",
                            (str(datetime.now()).split(" ")[0],))
        results = self.cursor.fetchall()
        resultList = []
        for regNo in results:
            self.cursor.execute("SELECT fullname,regNo,course,department,gender FROM studentz WHERE regNo=?",
                                (str(regNo[0]),))
            result = self.cursor.fetchone()
            resultList.append(result)
        self.conn.commit()
        return resultList

    def getCountAttendanceToday(self):
        self.cursor.execute("SELECT count(*) FROM attendanceSheet WHERE dateTimeOfAttendance=?",
                            (str(datetime.now()).split(" ")[0],))
        answer = self.cursor.fetchall()[0][0]
        self.conn.commit()
        return answer

    def getIndividualAttendance(self, regNo, unitCode=None):
        pass

    def fillRecognitionData(self, regNo):
        self.cursor.execute("SELECT fullname,course,regNo,phoneNum,gender,department FROM studentz WHERE regNo=?",
                            (regNo,))
        results = self.cursor.fetchall()
        self.conn.commit()
        return results


# dbconn = DbConnection()
# dbconn.deleteAttendace()
