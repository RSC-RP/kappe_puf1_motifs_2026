import json
import sys

infile = sys.argv[1]
outprefix = sys.argv[2]

with open(infile, mode = 'rt') as incon:
    myjson = json.load(incon)

myjson['records'][4]['attributes']

test = [rec['attributes']['predicted_go_function'] for rec in myjson['records']]
test = [t for t in test if t != None]

test = [rec['attributes']['predicted_go_id_function'] for rec in myjson['records']]
test = [t for t in test if t != None]

#len(test)

#len(myjson['records'])

function_dict1 = dict()
component_dict1 = dict()
process_dict1 = dict()
function_dict2 = dict()
component_dict2 = dict()
process_dict2 = dict()

for rec in myjson['records']:
    gn = rec['displayName']
    func1 = rec['attributes']['predicted_go_function']
    comp1 = rec['attributes']['predicted_go_component']
    proc1 = rec['attributes']['predicted_go_process']
    func2 = rec['attributes']['annotated_go_function']
    comp2 = rec['attributes']['annotated_go_component']
    proc2 = rec['attributes']['annotated_go_process']

    if func1 != None:
        funcs = func1.split(';')
        for f in funcs:
            if f in function_dict1.keys():
                function_dict1[f].append(gn)
            else:
                function_dict1[f] = [gn]
    if func2 != None:
        funcs = func2.split(';')
        for f in funcs:
            if f in function_dict2.keys():
                function_dict2[f].append(gn)
            else:
                function_dict2[f] = [gn]
    if comp1 != None:
        funcs = comp1.split(';')
        for f in funcs:
            if f in component_dict1.keys():
                component_dict1[f].append(gn)
            else:
                component_dict1[f] = [gn]
    if comp2 != None:
        funcs = comp2.split(';')
        for f in funcs:
            if f in component_dict2.keys():
                component_dict2[f].append(gn)
            else:
                component_dict2[f] = [gn]
    if proc1 != None:
        funcs = proc1.split(';')
        for f in funcs:
            if f in process_dict1.keys():
                process_dict1[f].append(gn)
            else:
                process_dict1[f] = [gn]
    if proc2 != None:
        funcs = proc2.split(';')
        for f in funcs:
            if f in process_dict2.keys():
                process_dict2[f].append(gn)
            else:
                process_dict2[f] = [gn]

#len(function_dict1)  # 771
#len(function_dict2)  # 282
#len(component_dict1) # 222
#len(component_dict2) # 177

out1 = f"{outprefix}_GO_predicted_function.json"
out2 = f"{outprefix}_GO_annotated_function.json"
out3 = f"{outprefix}_GO_predicted_component.json"
out4 = f"{outprefix}_GO_annotated_component.json"
out5 = f"{outprefix}_GO_predicted_process.json"
out6 = f"{outprefix}_GO_annotated_process.json"

with open(out1, mode = 'w') as outcon:
    json.dump(function_dict1, outcon)
with open(out2, mode = 'w') as outcon:
    json.dump(function_dict2, outcon)
with open(out3, mode = 'w') as outcon:
    json.dump(component_dict1, outcon)
with open(out4, mode = 'w') as outcon:
    json.dump(component_dict2, outcon)
with open(out5, mode = 'w') as outcon:
    json.dump(process_dict1, outcon)
with open(out6, mode = 'w') as outcon:
    json.dump(process_dict2, outcon)
