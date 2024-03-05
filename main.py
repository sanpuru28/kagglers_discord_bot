from kaggle import KaggleApi

api = KaggleApi()
api.authenticate()
print(type(api))


competitions = api.competitions_list(search='titanic')
for competition in competitions:
    print(competition.ref)
