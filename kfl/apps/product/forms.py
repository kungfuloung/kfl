# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductSearchForm_en(forms.Form):
    category = forms.ChoiceField(choices = ((0, 'All Products'), (1,'Qi Series'), (2,'Northern Mantis'), (3,'Northern Shaolin'), (4,'Taichi Series'), (5,'Weaponry Series'), (6,'Nanjing Series')))
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':14}))   
    level = forms.ChoiceField(choices = ((0, 'All Levels'), (1,'★'), (2,'★★'), (3,'★★★'), (4,'★★★★'), (5,'★★★★★'), (6,'★★★★★★')))
    language = forms.ChoiceField(choices = ((0, 'All languages'), (1,'English'), (2,'Chinese')))
    I_download = forms.BooleanField(required=False)

class ProductSearchForm_cn(forms.Form): 
    category = forms.ChoiceField(choices = ((0, '所有系列'), (1,'氣功系列'), (2,'北派螳螂拳'), (3,'北派少林拳'), (4,'太極拳系列'), (5,'兵器系列'), (6,'南京系')))
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':14}))
    level = forms.ChoiceField(choices = ((0, '所有上手難度'), (1,'★'), (2,'★★'), (3,'★★★'), (4,'★★★★'), (5,'★★★★★'), (6,'★★★★★★')))
    language = forms.ChoiceField(choices = ((0, '所有版本'), (1,'英文版'), (2,'中文版')))
    I_download = forms.BooleanField(required=False)



#   # ATI = forms.FloatField(required=True, validators=[MinValueValidator(0.0)])

#   # KPI1_weight = forms.FloatField(required=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
#   KPI1_active = forms.BooleanField(required=True)
#   KPI1_target = forms.FloatField(required=True)
#   KPI1_description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':2, 'cols':80}))
#   KPI1_unit = forms.CharField(required=True)

#   # KPI2_weight = forms.FloatField(required=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
#   KPI2_active = forms.BooleanField(required=False)
#   KPI2_target = forms.FloatField(required=False)
#   KPI2_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':2, 'cols':80}))
#   KPI2_unit = forms.CharField(required=False)
    
    
#   KPI3_weight = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
#   KPI3_active = forms.BooleanField(required=False)
#   KPI3_target = forms.FloatField(required=False)
#   KPI3_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':2, 'cols':80}))
#   KPI3_unit = forms.CharField(required=False)
    
    
#   KPI4_weight = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
#   KPI4_active = forms.BooleanField(required=False)
#   KPI4_target = forms.FloatField(required=False)
#   KPI4_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':2, 'cols':80}))
#   KPI4_unit = forms.CharField(required=False)


#   def clean_KPI2_target(self):
#       if self.cleaned_data['KPI2_active'] and not self.cleaned_data['KPI2_target']:
#           raise forms.ValidationError("Please provide valid data")
#       return self.cleaned_data['KPI2_target']
#   def clean_KPI2_description(self):
#       if self.cleaned_data['KPI2_active'] and not self.cleaned_data['KPI2_description']:
#           raise forms.ValidationError("Please provide valid description")
#       return self.cleaned_data['KPI2_description']
#   def clean_KPI2_unit(self):
#       if self.cleaned_data['KPI2_active'] and not self.cleaned_data['KPI2_unit']:
#           raise forms.ValidationError("Please provide valid unit")
#       return self.cleaned_data['KPI2_unit']


#   def clean_KPI3_target(self):
#       if self.cleaned_data['KPI3_active'] and not self.cleaned_data['KPI3_target']:
#           raise forms.ValidationError("Please provide valid data")
#       return self.cleaned_data['KPI3_target']
#   def clean_KPI3_description(self):
#       if self.cleaned_data['KPI3_active'] and not self.cleaned_data['KPI3_description']:
#           raise forms.ValidationError("Please provide valid description")
#       return self.cleaned_data['KPI3_description']
#   def clean_KPI3_unit(self):
#       if self.cleaned_data['KPI3_active'] and not self.cleaned_data['KPI3_unit']:
#           raise forms.ValidationError("Please provide valid unit")
#       return self.cleaned_data['KPI3_unit']       
#   def clean_KPI3_weight(self):
#       if self.cleaned_data['KPI3_weight']:
#           if abs(self.cleaned_data['KPI3_weight'] % 0.1)>.05:
#               ind = 0.1 - abs(self.cleaned_data['KPI3_weight'] % 0.1)
#           else:
#               ind = abs(self.cleaned_data['KPI3_weight'] % 0.1)
#           if ind>0.001:
#               raise forms.ValidationError("Please provide the weight in 0.1 increments")
#       return self.cleaned_data['KPI3_weight']     

#   def clean_KPI4_target(self):
#       if self.cleaned_data['KPI4_active'] and not self.cleaned_data['KPI4_target']:
#           raise forms.ValidationError("Please provide valid data")
#       return self.cleaned_data['KPI4_target']
#   def clean_KPI4_description(self):
#       if self.cleaned_data['KPI4_active'] and not self.cleaned_data['KPI4_description']:
#           raise forms.ValidationError("Please provide valid description")
#       return self.cleaned_data['KPI4_description']
#   def clean_KPI4_unit(self):
#       if self.cleaned_data['KPI4_active'] and not self.cleaned_data['KPI4_unit']:
#           raise forms.ValidationError("Please provide valid unit")
#       return self.cleaned_data['KPI4_unit']       
#   def clean_KPI4_weight(self):
#       if self.cleaned_data['KPI4_weight']:
#           if abs(self.cleaned_data['KPI4_weight'] % 0.1)>.05:
#               ind = 0.1 - abs(self.cleaned_data['KPI4_weight'] % 0.1)
#           else:
#               ind = abs(self.cleaned_data['KPI4_weight'] % 0.1)
#           if ind>0.001:
#               raise forms.ValidationError("Please provide the weight in 0.1 increments")
#       return self.cleaned_data['KPI4_weight']     

# class ForcastEditForm(forms.Form):

#   KPI1_FC_Q1 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI1_FC_Q2 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI1_FC_Q3 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI1_FC_Q4 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI1_FC_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])

#   KPI2_FC_Q1 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI2_FC_Q2 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI2_FC_Q3 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI2_FC_Q4 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI2_FC_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])

#   KPI3_FC_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI4_FC_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])



#   # KPI1_value_Q1 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI1_value_Q2 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI1_value_Q3 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI1_value_Q4 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])

#   # KPI2_value_Q1 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI2_value_Q2 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI2_value_Q3 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   # KPI2_value_Q4 = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])


#   KPI1_value_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI2_value_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI3_value_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])
#   KPI4_value_QF = forms.FloatField(required=False, validators=[MinValueValidator(0.0000)])


# class OverallStructureForm(forms.Form):
#   Min_cut_off_point = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(0.999999)])
#   Pay_out_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])          
#   SIP_Incentive_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])            
#   PMP_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])          
#   Unit_Factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])         

#   # SalesQuarterlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])          
#   # SalesYearlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])         

#   # PromotersQuarterlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])          
#   # PromotersYearlyPercentage = forms.FloatField(required=False, val('Q1','Q1'), ('Q1','Q1'), ('Q1','Q1'), ators=[MinValueValidator(0.0), MaxValueValidator(1.0)])            

#   Sales_KPI1_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   Sales_KPI2_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   Sales_KPI3_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   Sales_KPI4_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   

#   Promoter_KPI1_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])    
#   Promoter_KPI2_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])    
#   Promoter_KPI3_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])    
#   Promoter_KPI4_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])    

#   Sales_KPI_Percentage_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':7, 'cols':40}))
#   Promoter_KPI_Percentage_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':7, 'cols':40}))
    

#   Quarter_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)]) 
#   Quarter_Annual_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])  
#   Annual_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])  


#   # year = forms.IntegerField(required=False, validators=[MinValueValidator(2013)])
#   year = forms.IntegerField(required=False)

#   # # def clean_Sales_KPI1_Percentage(self):
#   # def clean(self):      
#   #   temp = 0

#   #   if self.cleaned_data['Sales_KPI1_Percentage']:
#   #       temp = temp + self.cleaned_data['Sales_KPI1_Percentage']
#   #   if self.cleaned_data['Sales_KPI2_Percentage']:
#   #       temp = temp + self.cleaned_data['Sales_KPI2_Percentage']
#   #   if self.cleaned_data['Sales_KPI3_Percentage']:
#   #       temp = temp + self.cleaned_data['Sales_KPI3_Percentage']
#   #   if self.cleaned_data['Sales_KPI4_Percentage']:
#   #       temp = temp + self.cleaned_data['Sales_KPI4_Percentage']

#   #   if temp!=1:
#   #       raise forms.ValidationError("Sum of Sales KPI weight needs to be 100%")

#   #   # if self.cleaned_data['Sales_KPI1_Percentage']+self.cleaned_data['Sales_KPI2_Percentage']+self.cleaned_data['Sales_KPI3_Percentage']+self.cleaned_data['Sales_KPI4_Percentage']!=1:
#   #       # raise forms.ValidationError("Sum of Sales KPI weight needs to be 100%")


#   #   else:
#   #       return self.cleaned_data

#   nMin_cut_off_point = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(0.999999)])
#   nPay_out_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])         
#   nSIP_Incentive_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])           
#   nPMP_factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])         
#   nUnit_Factor = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])            

#   # SalesQuarterlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])          
#   # SalesYearlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])         

#   # PromotersQuarterlyPercentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])          
#   # PromotersYearlyPercentage = forms.FloatField(required=False, val('Q1','Q1'), ('Q1','Q1'), ('Q1','Q1'), ators=[MinValueValidator(0.0), MaxValueValidator(1.0)])            

#   nSales_KPI1_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])  
#   nSales_KPI2_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])  
#   nSales_KPI3_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])  
#   nSales_KPI4_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])  

#   nPromoter_KPI1_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   nPromoter_KPI2_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   nPromoter_KPI3_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   
#   nPromoter_KPI4_Percentage = forms.FloatField(required=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])   

#   nSales_KPI_Percentage_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':7, 'cols':40}))
#   nPromoter_KPI_Percentage_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':7, 'cols':40}))
    

#   nQuarter_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])    
#   nQuarter_Annual_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)]) 
#   nAnnual_max = forms.FloatField(required=False, validators=[MinValueValidator(0.0)])     