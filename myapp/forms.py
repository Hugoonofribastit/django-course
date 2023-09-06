from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task's title", max_length=200)
    description=forms.CharField(label="Task description",widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project's name",max_length=200)