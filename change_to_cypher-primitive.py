#!/usr/bin/env python

import fileinput
import re

print "CREATE"

print "\n"
print "//These are the (LOCATIONS)"
print "(lmg_vessel:Vessel { location: 'Laurence M. Gould' }),"
print "(mcmurdo_station:Station { location: 'McMurdo Station' }),"
print "(nbp_vessel:Vessel { location: 'Nathaniel B. Palmer' }),"
print "(palmer_station:Station { location: 'Palmer Station' }),"
print "(south_pole_station:Station { location: 'Amundsen Scott South Pole Station' }),"
print "(rothera_station:Station { location: 'Rothera Research Station (UK' }),"
print "(ferraz_station:Station { location: 'Commandante Ferraz Antarctic Station (BR)'}),"
print "(oden_icebreaker:Vessel { location: 'Oden Icebreaker (SE)' }),"

print "\n"
print "//These are the (RESEARCH CATEGORIES)"
print "(a_astrophysics_and_geospace:Research_Category { category: 'Astrophysics and Geospace Sciences' }),"
print "(b_organisms_and_ecosystems:Research_Category { category: 'Organisms and Ecosystems' }),"
print "(c_integrated_system_science:Research_Category { category: 'Integrated System Science' }),"
print "(g_earth_science:Research_Category { category: 'Earth Science' }),"
print "(i_glaciology:Research_Category { category: 'Glaciology' }),"
print "(o_oceans_and_atmospheric_sciences:Research_Category { category: 'Oceans and Atmospheric Sciences' }),"
print "(t_technical_event:Science { category: 'Technical Event' }),"

# This are the relationships from (EVENT) to (GROUP) to (RESEARCH CATEGORY)

def create_relationship_event_to_group_to_research_category():
	for line in fileinput.input():

		# These functions extract the name of the group
		group_name = re.sub(r'^([A-Z]\-[0-9]{3}\-([A-Z]|[A-Z]\/[A-Z]|[A-Z]\/[A-Z]\/[A-Z]))\s.*$', r'\1', line)
		group_name = re.sub(r'-', r'', group_name)
		group_name = re.sub(r'/', r'_', group_name)
		group_name = group_name.lower()
		group_name = group_name.rstrip('\n')
		
		# This creates an array/list to put group names into for sorting below
		group_name_list = []
		group_name_list = group_name

		if group_name_list[0] == "a":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(a_astrophysics_and_geospace),"
		if group_name_list[0] == "b":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(b_organisms_and_ecosystems),"
		if group_name_list[0] == "c":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(c_integrated_system_science),"
		if group_name_list[0] == "g":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(g_earth_science),"
		if group_name_list[0] == "i":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(i_glaciology),"
		if group_name_list[0] == "o":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(o_oceans_and_atmospheric_sciences),"
		if group_name_list[0] == "t":
			print "(" + group_name + "_xx_yy:Event { event_number: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_CATEGORY]->(t_technical_event),"

print "\n"
print "//This creates relationships between (EVENT) to (GROUP) to (RESEARCH CATEGORY)"
create_relationship_event_to_group_to_research_category()


# This creates the (PRINCIPLE INVESTIGATOR) node and connects it to their (EVENT) and connects it to their (LOCATION)
def create_human_to_event_to_location():
	for line in fileinput.input():

		# Extracts capitalized names
		human_capitalized = re.sub(r'^([A-Z].*)(\t|\s\t)[A-Z]\-[0-9]{3}.*$', r'\1', line)
		human_capitalized = re.sub(r'\s$', r'', human_capitalized)
		human_capitalized = human_capitalized.rstrip('\t\n')

		# Changes spaces in names to underscore, accounts for middle initials, deletes periods after initials & changes to lowercase
		human_lowercase = re.sub(r'\,\s', r'_', human_capitalized)
		human_lowercase = re.sub(r'\s$', r'', human_lowercase)
		human_lowercase = re.sub(r'\s', r'_', human_lowercase)
		human_lowercase = re.sub(r'\.', r'', human_lowercase)
		human_lowercase = human_lowercase.lower()
		human_lowercase = re.sub(r'\-.*$', r'', human_lowercase)
		
		# Creates the (HUMAN) node
		node_human = "(" + human_lowercase + ":Human { name: '" + human_capitalized + "' })"

		# These functions extract the name of the event
		event_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-([A-Z]|[A-Z]\/[A-Z]|[A-Z]\/[A-Z]\/[A-Z]))(\s|\t|\s\t).*$', r'\1', line)
		event_name = re.sub(r'-', r'', event_name)
		event_name = re.sub(r'/', r'_', event_name)
		event_name = event_name.lower()
		event_name = event_name.rstrip('\n')
		node_event_name = "(" + event_name + "_xx_yy)"

# This creates an array/list to put group names into for sorting below
		event_name_list = []
		event_name_list = event_name
		
		# This matches the location code to locations in creating relationships from group to location

		if len(event_name_list)>4:
			if event_name_list[4] == "l":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(lmg_vessel),"
			if event_name_list[4] == "m":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(mcmurdo_station),"
			if event_name_list[4] == "n":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(nbp_vessel),"
			if event_name_list[4] == "p":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(palmer_station),"
			if event_name_list[4] == "s":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(south_pole_station),"

		if len(event_name_list)>5:
			if event_name_list[6] == "l":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(lmg_vessel),"
			if event_name_list[6] == "m":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(mcmurdo_station),"
			if event_name_list[6] == "n":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(nbp_vessel),"
			if event_name_list[6] == "p":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(palmer_station),"
			if event_name_list[6] == "s":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(south_pole_station),"

		if len(event_name_list)>7:
			if event_name_list[8] == "l":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(lmg_vessel),"
			if event_name_list[8] == "m":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(mcmurdo_station),"
			if event_name_list[8] == "n":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(nbp_vessel),"
			if event_name_list[8] == "p":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(palmer_station),"
			if event_name_list[8] == "s":
				print node_human + "-[:WORKS_FOR { group_role:'Principle Investigator' }]->" + node_event_name + "-[:IS_AT]->(south_pole_station),"

print "\n"
print "//These are the relationships from (HUMANS) to (EVENTS) to (LOCATIONS)"
create_human_to_event_to_location()

# This creates the relationship between (EVENT) and (FIELD SEASON YEAR)
def create_event_to_field_season_year():
	for line in fileinput.input():

		# These functions extract the name of the event
		event_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-([A-Z]|[A-Z]\/[A-Z]|[A-Z]\/[A-Z]\/[A-Z]))\s.*$', r'\1', line)
		event_name = re.sub(r'-', r'', event_name)
		event_name = re.sub(r'/', r'_', event_name)
		event_name = event_name.lower()
		event_name = event_name.rstrip('\n')
		node_event_name = "(" + event_name + "_xx_yy)"
		node_field_season_year = "(fs_xx_yy:Field_Season { field_season_year: 'USAP Field Season 20xx-20yy' })"

		print node_event_name + "-[:IS_YEAR]->" + node_field_season_year + ","

print "\n"
print "//These are the relationships from (EVENT) to (FIELD SEASON YEAR)"
create_event_to_field_season_year()