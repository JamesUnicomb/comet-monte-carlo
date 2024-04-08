from datetime import datetime
from load_gmat import gmat
from get_data import get_space_weather

epoch = datetime(2024, 4, 5, 4, 14, 46, 144996)
epochstr = epoch.strftime("%d %b %Y %H:%M:%S.%f")[:-3]

# Spacecraft configuration preliminaries
earthorb = gmat.Construct("Spacecraft", "EarthOrbiter")
earthorb.SetField("DateFormat", "UTCGregorian")
earthorb.SetField("Epoch", epochstr)

earthorb.SetField("CoordinateSystem", "EarthMJ2000Eq")
earthorb.SetField("DisplayStateType", "Cartesian")

# Orbital state
earthorb.SetField("X", 2018.8192616038249)
earthorb.SetField("Y", -2018.819261603827)
earthorb.SetField("Z", -7778.562873085272)
earthorb.SetField("VX", 5.226958779501885)
earthorb.SetField("VY", 5.226958779501884)
earthorb.SetField("VZ", -1.3748259907794183e-15)

# Spacecraft ballistic properties for the SRP and Drag models
earthorb.SetField("SRPArea", 2.5)
earthorb.SetField("Cr", 1.75)
earthorb.SetField("DragArea", 1.8)
earthorb.SetField("Cd", 2.1)
earthorb.SetField("DryMass", 80)

# Force model settings
fm = gmat.Construct("ForceModel", "FM")
fm.SetField("CentralBody", "Earth")

# An 21x21 JGM-3 Gravity Model
earthgrav = gmat.Construct("GravityField")
earthgrav.SetField("BodyName", "Earth")
earthgrav.SetField("PotentialFile", "../data/gravity/earth/JGM3.cof")
earthgrav.SetField("Degree", 21)
earthgrav.SetField("Order", 21)

# The Point Masses
moongrav = gmat.Construct("PointMassForce", "MoonGrav")
moongrav.SetField("BodyName", "Luna")
sungrav = gmat.Construct("PointMassForce", "SunGrav")
sungrav.SetField("BodyName", "Sun")
jupitergrav = gmat.Construct("PointMassForce", "JupiterGrav")
jupitergrav.SetField("BodyName", "Jupiter")

# Drag using Jacchia-Roberts
# get_space_weather()
jrdrag = gmat.Construct("DragForce", "JRDrag")
jrdrag.SetField("AtmosphereModel", "JacchiaRoberts")

# Build and set the atmosphere for the model
atmos = gmat.Construct("JacchiaRoberts", "Atmos")
jrdrag.SetReference(atmos)


# Solar Radiation Pressure
srp = gmat.Construct("SolarRadiationPressure", "SRP")

# Add all of the forces into the ODEModel container
fm.AddForce(earthgrav)
fm.AddForce(moongrav)
fm.AddForce(sungrav)
fm.AddForce(jupitergrav)
fm.AddForce(jrdrag)
fm.AddForce(srp)

gmat.Initialize()
