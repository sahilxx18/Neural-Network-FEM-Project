# -Neural -network-to-predict-the-displacement-of-the-beam.

Using the beam's FEM code, random topologies were created by varying the locations, sizes, and numbers of holes in a predictable way. CNN was then trained to predict the displacement of the beam for arbitrary force placements.

We had a data file with the load exerted on the beam and the coefficient of elasticity for each component of the beam given the Fem code.


In the first section, we had to anticipate the displacement of the beam, generate the data for testing and validation, and randomly position the hole in the beam.

The displacement of the beam in the separated section is then predicted by utilizing the original data file and varying the load's location among more than 1200 nodes.

Finding the maximum stress node and predicting displacement for it by creating data for the corresponding fornce and adjusting material attributes was the third and last step.

