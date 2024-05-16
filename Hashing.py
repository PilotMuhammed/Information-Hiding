'''
Requirements:
- Hashlib pckg.

'''

import hashlib
def generate_fingerprint(data):

 if not isinstance(data, bytes):
    data = data.encode('utf-8')
 hash_obj = hashlib.sha256()
 hash_obj.update(data)
 fingerprint = hash_obj.hexdigest()
 return fingerprint

def verify_fingerprint(data, expected_fingerprint):
# Generate the fingerprint for the given data
  actual_fingerprint = generate_fingerprint(data)

# Compare the generated fingerprint with the expected fingerprint
  return actual_fingerprint == expected_fingerprint



sample_text = "Hello, world!"
expected_fingerprint = generate_fingerprint(sample_text)
print(f"Expected Fingerprint of '{sample_text}': {expected_fingerprint}")
print('-------------------------------')
# Verifying the fingerprint
verification_result = verify_fingerprint(sample_text, expected_fingerprint)
print(f"Does the hash match? {verification_result}")
print('-------------------------------')
# Example with an incorrect hash
incorrect_fingerprint = "abcdef1234567890" # Example incorrect hash
verification_result_incorrect = verify_fingerprint(sample_text, incorrect_fingerprint)
print(f"Does the hash match with incorrect hash? {verification_result_incorrect}")
