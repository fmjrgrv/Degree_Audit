import pandas as pd

from Major_Requirements import MajorRequirements



class DegreeCompletionReport:
    columns = ['Student_ID', 'Major', 'GE_Status', 'Major_Status', 'Degree_Status', 'Total_Degree_Units','GE_Units', 'Total_Major_Units',
               'Degree_Major_Units', 'Elective_Units', 'Total_Missing', 'GE_Missing', 'Major_Missing_Courses',
               'Major_Missing_Units', 'Missing_GE',
               'Missing_Major_Courses', 'GE_Courses', 'Major_Courses', 'Elective_Courses', 'Unused_Courses']
    LS_AA_Degrees_df = pd.DataFrame(columns=columns)
    # degree_units_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
    # columns2 = ['Student_ID', 'Major', 'Degree_Units', 'GE_Courses', 'Major_Courses', 'Elective_Courses']
    # degree_courses_df = pd.DataFrame(columns=columns2)

    def __init__(self, major_requirements_dict, completed_ge_courses, completed_ge_units, major_course_dict,
                 area_units_dict, major_units_list, student_id, student_major, elective_units, elective_courses,
                 missing_ge, missing_major_courses, missing_units_dict):
        self.missing_major_courses = missing_major_courses
        self.missing_ge = missing_ge
        self.major_units_list = major_units_list
        self.area_units_dict = area_units_dict
        self.major_course_dict = major_course_dict
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.student_id = student_id
        self.student_major = student_major
        self.major_requirements_dict = major_requirements_dict
        self.elective_units = elective_units
        self.elective_courses = elective_courses
        self.missing_major_courses = missing_major_courses
        self.missing_units_dict = missing_units_dict

        # print('maj missing course dic', self.missing_major_courses)
        # print('comp ge units', completed_ge_units)

    def degree_completion(self):

        # length1 = len(DegreeCompletion.degree_units_df)
        length = len(DegreeCompletionReport.LS_AA_Degrees_df)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Student_ID'] = self.student_id
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major'] = self.student_major
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Units'] = sum(self.completed_ge_units)
        major_units_total_value = sum(self.area_units_dict.values())
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Major_Units'] = major_units_total_value
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Major_Units'] = sum(self.major_units_list)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Units'] = sum(self.elective_units)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Degree_Units'] = sum(self.completed_ge_units) +\
                                                                              sum(self.major_units_list) +\
                                                                              sum(self.elective_units)


        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Missing'] = len(self.missing_ge)
        values = self.missing_major_courses.values()
        missing_major_courses = sum(values)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing_Courses'] = missing_major_courses
        values = self.missing_units_dict.values()
        missing_major_units = sum(values)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing_Units'] = missing_major_units

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_GE'] = self.missing_ge

        missing_major_list = self.missing_major_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_Major_Courses'] = missing_major_list

        ge_list = self.completed_ge_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Courses'] = ge_list
        major_list = self.major_course_dict.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Courses'] = major_list
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Courses'] = self.elective_courses

        total_missing = len(self.missing_ge) + missing_major_courses
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Missing'] = total_missing
        return length, missing_major_courses


    def degree_status(self, length, missing_major_courses):
        degree_status_ge = False
        degree_status_major = False
        if len(self.missing_ge) == 0:
            DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Completed'
            degree_status_ge = True
        else:
            DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Incomplete'

        if missing_major_courses == 0:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Completed'
                degree_status_major = True
        else:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Incomplete'


        if sum(self.completed_ge_units) + sum(self.major_units_list) + sum(self.elective_units) >= 60:
            if degree_status_ge == True and degree_status_major == True:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Completed'
            else:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Incomplete'

        return length

    def unused_courses(self, length, ge_courses, major_courses, elective_courses, student_course_list):
        """
           This function will take as inputs ge courses, major courses, elective courses, and revised courses list. It will
           compare the revised course list to the other three lists and remove any courses that appear in the other lists. This
           will leave a list of unused courses, giving us information about where students are wasting their units.
           """
        unused_courses = []
        print('maj crses', major_courses)
        ge_course_list = ge_courses.values()
        print('ge crses', ge_course_list)

        for course_key in student_course_list:
            if course_key not in ge_course_list:
                if course_key not in major_courses:
                    if course_key not in elective_courses:
                        unused_courses.append(course_key)
        print('un crses', unused_courses)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Unused_Courses'] = unused_courses

