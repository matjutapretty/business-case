from django.db import models

class createForm(models.Model):
    # id = models.CharField(max_length=20)
    logo = models.ImageField(upload_to = "images/")
    Project_name = models.CharField(max_length=200)
    Business_case_proposal_date = models.DateField()
    sponsor = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    internal_stakeholder = models.CharField(max_length=200)
    external_stakeholder = models.CharField(max_length=200)
    Need_for_the_project = models.CharField(max_length=200)
    Alignment_with_Business_Priorities = models.CharField(max_length=200)
    Proposed_Solution_or_Methodology = models.CharField(max_length=200)
    Impacted_Business_Function_or_Area = models.CharField(max_length=200)
    Indicative_Risk_Level_of_the_Project = models.CharField(max_length=200)
    Proposed_Start_Date = models.DateField()
    Overall_Project_Timeframe = models.DateField()
    Estimated_completion_Date = models.DateField()
    Location_of_Project_Implementation = models.CharField(max_length=200)
    Approximate_costs_of_the_Project = models.CharField(max_length=200)
    Estimate_Benefits_Financial_or_Non_Financial = models.CharField(max_length=200)
    Impact_or_Risks_of_doing_nothing_Financial_or_Non_Financial = models.CharField(max_length=200)
    def __str__(self):
        return self.Project_name