import googlemaps

gmaps = googlemaps.Client(key="") #Add token

address = "4100 SE Stark Street, Portland, OR 97214"

def recursive_function(address, neighborhood=None):
    lat, lng = set_lat_and_lng(address)
    aux_neighborhood = set_neighborhood(lat, lng)

    if neighborhood and neighborhood != aux_neighborhood:
        return f"The first different neighborhood found is {aux_neighborhood} corresponding to the address {address}" 
    else:
        address_split = address.split(" ")
        firts_block_replaced = int(address_split[0]) + 100
        rest_addres = address_split[1:]
        rest_addres.insert(0, str(firts_block_replaced))
        new_addres = ' '.join(rest_addres)
        return recursive_function(new_addres, aux_neighborhood)

def set_lat_and_lng(address):
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    return lat, lng

def set_neighborhood(lat, lng):
    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    for element in reverse_geocode_result[0]['address_components']:
        if 'neighborhood' in element['types']:
            neighborhood = element['long_name']
            return neighborhood
