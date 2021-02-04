# -*-coding:utf8-*-
import random
from CryptoBaseWeb.abenc_bsw07 import *
from base.models import *


class RegistrationCenter:
    def __init__(self):
        self.groupObj = PairingGroup('SS512')
        self.cpabe = CPabe_BSW07(self.groupObj)
        (self.pk, self.mk) = self.cpabe.setup()

    def initation(self):
        cs_secret_key = [random.getrandbits(1024), random.getrandbits(1024)]

        MK = str(self.mk)
        service_key_01 = str(cs_secret_key[0])
        service_key_02 = str(cs_secret_key[1])
        g = self.groupObj.serialize(self.pk['g'])
        g2 = self.groupObj.serialize(self.pk['g2'])
        h = self.groupObj.serialize(self.pk['h'])
        f = self.groupObj.serialize(self.pk['f'])
        e_gg_alpha = self.groupObj.serialize(self.pk['e_gg_alpha'])
        self.PPK = {'g': g, 'g2': g2, 'h': h, 'f': f, 'e_gg_alpha': e_gg_alpha}

        BaseInformation.objects.create(service_id=1, service_key=service_key_01, tpk=str(self.PPK), mk=MK)
        BaseInformation2.objects.create(service_id=2, service_key=service_key_02, tpk=str(self.PPK), mk=MK)

    def smart_car(self, user_id, mNBPW):
        global service_key_01, service_key_02
        pair_key_01 = random.getrandbits(1024)
        pair_key_02 = random.getrandbits(1024)
        # conn_01 = sqlite3.connect('service_01.db')
        # conn_02 = sqlite3.connect('service_02.db')
        # c_01 = conn_01.cursor()
        # c_02 = conn_02.cursor()
        # cursor_01 = c_01.execute("SELECT service_key  from main.base_information")
        # for row_01 in cursor_01:
        #     service_key_01 = row_01[0]
        # cursor_02 = c_02.execute("SELECT service_key  from main.base_information")
        # for row_02 in cursor_02:
        #     service_key_02 = row_02[0]

        # c_01.execute("insert into main.authentica_information(user_id, user_fake_id, pair_key) "
        #              "values (\"{}\", \"{}\", \"{}\")".format(user_id, user_id + 200, str(pair_key_01)))
        # c_02.execute("insert into main.authentica_information(user_id, user_fake_id, pair_key) "
        #              "values (\"{}\", \"{}\", \"{}\")".format(user_id, user_id + 200, str(pair_key_02)))
        #
        # conn_01.commit()
        # conn_02.commit()
        # conn_01.close()
        # conn_02.close()

        service_key_01 = BaseInformation.objects.get(service_id=1)
        service_key_01 = service_key_01.service_key
        service_key_02 = BaseInformation2.objects.get(service_id=2)
        service_key_02 = service_key_02.service_key
        user_fake_id = int(user_id) + 200
        Authentic.objects.create(user_id=int(user_id), user_fake_id=user_fake_id, pair_key=str(pair_key_01))
        Authentic2.objects.create(user_id=int(user_id), user_fake_id=user_fake_id, pair_key=str(pair_key_02))

        M_01 = hash(str(hash(int(pair_key_01) ^ int(user_id))) + str(service_key_01))
        M_02 = hash(str(hash(int(pair_key_02) ^ int(user_id))) + str(service_key_02))
        N_01 = M_01 ^ mNBPW
        N_02 = M_02 ^ mNBPW
        NId_cs_01 = hash(str(1) + service_key_01)
        NId_cs_02 = hash(str(2) + service_key_02)
        # user temple_id ##############################################
        temple_user_id = int(user_id) + 200
        #
        attrs_01 = ['ONE', 'TWO', 'THREE']
        attrs_02 = ['ONE', 'TWO', 'THREE']
        sk_01 = self.cpabe.keygen(self.pk, self.mk, attrs_01)
        sk_02 = self.cpabe.keygen(self.pk, self.mk, attrs_02)

        sk_01 = RegistrationCenter.serialization(self, sk_01)
        sk_02 = RegistrationCenter.serialization(self, sk_02)

        service_result_01 = [1, N_01, NId_cs_01, attrs_01, sk_01]
        service_result_02 = [2, N_02, NId_cs_02, attrs_02, sk_02]
        sr = [service_result_01, service_result_02]
        smart_car_result = [temple_user_id, sr, self.PPK]

        return smart_car_result

        # base information
        # service id, service_key , master_key, master_public_key

    # def sezerlize(self, aim_dict):
    #     for index in aim_dict:
    #         temple = aim_dict[index]
    #         print(type(temple))
    #         aim_dict[index] = self.groupObj.serialize(temple)
    #     print(aim_dict)
    #     return aim_dict

    def serialization(self, original_sk):
        # groupObj = PairingGroup('SS512')  # temple

        D = original_sk['D']
        Dj = original_sk['Dj']
        Djp = original_sk['Djp']
        S = original_sk['S']

        # serialization D
        D = self.groupObj.serialize(D)

        # serialization Dj
        Dj_ONE = Dj['ONE']
        Dj_TWO = Dj['TWO']
        Dj_THREE = Dj['THREE']

        Dj_ONE = self.groupObj.serialize(Dj_ONE)
        Dj_TWO = self.groupObj.serialize(Dj_TWO)
        Dj_THREE = self.groupObj.serialize(Dj_THREE)

        Dj = {'ONE': Dj_ONE, 'TWO': Dj_TWO, 'THREE': Dj_THREE}

        # serialization Djp
        Djp_ONE = Djp['ONE']
        Djp_TWO = Djp['TWO']
        Djp_THREE = Djp['THREE']

        Djp_ONE = self.groupObj.serialize(Djp_ONE)
        Djp_TWO = self.groupObj.serialize(Djp_TWO)
        Djp_THREE = self.groupObj.serialize(Djp_THREE)

        Djp = {'ONE': Djp_ONE, 'TWO': Djp_TWO, 'THREE': Djp_THREE}

        # s is list

        return {'D': D, 'Dj': Dj, 'Djp': Djp, 'S': S}
