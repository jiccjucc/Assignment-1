# one birth every 7 seconds
# one death every 13 seconds
# one new immigrant every 45 seconds
# Write a program to display the population for each of the next five years.
# Assume the current population is 312032486 and one year has 365 days.
current_population = 312032486

seconds_per_year = 60 * 60 * 24 * 365

births_per_year = seconds_per_year // 7
deaths_per_year = seconds_per_year // 13
immigrants_per_year = seconds_per_year // 45

population_change = births_per_year - deaths_per_year + immigrants_per_year

population = current_population
print("Year 0 Population:", population )

population = population + population_change
print("Year 1 population:", population )

population = population + population_change
print("Year 2 population:", population )

population = population + population_change
print("Year 3 population:", population )

population = population + population_change
print("Year 4 population:", population )

population = population + population_change
print("Year 5 population:", population )