"""
Test the Linked list functionalities using pytest. 
@ Bhaskara Rao Karri,
Date : 09/07/2020.
"""

# Import required modules on here
import pytest

from linkedlist_lib.main import OpeartionsNode

o = OpeartionsNode() # Create Object on here for OpeartionsNode and reference to variable
# This test case only for inter are passed in place of nodes
def test_node_operation_integers():
    """ In this testcase suppose you are passing the integers type of data it can 
         access and it returns the excepted OutPut."""
    # Checking the Conditions on here
    assert o.delete_node(-1) == "No nodes are delete purpose"
    assert o.display_node() == "we don't have any nodes yet for Display Purpose"
    assert o.create_node(10,-1) == 10
    assert o.create_node(20,-1) == 20
    assert o.create_node(30,-1) == 30
    assert o.create_node(40,-1) == 40
    assert o.create_node(5,0) == 5
    assert o.create_node(0,0) == 0
    assert o.display_node() == [0,5,10,20,30,40]
    assert o.delete_node(-1) == True  
    assert o.display_node() == [0,5,10,20,30]
    assert o.delete_node(0) == True
    assert o.display_node() == [5,10,20,30]
    assert o.create_node(50,8) ==  " you can assign the 0 or -1th position "# int type of Value
    assert o.create_node(44,-6) ==  " you can assign the 0 or -1th position "# int type of Value
    assert o.display_node() == [5,10,20,30]
    
# This test case you passed except integer  in place of nodes
def test_node_except_integer():
    """ In this testcase suppose you are passing the except integers type of data it won't accept 
        and it returns the False."""
    # Checking the Conditions on here
    assert o.create_node(50.0,1) ==  False# float type of Value
    assert o.create_node("bha",8) == False # string type of Value
    assert o.create_node([1,2,3],0) == False# list type of Value
    assert o.create_node((1,2,3),-1) == False # tuple type of Value
    assert o.create_node({'x':1,'y':2},-5) ==False # dict type of Value
    assert o.create_node({1,2,3},0) == False # set type of Value
    assert o.create_node(True,1) == False # bool type of Value
    assert o.display_node() ==  [5,10,20,30] # display result
    assert o.delete_node(0) == True 
    assert o.display_node() ==  [10,20,30] # display result
    assert o.delete_node(-1) == True 
    assert o.display_node() == [10,20] # display result