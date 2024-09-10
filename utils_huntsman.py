''' ITERATION 5

Module: Huntsman Analytics - Reusable Module for My Data Analytics Projects

'''

#####################################
# Import Modules at the Top
#####################################

import statistics

#####################################
# Declare global variables 
#####################################

has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
accepting_new_clients: bool = True
years_of_experience: int = 4
sales_expertise: list = ["Confidence", "Customer Service", "Negotiating", "Problem-Solving"]
daily_temps: list = [68, 58, 54, 60, 68, 67, 52]


#####################################
# Calculate Basic Statistics 
#####################################

min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_temps: float = min(daily_temps)
max_temps: float = max(daily_temps)
mean_temps: float = statistics.mean(daily_temps)
stdev_temps: float = statistics.stdev(daily_temps)

#####################################
# Declare a global variable named byline. 
#####################################

byline: str = f"""
---------------------------------------------------------
Huntsman Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
Accepting New Clients:      {accepting_new_clients}
Years of Experience:        {years_of_experience}
Sales Expertise:            {sales_expertise}
Daily Temp Lows in Boston:  {daily_temps}
Minimum Temp Low:           {min_temps}
Maximum Temp Low:           {max_temps}
Mean Temp Low:              {mean_temps:.2f}
Standard Deviation:         {stdev_temps:.2f}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
