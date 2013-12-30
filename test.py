#!/usr/bin/env python

# NOTE: POPULATE GROUP + RESEARCH CATEGORY AT SAME TIME

import fileinput
import re

print "CREATE"

print "\n"
print "//These are the Locations"
print "(lmg_vessel:Vessel { name: 'Laurence M. Gould' }),"
print "(mcmurdo_station:Station { name: 'McMurdo Station' }),"
print "(nbp_vessel:Vessel { name: 'Nathaniel B. Palmer' }),"
print "(palmer_station:Station { name: 'Palmer Station' }),"
print "(south_pole_station:Station { name: 'Amundsen Scott South Pole Station' }),"

print "\n"
print "//These are the Research Categories"
print "(a_astrophysics_and_geospace:Research_Category { name: 'Astrophysics and Geospace Sciences' }),"
print "(b_organisms_and_ecosystems:Research_Category { name: 'Organisms and Ecosystems' }),"
print "(c_integrated_system_science:Research_Category { name: 'Integrated System Science' }),"
print "(g_earth_science:Research_Category { name: 'Earth Science' }),"
print "(i_glaciology:Research_Category { name: 'Glaciology' }),"
print "(o_oceans_and_atmospheric_sciences:Research_Category { name: 'Oceans and Atmospheric Sciences' }),"
print "(t_technical_event:Science { name: 'Technical Event' }),"

# This creates (EVENT) to (GROUP) to (RESEARCH CATEGORY)

def create_relationships_event_to_group_to_research_category():
	for line in fileinput.input():

		# These functions extract the name of the group
		group_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-([A-Z]|\/)*)\sExternal.*$', r'\1', line)
		group_name = re.sub(r'-', r'', group_name)
		group_name = re.sub(r'/', r'_', group_name)
		group_name = group_name.lower()
		group_name = group_name.rstrip('\n')
		
		# This creates an array/list to put group names into for sorting below
		group_name_list = []
		group_name_list = group_name

		if group_name_list[0] == "a":
			print "(" + group_name + "-xx_yy:Event { name: '" + group_name + " 20xx-yy'})-[:IS_GROUP]->(" + group_name + ")-[:IS_DISCIPLINE]->(a_astrophysics_and_geospace),"