from django.urls import path
import apis.views as api_view

urlpatterns = [
    path('details/', api_view.DetailView.as_view()),
    path('attendance/', api_view.AttendanceView.as_view()),
    path('marks/', api_view.MarksView.as_view()),
    path('timetable/', api_view.TimetableView.as_view()),
    path('average-marks/<int:subject_id>/', api_view.AverageMarksView.as_view()),
]