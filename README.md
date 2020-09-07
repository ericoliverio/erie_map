# erie_map
API and mapping tools for zip code-level visualizations of COVID-19 in Erie County

#TD: Add stackexhange tips

Contains: 
1) erie_total.csv #ts cases by zip code
2) erie_diff.csv #ts daily cases by zip code
3) erie_covid.csv #daily report for mapping

3) update_erie.py #use requests libraries to get HTTP data and update erie_total.csv
4) read_erie.py #calculates metrics (daily cases, growth factor, rolling avg), creates sorted bar graphs, and ts-cases by zip figures. Also creates/updates erie_diff.csv
    #creates erie_covid.csv for mapping

5) erie_folium.py #creates maps using erie_covid.csv to create daily map of any metric. 
