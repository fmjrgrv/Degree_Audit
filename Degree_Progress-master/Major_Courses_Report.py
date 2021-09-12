import pandas as pd

class MajorCompletionReport:
    # columns = ['Student_ID', 'Major', 'GE_Status', 'Major_Status', 'Total_GE_Units', 'Total_Major_Units',
    #            'Degree_Major_Units', 'Missing_Num_GE_Courses', 'Missing_Num_Major_Courses', 'Missing_Major_Units',
    #            'GE_Courses', 'Missing_GE_Area(s)', 'Missing_Major_Courses']
    # GE_Progress_df = pd.DataFrame(columns=columns)

    def __init__(self, student_id, major, missing_courses_dict, major_course_dict, missing_units_dict, major_units_dict,
                 major_units_list, dataframe):
        self.student_id = student_id
        self.major = major
        self.missing_courses_dict = missing_courses_dict
        self.major_course_dict = major_course_dict
        self.missing_units_dict = missing_units_dict
        self.major_units_dict = major_units_dict
        self.major_units_list = major_units_list
        self.dataframe = dataframe
    def major_completion(self):
        length = len(self.dataframe)
        self.dataframe.loc[length, 'Student_ID'] = self.student_id

        self.dataframe.loc[length, 'Major'] = self.major
        print('dataframe', self.dataframe)
        major_courses_list = self.major_course_dict.items()
        print(major_courses_list)
        self.dataframe.loc[length, 'Major_Courses'] = major_courses_list

        values = self.major_units_dict.values()
        total_major_units = sum(values)
        self.dataframe.loc[length, 'Total_Major_Units'] = total_major_units

        total_degree_major_units = sum(self.major_units_list)
        self.dataframe.loc[length, 'Degree_Major_Units'] = total_degree_major_units

        missing_courses_list = self.missing_courses_dict.items()
        self.dataframe.loc[length, 'Missing_Major_Courses'] = missing_courses_list

        missing_units_list = self.missing_units_dict.items()
        self.dataframe.loc[length, 'Missing_Major_Units'] = missing_units_list

        values = self.missing_courses_dict.values()
        missing_courses_total = sum(values)
        self.dataframe.loc[length, 'Missing_Num_Major_Courses'] = missing_courses_total

        values = self.missing_units_dict.values()
        missing_units_total = sum(values)
        self.dataframe.loc[length, 'Missing_Major_Units'] = missing_units_total

        if missing_courses_total == 0 and missing_units_total == 0:
            self.dataframe.loc[length, 'Major_Status'] = 'Complete'
        else:
            self.dataframe.loc[length, 'Major_Status'] = 'Incomplete'

        print(self.dataframe)
