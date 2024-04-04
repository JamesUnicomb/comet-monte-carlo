from load_gmat import gmat
from force_model import earthorb, fm

# Build the propagation container class
pdprop = gmat.Construct("Propagator", "PDProp")

# Create and assign a numerical integrator for use in the propagation
gator = gmat.Construct("PrinceDormand78", "Gator")
pdprop.SetReference(gator)

# Assign the force model imported from BasicFM
pdprop.SetReference(fm)

# Set some of the fields for the integration
pdprop.SetField("InitialStepSize", 60.0)
pdprop.SetField("Accuracy", 1.0e-13)
pdprop.SetField("MinStep", 0.0)

# Perform top level initialization
gmat.Initialize()

# Setup the spacecraft that is propagated
pdprop.AddPropObject(earthorb)
pdprop.PrepareInternals()

# Refresh the 'gator reference
gator = pdprop.GetPropagator()

# Take a 600 second steps for 1 day, showing the state before and after
time = 0.0
print(time, " sec, state = ", gator.GetState())

# Propagate for 1 day (via 144 10-minute steps)
for x in range(144):
    gator.Step()
    time = gator.GetTime()
    print(time, " sec, state = ", gator.GetState())
