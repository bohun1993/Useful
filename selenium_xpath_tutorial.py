"""

https://www.youtube.com/watch?v=5LV4z_-91WY&list=PLL34mf651faORDOyJrk0E6k9FM-wKgfPV&index=26&ab_channel=SoftwareTestingMentor


##########
# PART 1 #
##########


# Basic format of XPath:
XPath=//tag_name[@attribute='value']

f. ex.:
//input[@type='text']
//input[@type='hidden'][@id='hdnOperation_1']


##########
# PART 2 #
##########


# Absolute XPath:
    - it contains the complete path from the root element of page to the desired element
    - absolute XPath starts with root node - single forward slash (/)
    - drawback of using absolute XPath - any slight change in DOM (Document Object Model) makes XPath invalid

f. ex.:
/html/body/div[2]/div/div/div[2]/div/div/div/input[2]

#  Relative XPath:
    - with relative XPath, the XPath starts from the mid of the HTML DOM structure
    - it begins with the double forward slash (//)
    - it is less brittle (more reliable)

f. ex.:
//*[@id="hdnOperation_1"]


##########
# PART 3 #
##########


# XPath function - 'starts-with'
    - 'starts-with' function is very helpful in finding dynamic webelements
    - you can use it to match the starting value of web element which remains static
      (ex. ID = session62354624, session76548765)
    - 'starts-with' function can also find the element whose attribute value is static
    
format:
XPath=//tag_name[starts-with(@attribute, 'value')]

f. ex.:
//input[starts-with(@id,'last_name')]   # 'last_name' is the static part of dynamic value


##########
# PART 4 #
##########


# XPath function - 'contains'
    - 'contains' function is used for finding dynamic web elements
    - you can provide any partial attribute value to find the webelement

format:
XPath=//tag_name[contains(@attribute, 'value')]

f. ex.:
//input[contains(@name,'mail')]  # HTML: <input ... name="adia353user[email]" ...>


##########
# PART 5 #
##########


# XPath function - 'text()' method
    - 'text()' method is used to find element with exact text match

format:
XPath=//tag_name[text()='actualtext']

f. ex.:
//a[text()='Terms of Use']  # HTML: <a href=...> Terms of Use </a>


##########
# PART 6 #
##########


# How to use AND & OR in Selenium XPath
    - AND & OR expressions can also be use in Selenium XPath expression
    - very helpful if you want to use more that two attributes to find element on webpage

format:
XPath=//tag_name[@attribute='value' or @attribute='value']
XPath=//tag_name[@attribute='value' and @attribute='value']

f. ex.:
//input[@type='text' and @name='user[first_name]']


##########
# PART 7 #
##########


# XPath axes methods (parent, child, self): it represents relationship to the context node, it is used in locating
  nodes relative to that node in the tree.
    - parent: selects the parent of the context (current) node,
      format: //tag_name[@attribute='value']//parent::tag_name

    - child: selects all children of the current node,
      format: //tag_name[@attribute='value']//child::tag_name

    - self: selects the current node,
      format: //tag_name[@attribute='value']//self::tag_name

f. ex.:
//select[@name='user[country]']//self::select
//select[@name='user[country]']//parent::form
//select[@name='user[country]']//child::option[1]   # option[n] select n-position child, n belongs to |N


##########
# PART 8 #
##########


# XPath axes methods (descendant, descendant-or-self)
    - descendant: it selects all of the descendants (children, grandchildren, etc.) of context (current) node
      format: //tag_name[@attribute='value']//descendant::tag_name

    - descendant-or-self: it selects context (current) node and all of its descendants like (children, grandchildren,
      etc.), if tag_name for descendants and self are the same
      format: //tag_name[@attribute='value']//descendant-or-self::tag_name

f. ex.:
//div[@class='signup_container']//descendant::div
//div[@class='signup_container']//descendant-or-self::div


##########
# PART 9 #
##########


# XPath axes methods (ancestor, ancestor-or-self)
    - ancestor: it selects all of the ancestors (parent, grandparent, etc.) of context (current) node
      format: //tag_name[@attribute='value']//ancestor::tag_name

    - ancestor-or-self: it selects context (current) node and all of its ancestors like (parent, grandparent, etc.),
      if tag_name for ancestors and self are the same
      format: //tag_name[@attribute='value']//ancestor-or-self::tag_name

f. ex.:
//*[@class='signup_container']//ancestor::div   # '*' at the beginning of XPath means any node at the particular page
//div[@class='signup_container']//ancestor-or-self::div[@id='content']


###########
# PART 10 #
###########


# XPath axes methods (following, following-sibling)
    - following: it selects all the nodes that appear after the context (current) node
      format: //tag_name[@attribute='value']//following::tag_name

    - following-siblings: it selects all the nodes that have the same parent as the context (current) node and appear
      after the context (current) node
      format: //tag_name[@attribute='value']//following-siblings::tag_name

f. ex.:
//option[@value='AG']//following::option    # mark all 'option' in the following HTML
//option[@value='AG']//following-sibling::option    # mark only siblings at following HTML - in this case 'option'


###########
# PART 11 #
###########


# XPath axes methods (preceding, preceding-sibling)
  - preceding: it selects all nodes that appear before the context (current) node
    format: //tag_name[@attribute='value']//preceding::tag_name

  - preceding-sibling: it selects all nodes that have the same parent as the context (current) node and appear before
    the context (current) node
    format: //tag_name[@attribute='value']//preceding-sibling::tag_name

f. ex.:
//option[@value='AG']//preceding::option    # mark all 'option' in the preceding HTML code
//option[@value='AG']//preceding-sibling::option    # mark only siblings at preceding HTML code - in this case 'option'

"""
