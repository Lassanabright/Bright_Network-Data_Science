from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from brightnetwork.settings_dev import ML_FILES
from web.models import Job,JobApplication,Profile,Employer,University,Subject


class Command(BaseCommand):
    help = 'Collect all job applications and put them in a csv file'
    job_applications_path = ML_FILES+"job_applications.csv"

    def handle(self, *args, **options):
        d=self.create_csv_job_applications(Job,JobApplication,Profile,Employer,University,Subject)
        df=pd.DataFrame(d)
        df.to_csv(self.job_applications_path, sep=',', encoding='utf-8')
        print("job_applications saved")

    def create_csv_job_applications(self,Job,JobApplication,Profile,Employer,University,Subject):
        applications = JobApplication.objects.all()
        n=len(applications)
        print(n)
        compteur=0
        d = {}
        d["created_date"] = []
        d["job_application_id"] = []
        d["application_status"] = []
        d["employer_id"] = []
        d["job_id"] = []
        d["user_id"] = []
        d["gender"] = []
        d["graduation_year"] = []
        d["ethnicity"] = []
        d["degree_subject"] = []
        d["university_name"] = []
        d["career_status"] = []
        d["user_preference"] = []
        d["job_sector_title"] = []
        d["employer_sector_title"] = []
        d["job_description"] = []
        d["employer_title"] = []
        d["employer_description"] = []
        d["title"] = []
        for appli in applications:
            compteur+=1
            if compteur%5000==0:
                print("progress :",compteur)
            user = Profile.objects.get(pk=appli.member_profile_id)
            job = Job.objects.get(pk=appli.job_id)
            d["created_date"].append(appli.created_date)
            d["job_application_id"].append(appli.pk)
            d["application_status"].append(appli.application_status)
            d["employer_id"].append(appli.employer_id)
            d["job_id"].append(appli.job_id)
            d["user_id"].append(appli.member_profile_id)
            employer = Employer.objects.get(pk=appli.employer_id)
            d["gender"].append(user.gender)
            d["graduation_year"].append(user.graduation_year)
            d["ethnicity"].append(user.ethnicity)
            degree_subject_id = user.degree_subject_id
            try:
                degree_subject = Subject.objects.get(pk=degree_subject_id).name
            except:
                degree_subject=""
            university_id = user.university_id
            try:
                uni = University.objects.get(pk=university_id).name
            except:
                uni=""
            career_interests = []
            for sector in user.sector_interests.all():
                career_interests.append(sector.title)
            user_preference = ""
            for i in career_interests:
                user_preference += i + " "
            career_status = user.career_status
            d["degree_subject"].append(degree_subject)
            d["university_name"].append(uni)
            job_sectors = []
            employer_sectors = []
            for sector in job.sectors.all():
                job_sectors.append(sector.title)
            for sector in employer.sectors.all():
                employer_sectors.append(sector.title)
            job_sector_title = ""
            employer_sector_title = ""
            for i in job_sectors:
                job_sector_title += i + " "
            for i in employer_sectors:
                employer_sector_title += i + " "
            d["job_title"] = job.title
            d["career_status"].append(career_status)
            d["user_preference"].append(user_preference)
            d["job_sector_title"].append(job_sector_title)
            d["employer_sector_title"].append(employer_sector_title)
            d["job_description"].append(job.description)
            d["employer_title"].append(employer.title)
            d["employer_description"].append(employer.description)
            d["title"].append(job.title)
        return d


