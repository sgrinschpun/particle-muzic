import json

from particle import ParticleDT

def particle_json(name):
    params = {}
    particle = ParticleDT(name)
    params['name']=particle.name
    params['type']=particle.type
    params['mass']=particle.mass
    params['charge']=particle.charge
    params['composition']=particle.composition
    params['decay']=particle.decay
    params['time_to_decay']=particle.time_to_decay
    return json.dumps(params)
