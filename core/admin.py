from django.contrib import admin
from .models import *
# Register your models here.

class DoctorshipInLine(admin.TabularInline):
    model = Guest.doctors.through

class GuestAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in Guest._meta.fields]
    # list_filter = ["name"]
    # inlines = [ProductImageInline]


    class Meta:
        model = Guest

admin.site.register(Guest, GuestAdmin)


class GuestInline(admin.TabularInline):
    model = Guest
    # fields = ('name', 'patronomic', 'surname', 'sex','category')

    # list_display = ('name', 'patronomic', 'surname', 'sex')
    fields = ('name', 'patronomic', 'surname', 'sex','category')
class DoctorAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = ['name']
    # search_fields = ['name']
    inlines = [DoctorshipInLine, ]
    class Meta:
        model = Doctor

admin.site.register(Doctor, DoctorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = ['name']
    # search_fields = ['name']
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class TableAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in Guest._meta.fields]
    # list_filter = ["name"]
    # inlines = [ProductImageInline]
    # a = list()
    # tables = Guest.objects.order_by('table')
    # for guest in tables:
    #     # a = table.guest_set.filter(table_id= table.id)
    #     # print(guest.table.number, guest.name)
    #     a.append(guest.name)
    # list_display = []
    inlines = [GuestInline,]
    class Meta:
        model = Table

admin.site.register(Table, TableAdmin)

class RoomAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in Guest._meta.fields]
    # list_filter = ["name"]
    # inlines = [ProductImageInline]

    inlines = [GuestInline, ]
    class Meta:
        model = Room

admin.site.register(Room, RoomAdmin)