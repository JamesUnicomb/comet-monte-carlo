from load_gmat import gmat
from force_model import earthorb, fm
import requests

# Build the propagation container class
pdprop = gmat.Construct("Propagator", "PDProp")

# Create and assign a numerical integrator for use in the propagation
gator = gmat.Construct("PrinceDormand853", "Gator")
pdprop.SetReference(gator)

# Assign the force model imported from BasicFM
pdprop.SetReference(fm)

# Set some of the fields for the integration
pdprop.SetField("InitialStepSize", 60.0)
pdprop.SetField("Accuracy", 1.0e-12)
pdprop.SetField("MinStep", 0.0)

# Perform top level initialization
gmat.Initialize()

# Setup the spacecraft that is propagated
pdprop.AddPropObject(earthorb)
pdprop.PrepareInternals()

# Refresh the 'gator reference
gator = pdprop.GetPropagator()

# output initial state
print(gator.GetTime(), " sec, state = ", gator.GetState())

# Propagate for 1 day
# while gator.GetTime() < 86400:
for i in range(1440):
    gator.Step(60.0)

# output final state
print(gator.GetTime(), " sec, state = ", gator.GetState())
