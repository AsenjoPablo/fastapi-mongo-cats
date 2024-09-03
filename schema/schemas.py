from models.cats import Cat


def individual_serializer(individual: Cat):
    return {
        'id': str(individual['_id']),   # mongodb object id
        'name': individual['name'],
        'age': individual['age'],
        'breed': individual['breed'],
        'image': individual['image'],
        'vaccinations': individual['vaccinations']
    }

def list_serial(individuals):
    return [individual_serializer(individual) for individual in individuals]