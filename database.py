import sqlite3 as sq
from data_pz_15 import *

with sq.connect('deanary.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS faculties (
        id_faculty INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS departments (
        id_departments INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        id_faculty INTEGER NOT NULL,
        FOREIGN KEY (id_faculty) REFERENCES faculties (id_faculty)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS specialities (
        id_speciality INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        id_departments INTEGER NOT NULL,
        FOREIGN KEY (id_departments) REFERENCES departments (id_departments)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS subjects (
        id_subject INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")
        
    cur.execute("""CREATE TABLE IF NOT EXISTS submission_form (
        id_submission_form INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS syllabus(
        id_syllabus INTEGER PRIMARY KEY AUTOINCREMENT,
        id_speciality INTEGER,
        id_subject INTEGER NOT NULL,
        id_submission_form INTEGER NOT NULL,
        number_of_lecture_hours INTEGER,
        number_of_practical_hours INTEGER,
        number_of_laboratory_hours INTEGER,
        course_work BOOL NOT NULL,
        FOREIGN KEY (id_speciality) REFERENCES specialities (id_speciality),
        FOREIGN KEY (id_subject) REFERENCES subjects (id_subject),
        FOREIGN KEY (id_submission_form) REFERENCES submission_form (id_submission_form)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS applicants (
        id_applicant INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT NOT NULL,
        name TEXT NOT NULL,
        patronymic TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        birthday DATETIME,
        address TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL,
        data_postupleniya DATETIME,
        speciality VARCHAR,
        FOREIGN KEY (speciality) REFERENCES specialities (name)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS study_card (
        id_study_card INTEGER PRIMARY KEY AUTOINCREMENT,
        FIO_student TEXT NOT NULL,
        groupp INTEGER NOT NULL,
        speciality TEXT NOT NULL,
        subjects TEXT NOT NULL,
        submission_form VARCHAR NOT NULL,
        grade INTEGER,
        FOREIGN KEY (subjects) REFERENCES subjects (name),
        FOREIGN KEY (submission_form) REFERENCES submission_form (name)
    )""")
    # cur.executemany("INSERT INTO faculties VALUES (?, ?)", info_faculties)
    # cur.executemany("INSERT INTO departments VALUES (?, ?, ?)", info_departments)
    # cur.executemany("INSERT INTO specialities VALUES (?, ?, ?)", info_specialities)
    # cur.executemany("INSERT INTO subjects VALUES (?, ?)", info_subjects)
    # cur.executemany("INSERT INTO submission_form VALUES (?, ?)", info_submission_form)
    # cur.executemany("INSERT INTO syllabus VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_syllabus)
    # cur.executemany("INSERT INTO applicants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", info_applicants)
    # cur.executemany("INSERT INTO study_card VALUES (?, ?, ?, ?, ?, ?, ?)", info_study_card)

    # # Запросы на выборку данных

    # # 1. Вывести список всех студентов, зачисленных на факультет, с указанием номера группы.
    # cur.execute("SELECT * FROM study_card")
    # all_students = cur.fetchall()
    # print(all_students)

    # # 2. Вывести список всех специальностей факультета и количество студентов, обучающихся по каждой из них.
    # cur.execute("""SELECT id_speciality, name, 
    # (SELECT COUNT(applicants.speciality) FROM applicants 
    # WHERE applicants.speciality = specialities.name) 
    # FROM specialities""")
    # spec_students = cur.fetchall()
    # print(spec_students)

    # # 3. Вывести список всех кафедр факультета и количество студентов, обучающихся на каждой кафедре.
    # cur.execute("""SELECT *, 
    # (SELECT (SELECT COUNT(applicants.speciality) FROM applicants 
    # WHERE applicants.speciality =specialities.name) FROM specialities
    # WHERE specialities.id_departments = departments.id_departments)
    # FROM departments
    # """)
    # deps_studs =  cur.fetchall()
    # print(deps_studs)

    # # 4. Вывести список всех предметов и количество часов, выделенных на каждый предмет в учебном плане каждой специальности.
    # cur.execute("""SELECT *, 
    # (SELECT (number_of_lecture_hours + number_of_practical_hours + number_of_laboratory_hours) 
    # FROM syllabus WHERE syllabus.id_subject = subjects.id_subject) 
    # FROM subjects
    # """)
    # print(cur.fetchall())

    # # 5. Вывести список всех студентов, у которых есть неудовлетворительные оценки (меньше 4) по любому предмету.
    # cur.execute("SELECT id_study_card, FIO_student, grade FROM study_card WHERE grade < 4")
    # print(cur.fetchall()) 

    # # 6. Вывести список всех предметов, которые изучают студенты первого курса.
    # cur.execute("SELECT * FROM study_card WHERE groupp LIKE '1%'")
    # print(cur.fetchall())

    # # 7. Вывести список всех студентов, которые сдают курсовую работу в этом семестре.
    # cur.execute("SELECT * FROM study_card WHERE submission_form = 'Курсовая работа'")
    # print(cur.fetchall())

    # # 8. Вывести список всех абитуриентов, зачисленных на специальность "Информатика и вычислительная техника".
    # # вместо специальности "Информатика и вычислительная техника" - "ИС"
    # cur.execute("SELECT * FROM applicants WHERE speciality = 'ИС'")
    # print(cur.fetchall())

    # # 9. Вывести список всех предметов, которые изучают студенты группы 101.
    # # вместо группы 101 - группа 11
    # cur.execute("SELECT subjects FROM study_card WHERE groupp = 11")
    # print(cur.fetchall())
    
    # # 10. Вывести список студентов и их оценки за все предметы на специальности "Программная инженерия"
    # # вместо программная инженерия - ПЛА
    # cur.execute("SELECT id_study_card, FIO_student, speciality, subjects, grade FROM study_card WHERE speciality = 'ПЛА'")
    # print(cur.fetchall())

    # SQL-запросы на обновление данных в БД:

    # Обновление названия факультета с id=1 на "Новый факультет"
    cur.execute("UPDATE faculties SET name = 'Новый факультет' WHERE id_faculty = 1") #1
    
    # Обновление названия кафедры с id=2 на "Новая кафедра"
    cur.execute("UPDATE departments SET name = 'Новая кафедра' WHERE id_departments = 2") #2
    
    # Обновление названия специальности с id=3 на "Новая специальность"
    cur.execute("UPDATE specialities SET name = 'Новая специальность' WHERE id_speciality = 3") #3
    
    # Обновление названия предмета с id=4 на "Новый предмет"
    cur.execute("UPDATE subjects SET name = 'Новый предмет' WHERE id_subject = 4") #4
    
    # Обновление названия формы сдачи предмета с id=5 на "Новая форма сдачи"
    cur.execute("UPDATE submission_form SET name = 'Новая форма сдачи' WHERE id_submission_form = 5") #5
    
    # Обновление количества лекционных часов на 30 для учебного плана с id=6
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 30  WHERE id_syllabus = 6") #6
    
    # Обновление количества лекционных часов у предмета "математика" на учебном плане специальности "ИБТ"
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 5 WHERE id_speciality = 2 AND id_subject = 3") #7
    
    # Обновление количества лабораторных часов и формы сдачи предмета у специальности "СА" для предмета "программирование"
    cur.execute("UPDATE syllabus SET number_of_laboratory_hours = number_of_laboratory_hours +10 WHERE id_speciality = 5 AND id_subject = 15") #8
    
    # # Обновление количества лекционных и практических часов у предмета "информатика" на учебном плане кафедры "Информационный"
    # cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 5, number_of_practical_hours = number_of_practical_hours + 5 WHERE id_subject = 20 AND  ") #9
    
    # Обновить кол-во лекционных часов для всех предметов, где количество лекционных часов больше 30
    cur.execute("UPDATE syllabus SET number_of_lecture_hours = number_of_lecture_hours + 10 WHERE number_of_lecture_hours > 30") #10
    
    # Обновить фамилию и имя абитуриента по его идентификатору
    cur.execute("UPDATE applicants SET name = 'Виктор' AND surname = 'Баранов' WHERE id_applicant = 7") #11
    
    #  Обновить название кафедры для всех специальностей, где кафедра имеет id = 1
    cur.execute("UPDATE departmens SET name = 'Кафедра' WHERE id_departments = 1") #12
    
    #Обновить оценку по определенному предмету и форме сдачи для конкретного студента
    cur.execute("UPDATE study_card SET grade = 5  WHERE submission_form = 'Взятка' AND FIO_student = 'Клименко Олег Юрьевич' ") #13
    
    # Обновить название специальности для всех студентов, где специальность имеет id = 2
    cur.execute("UPDATE study_card SET speciality = 'Специальность' WHERE speciality = (SELECT name FROM specialities WHERE id_speciality = 2)") #14
    
    # Обновить все оценки студента с именем "Иван" на предмете "Математика" на значение 5
    cur.execute("UPDATE study_card SET grade = 2  WHERE FIO_student LIKE 'Иван' AND subjects = 'математика' ") #15
    
    # Обновить название факультета на "Факультет информационных технологий" для всех кафедр, относящихся к этому факультету
    cur.execute("UPDATE SET WHERE") #16
    
    # . Обновить количество лабораторных часов на предмете "Физика" для специальности "Физика и информатика" на 30
    cur.execute("UPDATE SET WHERE") #17