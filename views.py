from django.views.generic import TemplateView
from web.models import Job,JobApplication,JobSector,Profile,Employer,University,Subject
from django.views.generic import DetailView


class MachineLearningView(TemplateView):
    template_name = "data_science/homepage.html"
    job=Job
    job_appli=JobApplication
    jobsector=JobSector
    users_profile=Profile
    university=University
    employer=Employer
    subject=Subject

    def get_context_data(self, **kwargs):
        context = super(MachineLearningView, self).get_context_data(**kwargs)
        applications=self.job_appli.objects.all()
        d={}
        for appli in applications:
            d["created_date"]=appli.created_date
            d["job_application_id"]=appli.pk
            d["application_status"] = appli.application_status
            d["employer_id"] = appli.employer_id
            d["job_id"] = appli.job_id
            d["user_id"] = appli.member_profile_id
            user=self.users_profile.objects.get(pk=appli.member_profile_id)
            job = self.job.objects.get(pk=appli.job_id)
            employer = self.employer.objects.get(pk=appli.employer_id)
            d["gender"] = user.gender
            d["graduation_year"] = user.graduation_year
            d["ethnicity"] = user.ethnicity
            degree_subject_id=user.degree_subject_id
            degree_subject=self.subject.objects.get(pk=degree_subject_id)
            university_id=user.university_id
            uni=self.university.objects.get(pk=university_id)
            d["degree_subject"] = degree_subject.name
            d["university_name"] = uni.name
            job_sector_id=job.sectors
            d["job_title"] = job.title
            #d["job_sector_title"] = job_sector_title
            d["job_description"] = job.description
            d["employer_title"] = employer.title
            d["employer_description"] = employer.description
            d["title"] = job.title
            break
        context["test"]="test"
        return context
