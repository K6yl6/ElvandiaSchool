from django.contrib import admin
from .models import (
    schUpdate,
    candidateDetails,
    ftherDetails,
    mtherDetails,
    GuardDetails,
    emergencyContact1,
    emergencyContact2,
    emergencyContact3
)


@admin.register(schUpdate)
class SchUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'subject', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(candidateDetails)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('StuName', 'DOB', 'nationality', 'religion')
    search_fields = ('StuName', 'nationality', 'religion')
    list_filter = ('DOB',)


@admin.register(ftherDetails)
class FatherAdmin(admin.ModelAdmin):
    list_display = ('FtherName', 'email', 'phone', 'profession')
    search_fields = ('FtherName', 'email', 'phone', 'profession')
    list_filter = ('profession',)


@admin.register(mtherDetails)
class MotherAdmin(admin.ModelAdmin):
    list_display = ('FtherName', 'email', 'phone', 'profession')
    search_fields = ('FtherName', 'email', 'phone', 'profession')
    list_filter = ('profession',)

@admin.register(GuardDetails)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('FtherName', 'email', 'phone', 'profession')
    search_fields = ('FtherName', 'email', 'phone', 'profession')
    list_filter = ('profession',)


@admin.register(emergencyContact1)
class EmergencyContact1Admin(admin.ModelAdmin):
    list_display = ('relation', 'contact')
    search_fields = ('relation', 'contact')

@admin.register(emergencyContact2)
class EmergencyContact2Admin(admin.ModelAdmin):
    list_display = ('relation', 'contact')
    search_fields = ('relation', 'contact')

@admin.register(emergencyContact3)
class EmergencyContact3Admin(admin.ModelAdmin):
    list_display = ('relation', 'contact')
    search_fields = ('relation', 'contact')

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('name', 'email', 'message')
