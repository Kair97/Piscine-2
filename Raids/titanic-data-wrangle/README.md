# Titanic Survival Analysis

## Overview
This study provides an end-to-end data wrangling and demographic survival analysis on the Titanic passenger manifest (889 passengers post-cleaning). The overall survival rate across all passengers was 38.25% (0.3825).

## Demographic and Socioeconomic Disparities
Survival rates varied substantially by sex and passenger class. Female passengers experienced a 74.04% (0.7404) survival rate compared to 18.89% (0.1889) for males. Socioeconomic standing strongly influenced outcomes: first-class passengers survived at 62.62% (0.6262), second-class at 47.28% (0.4728), and third-class at only 24.24% (0.2424). First-class females had the highest survival rate at 96.74%, whereas third-class males experienced 13.54%.

Age segmentation revealed that children (AgeBand: Child) achieved the highest survival rate at 57.97% (0.5797), followed by teens (42.86%), seniors (39.69%), adults (35.33%), and elders (19.05%). Family structure also impacted outcomes: passengers traveling alone (IsAlone=1) had a survival rate of 30.09% (0.3009), whereas passengers traveling with family members achieved 50.56% (0.5056).

## Embarkation Port Dynamics
Analysis by port of embarkation showed Cherbourg with the highest survival rate at 55.36% (0.5536, n=168), followed by Queenstown at 38.96% (0.3896, n=77) and Southampton at 33.70% (0.3370, n=644). Across embarkation countries, females boarding in France survived at 87.67% and males at 30.53%, compared to England where females survived at 68.97% and males at 17.46%.

## Conclusion
While embarkation port correlates with survival disparities, this effect is likely confounded by the disproportionate concentration of first-class ticket holders boarding at Cherbourg rather than inherent geographic factors.
