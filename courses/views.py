from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
import json
from .models import *

# Create your views here.

'''
class CourseView(LoginRequiredMixin, View):
    model = Course
    context_object_name = 'courses'
'''


class SemesterListView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request, *args, **kwargs):
        s = Semester.objects.all()
        return render(request, self.template_name, {'semesters': s[2:]})


class CourseDetailView(LoginRequiredMixin, View):
    template_name = 'courses/course_detail.html'

    def get(self, request, course_code):
        course = get_object_or_404(Course, course_code=course_code)

        # Group sections via numero
        sections_by_number = {}
        for section in course.sections.all():
            if section.section_number not in sections_by_number:
                sections_by_number[section.section_number] = []
            sections_by_number[section.section_number].append(section)

        context = {
            'course': course,
            'sections_by_number': sections_by_number,
        }
        return render(request, self.template_name, context)


class CurriculumView(LoginRequiredMixin, View):
    login_url = 'accounts:login'
    template_name = 'courses/curriculum.html'

    def get(self, request, program_code):
        student = request.user
        # Get all curriculum courses for the student's program
        currs = CurriculumCourseSemester.objects.filter(program_code=student.study)

        backtobackwtf = []
        for cur in currs:
            academic_dreams = cur.semcor_academic_dream.filter(student=student)
            status = 'not_taken'

            if academic_dreams.exists():
                academic_dream = academic_dreams.first()
                if academic_dream.grade == -1:
                    status = 'not_taken'
                elif academic_dream.grade >= 50:
                    status = 'passed'
                else:
                    status = 'failed'

            backtobackwtf.append({'course': cur.course, 'status': status})

        context = {
            'courses_status': backtobackwtf,
            'program_code': program_code
        }
        return render(request, self.template_name, context)





class CourseSearchView(LoginRequiredMixin, View):
    login_url = 'accounts:login'

    def get(self, request):
        courses = Course.objects.all()
        course_data = []

        for course in courses:
            section_query = Section.objects.filter(course=course)
            section_list = list(section_query.values('section_number', 'day', 'starting_hour',
                                                     'room_name', 'building_name', 'floor_name'))
            course_data.append({
                'title': course.title,
                'sections': section_list
            })
        context = {'course_data': course_data}
        return JsonResponse(context)


class Dexter(LoginRequiredMixin, View):

    login_url = 'accounts:login'

    def get(self, request):
        return render(request, 'courses/dexter.html')
