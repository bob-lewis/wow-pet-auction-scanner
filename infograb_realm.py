__author__ = 'Bob'
import httplib2,json
PET_QUALITY = [ 'Poor', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary','unknown']

'''{
"realm":{"name":"Kilrogg","slug":"kilrogg"},
"auctions":{"auctions":[
    {"auc":497943703,"item":15892,"owner":"Herancal","ownerRealm":"Nagrand","bid":8132000,"buyout":8560000,"quantity":1,"timeLeft":"VERY_LONG","rand":0,"seed":0,"context":0},
    {"auc":496450200,"item":33568,"owner":"Ergotron","ownerRealm":"Runetotem","bid":382723,"buyout":425249,"quantity":11,"timeLeft":"MEDIUM","rand":0,"seed":0,"context":0},
'''
def petid_get_new(id):
    request = str('http://eu.battle.net/api/wow/battlePet/species/' + id)
    h = httplib2.Http(".cache",timeout = 60)
    content_headers, content = h.request(request)
    content = content.decode()
    obj = json.loads(content)

    if 'creatureId' in obj:

        return (obj['name'])
    else:
        return 'unknown pet'


def realmget(auc_api):
    auc_list = []
    print('Calculating ,please wait')
    h = httplib2.Http(".cache", timeout = 60)
    content_headers, content = h.request(auc_api)
    content = content.decode()
    obj = json.loads(content)
    x=( obj['auctions'])
    y=x['auctions']
    for i in y:
        if  (i['item'])==82800:
            temp_list=[]
            temp_list.append(i['owner'])
            temp_list.append(i['ownerRealm'])
            temp_list.append(i['buyout'])
            check=str(i['petSpeciesId'])
            id = petid_get_new(check)
            x=int((i['petQualityId']))
            quality = PET_QUALITY[x]
            petname = str(id + ' of ' + quality + ' quality.')
            temp_list.append(petname)
            temp_list.append(i['petBreedId'])
            #print(temp_list)
            auc_list.append(temp_list)
    return auc_list


def write_to_master(auc_list):
	with open('temp.txt', 'a') as master:
		for line in auc_list:
			master.write(str(line))

	print('details written to bargains.txt')

