"""
Problem: You are given some data containing {employee, manager} pairs, please build an organization chart from this set of data. 
Some sample input and output  can be found at the bottom.

Task: Implement the build_org_chart function

Each report (employee) should occupy one row with their names printed one column deeper than their managers, indented by dashes (-)

Reports should have one more dash than their respective managers. The top-level manager should not be indented. (See sample output below)

Reports should be sorted alphabetically at each level

Assume each report only has one manager

Assume there is only one top-level manager

Assume all names are unique

OPTIONAL

If there are no top level managers, the function should throw an error

If there is a circular chain of command, the function should throw an error. (i.e. Employee A -> Employee B -> Employee C -> Employee A)

Expectations:

All tests should pass
"""

class InputError(RuntimeError):
    pass

def indent(n):
    return "-" * n

def build_org_chart(employee_manager_pairs):
    # the root node has no manager
    root = None
    # keyed by manager name
    # G[jared] = [array of jared reports]
    G = {}
    pairs = employee_manager_pairs
    
    # READING DATA
    # o(N) if N number of pairs
    # push o(M) if M maximun number of employees
    for p in pairs:
        employee = p['employee']
        manager = p['manager']
        

        if manager and G.get(manager) is None:
            G[manager] = []
        elif not manager :
            # root
            root = employee
            if G.get(root) is None:
                G[root] = []
       
        if manager and employee:
            G[manager].append(employee)

    if root is None:
        raise InputError('no root')

    # SORTING DATA
    # we have all in a graph but it is not sorted alphabetically
    # if we sort is O(MlogM) on O(K) k being number of managers
    for k in G.keys():
        (G[k]).sort(reverse=True)

    # PRINTING DATA
    # now printing starting with root node
    queue = []
    queue.append((root,0))
    
    visited = {}

    output = ''

    while (len(queue)> 0):
        (node, _indent)  = queue.pop()
        if visited.get(node) is not None:
            # mmm circular reference
            raise InputError('circular reference')
        visited[node] = 1
        output  += indent(_indent)
        output += node
        output += "\n"
        if G.get(node) is not None:
            for n in G[node]:
                queue.append((n, _indent + 1))


    return output



    


org_data = [
  { "employee": "jared", "manager": "beck" },
  { "employee": "sofia", "manager": "beck" },
  { "employee": "carl", "manager": "jared" },
  { "employee": "luka", "manager": "sofia" },
  { "employee": "safiyyah", "manager": "sofia" },
  { "employee": "lex", "manager": "carl" },
  { "employee": "julia", "manager": "sofia" },
  { "employee": "edward", "manager": "sofia" },
  { "employee": "patty", "manager": "carl" },
  { "employee": "lorenzo", "manager": "beck" },
  { "employee": "beck", "manager": "" },
  { "employee": "mike", "manager": "sofia" },
  { "employee": "jess", "manager": "carl" },
  { "employee": "tess", "manager": "beck" },
  { "employee": "polly", "manager": "beck" },
  { "employee": "summer", "manager": "carl" },
  { "employee": "jack", "manager": "carl" },
  { "employee": "kylo", "manager": "beck" },
  { "employee": "dione", "manager": "carl" },
  { "employee": "jon", "manager": "carl" },
  { "employee": "matt", "manager": "sofia" },
  { "employee": "zach", "manager": "sofia" },
  { "employee": "luke", "manager": "carl" },
  { "employee": "tom", "manager": "beck" },
  { "employee": "chris", "manager": "sofia" },
  { "employee": "alisa", "manager": "carl" },
  { "employee": "jeff", "manager": "carl" },
  { "employee": "ashelee", "manager": "carl" },
  { "employee": "louis", "manager": "sofia" },
  { "employee": "maisy", "manager": "edward" },
  { "employee": "tammy", "manager": "tom" },
  { "employee": "jay", "manager": "edward" },
  { "employee": "jonathan", "manager": "louis" },
  { "employee": "vince", "manager": "edward" },
  { "employee": "billy", "manager": "carl" },
  { "employee": "bruno", "manager": "carl" },
]


output = """
beck
-jared
--carl
---alisa
---ashelee
---billy
---bruno
---dione
---jack
---jeff
---jess
---jon
---lex
---luke
---patty
---summer
-kylo
-lorenzo
-polly
-sofia
--chris
--edward
---jay
---maisy
---vince
--julia
--louis
---jonathan
--luka
--matt
--mike
--safiyyah
--zach
-tess
-tom
--tammy
"""


no_top_level_org_data = [
  { "employee": "jared", "manager": "beck" },
  { "employee": "sofia", "manager": "beck" },
  { "employee": "carl", "manager": "jared" },
  { "employee": "luka", "manager": "sofia" },
  { "employee": "safiyyah", "manager": "sofia" },
  { "employee": "lex", "manager": "carl" },
  { "employee": "julia", "manager": "sofia" },
  { "employee": "edward", "manager": "sofia" },
  { "employee": "patty", "manager": "carl" },
  { "employee": "lain", "manager": "beck" },
  { "employee": "mike", "manager": "sofia" },
  { "employee": "jess", "manager": "carl" },
  { "employee": "tess", "manager": "beck" },
  { "employee": "polly", "manager": "beck" },
  { "employee": "summer", "manager": "carl" },
  { "employee": "jack", "manager": "carl" },
  { "employee": "bianca", "manager": "beck" },
  { "employee": "dione", "manager": "carl" },
  { "employee": "jon", "manager": "carl" },
  { "employee": "matt", "manager": "sofia" },
  { "employee": "zach", "manager": "sofia" },
  { "employee": "luke", "manager": "carl" },
  { "employee": "tom", "manager": "beck" },
  { "employee": "chris", "manager": "sofia" },
  { "employee": "alisa", "manager": "carl" },
  { "employee": "jeff", "manager": "carl" },
  { "employee": "ashelee", "manager": "carl" },
  { "employee": "louis", "manager": "sofia" },
  { "employee": "maisy", "manager": "edward" },
  { "employee": "tammy", "manager": "tom" },
  { "employee": "jay", "manager": "edward" },
  { "employee": "jonathan", "manager": "louis" },
  { "employee": "vince", "manager": "edward" },
  { "employee": "billy", "manager": "carl" },
  { "employee": "bruno", "manager": "carl" },
]

circular_org_data = [
  { "employee": "beck", "manager": "" },
  { "employee": "jared", "manager": "beck" },
  { "employee": "sofia", "manager": "beck" },
  { "employee": "carl", "manager": "jared" },
  { "employee": "luka", "manager": "sofia" },
  { "employee": "safiyyah", "manager": "sofia" },
  { "employee": "lex", "manager": "carl" },
  { "employee": "julia", "manager": "sofia" },
  { "employee": "edward", "manager": "sofia" },
  { "employee": "patty", "manager": "carl" },
  { "employee": "lain", "manager": "beck" },
  { "employee": "mike", "manager": "sofia" },
  { "employee": "jess", "manager": "carl" },
  { "employee": "tess", "manager": "beck" },
  { "employee": "polly", "manager": "beck" },
  { "employee": "summer", "manager": "carl" },
  { "employee": "jack", "manager": "carl" },
  { "employee": "bianca", "manager": "beck" },
  { "employee": "dione", "manager": "carl" },
  { "employee": "jon", "manager": "carl" },
  { "employee": "matt", "manager": "sofia" },
  { "employee": "zach", "manager": "sofia" },
  { "employee": "luke", "manager": "carl" },
  { "employee": "tom", "manager": "beck" },
  { "employee": "chris", "manager": "sofia" },
  { "employee": "jared", "manager": "lex" },
  { "employee": "alisa", "manager": "carl" },
  { "employee": "jeff", "manager": "carl" },
  { "employee": "ashelee", "manager": "carl" },
  { "employee": "louis", "manager": "sofia" },
  { "employee": "maisy", "manager": "edward" },
  { "employee": "tammy", "manager": "tom" },
  { "employee": "jay", "manager": "edward" },
  { "employee": "jonathan", "manager": "louis" },
  { "employee": "vince", "manager": "edward" },
  { "employee": "billy", "manager": "carl" },
  { "employee": "bruno", "manager": "carl" },
]


import unittest

class Testing(unittest.TestCase):

    def test_build_org_chart(self):
        print output.strip()
        print build_org_chart(org_data)
        assert build_org_chart(org_data) == output.strip()

    def test_build_org_chart_no_top_level(self):
        with self.assertRaises(InputError):
            build_org_chart(no_top_level_org_data)

    def test_build_org_chart_circular_org(self):
        with self.assertRaises(InputError):
            build_org_chart(circular_org_data)

# Optional Below
'''


'''

unittest.main().result
