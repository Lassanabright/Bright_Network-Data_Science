from django.core.management.base import BaseCommand, CommandError
from celery.app import shared_task
from web.models import Page,Event,SuccessStory,Job,Employer
from web.models import Job,JobApplication,JobSector,Profile,Employer,University,Subject
from brightnetwork.settings_dev import ML_FILES
import re



@shared_task
def search_rank_recalc():
    from web.management.commands.search_ranks_update import Command
    cmd = Command()
    cmd.handle(
        no_delete_entries=False, rank_affecting_range=4, current_week=False,
        verbosity=2)


@shared_task
def pull_sf_accounts_data():
    from web.management.commands.salesforce_sync_profiles import Command
    cmd = Command()
    cmd.handle(dry_run=False, interval=6, verbosity=0)