#academy_seeds.py : para crear datos en mi BD

from django.core.management.base import BaseCommand
from academy.models import Teacher, Student, Course, Subject, Subscription

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--mode", type = str, help = "mode: load /clear")


    def handle(self, *args, **options):
        print("Data inicial")

        self.seeds_subject(options.get('mode'))
        print("Subjects: ", Subject.objects.all().count())

        self.seeds_student(options.get('mode'))
        print("Students: ", Student.objects.all().count())

        self.seeds_course(options.get('mode'))
        print("Courses: ", Course.objects.all().count())

        self.seeds_teacher(options.get('mode'))
        print("Teachers: ", Teacher.objects.all().count())


    def seeds_teacher(self, mode):
        if mode == "load" and Teacher.objects.all().count() <= 0:
            t = Teacher()
            t.first_name = "Pepito"
            t.last_name = "Alcachofa"
            t.email = "palcachofa@academy.edu"
            t.bio = "Este es un bio de docente 1"
            t.save()

            t = Teacher()
            t.first_name = "Juanito"
            t.last_name = "Picante"
            t.email = "jpicante@academy.edu"
            t.bio = "Este es un bio de docente 2"
            t.save()

        elif mode == "clear":
            Teacher.objects.all().delete()

    def seeds_student(self, mode):
        if mode == "load" and Student.objects.all().count() <= 0:
            s = Student()
            s.first_name = "Carlitos"
            s.last_name = "Nuñez"
            s.email = "cnunez@academy.edu"
            s.save()

            s = Student()
            s.first_name = "Luchito"
            s.last_name = "Perez"
            s.email = "lperez@academy.edu"
            s.save()

        elif mode == "clear":
            Student.objects.all().delete()

    def seeds_course(self, mode):
        if mode == "load" and Course.objects.all().count() <= 0:
            c = Course()
            c.name = "BD1"
            c.desription = "Descripcion curso"
            c.save()

            c = Course()
            c.name = "BD2"
            c.desription = "Descripcion curso"
            c.save()

        elif mode == "clear":
            Course.objects.all().delete()


    def seeds_subject(self, mode):
        if mode == "load" and Subject.objects.all().count() <= 0:
            self.seeds_course(mode)
            self.seeds_teacher(mode)
            ss = Subject()
            ss.course = Course.objects.get(name = "BD1")
            ss.teacher = Teacher.objects.get(first_name = "Pepito")
            ss.start_date = "2023-10-15"
            ss.save()

            ss = Subject()
            ss.course = Course.objects.get(name = "BD2")
            ss.teacher = Teacher.objects.get(first_name = "Juanito")
            ss.start_date = "2023-10-15"
            ss.save()

        elif mode == "clear":
            Subject.objects.all().delete()


    #def seed_subcription(self, mode):
     #   if mode == "load" and Subject.objects.all().count() <= 0:
      #      sc = Subscription()
       #     sc.subject = 
        #    sc.student = 

        #elif mode == "clear":
        #   Subscription.objects.all().delete()