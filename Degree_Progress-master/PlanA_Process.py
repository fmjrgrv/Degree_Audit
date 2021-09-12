from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress import GEProgress
from GE_Requirements import GeRequirements
from Major_Progress import MajorProgress
from Major_Requirements import MajorRequirements
from Student_Info import StudentInfo
# from main import enrollment_history


def plana_processing(student_id, courses, major_name, major_course_requirements, **kwargs):
    plana_ge_requirements = {'Math_Proficiency': 0, 'Writing_Proficiency': 0, 'Reading_Proficiency': 0,
                          'Health_Proficiency': 0, 'Nat_Sci': 0,
                          'Soc_Sci': 0, 'FA_Hum': 0, 'Comp': 0, 'Analytic': 0}

    student = StudentInfo(student_id, courses)
    student.eligible_course_list()
    ge_requirements = GeRequirements(student.degree_applicable_dict, ge_plan='PlanA_GE.csv')
    ge_dataframe = ge_requirements.dataframe()
    ge_requirements.ge_courses_completed('Math_Proficiency', ge_dataframe)
    ge_requirements.ge_courses_completed('Writing_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Health_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Reading_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Nat_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Soc_Sci', ge_dataframe=ge_dataframe)
    # ge_requirements.ge_courses_completed('Beh_Sci')
    ge_requirements.ge_courses_completed('FA_Hum', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Comp', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Analytic', ge_dataframe=ge_dataframe)
    ge_requirements.area_e_ge_requirements(ge_dataframe=ge_dataframe)


    major = MajorRequirements(revised_course_list=student.degree_applicable_dict,
                              completed_ge_courses=ge_requirements.completed_ge_courses,
                              major_requirements=major_course_requirements,
                              major_name=major_name)
    if len(kwargs) == 15:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])
        major.major_courses_completed(area_name=kwargs['major5'], total_units=kwargs['major5_units'],
                                      number_of_disciplines=kwargs['major5_disciplines'])
    elif len(kwargs) == 12:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

    elif len(kwargs) == 9:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])

    elif len(kwargs) == 6:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])

    elif len(kwargs) ==3:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])

    major_progress = MajorProgress(student_id=student.student_id,
                                   major_course_dict=major.major_course_dict,
                                   major_units_required=major.major_num_of_units_dict,
                                   area_units=major.area_units_dict,
                                   num_of_courses_required=major.major_num_of_courses_dict)

    missing_courses_dict = major_progress.major_num_of_courses()
    missing_units_dict = major_progress.major_num_of_units()
    ge_requirements.reading_proficiency()
    ge_progress = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                             student.student_id, ge_plan_requirements=plana_ge_requirements)
    missing_ge_courses, completed_ge_courses, completed_ge_units = ge_progress.ge_requirements_completed()

    degree_app = DegreeApplicableUnits(student_id,
                                                    student.eligible_course_list(),
                                                    major.major_courses_list,
                                                    ge_requirements.area_e_ge_requirements(ge_dataframe=ge_dataframe),
                                                    ge_requirements.completed_ge_units,
                                                    major.major_units_list)
    elective_units, elective_courses, elective_dict = degree_app.elective_courses()

    # degree_applicable_units = DegreeApplicableUnits(student.eligible_course_list(),
    #                                                 major.major_courses_list,
    #                                                 ge_requirements.area_e_ge_requirements(ge_dataframe=ge_dataframe),
    #                                                 ge_requirements.completed_ge_units,
    #                                                 major.major_units_list)
    # degree_applicable_units.elective_courses()
    # ge_requirements.reading_proficiency()

    # major_report = MajorProgress(student_id=student.student_id,
    #                              major_course_dict=major.major_course_dict,
    #                              major_units_required=major.major_units_list,
    #                              area_units=major.area_units_dict,
    #                              num_of_courses_required=major.major_num_of_courses_dict)
    #
    # major_report.major_num_of_courses()


    # degree_reports.area_e_requirements_completed()
    # degree_reports.area_e_requirements_completed()

    degree_completion = DegreeCompletionReport(
        major_requirements_dict=major.major_num_of_units_dict,
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        major_course_dict=major.major_course_dict,
        area_units_dict=major.area_units_dict,
        elective_courses=degree_app.elective_course_list,
        elective_units=degree_app.elective_units_list,
        major_units_list=major.major_units_list,
        student_id=student_id,
        student_major=major_name,
        missing_ge=ge_progress.missing_ge_courses,
        missing_major_courses=major_progress.missing_courses_dict,
        missing_units_dict=major_progress.missing_units_dict)

    length, missing_major_courses = degree_completion.degree_completion()
    length = degree_completion.degree_status(length=length, missing_major_courses=missing_major_courses)
    degree_completion.unused_courses(length=length ,ge_courses=ge_requirements.completed_ge_courses,
                                     major_courses=major.major_courses_list2,
                                     elective_courses=degree_app.elective_course_list,
                                     student_course_list=student.degree_applicable_dict)




def sorting_PlanA_majors(enrollment_history, major_name, major_course_requirements, **kwargs):
    student_id_list = []

    for i in range(len(enrollment_history)):
        if enrollment_history.loc[i, "ID"] not in student_id_list:
            print('major in sorting majors', major_name)
            print(enrollment_history.loc[i, "Major"])
            if enrollment_history.loc[i, "Major"] == major_name:
                student_id_list.append(enrollment_history.loc[i, "ID"])
                print(student_id_list)

    for student_id in student_id_list:
        plana_processing(student_id=student_id, courses=enrollment_history, major_name=major_name,
                         major_course_requirements=major_course_requirements, **kwargs)