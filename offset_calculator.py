# GHT NH 3/4in 11.5TPI
tpi = 11.5  # threads per inch
angle = 60  # degrees
major_diameter_external = 1.0625
major_diameter_internal = 1.0725
minor_diameter_external = 0.9495
minor_diameter_internal = 0.9595
pitch_diameter_external = 1.0060
pitch_diameter_internal = 1.0160

# widening for 3DP tolerance differences
internal_offset = 0.010  # A little less for external because of shrinkage
external_offset = 0.015

made_new = major_diameter_external-external_offset
madi_new = major_diameter_internal+internal_offset
mide_new = minor_diameter_external-external_offset
midi_new = minor_diameter_internal+internal_offset
pide_new = made_new - ((made_new-mide_new)/2)
pidi_new = madi_new - ((madi_new-midi_new)/2)


print("NEW VALUES")
print(f"Major Diameter External: {made_new}")
print(f"Pitch Diameter External: {pide_new}")
print(f"Minor Diameter External: {mide_new}")

print(f"Major Diameter Internal: {madi_new}")
print(f"Pitch Diameter Internal: {pidi_new}")
print(f"Minor Diameter Internal: {midi_new}")
