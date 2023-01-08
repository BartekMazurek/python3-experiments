# GENERATOR FUNCTION
# YIELD NEW (NEXT) VALUE ON EVERY CALL
# KEEPS LOCAL STATE AFTER CALL & YIELDS NEXT VALUE IN NEXT CALL

def generate_even_numbers():
    for element in range(10000):
        if (element % 2) == 0:
            yield element


# CREATES GENERATOR
numberGenerator = generate_even_numbers()
print(list(numberGenerator))
