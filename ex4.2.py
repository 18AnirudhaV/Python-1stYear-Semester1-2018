'''
Amirdha Verma - 20128760

CISC 121 Exercise 4
'''

'''
Program 2
'''

import json

'''FUNCTIONS'''

'''
Finds the class average for a single gradeable item.
The first parameter is a str representing the gradeable item;
the second is a list of student data for the class.
Returns the average as a float.
'''
def average_on_gradeable (gradeable_item, student_data):
	sum = 0.0
	for i in range(len(student_data)):
		'''
		Handle the case where gradeable_item doesn't match any of
		the items in the student_data (possibly owing to a typo).
		'''
		try:
			# sum = student_data[i].get('grades').get('gradeable_item') -- Original
			sum += student_data[i].get('grades').get(gradeable_item)
		except TypeError:
			print ('"' + gradeable_item + '" missing from grades data.')
	'''
	Catch the division by zero exception caused if student_data
	is an empty list (of length 0, implying no students).
	'''
	try:
		return sum / len(student_data)
	except:
		return 0.0

'''
Extract the gradeables used in the student data.
The parameter is the list of student data for the class.
Returns a list comprising the gradeables.
'''
def get_gradeables_list (student_data):
	'''
	Catch the index out of bounds error that would occur on trying
	to access student_data[0] if	student_data is an empty list.
	'''
	try:
		return [*student_data[0].get('grades')]
	except:
		return []

'''
Extract a list of students and their IDs from the student data.
The parameter is the list of student data for the class.
Returns a list of student IDs and names.
'''
def get_class_list (student_data):
	# class_list = {} -- Original
	class_list = []
	for i in range(len(student_data)):
		s = student_data[i]
		s_info = str(s.get('id')) + ': ' + s.get('surname') + ', ' + s.get('given_names')
		class_list.append(s_info)
	return class_list

'''
Puts together a report, including grades, for a particular student.
The first parameter is an int representing the id of the student.
The second is the list of student data. The third is a dictionary of
gradeables and their weights (each a fraction of 1.0).
Returns a str representing the report or, in the case where no such
student ID exists, an indication that the student ID is invalid.
'''
def get_student_report (student_id, student_data, weights_data):
	report = ''
	i = 0

	# [Not there before] -- Created
	found = False
	while not found and i < len(student_data):
		if student_id in student_data[i].values():
			found = True
			course_total = 0.0
			report += 'ID: ' + str(student_data[i].get('id')) + '\n'
			report += 'Name: ' + student_data[i].get('surname') + ', ' + student_data[i].get('given_names') + '\n'
			for key in student_data[i].get('grades'):
				report += key + ': ' + str(student_data[i].get('grades').get(key)) + '\n'
				course_total += student_data[i].get('grades').get(key) * weights_data.get(key)
			report += 'course total: ' + str(course_total)
		i += 1
	if not found:
		report = 'Invalid student ID: ' + str(student_id) + '.'

	# [Not there before] -- Created
	return report

'''
Puts together a collection of reports, including grades, for all students.
The first parameter is the list of student data. The second is a dictionary of
gradeables and their weights (each a fraction of 1.0).
Returns a (possibly empty) list of reports, each of which is a str.
'''
def get_all_student_reports (student_data, weights_data):
	reports_list = []
	for i in range(len(student_data)):
			report = ''
			course_total = 0.0
			report += 'ID: ' + str(student_data[i].get('id')) + '\n'
			report += 'Name: ' + student_data[i].get('surname') + ', ' + student_data[i].get('given_names') + '\n'
			for key in student_data[i].get('grades'):
				report += key + ': ' + str(student_data[i].get('grades').get(key)) + '\n'
				course_total += student_data[i].get('grades').get(key) * weights_data.get(key)
			report += 'course total: ' + str(round(course_total, 1))
			reports_list.append(report)
	return reports_list

'''MAIN PROGRAM'''

'''
Read class data file (as json)
'''
with open('class_data.json', 'r') as class_data_file:
	class_data = json.load(class_data_file)
	class_data_file.close()

'''
Read weights data file (as json)
'''
with open('weights_data.json', 'r') as weights_data_file:
	weights_data = json.load(weights_data_file)
	weights_data_file.close()

'''
Print a class list
'''
print ('Class list')
print ()
print ('\n'.join(get_class_list(class_data)))
print ()

'''
Print the class average for each gradeable
'''
print ('Class averages')
print ()
gradeables = get_gradeables_list(class_data)
for i in range(len(gradeables)):
	print (gradeables[i] + ': ' + str(average_on_gradeable(gradeables[i], class_data)))

# print ' ' -- Original
print ('')

'''
Print reports for specific students, selected by their student numbers...
'''
print ('Reports for specific students (selected by ID)')
print ()
print (get_student_report (2293490, class_data, weights_data))
print ()
print (get_student_report (1234567, class_data, weights_data))
print ()

'''
Print reports for everyone.
'''
print ('Reports for entire class')
print ()
print ('\n\n'.join(get_all_student_reports (class_data, weights_data)))