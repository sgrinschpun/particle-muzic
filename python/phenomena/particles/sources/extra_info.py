import json
#from os.path import expanduser, join

import pkg_resources
#HOME = expanduser("~")
#JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
path = 'particle_extra_info/part_extra_info.json'  # always use slash
JSON_PATH = pkg_resources.resource_filename(__name__, path)
XTRA_INFO = json.load(open(JSON_PATH))

COMP_NAME= {('c', 's', 's'): ['Omega_c0'], ('ubar', 'b'): ['B-'], ('sbar', 'sbar', 'bbar'): ['Omega_bbar+'], ('d', 'dbar'): ['pi0'],('u', 'ubar'): ['pi0'], ('d', 'c', 's'): ['Xi_cbar0'], ('dbar', 'c'): ['D+'], ('ubar', 'ubar', 'cbar'): ['Sigma_cbar--'], ('d', 's', 'b'): ['Xi_b-'], ('b', 'bbar'): ['Upsilon'], ('u', 'u', 'u'): ['Delta++'], ('c', 'sbar'): ['D_s+'], ('u', 'u', 'd'): ['p+','Delta+'], ('u', 'u', 's'): ['Sigma+'], ('s', 's','s'): ['Omega-'], ('s', 'sbar'): ['phi'], ('u', 's', 's'): ['Xi0'], ('d', 'd', 'd'): ['Delta-'], ('ubar', 's'): ['K-'], ('s', 's', 'b'): ['Omega_b-'], ('ubar', 'ubar', 'ubar'): ['Deltabar--'], ('u', 's', 'b'): ['Xi_b0'], ('u', 'u', 'c'): ['Sigma_c++'], ('dbar', 'sbar', 'bbar'): ['Xi_bbar+'], ('d', 'd', 'b'): ['Sigma_b-'], ('u', 'dbar'): ['pi+','rho+'], ('u', 'c', 's'): ['Xi_c+'], ('dbar', 'sbar', 'sbar'): ['Xibar+'], ('d', 'bbar'): ['B0'], ('s', 'bbar'): ['B_s0'], ('u', 'd', 'c'): ['Sigma_c+'], ('c', 'cbar'): ['J/psi'], ('u', 'sbar'): ['K+'], ('ubar', 'cbar', 'sbar'): ['Xi_cbar-'], ('d', 'd', 's'): ['Sigma-'], ('ubar', 'd'): ['pi-'], ('u', 'bbar'): ['B+'], ('c', 'bbar'): ['B_c+'], ('u', 'd', 'd'): ['n0','Delta0','Sigma0','Lambda0'], ('d', 'sbar'): ['K0'], ('ubar', 'c'): ['D0'], ('ubar', 'ubar', 'dbar'): ['pbar-'], ('sbar', 'sbar', 'sbar'): ['Omegabar+'], (): ['Z0'], ('u', 'u', 'b'): ['Sigma_b+'], ('d', 'cbar'): ['D-'], ('d', 's', 's'): ['Xi-'],('ubar', 'dbar', 'cbar'): ['Sigma_cbar-']}

basic_particle_array = ['u','ubar','s','sbar','t','tbar','b','bbar','c','cbar','d','dbar','e+','e-','g','gamma','h0(H_1)','mu+','mu-','tau+','tau-','nu_e','nu_ebar','nu_mu','nu_mubar','nu_tau','nu_taubar','W+','W-','Z0','pi+','pi-','pi0','K+','K-','K0','J/psi','phi','Upsilon','B0','B+','B-','B_s0','B_c+','D+','D-','D0','D_s+','n0','p+','pbar-','Omega-','Omegabar+','Omega_c0','Omega_b-','Omega_bbar+','Xi0','Xi-','Xibar+','Xi_b0','Xi_b-','Xi_bbar+','Xi_cbar0','Xi_cbar-','Xi_c+','Sigma-','Sigma+','Sigma_b-','Sigma_b+','Sigma_cbar-','Sigma_cbar--','Sigma_c+','Sigma_c++','Delta++','Delta-','Deltabar--','pbar-']

class ExtraInfoFetcher(object):

    @staticmethod
    def getComposition(pdgid):
        composition =[]
        try:
            if XTRA_INFO[str(pdgid)]['composition'] != []:
                for quark in XTRA_INFO[str(pdgid)]['composition'][0]: #only consider first superposition of quarks
                    composition.append(quark.encode('utf-8'))
        except KeyError:
            composition =[]
        finally:
            return composition

    @staticmethod
    def getType(pdgid):
        try:
            type = XTRA_INFO[str(pdgid)]['type'].encode('utf-8')
        except KeyError:
            type = 'quark'
        finally:
            return type

    @staticmethod
    def getParticleByComposition(composition):
        try:
            name_array = COMP_NAME[composition]
        except:
            name_array = []
        finally:
            return name_array
