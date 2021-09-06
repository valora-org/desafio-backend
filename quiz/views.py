from django.shortcuts import render


def profile(request):
    profile = models.Profile.objects.first()
    education = models.Education.objects.all()
    xp = models.XP.objects.all()
    current_xp = models.XP.objects.filter(is_current=True)
    current_education = models.Education.objects.filter(is_current=True)
    data = {
        'profile':profile, 
        'xp':xp, 
        'education':education,
        'current_xp':current_xp,
        'current_education':current_education,
    }
    return render(request, 'cv/profile.html', data)