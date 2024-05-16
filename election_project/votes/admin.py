from django.contrib import admin
from .models import Candidate, Voter, Vote

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Vote)
