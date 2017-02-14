<!-- {"full_title": "Plasma current reconstruction"} -->

# Current reconstruction in tokamak plasmas <a href="https://github.com/sballin/filament"><i class="fa fa-github"></i></a>

I've worked a lot on Tokamaks. Tokamaks are donut-shaped containers for hydrogen plasmas that we heat to ludicrous temperatures so that charged particles overcome their mutual repulsion and fuse, releasing energy that could be used to turn a steam turbine and power the lights in your house. To keep the plasma at such enormous temperatures and to protect the Tokamak's interior, the plasma is suspended in midair using magnetic fields. Tokamaks are surrounded by electromagnetic coils that generate powerful magnetic fields, but they also rely on an electric current going through the plasma itself to create the perfect confining magnetic field. This plasma current is induced by a transformer coil at the center of the torus:

<center><a href="http://cswim.org/imageslibrary/tokamak_schema.gif/view"><img src="{{top-path}}/{{article-path}}/tokamak.gif"/></a></center>

I'm working on a Python program that uses magnetic sensor measurements to reconstruct the plasma current profile on Columbia's High-beta Tokamak. 

It can calculate the magnetic field at any location resulting from current in a circular coil:

$$B = G(r, z, r_{coil}, z_{coil})\cdot I_{coil}$$

where G is a Green's function of their positions in cylindrical coordinates. For each magnetic sensor, we subtract the coil fields from the sensor's readings to get the field of the plasma current alone. Then we do the linear algebra version of $I = G^{-1}B$ to calculate the plasma current over a grid of different positions.

<!--  -->

<center><a href="https://github.com/sballin/filament"><img src="{{top-path}}/{{article-path}}/reconstruction.gif"/></a></center>

The plasma current in the above image is actually wrong, because the code is not completely precise, and the least-squares inversion of the Green's function matrix makes errors even bigger. The image below shows how accurately the code can predict what a given sensor sees in a shot where only the vertical field coil is active.
 
<center><a href="https://raw.githubusercontent.com/sballin/filament/master/resources/montage.jpg"><img width="450px" src="{{top-path}}/{{article-path}}/PA2_S22P.png"/></a></center>

I'm currently writing code to account for eddy currents in the machine's stainless steel shells, which will help produce an accurate end result. On a flat piece of metal, eddy currents can look like this:

<center><a href="https://en.wikipedia.org/wiki/Eddy_current"><img width="100%" src="{{top-path}}/{{article-path}}/eddy-current.png"/></a></center>

But there are other possible configurations. The only constraint is that when we add up the currents along a slice of the material (e.g. the red arrows), their sum is zero. To find the different modes, we imagine that the material is made up of filaments that carry current. 

<center><object type="image/svg+xml" width="100%" data="{{top-path}}/{{article-path}}/3d.svg">SVG not loaded.</object></center>

We model the eddy currents as loops going all the way around the tokamak, through the SS shells, colored from red to blue according to the first eigenmode. Poloidal sensors are orange, radial ones are blue.

The eigenvectors of the system of resistances and inductances between the filaments that correspond to the longest L/R times are the significant eigenmodes. Here, the program has found the top 3 eigenmodes for one of the steel shells:

<center><a href="https://raw.githubusercontent.com/sballin/filament/master/resources/eigen_comparison.jpg"><img src="{{top-path}}/{{article-path}}/eigenmodes.png"/></a></center>
