@login_required()
def add_student(request):
    # If the user is not admin, they will be redirected to home
    if not request.user.is_superuser:
        return redirect("/")

    if request.method == 'POST':
        # Retrieving all the form data that has been inputted
        class_id = get_object_or_404(Class, id=request.POST['class'])
        name = request.POST['full_name']
        usn = request.POST['usn']
        dob = request.POST['dob']
        sex = request.POST['sex']
        email = request.POST.get('email', '')  # Retrieve email from POST data

        # Creating a User with student username and password format
        # USERNAME: firstname + underscore + last 3 digits of USN
        # PASSWORD: firstname + underscore + year of birth(YYYY)
        user = User.objects.create_user(
            username=name.split(" ")[0].lower() + '_' + usn[-3:],
            password=name.split(" ")[0].lower() + '_' + dob.replace("-", "")[:4],
            email=email  # Include email when creating the user
        )
        user.save()

        # Creating a new student instance with given data and saving it.
        Student(
            user=user,
            USN=usn,
            class_id=class_id,
            name=name,
            sex=sex,
            DOB=dob,
            email=email  # Save the email address to the Student model
        ).save()
        return redirect('/')
    
    all_classes = Class.objects.order_by('-id')
    context = {'all_classes': all_classes}
    return render(request, 'info/add_student.html', context)
