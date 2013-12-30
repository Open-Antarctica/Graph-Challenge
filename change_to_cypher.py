#!/usr/bin/env python

import fileinput
import re

def extract_node_humans():
	for line in fileinput.input():
		# These functions strip tabs, spaces, the text External Non U.S... and everything else besides names
		line.replace("\t", "")
		line.replace("\n\n", "\n")
		line.replace(" External Non U.S. Government Site", "")
		humans_capitalized = re.sub(r'^([A-Z][a-z].*)(\s|\t)*[A-Z]\-.*', r'\1', line)
		humans_capitalized = re.sub(r'\s[A-Z]-[0-9].*$', r'',humans_capitalized)
		humans_capitalized = humans_capitalized.rstrip('\s\t\n')
	
		# These functions changes spaces in names to underscore, accounts for middle initials, changes to lowercase
		humans_lowercase = re.sub(r'\,\s', r'_', humans_capitalized)
		humans_lowercase = re.sub(r'\s', r'_', humans_lowercase)
		humans_lowercase = humans_lowercase.rstrip('\s\t\n_')
		humans_lowercase = humans_lowercase.lower()
		humans_lowercase = re.sub(r'\-.*$', r'', humans_lowercase)
		
		# Puts names in Cypher-readable format to create the "humans" node
		node_humans = "(" + humans_lowercase + ":Researcher { name: '" + humans_capitalized + "' }),"

		print node_humans

def extract_node_groups():
	for line in fileinput.input():
		# These functions extract the name of the group
		group_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-.*)\sExternal.*$', r'\1', line)
		group_name = re.sub(r'(^.*[A-Z].*)\s.*$', r'\1', group_name)
		group_name = re.sub(r'/', r'_', group_name)
		group_name = re.sub(r'-', r'', group_name)
		group_name = group_name.lower()

		# These functions extract the group description
		group_description = re.sub(r'External.*Government Site', r'', line)
		# Strip name and group ID from the beginning of each line
		group_description = re.sub(r'^.*[0-9]\-[A-Z](.*$)', r'\1', group_description)
		group_description = re.sub(r'^\/[A-Z](.*$)', r'\1', group_description)
		group_description = re.sub(r'^\/[A-Z](.*$)', r'\1', group_description)
		# Strip tab from the beginning of each group description
		group_description = re.sub(r'^.{2}', r'', group_description)
		# Strip line break from the end of each line
		group_description = re.sub(r'\n', r'', group_description)
		node_groups = "(" + group_name + ":Group { group_description: '" + group_description + "' }),"
		print node_groups

extract_node_humans()

extract_node_groups()

def create_relationships_humans_to_groups():
	for line in fileinput.input():


		# This duplicates all the code above to create (researcher)-[:WORKS_ON]->(group)
		# Which is just a test, b/c they'll actually link to the event-year
		line.replace("\t", "")
		line.replace("\n\n", "\n")
		line.replace(" External Non U.S. Government Site", "")
		humans_capitalized = re.sub(r'^([A-Z][a-z].*)(\s|\t)*[A-Z]\-.*', r'\1', line)
		humans_capitalized = re.sub(r'\s[A-Z]-[0-9].*$', r'',humans_capitalized)
		humans_capitalized = humans_capitalized.rstrip('\s\t\n')
	
		# These functions changes spaces in names to underscore, accounts for middle initials, changes to lowercase
		humans_lowercase = re.sub(r'\,\s', r'_', humans_capitalized)
		humans_lowercase = re.sub(r'\s', r'_', humans_lowercase)
		humans_lowercase = humans_lowercase.rstrip('\s\t\n_')
		humans_lowercase = humans_lowercase.lower()
		humans_lowercase = re.sub(r'\-.*$', r'', humans_lowercase)
		
		# These functions extract the name of the group
		group_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-.*)\sExternal.*$', r'\1', line)
		group_name = re.sub(r'(^.*[A-Z].*)\s.*$', r'\1', group_name)
		group_name = re.sub(r'/', r'_', group_name)
		group_name = re.sub(r'-', r'', group_name)
		group_name = group_name.lower()

		print "(" + humans_lowercase +")"+ "-[:WORKS_ON]->" + "(" + group_name + "),"

create_relationships_humans_to_groups()

def create_relationships_groups_to_locations():
	for line in fileinput.input():

		# These functions extract the name of the group
		group_name = re.sub(r'^.*([A-Z]\-[0-9]{3}\-.*)\sExternal.*$', r'\1', line)
		group_name = re.sub(r'(^.*[A-Z].*)\s.*$', r'\1', group_name)
		group_name = re.sub(r'/', r'_', group_name)
		group_name = re.sub(r'-', r'', group_name)
		group_name = group_name.lower()

		group_location


