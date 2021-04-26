import json
import nltk
import collections

# convenient methods to extract text from input data

Point = collections.namedtuple('Point', ['x', 'y'])


def get_display_coordinates(content_dict):
    if 'DISPLAY' in content_dict:
        if content_dict["DISPLAY"]["latitude"] and content_dict["DISPLAY"]["longitude"]:
            display_cord = Point(content_dict["DISPLAY"]["latitude"], content_dict["DISPLAY"]["longitude"])
            return display_cord
    return "NotFound"


def get_routing_coordinates(content_dict):
    if "ROUTING" in content_dict:
        if content_dict["ROUTING"]["latitude"] and content_dict["ROUTING"]["longitude"]:
            routing_cord = Point(content_dict["ROUTING"]["latitude"], content_dict["ROUTING"]["longitude"])
            return routing_cord
    return "NotFound"


# returns unparsed address
def get_address(content_dict):
    address_list = []
    if "town" in content_dict:
        address_list.append(content_dict["town"])
    if "city" in content_dict:
        address_list.append(content_dict["city"])
    if "district" in content_dict:
        address_list.append(content_dict["district"])
    if "state" in content_dict:
        address_list.append(content_dict["state"])

    return ' '.join(address_list)


def get_name(content_dict):
    if "name" in content_dict:
        return content_dict["name"]
    return "NotFound"


def get_id(content_dict):
    if "placeid" in content_dict:
        return content_dict["placeid"]
    return "NotFound"


def remove_duplicates(address):
    nltk_tokens = nltk.word_tokenize(address)
    ordered_tokens = set()
    result = []
    for word in nltk_tokens:
        if word not in ordered_tokens:
            ordered_tokens.add(word)
            result.append(word)
    return ' '.join(result)

# with open("single_output.txt",encoding="utf8") as f:
#     content = f.read()
#     content_dict = json.loads(content)
#     d = get_display_coordinates(content_dict)
#     print(d)
#     print(d['lat'])
#     print(content)



