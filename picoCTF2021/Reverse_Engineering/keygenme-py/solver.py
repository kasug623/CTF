import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"

username_trial = b"FRASER"

key = ""
key += hashlib.sha256(username_trial).hexdigest()[4]
key += hashlib.sha256(username_trial).hexdigest()[5]
key += hashlib.sha256(username_trial).hexdigest()[3]
key += hashlib.sha256(username_trial).hexdigest()[6]
key += hashlib.sha256(username_trial).hexdigest()[2]
key += hashlib.sha256(username_trial).hexdigest()[7]
key += hashlib.sha256(username_trial).hexdigest()[1]
key += hashlib.sha256(username_trial).hexdigest()[8]

print(key_part_static1_trial + key + key_part_static2_trial)