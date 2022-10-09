# automated-hiring-process
This program extracts all the Candidate info from an Excel File, shortlists them based on a given criteria and automatically sends an email to them for interview timings. Also sends an automated scheduled Whatsapp message to the hired candidate.


Candidates.csv: This csv file has a list of all the candidates and their contact information along with boolean parameters for whether they have certain experience or not.

main.py: This python script imports the .csv data, and filters the candidates who fulfil the requirements, and makes another file for it. It also sends an email automatically asking them to reply with an interview time.

whatsapp.py: This pythion script sends an automatic scheduled whatsapp message to the hired candidate, the next day at 9am.
