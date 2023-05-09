import pandas as pd
import json

# Formatting each frame

def coordinate_from_array(array):
    #array: [<frame_id>, <object_class>, <x>, <y>]
    frame, id, x ,y = array
    labelN = {
        'frame': frame, #int: frame id
        'id': id, #int: object id
        'x': x, #int: x coordinate
        'y': y  #int: y coordinate
    }
    return labelN


## ! convert from yolo output to csv format

# def coordinate_from_yolo(frame, array):
#     #array: [<object_class>, <x>, <y>, <width>, <height>]
#     id, x, y, _, _ = array
#     labelN = {
#         'frame': frame, #int: frame id
#         'id': id, #int: object id
#         'x': x, #int: x coordinate
#         'y': y  #int: y coordinate
#     }
#     return labelN


# This function saves a list of dictionaries to a csv file
def saveList(list_with_values: list, path: str):
    df = pd.DataFrame(list_with_values)
    df = df.sort_values(by = ['hexbug', 't'],ignore_index=True) # we sort the values by hexbug and frame
    # now the values are in the correct order, so we save the csv file
    print('Saving to csv')
    df.to_csv(path)
    print('Done')
    

def tracoToCsv(traco_path, csv_path):
    print('Opening file: ', traco_path)
    with open(traco_path, 'r') as traco_file:
        rois = json.load(traco_file)['rois']
    
    tmp = [] # -> creating an empty list to append the values contained in "rois"
    for roi in rois:
        # we create a dictionary for each roi in the correct format
        e = {
            't': roi['z'],
            'hexbug': roi['id'],
            'x': roi['pos'][0],
            'y': roi['pos'][1]
        }
        # and we append it to the list
        tmp.append(e)
    # we save the list to a csv file
    saveList(tmp, csv_path)



def fromArrayToDict(array, tmp = None):
    #array: [<frame_id>, <object_class>, <x>, <y>]
    #array: [<frame>, <hexbug_id>, <x>, <y>]
    frame, id, x ,y = array
    if tmp is None: # --> If there is no list to append the values contained in "array" we create an empty list
        tmp = []
    # we create a dictionary for each roi in the correct format
    e = {
            't': frame,
            'hexbug': id,
            'x': x,
            'y': y
        }
    tmp.append(e)
    return tmp


if __name__ == "__main__":

    ## Example 1
    tracoToCsv("./traco_example.traco", "example1.csv")


    # Example 2: 
    list_with_data = [[0,0,609.1475208527264,177.84445391353734],
    [0,1,822.7252539996302,92.57577718188634],
    [0,2,897.9980055112678,156.73480170667477],
    [0,3,546.1093810385692,870.4226598045357],
    [1,0,583.1608765154604,97.44827299511995],
    [1,1,817.8527581863927,86.07911609756982],
    [1,2,872.8600104439311,128.31793771751148],
    [1,3,436.8137503110175,858.400140424505]]

    tmp = [] # you can skip this step
    for val in list_with_data: 
        tmp = fromArrayToDict(val,tmp) #  fromArrayToDict(val)

    saveList(tmp, "example2.csv")