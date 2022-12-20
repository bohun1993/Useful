"""

https://www.youtube.com/watch?v=RUT6fZeLnGk&list=PLL34mf651faORDOyJrk0E6k9FM-wKgfPV&index=36&ab_channel=SoftwareTestingMentor


##########
# PART 1 #
##########


# What is CSS and CSS selector (basic CSS selector syntax)
    - CSS stands for Cascading Style Sheets
    - CSS is a style sheet language which describes the presentation of the HTML document
    - CSS selectors are used to target the HTML elements on web page

format: tag_name[attribute_name='attribute_value']

f.ex.:
input[id=first_name]

# CSS selector: select by ID
    - if the webelement has an ID attribute you can use the ID attribute details in CSS selector
    - ID attribute in CSS selector is symbolised by the hash (#) sign

format: tag_name#elementID

f. ex.:
input#first_name


##########
# PART 2 #
##########


# CSS selector using 'class' attribute
    - if the webelement has the 'class 'attribute you can use 'class' attribute details in CSS selector
    - 'class' attribute in CSS selector is symbolised by the dot (.) sign

format: tag_name.class_name

f.ex.:
input.signup


##########
# PART 3 #
##########


# CSS selector using other webelement attributes
  you can create CSS selector for webelements which hav other attributes as wall, like 'type', 'placeholder', 'value' 
  etc.
  
format: tag_name[attribute_name='attribute_value']
  
f.ex.:
input[value='Sign me up']

# Advanced CSS selectors (using mix of tag, ID and class_name)
  you can write CSS selector using mix of ID or class_name and other attributes of webelement

format: tag_name.class_value[attribute_name='attribute_value']
        tag_name#id_value[attribute_name='attribute_value']

f.ex.:

input.signup[type='submit'][value='Sign me up']
input#submit_btn[type='submit'][value='Sign me up']


##########
# PART 4 #
##########


# CSS selector sub-string
    - sub-string matches are very helpful in identifying dynamic webelements with the help of partial string matches
    - the 3 important special characters in css syb-string selectors are:
        '^' sign - signify's the prefix of the text
        '$' sign - signify's the suffix of the text
        '*' sign - signify's the sub-string of the text

f. ex.:
input[name^='country_c']    # match prefix of the text
input[name$='y_client']    # match suffix of the text
input[name*='try_cl']    # match sub-string of the text


##########
# PART 5 #
##########


# Finding child or subchild elements
    - direct child, child combinator (>) is used to select direct child
      format: tag_name[attribute_name='attribute_value'] > tag_name[attribute_name='attribute_value']

    f.ex.:
    select#country > option[value='AU']     # HTML:

    - child or subchild, descendant combinator ( ) is used to select child or subchild (child or grandchild etc.)
      format: tag_name[attribute_name='attribute_value'] tag_name[attribute_name='attribute_value']

    f.ex.:
    form#deorg_form div     # HTML:


##########
# PART 6 #
##########


# CSS selector - next sibling
    - sibling elements are located using the + operator
    - adjacent sibling combinator (+) separates two CSS selectors and matches the second webelement only if it
      immediately follows the first webelement, and both are the child of same parent webelement
      format: tag_name[attribute_name='attribute_value']+tag_name[attribute_name='attribute_value']

f.ex.:
option[value='Developer']+option    # very useful when you want to select webelement which has only dynamic parameters


##########
# PART 7 #
##########


# CSS selector pseudo-classes, first-child, last-child, nth-child, nth-last-child
    - CSS pseudo-class is a keyword added to a selector that specifies a special state of the selected webelement
    - first-child - returns first element from the group of sibling elements
    - last-child - returns last element from the group of sibling elements
    - nth-child() - returns elements based on their position in a group of siblings
    - nth-last-child() - returns elements based on their position among a group of siblings, counting from the end

f.ex.:
select#job_role option:nth-child(2)
select#job_role *:nth-child(2)      # '*' means any tag_name
select#job_role *:first-child
select#job_role *:last-child
select#job_role *:nth-last-child(3)


##########
# PART 8 #
##########


# CSS selector pseudo-classes cont. first-of-type, last-of-type, nth-of-type()
    - first-of-type - returns the first element of its type among a group of sibling elements
    - last-of-type - returns the last element of its type among a group of sibling elements
    - nth-of-type() - matches elements of a given type, based on their position among a group of siblings

f.ex.:
select#job_role option:first-of-type
select#job_role option:last-of-type
select#job_role option:nth-of-type(5)

"""
