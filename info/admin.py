class StudentAdmin(admin.ModelAdmin):
    list_display = ('USN', 'name', 'class_id', 'email')  # Added 'email' here
    search_fields = ('USN', 'name', 'class_id__id', 'class_id__dept__name', 'email')  # Added 'email' here
    ordering = ['class_id__dept__name', 'class_id__id', 'USN']
